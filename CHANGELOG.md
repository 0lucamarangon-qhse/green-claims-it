# Changelog

Le versioni seguono il formato MAGGIORE.MINORE.CORREZIONE. Ogni versione riporta la data a cui sono
stati verificati i riferimenti normativi in `green-claims-it/references/`.

## [1.1.0] – 27/11/2026
Revisione a seguito di una verifica esterna della 1.0.1.

**Corretto (classificazione)**:
- microimprese: per la pubblicità ingannevole e comparativa la base è il D.Lgs. 145/2007 (art. 19, c. 1
  del Codice), non gli artt. 21-23;
- marchi di sostenibilità: uno schema proprio dell'azienda è ammesso se rispetta i criteri del sistema
  di certificazione (considerando 7; FAQ della Commissione, D8); non è più ⛔ per il solo fatto di essere
  autoprodotto;
- «sostenibile», «responsabile», «consapevole» e «biodegradabile»: righe proprie secondo il
  considerando 10;
- eccezioni per i termini del biologico (Reg. (UE) 2018/848) e per le forme di espressione sugli alimenti
  (art. 35 Reg. (UE) 1169/2011);
- punti 4 ter e 4 quater: ⛔ se il fatto risulta, 🟡 se non è accertabile;
- «plausibile» sostituito da un criterio operativo: 🟡 solo con un indizio concreto nelle fonti o nei
  documenti;
- servizi, durabilità e riparabilità, casi non tabellati e sovrapposizioni.

**Cambiato (metriche)**: score e copertura sostituiti da distribuzione per fascia, intervallo di
conformità e quota di claim decisi; lo score resta come dato secondario.

**Corretto (script)**: controllo del JSON prima di costruire il documento (righe con celle in più o in
meno, tabelle vuote, celle non testuali, `dimensione` non intera); rimozione dei caratteri di controllo;
le omissioni […] non vengono più evidenziate come dati mancanti; colore della fascia anche quando la
cella contiene l'emoji («✅ Consentito»); niente intestazione di prima pagina vuota se il modello non la
prevede; messaggi di errore in italiano.

**Corretto (documentazione)**: Codice del consumo = D.Lgs. 206/2005 come modificato dal D.Lgs. 30/2026;
comando dello script con percorso completo; lettura delle pagine senza pause non eseguibili; zip da
usare per Claude.ai; stato della proposta «Green Claims»; `description` con il «quando usarla»; domanda
su dove salvare solo in Claude Code; sezione 9 del report quando non si chiedono riscritture.

**Riferimenti verificati**:
- Dir. (UE) 2024/825, considerando 7 e 10, art. 1 (art. 6 par. 2 lett. d) (EUR-Lex) – 26/11/2026
- Dir. 2005/29/CE consolidata, art. 2 lett. c, art. 3 par. 4 (EUR-Lex) – 26/11/2026
- Codice del consumo, art. 18 lett. c, art. 19 c. 3 (Normattiva) – 26/11/2026
- FAQ della Commissione sulla Dir. (UE) 2024/825, settembre 2026, D8, D14, D18 – 26/11/2026
- Programma di lavoro della Commissione 2027, COM(2026) 710, allegato III – 26/11/2026
- Altri riferimenti invariati (17-18/11/2026).

## [1.0.1] – 25/11/2026
**Corretto**: nel passo 1 le pagine di un sito si leggono in sequenza, con una pausa tra le
richieste, e si scartano le pagine di errore (es. stato 508 degli hosting condivisi), che
altrimenti verrebbero analizzate come contenuto del sito.

**Riferimenti verificati**: invariati rispetto alla 1.0.0 (17-18/11/2026).

## [1.0.0] – 18/11/2026
Prima versione pubblica.

**Ambito**: asserzioni ambientali e di sostenibilità secondo la Dir. 2005/29/CE come modificata dalla
Dir. (UE) 2024/825 e il Codice del consumo come modificato dal D.Lgs. 30/2026. Le regole su durabilità
e riparabilità sono riportate come riferimento, non ancora usate nella classificazione.

**Riferimenti verificati**:
- Dir. 2005/29/CE, testo consolidato al 27/09/2026 (EUR-Lex) – 17/11/2026
- Dir. (UE) 2024/825, artt. 1, 2 e 4, considerando 9, 11 e 12 (EUR-Lex) – 17-18/11/2026
- Codice del consumo, artt. 18-27-ter, 48, 65-ter (Normattiva) – 17-18/11/2026
- D.Lgs. 30/2026, D.Lgs. 146/2007, D.Lgs. 145/2007 (Normattiva) – 17/11/2026
- Politica di riuso di EUR-Lex e art. 5 L. 633/1941 – 18/11/2026

**Contenuto**: classificazione in tre fasce, score e copertura, riscritture con avvertenza IA, report
Word con modello neutro (alternativa in Markdown).
