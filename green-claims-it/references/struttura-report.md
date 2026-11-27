# Struttura del report

1. **Oggetto e sintesi**: le metriche (vedi «Metriche»), 3-5 punti chiave, azione proposta.
2. **Perimetro**: fonti esaminate (URL, lingua, data); documenti ricevuti; fonti non lette o lette in
   parte; affermazioni fuori ambito; data di verifica dei riferimenti normativi, con avviso se ha più di
   6 mesi.
3. **Quadro di riferimento**: norme, date, base giuridica per i destinatari (da `fonti-ue.md` e
   `fonti-italia.md`).
4. **Evidenze disponibili**: tabella dei dati e documenti dell'azienda usati per il riscontro.
5. **Analisi dei claim**: ID | claim (fonte, lingue) | fascia | riscontro e motivazione | riferimento |
   azione o documento da procurare. Ordine: ⛔, 🟡, ✅.
6. **Metriche**: formule, valori e, nelle revisioni, lo storico.
7. **Incoerenze tra pagine e lingue.**
8. **Documenti da raccogliere** (dai 🟡).
9. **Proposte di riscrittura** (solo i claim scelti dall'utente), con l'avvertenza IA. Se l'utente non
   ne sceglie nessuno, la sezione resta con la sola frase «Nessuna riscrittura richiesta».
10. **Limiti dell'analisi**, con l'avvertenza IA.
11. **Riferimenti**: link alle fonti e data di verifica.

## Metriche
Si riportano **sempre insieme**, in percentuale senza decimali:
1. **Distribuzione**: ✅ n (%) · 🟡 n (%) · ⛔ n (%) sul totale dei claim.
2. **Intervallo di conformità**: da ✅ / totale (minimo, se nessun 🟡 risultasse conforme) a
   (✅ + 🟡) / totale (massimo, se tutti i 🟡 fossero dimostrati).
3. **Claim decisi** = (✅ + ⛔) / totale: la quota di claim classificati in modo definitivo.
4. **Score sui claim decisi** = ✅ / (✅ + ⛔), solo come dato secondario e sempre con la dicitura
   «calcolato sui soli claim decisi; esclude i claim da approfondire».

Se un denominatore è zero: «n.d.». Nessuna metrica si presenta da sola nel titolo o nella sintesi.
Nei report che aggiornano una revisione emessa con score e copertura, si riportano i valori vecchi
accanto ai nuovi (copertura = claim decisi).
La metrica «claim decisi» non va confusa con il perimetro (fonti lette e non lette).

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
La `dimensione` del testo è in **mezzi punti** (interi): 15 = 7,5 pt, 16 = 8 pt.
- Analisi dei claim (§ 5): `[500, 1950, 1250, 2500, 1500, 1711]`, dimensione 15: la colonna della
  fascia resta ≥ 1250 perché «Da approfondire» non vada a capo.
- Riscritture (§ 9): `[1200, 8211]`, dimensione 16; claim con la stessa soluzione in una riga.

## Colori nel Word
✅ verde C6EFCE · 🟡 ambra FFE699 · ⛔ rosso FFC7CE (nella cella della fascia il testo è esattamente
«Consentito», «Da approfondire» o «Non consentito»); dati mancanti tra [parentesi quadre] evidenziati
in giallo; avvertenze in corsivo grigio.

Le parentesi quadre servono **solo** per i dati mancanti. Nelle citazioni le omissioni si scrivono
[…] (non evidenziate); numeri di GU, CELEX, note e rimandi vanno tra parentesi tonde. Ogni riga di
tabella ha tante celle quante sono le larghezze: lo script si ferma se non è così.

## Se il Word non si può generare
Se l'ambiente non permette di eseguire lo script (manca Python o python-docx), il report si produce
in Markdown con gli stessi capitoli e tabelle; la fascia si indica con ✅ 🟡 ⛔ seguiti dal nome.
Avvertenza IA e righe del piè di pagina vanno in fondo al documento.
