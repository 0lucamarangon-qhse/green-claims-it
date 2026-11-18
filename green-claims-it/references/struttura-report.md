# Struttura del report

1. **Oggetto e sintesi**: score, copertura, numero di claim per fascia, 3-5 punti chiave, azione proposta.
2. **Perimetro**: fonti esaminate (URL, lingua, data); documenti ricevuti; fonti non lette o lette in
   parte; affermazioni fuori ambito; data di verifica dei riferimenti normativi, con avviso se ha più di
   6 mesi.
3. **Quadro di riferimento**: norme, date, base giuridica per i destinatari (da `fonti-ue.md` e
   `fonti-italia.md`).
4. **Evidenze disponibili**: tabella dei dati e documenti dell'azienda usati per il riscontro.
5. **Analisi dei claim**: ID | claim (fonte, lingue) | fascia | riscontro e motivazione | riferimento |
   azione o documento da procurare. Ordine: ⛔, 🟡, ✅.
6. **Score e copertura**: formule, valori e, nelle revisioni, lo storico.
7. **Incoerenze tra pagine e lingue.**
8. **Documenti da raccogliere** (dai 🟡).
9. **Proposte di riscrittura** (solo i claim scelti dall'utente), con l'avvertenza IA.
10. **Limiti dell'analisi**, con l'avvertenza IA.
11. **Riferimenti**: link alle fonti e data di verifica.

## Score
Score di conformità = ✅ / (✅ + ⛔), in percentuale senza decimali.
Copertura = (✅ + ⛔) / totale dei claim. Se il denominatore è zero: «n.d.».

## Avvertenza IA (sotto la tabella delle riscritture e nei limiti dell'analisi)
> *Testo proposto con l'ausilio dell'intelligenza artificiale. Non costituisce parere legale e non
> comporta alcuna assunzione di responsabilità: chi pubblica resta responsabile della veridicità e
> della dimostrabilità di quanto dichiarato.*

## Piè di pagina (già nel modello Word)
- Pagina X di Y.
- *Report generato con la skill «green-claims-it» di Luca Marangon – © 2026, licenza CC BY 4.0.*
- *Analisi automatizzata a scopo didattico e informativo: non costituisce parere legale; le
  classificazioni valgono solo per le fonti e i documenti elencati nel report.*

## Impaginazione delle tabelle (larghezze in dxa, totale 9411)
- Analisi dei claim (§ 5): `[500, 1950, 1250, 2500, 1500, 1711]`, dimensione 15: la colonna della
  fascia resta ≥ 1250 perché «Da approfondire» non vada a capo.
- Riscritture (§ 9): `[1200, 8211]`, dimensione 16; claim con la stessa soluzione in una riga.

## Colori nel Word
✅ verde C6EFCE · 🟡 ambra FFE699 · ⛔ rosso FFC7CE (nella cella della fascia il testo è esattamente
«Consentito», «Da approfondire» o «Non consentito»); dati mancanti tra [parentesi quadre] evidenziati
in giallo; avvertenze in corsivo grigio.

## Se il Word non si può generare
Se l'ambiente non permette di eseguire lo script (manca Python o python-docx), il report si produce
in Markdown con gli stessi capitoli e tabelle; la fascia si indica con ✅ 🟡 ⛔ seguiti dal nome.
Avvertenza IA e righe del piè di pagina vanno in fondo al documento.
