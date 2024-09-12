# e-service erogate dall'IPA

Il presente repo contiene gli e-service che saranno erogati da IPA a tutte le PA per il tramite della PDND interoperabilità.

Gli e-service sono definiti assumento il modello dati dell'IPA riportato nel seguente ER-diagram.

![IPA ER-diagram](/IPA-DATA_ER%20diagram.drawio.png)

Nel folder noflatversion è presente la versione di lavorazione degli openAPI che prevede l'inclusione degli oggetti comuni, lo script python scriptFlattingYML.py predispone la versione flattata degli openAPI nel folder flatversion.

Le API previste sono:

| # | e-service |
|---|---|
| x01 | API per la consultazione delle AOO |
| x02 | API per la consultazione delle AOO di un ENTE |
| x03 | API per la consultazione dei DD di un AOO |
| x04 | API per la consultazione dei DD di un ENTE |
| x05 | API per la consultazione dei DD di un UO |
| x06 | API per la consultazione delle PEC/RECAPITO CERTIFICATO di un AOO |
| x07 | API per la consultazione delle PEC/RECAPITO di un ENTE |
| x08 | API per la consultazione delle PEC/RECAPITO di un UO |
| x09 | API per la consultazione delle SFE di un ENTE |
| x10 | API per la consultazione delle UO |
| x11 | API per la consultazione delle UO di un ENTE |
| x12 | API per la consultazione degli ENTI |
| x13 | API per la consultazione degli indirizzi di un AOO |
| x14 | API per la consultazione degli indirizzi di un ENTE |
| x15 | API per la consultazione degli indirizzi di un UO |
| x16 | API per la consultazione dei rappresentanti di un AOO |
| x17 | API per la consultazione dei rappresentanti di un ENTE |
| x18 | API per la consultazione dei rappresentanti di un UO |
| x19 | API per la consultazione delle AOO variate alla data |
| x20 | API per la consultazione delle AOO di un ENTE variate alla data |
| x21 | API per la consultazione dei DD di un AOO variati alla data |
| x22 | API per la consultazione dei DD di un ENTE variati alla data |
| x23 | API per la consultazione dei DD di un UO variati alla data |
| x24 | API per la consultazione delle PEC/RECAPITO di un AOO variate alla data |
| x25 | API per la consultazione delle PEC/RECAPITO di un ENTE variate alla data |
| x26 | API per la consultazione delle PEC/RECAPITO di un UO variate alla data |
| x27 | API per la consultazione delle SFE di un ENTE variate alla data |
| x28 | API per la consultazione delle UO variate alla data |
| x29 | API per la consultazione delle UO di un ENTE variate alla data |
| x30 | API per la consultazione degli ENTI variati alla data |
| x31 | API per la consultazione degli indirizzi di un AOO variati alla data |
| x32 | API per la consultazione degli indirizzi di un ENTE variati alla data |
| x33 | API per la consultazione degli indirizzi di un UO variati alla data |
| x34 | API per la consultazione dei rappresentanti di un AOO variati alla data |
| x35 | API per la consultazione dei rappresentanti di un ENTE variati alla data |
| x36 | API per la consultazione dei rappresentanti di un UO variati alla data |
| x37 | API per la consultazione dell’elenco delle AOO alla data  |
| x38 | API per la consultazione dell’elenco delle ENTE alla data  |
| x39 | API per la consultazione dell’elenco delle UO alla data  |
| x40 | API per la consultazione unica di Ente, AOO e UO |
