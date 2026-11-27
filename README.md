# green-claims-it

Skill per Claude che verifica le **asserzioni ambientali** («green claims») di siti web, cataloghi e
comunicazioni aziendali rispetto alla **direttiva 2005/29/CE** sulle pratiche commerciali sleali, come
modificata dalla **direttiva (UE) 2024/825**, e al **Codice del consumo** italiano (D.Lgs. 206/2005,
come modificato dal D.Lgs. 30/2026).

> ⚠️ Strumento didattico e informativo. **Non è un parere legale**: le classificazioni valgono solo per
> le fonti e i documenti esaminati. Per decisioni con conseguenze rilevanti rivolgersi a un professionista.

## Cosa fa
1. Raccoglie le asserzioni ambientali dalle fonti indicate (anche versioni in lingua, loghi e nomi di prodotto).
2. Le confronta con i documenti dell'azienda (dati, certificati, dichiarazioni dei fornitori).
3. Le classifica in tre fasce:

| Fascia | Significato |
|---|---|
| ✅ Consentito | Formulazione conforme e dimostrata dai documenti forniti |
| 🟡 Da approfondire | Può essere conforme, ma manca la prova: il report indica quale documento procurare |
| ⛔ Non consentito | Vietato in ogni caso, oppure smentito dai dati forniti |

4. Calcola le **metriche**, sempre insieme: distribuzione per fascia, intervallo di conformità
   (da ✅ / totale a (✅ + 🟡) / totale) e quota di claim decisi ((✅ + ⛔) / totale); lo score
   ✅ / (✅ + ⛔) solo come dato secondario, calcolato sui claim decisi.
5. Propone riscritture dei claim critici, con avvertenza sull'uso dell'IA.
6. Produce un **report Word** (o Markdown, se il Word non si può generare).

## Installazione

### Claude.ai (web e app desktop)
1. Scarica `green-claims-it.zip` dalla sezione *Releases* del repository, oppure crea uno zip della
   cartella **interna** `green-claims-it/` (quella che contiene `SKILL.md`): lo zip deve contenere la
   cartella, non i file sciolti. Non usare «Source code (zip)» di GitHub: contiene la cartella un
   livello più in basso.
2. In Claude: **Customize → Skills → «+» → Create skill → Upload a skill** e carica lo zip.
3. Attiva l'esecuzione del codice: **Settings → Capabilities → «Code execution and file creation»**.
   Nei piani Team ed Enterprise può servire l'autorizzazione dell'amministratore.

### Claude Code
Copia la cartella `green-claims-it/` in:
- `~/.claude/skills/green-claims-it/` (uso personale), oppure
- `.claude/skills/green-claims-it/` nel tuo progetto.

Le skill caricate su Claude.ai e quelle installate in Claude Code sono gestite separatamente: verifica
nella documentazione della tua versione di Claude Code se le skill dell'account vengono sincronizzate;
altrimenti installala in entrambi gli ambienti.

## Requisiti
- Per il report Word: Python 3 e la libreria `python-docx` (in Claude Code: `pip install python-docx`).
  In Claude.ai la disponibilità della libreria non è documentata: se manca, la skill produce il report
  in Markdown.
- Per leggere i siti: accesso al web dall'ambiente in uso; in alternativa si caricano le pagine come file.

## Come si usa
Esempio di richiesta:
> *Verifica le asserzioni ambientali del sito www.esempio.it, pagine «Sostenibilità» e «Prodotti»,
> anche in inglese. Ti allego il certificato ISO 14001 e i dati energetici 2025.*

La skill chiede il perimetro, mostra la tabella dei claim in chat, chiede quali riscritture proporre e
poi genera il report.

## Aggiornamento normativo
I riferimenti sono in `green-claims-it/references/`, ognuno con la data «Verificato il». Se sono
passati più di 6 mesi, la skill lo segnala nel report e invita a riscontrare le fonti ufficiali
(EUR-Lex, Normattiva). Le date di verifica di ogni versione sono nel [CHANGELOG](CHANGELOG.md).

## Sicurezza
L'unico codice eseguibile è `green-claims-it/scripts/genera_report.py`, che crea il Word a partire
da un file JSON. Come per ogni skill di terze parti, leggilo prima di usarlo.

## Limiti
- Copre solo il diritto UE e italiano sulle pratiche commerciali verso i consumatori, con le
  microimprese incluse dal Codice del consumo. Per la pubblicità verso le microimprese e tra imprese
  cita il D.Lgs. 145/2007 senza analizzarlo nel dettaglio.
- I divieti specifici su durabilità, riparabilità e aggiornamenti software non sono ancora applicati:
  questi claim si valutano come claim specifici.
- Non verifica la veridicità dei documenti forniti e non legge contenuti protetti da accesso.
- La proposta di direttiva «Green Claims» non è legge applicabile e non è usata nella classificazione;
  la Commissione ne ha previsto il ritiro nel programma di lavoro 2027.

## Licenza
Contenuti in **CC BY 4.0** (citare «green-claims-it» di Luca Marangon con il link al repository),
script in **MIT**. Dettagli in [LICENSE](LICENSE).

## Autore
**Luca Marangon** – Consulenza e formazione | QHSE
[LinkedIn](https://www.linkedin.com/in/lucamarangon/) · segnalazioni e proposte tramite le *Issues* del repository.

---

*English summary*: a Claude skill that checks environmental claims of Italian companies against the EU
Unfair Commercial Practices Directive as amended by Directive (EU) 2024/825 and the Italian Consumer
Code. Three-tier classification, compliance metrics (tier distribution, compliance range), rewrite suggestions and a Word report. Educational
tool, not legal advice. Content CC BY 4.0, scripts MIT.
