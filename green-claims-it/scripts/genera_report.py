"""Genera il report Word della skill green-claims-it.

© 2026 Luca Marangon – rilasciato con licenza MIT (vedi LICENSE nella radice del repository).

Uso:  python genera_report.py contenuto.json output.docx [modello.docx]

contenuto.json:
{
  "intestazione": "Verifica asserzioni ambientali",
  "data": "17/11/2026",
  "titolo_documento": "Comunicazione ambientale sul sito web – <Cliente>",
  "blocchi": [
    {"tipo": "titolo", "testo": "..."},
    {"tipo": "sottotitolo", "testo": "..."},
    {"tipo": "h1", "testo": "1. Oggetto e sintesi"},
    {"tipo": "h2", "testo": "..."},
    {"tipo": "p", "testo": "testo con **grassetto** e [dato mancante]"},
    {"tipo": "bullet", "testo": "..."},
    {"tipo": "avvertenza", "testo": "corsivo grigio"},
    {"tipo": "tabella", "larghezze": [2000, 3000, ...], "righe": [["intestazione", ...], [...]],
     "dimensione": 17}
  ]
}

Convenzioni:
- **testo** = grassetto; [testo] = evidenziato in giallo (dato mancante o da verificare).
- nelle tabelle, una cella che contiene esattamente «Consentito», «Da approfondire» o
  «Non consentito» viene colorata (verde, ambra, rosso).
- la prima riga di ogni tabella è l'intestazione e si ripete a ogni pagina.
"""
import sys, os, re, copy, json
import docx
from docx.oxml.ns import qn
from docx.oxml import parse_xml

W = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
FASCE = {'consentito': 'C6EFCE', 'da approfondire': 'FFE699', 'non consentito': 'FFC7CE'}
GRIGIO = '6B6B6B'
TESTO = '222222'
TOKEN = {'titolo': 'TITOLO', 'sottotitolo': 'SOTTOTITOLO', 'h1': 'H1', 'h2': 'H2',
         'p': 'BODY', 'bullet': 'BULLET', 'avvertenza': 'BODY'}
SPLIT = re.compile(r'(\*\*.+?\*\*|\[[^\]]+\])')


ORDINE = ['rStyle', 'rFonts', 'b', 'bCs', 'i', 'iCs', 'caps', 'smallCaps', 'strike', 'dstrike', 'outline',
          'shadow', 'emboss', 'imprint', 'noProof', 'snapToGrid', 'vanish', 'webHidden', 'color', 'spacing', 'w',
          'kern', 'position', 'sz', 'szCs', 'highlight', 'u', 'effect', 'bdr', 'shd', 'fitText', 'vertAlign', 'rtl',
          'cs', 'em', 'lang', 'eastAsianLayout', 'specVanish', 'oMath']


def ordina(rp):
    """Riordina le proprietà del testo secondo lo schema di Word."""
    figli = list(rp)
    for f in figli:
        rp.remove(f)
    nome = lambda e: e.tag.split('}')[-1]
    for f in sorted(figli, key=lambda e: ORDINE.index(nome(e)) if nome(e) in ORDINE else len(ORDINE)):
        rp.append(f)
    return rp


def esc(s):
    return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


def carica(modello):
    d = docx.Document(modello)
    body = d.element.body
    proto = {}
    for p in list(d.paragraphs):
        m = re.fullmatch(r'\{\{(\w+)\}\}', p.text.strip())
        if m:
            proto[m.group(1)] = copy.deepcopy(p._p)
            body.remove(p._p)
    return d, proto


def paragrafo(d, proto, tipo, testo):
    p = copy.deepcopy(proto[TOKEN[tipo]])
    runs = p.findall(qn('w:r'))
    rpr = runs[0].find(qn('w:rPr')) if runs else None
    for r in runs:
        p.remove(r)
    for parte in SPLIT.split(testo):
        if not parte:
            continue
        rp = copy.deepcopy(rpr) if rpr is not None else parse_xml(f'<w:rPr xmlns:w="{W}"/>')
        t = parte
        if parte.startswith('**') and parte.endswith('**'):
            t = parte[2:-2]
            for vecchio in rp.findall(qn('w:b')):
                rp.remove(vecchio)
            rp.append(parse_xml(f'<w:b xmlns:w="{W}"/>'))
        elif parte.startswith('[') and parte.endswith(']'):
            rp.append(parse_xml(f'<w:highlight xmlns:w="{W}" w:val="yellow"/>'))
        if tipo == 'avvertenza':
            for c in rp.findall(qn('w:color')) + rp.findall(qn('w:i')):
                rp.remove(c)
            rp.append(parse_xml(f'<w:i xmlns:w="{W}"/>'))
            rp.append(parse_xml(f'<w:color xmlns:w="{W}" w:val="{GRIGIO}"/>'))
        r = parse_xml(f'<w:r xmlns:w="{W}"/>')
        r.append(ordina(rp))
        r.append(parse_xml(f'<w:t xmlns:w="{W}" xml:space="preserve">{esc(t)}</w:t>'))
        p.append(r)
    d.element.body.insert(len(d.element.body) - 1, p)


