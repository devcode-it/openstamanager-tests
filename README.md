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
|03| Dashboard |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-|:heavy_check_mark:|-|
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
|14| Movimenti |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-|:heavy_check_mark:|-|
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
|--|-------- | -------| :---------------: | :------: | :-----------: |:--:| ---------- |
|02| Anagrafiche | Referenti |:heavy_check_mark:|:x:|:x:|:heavy_check_mark:|-|
|02| Anagrafiche | Sedi aggiuntive |:heavy_check_mark:|:x:|:x:|:heavy_check_mark:|-|
|02| Anagrafiche | Statistiche |-|-|-|:heavy_check_mark:|-|
|02| Anagrafiche | Dichiarazione d'intento |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:| Fattura di vendita |
|02| Anagrafiche | Assicurazione crediti |:heavy_check_mark:|:heavy_check_mark:| :heavy_check_mark:| :heavy_check_mark:| Fattura di vendita |
|04| Articoli | Serial |:heavy_check_mark:|-|:heavy_check_mark:|:heavy_check_mark:|-|
|04| Articoli | Provvigioni |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|:x:|-|
|04| Articoli | Listino fornitori |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:| :x: |-|
|04| Articoli | Giacenze |-|-|-|:heavy_check_mark:|-|
|04| Articoli | Movimenti |-|-|-|:heavy_check_mark:|-|
|04| Articoli | Statistiche |-|-|-|:heavy_check_mark:|-|
|04| Articoli | Netto clienti |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|:x:|-|
|04| Articoli | Varianti articolo | - | - | - |:heavy_check_mark:| Attributi e combinazioni |
|05| Anagrafiche | Storico attività |-|-|-|:heavy_check_mark:|-|
|06| Fatture di acquisto | Registrazioni |-|-|-|:heavy_check_mark:|-|
|06| Fatture di acquisto | Movimenti contabilili |-|-|-|:heavy_check_mark:|-|
|07| Fatture di vendita | Movimenti contabilili |-|-|-|:heavy_check_mark:|-|
|07| Anagrafiche | Movimenti contabili |-|-|-|:heavy_check_mark:|-|
|07| Anagrafiche | Regole pagamenti |:heavy_check_mark:|:x:|:heavy_check_mark:|:heavy_check_mark:|controllo in scadenzario|
|07| Fatture di vendita | Registrazioni |-|-|-|:heavy_check_mark:|-|
|07| Anagrafiche | Allegati |-|-|-|:heavy_check_mark:|-|
|07| Articoli | Statistiche vendita |-|-|-|:heavy_check_mark:|-|
|09| Anagrafiche | Ddt del cliente |-|-|-|:heavy_check_mark:|-|
|11| Ordini cliente | Consuntivo |-|-|-|:heavy_check_mark:|-|

|12| Anagrafiche | Contratti del cliente |-|-|-|:heavy_check_mark:|-|
|12| Contratti | Consuntivo |-|-|-|:heavy_check_mark:|-|
|12| Contratti | Pianificazione attività |:heavy_check_mark:|:x:|:x:|:heavy_check_mark:|-|
|12| Contratti | Rinnovi |:heavy_check_mark:|-|:heavy_check_mark:|-|-|
|12| Contratti | Pianificazione fatturazione |:heavy_check_mark:|-|-|:heavy_check_mark:|controllo in Fatture e widget Dashboard|
|13| Preventivi | Consuntivo |-|-|-|:heavy_check_mark:|-|
|13| Preventivi | Revisioni |-|-|-|:heavy_check_mark:|-|
|35| Articoli | Piani di sconto/maggiorazione |-|-|-|:heavy_check_mark:|-|
|40| Impianti | Interventi svolti |-|-|-|:heavy_check_mark:|-|
|40| Impianti | Componenti |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-|
|40| Anagrafiche | Impianti del cliente |-|-|-|:heavy_check_mark:|-|
|40| Attività | Impianti |:heavy_check_mark:|:x:|:heavy_check_mark:|:heavy_check_mark:|:x: (controllo impianti interventi svolti)|
|:x:| Fatture di vendita | Fatturazione elettronica |:x:|:x:|:x:|:x:|:x:|
|:x:| Scadenzario | Presentazioni bancarie |:x:|:x:|:x:|:x:|:x:|


