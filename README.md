# Test di OpenSTAManager

Insieme di test [Selenium](https://selenium.dev/) sulle funzionalità di base di OpenSTAManager, sviluppati in [Python](https://www.python.org/).

## Esecuzione

L'esecuzione degli script richiede la presenza di alcuni pacchetti Python aggiuntivi che possono essere installati tramite [Pip (https://www.pypa.io/en/latest/)](https://www.pypa.io/en/latest/), con il seguente comando sulla cartella principale:

```bash
pip3 install -r requirements.txt
```

Occorre installare anche geckodriver:

https://github.com/mozilla/geckodriver/releases

L'avvio di un determinato script può essere effettuato attraverso al seguente riga di comando:
```bash
python3 -m pytest Init.py
python3 -m pytest tests
```
L'avvio di tutti gli script può essere effettuato attraverso al seguente riga di comando:
```bash
python3 -m unittest discover tests -p '*.py'
```

## Moduli

Legenda:
- :heavy_plus_sign: Crea
- :pencil: Modifica
- :wastebasket: Elimina
- :bookmark_tabs: Righe
- ☑️ Verifica

|N°| Modulo  | :heavy_plus_sign:| :pencil:|:wastebasket:|:bookmark_tabs: |☑️| Altro |
|--|-------- | :---------------:|:-------:|:-----------:|:--------------:|:-:|:---:|
|00| Backup | :heavy_check_mark: | - |-|-|-|-|
|01| Stato dei servizi |:heavy_check_mark:|:heavy_check_mark:|-|-|-|-|
|02| Anagrafiche | :heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-|:heavy_check_mark:| + documenti|
|03| Dashboard |:heavy_check_mark:|:heavy_check_mark:|-|-|:heavy_check_mark:|-
|04| Articoli |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-|:heavy_check_mark:|
|05| Attività |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:| + duplica|
|06| Fatture di acquisto |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:| + autofattura|
|07| Fatture di vendita |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:| + nota di credito, duplica e autofattura
|08| DDT in entrata |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:| + duplica|
|09| DDT in uscita |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|+duplica|
|10| Ordini fornitore |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-|
|11| Ordini cliente |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-|
|12| Contratti |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|+ duplica|
|13| Preventivi |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|+duplica e creazione documenti|
|14| Movimenti |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-|:heavy_check_mark:|- |
|15| Attività - Dashboard |:heavy_check_mark:|-|-|-|:heavy_check_mark:| +trascinamento|
|16| Relazioni |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-|:heavy_check_mark:|-|
|17| Zone |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-|:heavy_check_mark:|-|
|18| Provenienze clienti |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-|:heavy_check_mark:|-|
|19| Settori merceologici |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-|:heavy_check_mark:|-|
|20| Newsletter |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-|:heavy_check_mark:|-|
|21| Liste |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-|:heavy_check_mark:|-|
|22| Template email |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-|:heavy_check_mark:|-|
|23| Account email |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-|:heavy_check_mark:|-|
|24| Gestione documentale |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-|:heavy_check_mark:|-|
|25| Categorie documenti |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-|:heavy_check_mark:|-|
|26| Tipi attività |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-|:heavy_check_mark:|-|
|27| Fasce orarie |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-|:heavy_check_mark:|-|
|28| Stati attività |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-|:heavy_check_mark:|-|
|29| Tecnici tariffe |-|:heavy_check_mark:|-|-|:heavy_check_mark:|-|
|30| Tags |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:| -|:heavy_check_mark:|-|
|31| Stampe contabili | -|-|-|-|-|-|
|32| Prima nota |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-|:heavy_check_mark:|-|
|33| Tipi anagrafiche |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-|:heavy_check_mark:|-|
|34| Scadenzario |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-|:heavy_check_mark:|-|
|35| Piani sconto maggiorazione |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-|:heavy_check_mark:|-|
|36| Listini |-|-|-|-|-|-|
|37| Giacenze sedi|:heavy_check_mark:|:heavy_check_mark:| -|-|:heavy_check_mark:|+spostamento tra sedi|
|38| Attributi combinazioni |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-|:heavy_check_mark:|-|
|39| Combinazioni |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-|:heavy_check_mark:|-|
|40| Impianti |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-|:heavy_check_mark:|-|
|41| Categorie impianti |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-|:heavy_check_mark:|-|
|42| Statistiche |-|-|-|-|:heavy_check_mark:|-|
|43| Mappa |-|-|-|-|-|-|
|44| Campi personalizzati |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-|:heavy_check_mark:|-|
|45| Viste |-|-|-|-|:heavy_check_mark:|-|
|46| Utenti permessi |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-|:heavy_check_mark:|-|
|47| Tipi spedizione |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-|:heavy_check_mark:|-|
|48| Eventi |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-|:heavy_check_mark:|-|
|49| Tipi documento |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-|:heavy_check_mark:|-|
|50| Causali movimenti |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-|:heavy_check_mark:|-|
|51| Tipi scadenze |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-|:heavy_check_mark:|-|
|52| Stati contratti |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-|:heavy_check_mark:|-|
|53| Stati preventivi |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-|:heavy_check_mark:|-|
|54| Ritenute previdenziali |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-|:heavy_check_mark:|-|
|55| Casse previdenziali |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-|:heavy_check_mark:|-|
|56| IVA |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-|:heavy_check_mark:|-|
|57| Modelli prima nota |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-|:heavy_check_mark:|-|
|58| Banche |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-|:heavy_check_mark:|-|
|59| Ritenute acconto |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-|:heavy_check_mark:|-|
|60| Categorie articoli |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-|:heavy_check_mark:|-|
|61| Pagamenti |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-|:heavy_check_mark:|-|
|62| Porto |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-|:heavy_check_mark:|-|
|63| Unità misura |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-|:heavy_check_mark:|-|
|64| Aspetto beni |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-|:heavy_check_mark:|-|
|65| Causali trasporto |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-|:heavy_check_mark:|-|
|66| Mansioni referenti |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-|:heavy_check_mark:|-|
|67| Segmenti |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-|:heavy_check_mark:|-|
|68| Import |-|-|-|-|-|-|
|69| Stampe |-|-|-|-|-|-|
|70| Checklists |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-|:heavy_check_mark:|+check in attività|
|71| Aggiornamenti |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-|:heavy_check_mark:|-|
|72| Listini clienti |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-|:heavy_check_mark:|-|
|73| Widgets |-|-|-|-|:heavy_check_mark:|-|
|74| Automezzi |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:| -|:heavy_check_mark:|-|
|75| Marche impianti |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-|:heavy_check_mark:|-|
|76| Adattatori di archiviazione |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-|:heavy_check_mark:|-|
|77| Gestione task |-|:heavy_check_mark:|-|-|:heavy_check_mark:|-|
|78| Stati fatture |-|:heavy_check_mark:|-|-|:heavy_check_mark:|-|
|79| Stati degli ordini |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-|:heavy_check_mark:|-|

## Plugin

Legenda:
- :heavy_plus_sign: Aggiunta
- :pencil: Modifica
- :wastebasket: Eliminazione
- ☑️ Verifica
- :question: Funzionamento


|N°| Modulo  | Plugin | :heavy_plus_sign: | :pencil: | :wastebasket: | ☑️ | :question: |
|--|-------- | -------| :---------------: | :------: | :-----------: |:-:| -------- |
|40| Anagrafiche | Impianti del cliente |-|-|-|:heavy_check_mark:|-|
|02| Anagrafiche | Referenti |:heavy_check_mark:|:x:|:x:|:heavy_check_mark:|aggiunta mansione|
|02| Anagrafiche | Sedi aggiuntive |:heavy_check_mark:|:x:|:x:|:heavy_check_mark:|-|
|02| Anagrafiche | Statistiche |-|-|-|:heavy_check_mark:|-|
|09| Anagrafiche | Ddt del cliente |-|-|-|:heavy_check_mark:|-|
|02| Anagrafiche | Dichiarazione d'intento |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|controllo in fatture|
|05| Anagrafiche | Storico attività |-|-|-|:heavy_check_mark:|-|
|07| Anagrafiche | Allegati |-|-|-|:heavy_check_mark:|-|
|12| Anagrafiche | Contratti del cliente |-|-|-|:heavy_check_mark:|-|
|02| Anagrafiche | Assicurazione crediti |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|controllo in fatture|
|07| Anagrafiche | Movimenti contabili |-|-|-|:heavy_check_mark:|-|
|07| Anagrafiche | Regole pagamenti |:heavy_check_mark:|:x:|:heavy_check_mark:|:heavy_check_mark:|controllo in scadenzario|
|40| Attività | Impianti |:heavy_check_mark:|:x:|:heavy_check_mark:|:heavy_check_mark:|:x: (controllo impianti interventi svolti)|
|12| Contratti | Consuntivo |-|-|-|:heavy_check_mark:|-|
|12| Contratti | Pianificazione attività |:heavy_check_mark:|:x:|:x:|:heavy_check_mark:|-|
|12| Contratti | Rinnovi |:heavy_check_mark:|-|:heavy_check_mark:|-|-|
|12| Contratti | Pianificazione fatturazione |:heavy_check_mark:|-|-|:heavy_check_mark:|controllo in Fatture e widget Dashboard|
|13| Preventivi | Consuntivo |-|-|-|:heavy_check_mark:|-|
|13| Preventivi | Revisioni |-|-|-|:heavy_check_mark:|-|
|11| Ordini cliente | Consuntivo |-|-|-|:heavy_check_mark:|-|
|:x:| Fatture di vendita | Fatturazione elettronica |:x:|:x:|:x:|:x:|:x:|
|07| Fatture di vendita | Movimenti contabilili |-|-|-|:heavy_check_mark:|-|
|07| Fatture di vendita | Registrazioni |-|:heavy_check_mark:|-|:heavy_check_mark:|-|
|06| Fatture di acquisto | Movimenti contabilili |-|-|-|:heavy_check_mark:|-|
|06| Fatture di acquisto | Registrazioni |-|:heavy_check_mark:|-|-|-|
|:x:| Scadenzario | Presentazioni bancarie |:x:|:x:|:x:|:x:|:x:|
|04| Articoli | Movimenti |-|-|-|:heavy_check_mark:|-|
|04| Articoli | Serial |:heavy_check_mark:|-|:heavy_check_mark:|:heavy_check_mark:|-|
|04| Articoli | Giacenze |-|-|-|:heavy_check_mark:|-|
|04| Articoli | Statistiche |-|-|-|:heavy_check_mark:|-|
|04| Articoli | Netto clienti |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-|
|04| Articoli | Listino fornitori |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-|
|35| Articoli | Piani di sconto/maggiorazione |-|-|-|:heavy_check_mark:|-|
|04| Articoli | Varianti articolo |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|controllo e creazione in attributi combinazioni|
|04| Articoli | Provvigioni |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-|
|04| Articoli | Statistiche vendita |-|-|-|:heavy_check_mark:|-|
|40| Impianti | Interventi svolti |-|-|-|:heavy_check_mark:|-|
|40| Impianti | Componenti |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-|


## Azioni di gruppo

Legenda:
- ☑️ Verifica


|N°| Modulo  | Azioni di gruppo | ☑️ |
|--|-------- | ---------------- |:-:|
|02| Anagrafiche  | Esporta selezionati | |
|02| Anagrafiche  | Cambia relazione |:heavy_check_mark:|
|02| Anagrafiche  | Aggiorna listino cliente |:heavy_check_mark:|
|02| Anagrafiche  | Elimina selezionati |:heavy_check_mark:|
|02| Anagrafiche  | Ricerca coordinate |:heavy_check_mark:|
|05| Attività | Esporta stampe | |
|05| Attività | Fattura attività |:heavy_check_mark:|
|05| Attività | Cambia stato |:heavy_check_mark:|
|05| Attività | Duplica attività |:heavy_check_mark:|
|05| Attività | Stampa riepilogo | |
|23| Attività | Invia mail |:heavy_check_mark:|
|05| Attività | Firma interventi  |:heavy_check_mark:|
|05| Attività | Elimina selezionati |:heavy_check_mark:|
|12| Contratti | Fattura contratti |:heavy_check_mark:|
|12| Contratti | Rinnova contratti |:heavy_check_mark:|
|12| Contratti | Cambia stato |:heavy_check_mark:|
|13| Preventivi | Fattura preventivi |:heavy_check_mark:|
|13| Preventivi | Cambia stato |:heavy_check_mark:|
|11| Ordini cliente | Fattura ordini cliente |:heavy_check_mark:|
|11| Ordini cliente | Cambia stato |:heavy_check_mark:|
|11| Ordini cliente | Unisci RDO | |
|58| Fatture di vendita | Aggiorna banca |:heavy_check_mark:|
|07| Fatture di vendita | Cambia sezionale |:heavy_check_mark:|
|07| Fatture di vendita | Controlla fatture elettroniche ||
|07| Fatture di vendita | Duplica selezionati |:heavy_check_mark:|
|07| Fatture di vendita | Emetti fatture |:heavy_check_mark:|
|07| Fatture di vendita | Esporta stampe ||
|07| Fatture di vendita | Esporta stampe FE ||
|07| Fatture di vendita | Esporta ricevute ||
|07| Fatture di vendita | Esporta XML ||
|07| Fatture di vendita | Genera fatture elettroniche ||
|07| Fatture di vendita | Registrazione contabile |:heavy_check_mark:|
|07| Fatture di vendita | Coda di invio FE ||
|07| Fatture di vendita | Elimina selezionati |:heavy_check_mark:|
|10| Ordini fornitore | Cambia stato |:heavy_check_mark:|
|58| Fatture di acquisto | Aggiorna banca |:heavy_check_mark:|
|06| Fatture di acquisto | Cambia sezionale |:heavy_check_mark:|
|06| Fatture di acquisto | Duplica selezionati |:heavy_check_mark:|
|06| Fatture di acquisto | Esporta selezionati | |
|06| Fatture di acquisto | Esporta stampa FE | |
|06| Fatture di acquisto | Esporta ricevute | |
|06| Fatture di acquisto | Esporta XML | |
|06| Fatture di acquisto | Registrazione contabile |:heavy_check_mark:|
|06| Fatture di acquisto | Elimina selezionati |:heavy_check_mark:|
|32| Prima nota | Esporta PDF | |
|34| Scadenzario | Registrazione contabile |:heavy_check_mark:|
|34| Scadenzario | Info distinta |:heavy_check_mark:|
|58| Scadenzario | Aggiorna banca |:heavy_check_mark:|
|34| Scadenzario | Invia mail sollecito | |
|04| Articoli | Esporta selezionati | |
|04| Articoli | Aggiorna prezzo di acquisto |:heavy_check_mark:|
|04| Articoli | Aggiorna prezzo di vendita |:heavy_check_mark:|
|04| Articoli | Aggiorna coefficiente di vendita |:heavy_check_mark:|
|04| Articoli | Stampa etichette | |
|04| Articoli | Aggiorna quantità |:heavy_check_mark:|
|04| Articoli | Crea preventivo |:heavy_check_mark:|
|04| Articoli | Aggiorna categoria e sottocategoria |:heavy_check_mark:|
|04| Articoli | Aggiorna aliquota iva |:heavy_check_mark:|
|04| Articoli | Imposta prezzo di acquisto da fattura |:heavy_check_mark:|
|04| Articoli | Aggiorna unità di misura |:heavy_check_mark:|
|04| Articoli | Aggiorna conto predefinito di acquisto |:heavy_check_mark:|
|04| Articoli | Aggiorna conto predefinito di vendita |:heavy_check_mark:|
|04| Articoli | Imposta una provvigione |:heavy_check_mark:|
|04| Articoli | Aggiungi a listino cliente |:heavy_check_mark:|
|04| Articoli | Elimina selezionati |:heavy_check_mark:|
|36| Listini | Copia listini |:heavy_check_mark:|
|36| Listini | Aggiorna prezzo unitario |:heavy_check_mark:|
|09| Ddt in uscita | Fattura ddt in uscita |:heavy_check_mark:|
|09| Ddt in uscita | Cambia stato |:heavy_check_mark:|
|09| Ddt in uscita | Elimina selezionati |:heavy_check_mark:|
|08| Ddt in entrata | Fattura ddt in entrata |:heavy_check_mark:|
|08| Ddt in entrata | Cambia stato |:heavy_check_mark:|
|08| Ddt in entrata | Elimina selezionati |:heavy_check_mark:|
|40| Impianti | Esporta selezionati | |
|40| Impianti | Elimina selezionati |:heavy_check_mark:|

