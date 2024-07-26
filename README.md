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
|05| Attività | Stampa riepilogo |:heavy_check_mark:|
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
|07| Fatture di vendita | Genera fatture elettroniche |:heavy_check_mark:|
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
|04| Articoli | Stampa etichette |:heavy_check_mark:|
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


## Impostazioni

Legenda:
- ☑️ Verifica
- :question: Funzionamento

| Nome | ☑️ | :question: |
|------|:-:|:----------:| 
| Attiva aggiornamenti | ||
| Abilita canale pre-release per aggiornamenti | ||
| Formato codice anagrafica |:heavy_check_mark:|Crea anagrafica|
| Lunghezza pagine per API | ||
| apilayer API key for VAT number | ||
| Google Maps API key per Tecnici | ||
| Mostra prezzi | ||
| Sincronizza solo i Clienti per cui il Tecnico ha lavorato in passato | ||
| Mesi per lo storico delle Attività | ||
| Abilita la modifica di altri tecnici | ||
| Visualizza promemoria | ||
| Visualizza solo promemoria assegnati | ||
| Permetti l'accesso agli amministratori | ||
| Limita la visualizzazione degli impianti a quelli gestiti dal tecnico | ||
| Mostra i prezzi al tecnico |:heavy_check_mark:|Crea attività|
| Stampa per anteprima e firma | ||
| Permetti inserimento sessioni degli altri tecnici |:heavy_check_mark:|Crea attività|
| Giorni lavorativi | ||
| Notifica al tecnico l'aggiunta della sessione nell'attività | ||
| Notifica al tecnico la rimozione della sessione dall'attività | ||
| Stato dell'attività dopo la firma |:heavy_check_mark:|Crea attività e firma attività|
| Espandi automaticamente la sezione "Dettagli aggiuntivi" |:heavy_check_mark:|Crea attività|
| Alert occupazione tecnici | ||
| Verifica numero intervento |:heavy_check_mark:|Crea attività|
| Formato ore in stampa |:heavy_check_mark:|Stampa intervento|
| Notifica al tecnico l'assegnazione all'attività | ||
| Notifica al tecnico la rimozione dell'assegnazione dall'attività | ||
| Descrizione personalizzata in fatturazione |:heavy_check_mark:||
| Stato predefinito dell'attività da Dashboard |:heavy_check_mark:|Crea attività|
| Stato predefinito dell'attività |:heavy_check_mark:|Crea attività|
| Numero di minuti di avanzamento delle sessioni delle attività | ||
| Numero di backup da mantenere | ||
| Backup automatico | ||
| Permetti il ripristino di backup da file esterni | ||
| "Condizioni generali di fornitura contratti" |:heavy_check_mark:|Crea contratto|
| Crea contratto rinnovabile di default |:heavy_check_mark:|Crea contratto|
| Giorni di preavviso di default |:heavy_check_mark:||
| Utilizzare i tooltip sul calendario | ||
| Visualizzare la domenica sul calendario |:heavy_check_mark:|Calendario|
| Vista dashboard |:heavy_check_mark:|Calendario|
| Ora inizio sul calendario |:heavy_check_mark:|Calendario|
| Ora fine sul calendario |:heavy_check_mark:|Calendario|
| Visualizza informazioni aggiuntive sul calendario |:heavy_check_mark:|Calendario|
| Visualizzazione colori sessioni | ||
| Tempo predefinito di snap attività sul calendario | ||
| Cambia automaticamente stato ddt fatturati |:heavy_check_mark:|Crea ddt sia in entrata che in uscita|
| Iva predefinita |:heavy_check_mark:|Crea fattura|
| Tipo di pagamento predefinito | ||
| Ritenuta d'acconto predefinita | ||
| Cassa previdenziale predefinita | ||
| Importo marca da bollo | ||
| Soglia minima per l'applicazione della marca da bollo | ||
| Conto aziendale predefinito | ||
| Conto predefinito fatture di vendita | ||
| Conto predefinito fatture di acquisto | ||
| "Dicitura fissa fattura" | ||
| Metodologia calcolo ritenuta d'acconto predefinito | ||
| Ritenuta previdenziale predefinita | ||
| Addebita marca da bollo al cliente | ||
| Descrizione addebito bollo | ||
| Conto predefinito per la marca da bollo | ||
| Iva per lettere d'intento | ||
| Utilizza prezzi di vendita comprensivi di IVA  | ||
| Liquidazione iva | ||
| Conto anticipo clienti | ||
| Conto anticipo fornitori | ||
| Descrizione fattura pianificata | ||
| Aggiorna info di acquisto | ||
| Sezionale per autofatture di vendita | ||
| Sezionale per autofatture di acquisto | ||
| Bloccare i prezzi inferiori al minimo di vendita | ||
| Permetti fatturazione delle attività collegate a contratti | ||
| Data emissione fattura automatica  | ||
| Permetti fatturazione delle attività collegate a ordini | ||
| Permetti fatturazione delle attività collegate a preventivi | ||
| Data inizio verifica contatore fattura di vendita | ||
| Raggruppa attività per tipologia in fattura | ||
| Allega stampa per fattura verso Privati | ||
| Allega stampa per fattura verso Aziende | ||
| Allega stampa per fattura verso PA | ||
| Regime Fiscale | ||
| Tipo Cassa Previdenziale | ||
| Causale ritenuta d'acconto | ||
| Authorization ID Indice PA | ||
| OSMCloud Services API Token | ||
| Terzo intermediario | ||
| Riferimento dei documenti in Fattura Elettronica | ||
| OSMCloud Services API URL | ||
| OSMCloud Services API Version | ||
| Data inizio controlli su stati FE | ||
| Movimenta magazzino da fatture di acquisto | ||
| Rimuovi avviso fatture estere | ||
| Creazione seriali in import FE | ||
| Giorni validità fattura scartata | ||
| Azienda predefinita | ||
| Nascondere la barra sinistra di default |:heavy_check_mark:|Impostazioni|
| Cifre decimali per importi |:heavy_check_mark:|Crea fattura|
| CSS Personalizzato | ||
| Attiva notifica di presenza utenti sul record | ||
| Timeout notifica di presenza (minuti) | ||
| Prima pagina | ||
| Cifre decimali per quantità | ||
| Tempo di attesa ricerche in secondi | ||
| Logo stampe | ||
| Abilita esportazione Excel e PDF | ||
| Valuta |:heavy_check_mark:|Apro fattura|
| Visualizza riferimento su ogni riga in stampa | ||
| Lunghezza in pagine del buffer Datatables | ||
| Autocompletamento form | ||
| Filigrana stampe | ||
| Attiva scorciatoie da tastiera | ||
| Modifica Viste di default | ||
| Totali delle tabelle ristretti alla selezione | ||
| Nascondere la barra dei plugin di default | ||
| Soft quota | ||
| Permetti selezione articoli con quantità minore o uguale a zero in Documenti di Vendita | ||
| Inizio periodo calendario |:heavy_check_mark:|Dashboard|
| Fine periodo calendario |:heavy_check_mark:|Dashboard|
| Permetti il superamento della soglia quantità dei documenti di origine | ||
| Aggiungi riferimento tra documenti | ||
| Mantieni riferimenti tra tutti i documenti collegati | ||
| Aggiungi le note delle righe tra documenti | ||
| Dimensione widget predefinita | ||
| Posizione del simbolo valuta | ||
| Tile server OpenStreetMap | ||
| Sistema di firma | ||
| Tipo di sconto predefinito | ||
| Cifre decimali per importi in stampa | ||
| Cifre decimali per quantità in stampa | ||
| Cifre decimali per totali in stampa | ||
| Listino cliente predefinito | ||
| Lingua |:heavy_check_mark:|Impostazioni|
| Ridimensiona automaticamente le immagini caricate | ||
| Larghezza per ridimensionamento immagini | ||
| Movimenta il magazzino durante l'inserimento o eliminazione dei lotti/serial n|umber | |
| Serial number abilitato di default | ||
| Magazzino cespiti | ||
| Numero di giorni mantenimento coda di invio | ||
| Numero massimo di tentativi | ||
| Numero email da inviare in contemporanea per account | ||
| Cambia automaticamente stato ordini fatturati | ||
| Conferma automaticamente le quantità negli ordini cliente | ||
| Conferma automaticamente le quantità negli ordini fornitore | ||
| Visualizza numero ordine cliente | ||
| Conto per Riepilogativo fornitori | ||
| Conto per Riepilogativo clienti | ||
| Conto per Iva indetraibile | ||
| Conto per Iva su vendite | ||
| Conto per Iva su acquisti | ||
| Conto per Erario c/ritenute d'acconto | ||
| Conto per Erario c/INPS | ||
| Conto per Erario c/enasarco | ||
| Conto per Apertura conti patrimoniali | ||
| Conto per Chiusura conti patrimoniali | ||
| Conto per autofattura | ||
| Conto di secondo livello per i crediti clienti | ||
| Conto di secondo livello per i debiti fornitori | ||
| "Condizioni generali di fornitura preventivi" | ||
| Conferma automaticamente le quantità nei preventivi | ||
| Esclusioni default preventivi | ||
| Invio solleciti in automatico | ||
| Template email primo sollecito | ||
| Ritardo in giorni della scadenza della fattura per invio sollecito pagamento || |
| Ritardo in giorni dall'ultima email per invio sollecito pagamento | ||
| Template email secondo sollecito | ||
| Template email terzo sollecito | ||
| Template email mancato pagamento dopo i solleciti | ||
| Indirizzo email mancato pagamento dopo i solleciti | ||
| Template email promemoria scadenza | ||
| Intervallo di giorni in anticipo per invio promemoria scadenza | ||
| Licenza Wacom SDK - Key | ||
| Sfondo firma tavoletta Wacom | ||
| Luminosità firma Wacom | ||
| Contrasto firma Wacom | ||
| Secondi timeout tavoletta Wacom | ||
| Licenza Wacom SDK - Secret | ||