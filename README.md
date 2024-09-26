# e-service erogate dall'IPA

Il presente repo contiene gli e-service che saranno erogati da IPA a tutte le PA per il tramite della PDND interoperabilità.

Gli e-service sono definiti assumento il modello dati dell'IPA riportato nel seguente ER-diagram.

![IPA ER-diagram](/IPA-DATA_ER%20diagram.drawio.png)

Nel folder noflatversion è presente la versione di lavorazione degli openAPI che prevede l'inclusione degli oggetti comuni, lo script python scriptFlattingYML.py predispone la versione flattata degli openAPI nel folder flatversion.

Le API previste sono:

| # | e-service |
|---|---|
| 01 | API per la consultazione delle AOO |
| 02 | API per la consultazione delle AOO di un ENTE |
| 03 | API per la consultazione dei DD di un AOO |
| 04 | API per la consultazione dei DD di un ENTE |
| 05 | API per la consultazione dei DD di un UO |
| 06 | API per la consultazione delle PEC/RECAPITO CERTIFICATO di un AOO |
| 07 | API per la consultazione delle PEC/RECAPITO di un ENTE |
| 08 | API per la consultazione delle PEC/RECAPITO di un UO |
| 09 | API per la consultazione delle SFE di un ENTE |
| 10 | API per la consultazione delle UO |
| 11 | API per la consultazione delle UO di un ENTE |
| 12 | API per la consultazione degli ENTI |
| 13 | API per la consultazione degli indirizzi di un AOO |
| 14 | API per la consultazione degli indirizzi di un ENTE |
| 15 | API per la consultazione degli indirizzi di un UO |
| 16 | API per la consultazione dei rappresentanti di un AOO |
| 17 | API per la consultazione dei rappresentanti di un ENTE |
| 18 | API per la consultazione dei rappresentanti di un UO |
| 19 | API per la consultazione delle AOO variate alla data |
| 20 | API per la consultazione delle AOO di un ENTE variate alla data |
| 21 | API per la consultazione dei DD di un AOO variati alla data |
| 22 | API per la consultazione dei DD di un ENTE variati alla data |
| 23 | API per la consultazione dei DD di un UO variati alla data |
| 24 | API per la consultazione delle PEC/RECAPITO di un AOO variate alla data |
| 25 | API per la consultazione delle PEC/RECAPITO di un ENTE variate alla data |
| 26 | API per la consultazione delle PEC/RECAPITO di un UO variate alla data |
| 27 | API per la consultazione delle SFE di un ENTE variate alla data |
| 28 | API per la consultazione delle UO variate alla data |
| 29 | API per la consultazione delle UO di un ENTE variate alla data |
| 30 | API per la consultazione degli ENTI variati alla data |
| 31 | API per la consultazione degli indirizzi di un AOO variati alla data |
| 32 | API per la consultazione degli indirizzi di un ENTE variati alla data |
| 33 | API per la consultazione degli indirizzi di un UO variati alla data |
| 34 | API per la consultazione dei rappresentanti di un AOO variati alla data |
| 35 | API per la consultazione dei rappresentanti di un ENTE variati alla data |
| 36 | API per la consultazione dei rappresentanti di un UO variati alla data |
| 37 | API per la consultazione dell’elenco delle AOO alla data corrente  |
| 38 | API per la consultazione dell’elenco delle ENTE alla data corrente  |
| 39 | API per la consultazione dell’elenco delle UO alla data corrente  |
| 40 | API per la consultazione unica di Ente, AOO e UO |
