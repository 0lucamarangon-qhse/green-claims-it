---
name: green-claims-it
description: "Verifica green claims e greenwashing di siti e comunicazioni aziendali (Dir. 2005/29/CE mod. 2024/825, Codice del consumo). Usare per valutare claim ambientali o aggiornare un report."
license: "CC BY 4.0 (contenuti), MIT (scripts/). Vedi LICENSE nel repository."
---

# Verifica delle asserzioni ambientali (green claims) – Italia

Verifica le asserzioni ambientali e di sostenibilità di un'azienda (sito web anche nelle versioni in
lingua, cataloghi, schede prodotto, post, documenti pubblici) rispetto alla direttiva 2005/29/CE sulle
pratiche commerciali sleali, come modificata dalla direttiva (UE) 2024/825, e al Codice del consumo
italiano. Classifica ogni claim in tre fasce (consentito, da approfondire, non consentito), calcola
le metriche di conformità, propone riscritture e produce un report Word. Si usa quando si chiede di valutare
claim «green», asserzioni ambientali o il greenwashing di una comunicazione aziendale, o di aggiornare
un report di verifica con nuovi documenti.

Strumento didattico e informativo: **non è un parere legale**. Il report vale solo per le fonti e i
documenti esaminati.

## Prima di iniziare
1. Leggi `references/classificazione.md` e `references/struttura-report.md`.
2. I riferimenti normativi stanno **solo** in `references/fonti-ue.md`, `references/fonti-italia.md`
   e `references/corrispondenze.md`. Non citare norme, articoli o date che non trovi lì: se servono,
   verificali prima sulla fonte ufficiale (EUR-Lex, Normattiva) oppure dichiarali come «da verificare».
3. **Controlla la data «Verificato il»** in testa ai file di riferimento. Se sono passati più di 6
   mesi dalla data odierna, dillo all'utente prima di procedere e scrivilo nel perimetro del report.
   Se puoi navigare sul web, proponi di riscontrare le fonti indicate nei file prima di citarle.

## Passo 0 — Inquadramento
Chiedi all'utente, se non li ha già indicati:
1. **Azienda** e **fonti da esaminare**: URL (con le versioni in lingua), PDF, cataloghi, post. Le
   fonti che non puoi leggere vanno caricate come file.
2. **Documenti dell'azienda** che provano i claim: dati di consumo ed emissioni, certificati (numero,
   campo di applicazione, scadenza), garanzie d'origine, dichiarazioni dei fornitori. Se non ce ne
   sono, avvisa che molti claim resteranno «da approfondire» e i claim decisi saranno pochi.
3. **Destinatari** della comunicazione: consumatori, microimprese o solo imprese. Serve per la base
   giuridica (vedi `classificazione.md`: per le microimprese la pubblicità segue il D.Lgs. 145/2007).
4. **Dove salvare** il report: solo in Claude Code. In Claude.ai non chiederlo: il file si scarica
   dalla conversazione.
Riepiloga il perimetro e chiedi conferma.

## Passo 1 — Raccolta ed estrazione dei claim
1. Leggi ogni fonte e annota URL, lingua e data di consultazione. Segna le parti non lette (pagine
   troncate, testi dentro immagini, contenuti che richiedono accesso). Le pagine di un sito si
   leggono **una alla volta**, attendendo ciascuna risposta prima della richiesta successiva (mai
   in parallelo): sugli hosting condivisi le richieste in parallelo superano il limite del piano.
   Molti strumenti di lettura non mostrano il codice di stato: riconosci una pagina di errore dal
   contenuto (poco testo, titoli come «508», «429», «Resource Limit Exceeded», «Accesso negato»).
   Se rilevi un errore, riprova la pagina una sola volta più tardi (in Claude Code, se serve,
   `sleep 30` da terminale); se fallisce ancora, elenca la pagina tra le fonti non lette. Non
   estrarre claim da pagine di errore.
2. Estrai **ogni** asserzione ambientale secondo le regole di `classificazione.md` (anche loghi,
   immagini, nomi di prodotto e di linea). Numera C01, C02… con fonte e lingue. Le affermazioni su
   terzi vanno nel perimetro come «fuori ambito».
3. Riporta i claim testualmente. Se lo strumento di lettura restituisce una sintesi invece del
   testo, rileggi la pagina o segnala nel perimetro che la citazione va verificata sul sito.

## Passo 2 — Riscontro e classificazione
1. Per ogni claim cerca l'evidenza nei documenti forniti (documento, data, perimetro) o annota che manca.
2. Classifica con `classificazione.md`: ✅ consentito · 🟡 da approfondire · ⛔ non consentito.
3. Per 🟡 e ⛔ indica la coppia di riferimenti (direttiva + Codice del consumo, da
   `corrispondenze.md`) e spiega la criticità; per 🟡 indica il **documento preciso da procurare**.
4. Calcola le **metriche** come indicato in `struttura-report.md` (sezione «Metriche»).
5. Annota le incoerenze tra pagine e lingue.
6. **Mostra in chat** perimetro, tabella dei claim, metriche e incoerenze, e chiedi conferma o correzioni
   prima di scrivere il report.

## Passo 3 — Riscritture
1. Proponi di riscrivere tutti i ⛔ e i 🟡; l'utente sceglie quali tenere o aggiungere.
2. Per ogni claim scelto scrivi una o due alternative specifiche (caratteristica, perimetro, dato,
   anno, fonte), con i dati mancanti tra [parentesi quadre] (solo per i dati mancanti: vedi
   `struttura-report.md`). **Non inventare dati, percentuali o certificazioni.**
3. Sotto le riscritture e nei limiti dell'analisi riporta l'avvertenza IA di `struttura-report.md`.

## Passo 4 — Report
0. Verifica che Python 3 esegua `import docx` (libreria python-docx); l'interprete può chiamarsi
   `python3` (macOS, Linux) o `python` (Windows). Se non è disponibile, passa direttamente al
   punto 3 (report in Markdown) e dillo all'utente.
1. Prepara il contenuto in JSON secondo `struttura-report.md` (formato descritto in testa allo
   script) e genera il Word con il **percorso completo** della cartella della skill, ad esempio:
   `python3 ~/.claude/skills/green-claims-it/scripts/genera_report.py contenuto.json <cartella>/Report_asserzioni_ambientali_<Azienda>.docx`
   (in Claude.ai usa il percorso in cui l'ambiente ha caricato la skill). Il modello predefinito
   `assets/modello_report.docx` viene trovato dallo script. Se lo script si ferma con un messaggio
   sul JSON, correggi il blocco indicato e rilancia.
2. Se puoi, esporta in PDF e controlla l'impaginazione (tabelle, colori delle fasce, segnaposto).
3. **Se lo script non si può eseguire** (manca Python o python-docx), produci il report in Markdown
   come descritto in `struttura-report.md`.

## Passo 5 — Aggiornamento con nuovi documenti
Se l'utente fornisce nuovi documenti, riclassifica solo i claim interessati e produci una nuova
revisione (`_rev1`, `_rev2`…) con lo storico delle metriche e l'elenco dei claim che hanno
cambiato fascia.

## Regole
- Mostra la classificazione in chat e attendi conferma prima di generare il report.
- Nessun riferimento normativo fuori dai file di `references/` senza verifica sulla fonte ufficiale.
- Nessuna affermazione su come agiscono di solito autorità, aziende o consumatori: solo la lettura del
  testo normativo e dei documenti forniti.
- Il report non è un parere legale: per decisioni con conseguenze rilevanti l'utente deve rivolgersi a
  un professionista.