def cella(w, testo, intestazione, sz):
    fill = '404040' if intestazione else FASCE.get(testo.strip().lower())
    shd = f'<w:shd w:val="clear" w:color="auto" w:fill="{fill}"/>' if fill else ''
    colore = 'FFFFFF' if intestazione else TESTO
    paras = ''
    for riga in str(testo).split('\n'):
        runs = ''
        for parte in SPLIT.split(riga):
            if not parte:
                continue
            b = '<w:b/>' if (intestazione or (parte.startswith('**') and parte.endswith('**'))) else ''
            hl = ('<w:highlight w:val="yellow"/>'
                  if (parte.startswith('[') and parte.endswith(']') and not intestazione) else '')
            t = parte[2:-2] if (parte.startswith('**') and parte.endswith('**')) else parte
            runs += (f'<w:r><w:rPr><w:rFonts w:ascii="Calibri" w:hAnsi="Calibri" w:cs="Calibri" w:eastAsia="Calibri"/>'
                     f'{b}<w:color w:val="{colore}"/><w:sz w:val="{sz}"/>{hl}'
                     f'<w:lang w:val="it-IT"/></w:rPr>'
                     f'<w:t xml:space="preserve">{esc(t)}</w:t></w:r>')
        paras += f'<w:p><w:pPr><w:spacing w:after="20"/></w:pPr>{runs}</w:p>'
    return f'<w:tc><w:tcPr><w:tcW w:w="{w}" w:type="dxa"/>{shd}</w:tcPr>{paras}</w:tc>'


def tabella(d, proto, larghezze, righe, sz=17):
    grid = ''.join(f'<w:gridCol w:w="{w}"/>' for w in larghezze)
    bordi = ''.join(f'<w:{s} w:val="single" w:sz="4" w:space="0" w:color="BFBFBF"/>'
                    for s in ('top', 'left', 'bottom', 'right', 'insideH', 'insideV'))
    trs = ''
    for i, riga in enumerate(righe):
        hdr = '<w:tblHeader/>' if i == 0 else ''
        trs += (f'<w:tr><w:trPr><w:cantSplit/>{hdr}<w:jc w:val="center"/></w:trPr>'
                + ''.join(cella(w, t, i == 0, sz) for w, t in zip(larghezze, riga)) + '</w:tr>')
    xml = (f'<w:tbl xmlns:w="{W}"><w:tblPr><w:tblStyle w:val="TableGrid"/>'
           f'<w:tblW w:w="{sum(larghezze)}" w:type="dxa"/><w:jc w:val="center"/>'
           f'<w:tblBorders>{bordi}</w:tblBorders><w:tblLayout w:type="fixed"/>'
           f'<w:tblLook w:val="04A0" w:firstRow="1" w:lastRow="0" w:firstColumn="1" w:lastColumn="0" '
           f'w:noHBand="0" w:noVBand="1"/></w:tblPr><w:tblGrid>{grid}</w:tblGrid>{trs}</w:tbl>')
    d.element.body.insert(len(d.element.body) - 1, parse_xml(xml))
    paragrafo(d, proto, 'p', '')


def intestazione(d, testo, data):
    for s in d.sections:
        for part in (s.header, s.first_page_header):
            for t in part._element.iter(qn('w:t')):
                if not t.text:
                    continue
                if '{{INTESTAZIONE}}' in t.text:
                    t.text = t.text.replace('{{INTESTAZIONE}}', testo)
                if '{{DATA}}' in t.text:
                    t.text = t.text.replace('{{DATA}}', data)


def main():
    src, out = sys.argv[1], sys.argv[2]
    modello = sys.argv[3] if len(sys.argv) > 3 else os.path.join(
        os.path.dirname(os.path.abspath(__file__)), '..', 'assets', 'modello_report.docx')
    c = json.load(open(src, encoding='utf-8'))
    d, proto = carica(modello)
    intestazione(d, c.get('intestazione', 'Verifica asserzioni ambientali'), c.get('data', ''))
    d.core_properties.title = c.get('titolo_documento', '')
    for b in c['blocchi']:
        if b['tipo'] == 'tabella':
            tabella(d, proto, b['larghezze'], b['righe'], b.get('dimensione', 17))
        else:
            paragrafo(d, proto, b['tipo'], b['testo'])
    if os.path.exists(out):
        sys.exit(f'Il file esiste già: {out} (scegli un nome di revisione)')
    d.save(out)
    print('ok', out)


if __name__ == '__main__':
    main()
