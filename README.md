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

## Stato di avanzamento

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
|06| Fatture di acquisto |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-|
|07| Fatture di vendita |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:| + nota di credito
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
|30| Voci servizio |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-|:heavy_check_mark:|-|
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
|42| Statistiche |-|-|-|-|-|-|
|43| Mappa |-|-|-|-|-|-|
|44| Campi personalizzati |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-|:heavy_check_mark:|-|
|45| Viste |-|-|-|-|-|-|
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