## Azioni di gruppo

Legenda:
- ☑️ Verifica

|N°| Modulo  | Azioni di gruppo | ☑️ |
|--|-------- | ---------------- |:--:|
|02| Anagrafiche  | Ricerca coordinate |:heavy_check_mark:|
|02| Anagrafiche  | Elimina selezionati |:heavy_check_mark:|
|02| Anagrafiche  | Cambia relazione |:heavy_check_mark:|
|04| Articoli | Aggiorna prezzo di acquisto |:heavy_check_mark:|
|04| Articoli | Aggiorna prezzo di vendita |:heavy_check_mark:|
|04| Articoli | Aggiorna coefficiente di vendita |:heavy_check_mark:|
|04| Articoli | Aggiorna quantità |:heavy_check_mark:|
|04| Articoli | Crea preventivo |:heavy_check_mark:|
|04| Articoli | Aggiorna aliquota iva |:heavy_check_mark:|
|04| Articoli | Aggiorna unità di misura |:heavy_check_mark:|
|04| Articoli | Aggiorna conto predefinito di acquisto |:heavy_check_mark:|
|04| Articoli | Aggiorna conto predefinito di vendita |:heavy_check_mark:|
|04| Articoli | Imposta una provvigione |:heavy_check_mark:|
|04| Listini | Aggiorna prezzo unitario |:heavy_check_mark:|
|04| Listini | Copia listini |:heavy_check_mark:|
|04| Articoli | Imposta prezzo di acquisto da fattura |:heavy_check_mark:|
|04| Articoli | Stampa etichette |:heavy_check_mark:|
|04| Articoli | Elimina selezionati |:heavy_check_mark:|
|05| Attività | Cambia stato |:heavy_check_mark:|
|05| Attività | Duplica attività |:heavy_check_mark:|
|05| Attività | Elimina selezionati |:heavy_check_mark:|
|05| Attività | Firma interventi  |:heavy_check_mark:|
|05| Attività | Fattura attività |:heavy_check_mark:|
|05| Attività | Stampa riepilogo |:heavy_check_mark:|
|06| Fatture di acquisto | Cambia sezionale |:heavy_check_mark:|
|06| Fatture di acquisto | Duplica selezionati |:heavy_check_mark:|
|06| Fatture di acquisto | Registrazione contabile |:heavy_check_mark:|
|06| Fatture di acquisto | Elimina selezionati |:heavy_check_mark:|
|07| Fatture di vendita | Cambia sezionale |:heavy_check_mark:|
|07| Fatture di vendita | Duplica selezionati |:heavy_check_mark:|
|07| Fatture di vendita | Emetti fatture |:heavy_check_mark:|
|07| Fatture di vendita | Controlla fatture elettroniche |:heavy_check_mark:|
|07| Fatture di vendita | Registrazione contabile |:heavy_check_mark:|
|07| Fatture di vendita | Genera fatture elettroniche |:heavy_check_mark:|
|07| Fatture di vendita | Elimina selezionati |:heavy_check_mark:|
|08| Ddt in entrata | Cambia stato |:heavy_check_mark:|
|08| Ddt in entrata | Fattura ddt in entrata |:heavy_check_mark:|
|08| Ddt in entrata | Elimina selezionati |:heavy_check_mark:|
|09| Ddt in uscita | Cambia stato |:heavy_check_mark:|
|09| Ddt in uscita | Fattura ddt in uscita |:heavy_check_mark:|
|09| Ddt in uscita | Elimina selezionati |:heavy_check_mark:|
|10| Ordini fornitore | Cambia stato |:heavy_check_mark:|
|11| Ordini cliente | Cambia stato |:heavy_check_mark:|
|11| Ordini cliente | Fattura ordini cliente |:heavy_check_mark:|

|12| Contratti | Fattura contratti |:heavy_check_mark:|
|12| Contratti | Rinnova contratti |:heavy_check_mark:|
|12| Contratti | Cambia stato |:heavy_check_mark:|
|13| Preventivi | Fattura preventivi |:heavy_check_mark:|
|13| Preventivi | Cambia stato |:heavy_check_mark:|
|23| Attività | Invia mail |:heavy_check_mark:|
|32| Prima nota | Esporta PDF | |
|34| Scadenzario | Registrazione contabile |:heavy_check_mark:|
|34| Scadenzario | Invia mail sollecito | |
|34| Scadenzario | Info distinta |:heavy_check_mark:|
|40| Impianti | Esporta selezionati | |
|40| Impianti | Elimina selezionati |:heavy_check_mark:|
|58| Fatture di vendita | Aggiorna banca |:heavy_check_mark:|
|58| Fatture di acquisto | Aggiorna banca |:heavy_check_mark:|
|58| Scadenzario | Aggiorna banca |:heavy_check_mark:|
|72| Anagrafiche  | Aggiorna listino cliente |:heavy_check_mark:|
|:x:| Anagrafiche  | Esporta selezionati |:x:|
|:x:| Articoli | Esporta selezionati |:x:|
|:x:| Articoli | Aggiorna categoria e sottocategoria |:x:|
|:x:| Articoli | Aggiungi a listino cliente |:x:|
|:x:| Attività | Esporta stampe |:x:|
|:x:| Fatture di acquisto | Esporta selezionati |:x:|
|:x:| Fatture di acquisto | Esporta stampa FE |:x:|
|:x:| Fatture di acquisto | Esporta ricevute |:x:|
|:x:| Fatture di acquisto | Esporta XML |:x:|
|:x:| Fatture di vendita | Esporta stampe |:x:|
|:x:| Fatture di vendita | Esporta stampe FE |:x:|
|:x:| Fatture di vendita | Esporta ricevute |:x:|
|:x:| Fatture di vendita | Esporta XML |:x:|
|:x:| Fatture di vendita | Coda di invio FE |:x:|
|:x:| Ordini cliente | Unisci RDO |:x:|

## Impostazioni

Legenda:
- ☑️ Verifica
- :question: Funzionamento

| Sezione | Nome | ☑️ | :question: |
|---------|------|:-:|:----------:| 
| Aggiornamenti | Attiva aggiornamenti |-|-|
| Aggiornamenti | Abilita canale pre-release per aggiornamenti |-|-| 
| Anagrafiche | Formato codice anagrafica |:heavy_check_mark:|Crea anagrafica| 
| API | Lunghezza pagine per API|:x:|:x:|
| API | apilayer API key for VAT number|:x:|:x:|
| Attività | Mostra i prezzi al tecnico |:heavy_check_mark:|Crea attività|
| Attività | Stampa per anteprima e firma | ||
| Attività | Permetti inserimento sessioni degli altri tecnici |:heavy_check_mark:|Crea attività|
| Attività | Giorni lavorativi |:heavy_check_mark:|Calendario|
| Attività | Notifica al tecnico l'aggiunta della sessione nell'attività |:heavy_check_mark:|Aggiungi sessione di lavoro|
| Attività | Notifica al tecnico la rimozione della sessione dall'attività |:heavy_check_mark:|Elimina sessione di lavoro|
| Attività | Stato dell'attività dopo la firma |:heavy_check_mark:|Crea attività e firma attività|
| Attività | Espandi automaticamente la sezione "Dettagli aggiuntivi" |:heavy_check_mark:|Crea attività|
| Attività | Alert occupazione tecnici |:heavy_check_mark:|Crea attività|
| Attività | Verifica numero intervento |:heavy_check_mark:|Crea attività|
| Attività | Formato ore in stampa |:heavy_check_mark:|Stampa intervento|
| Attività | Notifica al tecnico l'assegnazione all'attività |:heavy_check_mark:|Aggiungi assegnazione|
| Attività | Notifica al tecnico la rimozione dell'assegnazione dall'attività |:heavy_check_mark:|Elimina assegnazione|
| Attività | Descrizione personalizzata in fatturazione |:heavy_check_mark:|Fattura attività|
| Attività | Stato predefinito dell'attività da Dashboard |:heavy_check_mark:|Crea attività|
| Attività | Stato predefinito dell'attività |:heavy_check_mark:|Crea attività|
| Attività | Numero di minuti di avanzamento delle sessioni delle attività |-|-|
| Backup | Numero di backup da mantenere |-|-|
| Backup | Backup automatico |-|-|
| Contratti | "Condizioni generali di fornitura contratti" |:heavy_check_mark:|Crea contratto|
| Contratti | Crea contratto rinnovabile di default |:heavy_check_mark:|Crea contratto|
| Contratti | Giorni di preavviso di default |:heavy_check_mark:|Crea contratto|
| Dashboard | Utilizzare i tooltip sul calendario | ||
| Dashboard | Visualizzare la domenica sul calendario |:heavy_check_mark:|Calendario|
| Dashboard | Vista dashboard |:heavy_check_mark:|Calendario|
| Dashboard | Ora inizio sul calendario |:heavy_check_mark:|Calendario|
| Dashboard | Ora fine sul calendario |:heavy_check_mark:|Calendario|
| Dashboard | Visualizza informazioni aggiuntive sul calendario |:heavy_check_mark:|Calendario|
| Dashboard | Visualizzazione colori sessioni |:heavy_check_mark:|Calendario|
| Dashboard | Tempo predefinito di snap attività sul calendario | ||
| Ddt| Cambia automaticamente stato ddt fatturati |:heavy_check_mark:|Crea ddt sia in entrata che in uscita|
| Fatturazione | Iva predefinita |:heavy_check_mark:|Crea fattura|
| Fatturazione | Tipo di pagamento predefinito |:heavy_check_mark:|Crea fattura|
| Fatturazione | Ritenuta d'acconto predefinita |:heavy_check_mark:|Aggiungi riga|
| Fatturazione | Cassa previdenziale predefinita |:heavy_check_mark:|Crea anagrafica|
| Fatturazione | Importo marca da bollo |:heavy_check_mark:|Aggiungi riga|
| Fatturazione | Soglia minima per l'applicazione della marca da bollo |:heavy_check_mark:|Aggiungi riga|
| Fatturazione | Conto aziendale predefinito |:x:|:x:|
| Fatturazione | Conto predefinito fatture di vendita |:heavy_check_mark:|Aggiungi riga|
| Fatturazione | Conto predefinito fatture di acquisto |:heavy_check_mark:|Aggiungi riga|
| Fatturazione | "Dicitura fissa fattura" | ||
| Fatturazione | Metodologia calcolo ritenuta d'acconto predefinito | ||
| Fatturazione | Ritenuta previdenziale predefinita |:heavy_check_mark:|Crea fattura|
| Fatturazione | Descrizione addebito bollo |:heavy_check_mark:|Crea fattura|
| Fatturazione | Conto predefinito per la marca da bollo |:heavy_check_mark:|Crea fattura|
| Fatturazione | Iva per lettere d'intento |:heavy_check_mark:|Crea fattura|
| Fatturazione | Utilizza prezzi di vendita comprensivi di IVA |:heavy_check_mark:|Crea articolo e fatturazione|
| Fatturazione | Liquidazione iva |:heavy_check_mark:|Stampe contabili|
| Fatturazione | Conto anticipo clienti | ||
| Fatturazione | Conto anticipo fornitori | ||
| Fatturazione | Descrizione fattura pianificata |:heavy_check_mark:|Crea fattura pianificata|
| Fatturazione | Aggiorna info di acquisto | ||
| Fatturazione | Bloccare i prezzi inferiori al minimo di vendita | ||
| Fatturazione | Permetti fatturazione delle attività collegate a contratti |:heavy_check_mark:|Crea attività e contratto|
| Fatturazione | Data emissione fattura automatica  | ||
| Fatturazione | Permetti fatturazione delle attività collegate a ordini |:heavy_check_mark:|Crea attività e ordine|
| Fatturazione | Permetti fatturazione delle attività collegate a preventivi | ||
| Fatturazione | Data inizio verifica contatore fattura di vendita | ||
| Fatturazione | Raggruppa attività per tipologia in fattura | ||
| Fatturazione Elettronica | Allega stampa per fattura verso Privati |:heavy_check_mark:|Crea fattura|
| Fatturazione Elettronica | Allega stampa per fattura verso Aziende |:heavy_check_mark:|Crea fattura|
| Fatturazione Elettronica | Allega stampa per fattura verso PA |:heavy_check_mark:|Crea fattura|
| Fatturazione Elettronica | Regime Fiscale |:heavy_check_mark:|Apri fattura elettronica|
| Fatturazione Elettronica | Tipo Cassa Previdenziale |:heavy_check_mark:|Apri fattura elettronica|
| Fatturazione Elettronica | Causale ritenuta d'acconto |:heavy_check_mark:|Apri fattura elettronica|
| Fatturazione Elettronica | Authorization ID Indice PA | ||
| Fatturazione Elettronica | OSMCloud Services API Token | ||
| Fatturazione Elettronica | Terzo intermediario | ||
| Fatturazione Elettronica | Riferimento dei documenti in Fattura Elettronica |:heavy_check_mark:|Apri fattura elettronica|
| Fatturazione Elettronica | OSMCloud Services API URL | ||
| Fatturazione Elettronica | OSMCloud Services API Version | ||
| Fatturazione Elettronica | Data inizio controlli su stati FE | ||
| Fatturazione Elettronica | Movimenta magazzino da fatture di acquisto | ||
| Fatturazione Elettronica | Rimuovi avviso fatture estere | ||
| Fatturazione Elettronica | Creazione seriali in import FE | ||
| Fatturazione Elettronica | Giorni validità fattura scartata | ||
| Generali | Azienda predefinita | ||
| Generali | Nascondere la barra sinistra di default |:heavy_check_mark:|Impostazioni|
| Generali | Cifre decimali per importi |:heavy_check_mark:|Crea fattura|
| Generali | CSS Personalizzato | ||
| Generali | Attiva notifica di presenza utenti sul record | ||
| Generali | Timeout notifica di presenza (minuti) | ||
| Generali | Prima pagina |:heavy_check_mark:|Anagrafiche|
| Generali | Cifre decimali per quantità |:heavy_check_mark:|Crea fattura|
| Generali | Tempo di attesa ricerche in secondi | ||
| Generali | Logo stampe | ||
| Generali | Abilita esportazione Excel e PDF |:heavy_check_mark:|Esporta fattura|
| Generali | Valuta |:heavy_check_mark:|Apro fattura|
| Generali | Visualizza riferimento su ogni riga in stampa |:heavy_check_mark:|Stampa fattura|
| Generali | Lunghezza in pagine del buffer Datatables | ||
| Generali | Autocompletamento form | ||
| Generali | Filigrana stampe | ||
| Generali | Attiva scorciatoie da tastiera | ||
| Generali | Modifica Viste di default | ||
| Generali | Totali delle tabelle ristretti alla selezione | ||
| Generali | Nascondere la barra dei plugin di default |:x:|:x:|
| Generali | Soft quota | ||
| Generali | Permetti selezione articoli con quantità minore o uguale a zero in Documenti di Vendita |:heavy_check_mark:|Crea fattura|
| Generali | Inizio periodo calendario |:heavy_check_mark:|Dashboard|
| Generali | Fine periodo calendario |:heavy_check_mark:|Dashboard|
| Generali | Permetti il superamento della soglia quantità dei documenti di origine |:heavy_check_mark:|Crea attività, preventivo, contratto, ddt, ordine, fattura|
| Generali | Aggiungi riferimento tra documenti |:heavy_check_mark:|Aggiungi ddt in fattura|
| Generali | Mantieni riferimenti tra tutti i documenti collegati | ||
| Generali | Aggiungi le note delle righe tra documenti |:heavy_check_mark:|Fattura preventivo|
| Generali | Dimensione widget predefinita |:heavy_check_mark:|Dashboard|
| Generali | Posizione del simbolo valuta | ||
| Generali | Tile server OpenStreetMap | ||
| Generali | Sistema di firma | ||
| Generali | Tipo di sconto predefinito |:heavy_check_mark:|Crea fattura|
| Generali | Cifre decimali per importi in stampa |:heavy_check_mark:|Stampa fattura|
| Generali | Cifre decimali per quantità in stampa |:heavy_check_mark:|Stampa fattura|
| Generali | Cifre decimali per totali in stampa |:heavy_check_mark:|Stampa fattura|
| Generali | Listino cliente predefinito |:heavy_check_mark:|Crea anagrafica|
| Generali | Lingua |:heavy_check_mark:|Impostazioni|
| Generali | Ridimensiona automaticamente le immagini caricate | ||
| Generali | Larghezza per ridimensionamento immagini | ||
| Magazzino | Movimenta il magazzino durante l'inserimento o eliminazione dei lotti/serial number | ||
| Magazzino | Serial number abilitato di default |:heavy_check_mark:|Crea articolo|
| Magazzino | Magazzino cespiti | ||
| Mail | Numero di giorni mantenimento coda di invio | ||
| Newsletter | Numero massimo di tentativi | ||
| Newsletter | Numero email da inviare in contemporanea per account | ||
| Ordini | Cambia automaticamente stato ordini fatturati |:heavy_check_mark:|Fattura ordine|
| Ordini | Conferma automaticamente le quantità negli ordini cliente |:heavy_check_mark:|Crea ordine cliente|
| Ordini | Conferma automaticamente le quantità negli ordini fornitore |:heavy_check_mark:|Crea ordine fornitore|
| Ordini | Visualizza numero ordine cliente | ||
| Piano dei conti | Conto per Riepilogativo fornitori | ||
| Piano dei conti | Conto per Riepilogativo clienti | ||
| Piano dei conti | Conto per Iva indetraibile | ||
| Piano dei conti | Conto per Iva su vendite | ||
| Piano dei conti | Conto per Iva su acquisti | ||
| Piano dei conti | Conto per Erario c/ritenute d'acconto | ||
| Piano dei conti | Conto per Erario c/INPS | ||
| Piano dei conti | Conto per Erario c/enasarco | ||
| Piano dei conti | Conto per Apertura conti patrimoniali | ||
| Piano dei conti | Conto per Chiusura conti patrimoniali | ||
| Piano dei conti | Conto per autofattura | ||
| Piano dei conti | Conto di secondo livello per i crediti clienti | ||
| Piano dei conti | Conto di secondo livello per i debiti fornitori | ||
| Preventivi | "Condizioni generali di fornitura preventivi" |:heavy_check_mark:|Stampa preventivo|
| Preventivi | Conferma automaticamente le quantità nei preventivi |:heavy_check_mark:|Aggiungi articolo|
| Preventivi | Esclusioni default preventivi |:heavy_check_mark:|Crea preventivo|
| Scadenzario | Invio solleciti in automatico | ||
| Scadenzario | Template email primo sollecito | ||
| Scadenzario | Ritardo in giorni della scadenza della fattura per invio sollecito pagamento | ||
| Scadenzario | Ritardo in giorni dall'ultima email per invio sollecito pagamento | ||
| Scadenzario | Template email secondo sollecito | ||
| Scadenzario | Template email terzo sollecito | ||
| Scadenzario | Template email mancato pagamento dopo i solleciti | ||
| Scadenzario | Indirizzo email mancato pagamento dopo i solleciti | ||
| Scadenzario | Template email promemoria scadenza | ||
| Scadenzario | Intervallo di giorni in anticipo per invio promemoria scadenza | ||