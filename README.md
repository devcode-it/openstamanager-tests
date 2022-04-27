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
 Modulo  | :eye:|:heavy_plus_sign:| :pencil:|:wastebasket:|:bookmark_tabs: | Note |
-------- | :----:|:----------------:|:-------:|:-----------:|:--------------:|:---:|
 Dashboard  | :heavy_check_mark: |||-|-||
 Anagrafiche  | :heavy_check_mark: |:heavy_check_mark: | :heavy_check_mark:|:heavy_check_mark: |-||
 » Relazioni  | :heavy_check_mark: |  :heavy_check_mark: |:heavy_check_mark:|:heavy_check_mark:|-||
 » Zone  | :heavy_check_mark: | :heavy_check_mark: |:heavy_check_mark:|:heavy_check_mark:|-||
 Gestione email  | :heavy_check_mark:|-|-|-|-||
 » Newsletter  | :heavy_check_mark: |:heavy_check_mark: |:heavy_check_mark:|:heavy_check_mark:|-||
 » Coda di invio  | :heavy_check_mark: |-|-|-|-||
 » Template email  | :heavy_check_mark: |  :heavy_check_mark: |:heavy_check_mark:|:heavy_check_mark:|-||
 » Account email  | :heavy_check_mark: | :heavy_check_mark: |:heavy_check_mark:|:heavy_check_mark:|-||
 Gestione documentale  | :heavy_check_mark: | :heavy_check_mark: |:heavy_check_mark:|:heavy_check_mark:|-||
 » Categorie documenti  | :heavy_check_mark: |:heavy_check_mark: |:heavy_check_mark: |:heavy_check_mark: |-||
 Attività  | :heavy_check_mark: |  :heavy_check_mark: |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark: ||
 » Tipi di attività  | :heavy_check_mark: | :heavy_check_mark: |:heavy_check_mark:|:heavy_check_mark:|-||
 » Fasce orarie  | :heavy_check_mark: | :heavy_check_mark: |:heavy_check_mark:|:heavy_check_mark:|-||
 » Stati di attività  | :heavy_check_mark: | :heavy_check_mark: |:heavy_check_mark:|:heavy_check_mark:|-||
 » Tecnici e tariffe |:heavy_check_mark:|-|:heavy_check_mark:|-|-||
 Vendite  | :heavy_check_mark:| -|-|-|-||
 » Preventivi  | :heavy_check_mark: | :heavy_check_mark: |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark: ||
 » Contratti  | :heavy_check_mark: | :heavy_check_mark: |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark: ||
 » Ordini cliente  | :heavy_check_mark: |  :heavy_check_mark: |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark: ||
 » Fatture di vendita  | :heavy_check_mark: | :heavy_check_mark:  | :heavy_check_mark:| :heavy_check_mark: |:heavy_check_mark: | Fattura + Nota di credito|
 Acquisti  | :heavy_check_mark: |-|-|-|-||
 » Ordini fornitore  | :heavy_check_mark: |:heavy_check_mark: |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark: ||
 » Fatture di acquisto  | :heavy_check_mark: |:heavy_check_mark: |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark: ||
 Contabilità  |:heavy_check_mark:|-|-|-|-||
 » Stampe contabili  | :heavy_check_mark: | -|-|-|-||
 » Prima nota  | :heavy_check_mark: |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-||
 » Piano dei conti  | :heavy_check_mark: | -|-|-|-||
 » Scadenzario  | :heavy_check_mark: | :heavy_check_mark: |:heavy_check_mark:|:heavy_check_mark:|-||
 Magazzino  | :heavy_check_mark: |-|-|-|-||
 » Articoli  | :heavy_check_mark: | :heavy_check_mark: |:heavy_check_mark:|:heavy_check_mark:|-||
 » Movimenti  | :heavy_check_mark: | :heavy_check_mark: |-|:heavy_check_mark:  |-||
 » Listini  | :heavy_check_mark: | - |-|-|-||
 » Piani di sconto/magg.  | :heavy_check_mark: |  :heavy_check_mark: |:heavy_check_mark: |:heavy_check_mark: |-||
 » Ddt in uscita  | :heavy_check_mark: |:heavy_check_mark: |:heavy_check_mark: |:heavy_check_mark: |:heavy_check_mark: ||
 » Ddt in entrata  | :heavy_check_mark: | :heavy_check_mark: |:heavy_check_mark: |:heavy_check_mark: |:heavy_check_mark: ||
 » Giacenze sedi  | :heavy_check_mark: |-|-|-|-||
 » Attributi Combinazioni  | :heavy_check_mark: |:heavy_check_mark: |:heavy_check_mark:|:heavy_check_mark:|-||
 » Combinazioni  | :heavy_check_mark: | :heavy_check_mark: |:heavy_check_mark:|:heavy_check_mark:|-||
 Impianti  | :heavy_check_mark: |  :heavy_check_mark: |:heavy_check_mark:|:heavy_check_mark:|-||
 » Categorie impianti  | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark:| :heavy_check_mark:|-||
 » Statistiche | :heavy_check_mark: | - | -| -|-||
 Strumenti  | - |-|-|-|-||
 » Tabelle  | - |-|-|-|-||
 »» Tipi di spedizione  | :heavy_check_mark: | :heavy_check_mark: |:heavy_check_mark:|:heavy_check_mark:|-||
 »» Eventi  | :heavy_check_mark: |:heavy_check_mark: |:heavy_check_mark:|:heavy_check_mark:|-||
 »» Tipi documento  | :heavy_check_mark: | :heavy_check_mark: |:heavy_check_mark:|:heavy_check_mark:|-||
 »» Causali movimenti  | :heavy_check_mark: | :heavy_check_mark: |:heavy_check_mark: |:heavy_check_mark: |-||
 »» Tipi scadenze  | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark:| :heavy_check_mark:|-||
 »» Stati dei contratti  | :heavy_check_mark: | :heavy_check_mark: |:heavy_check_mark:|:heavy_check_mark:|-||
 »» Stati dei preventivi  | :heavy_check_mark: | :heavy_check_mark: |:heavy_check_mark:|:heavy_check_mark:|-||
 »» Ritenute previdenziali  | :heavy_check_mark: | :heavy_check_mark: |:heavy_check_mark:|:heavy_check_mark:|-||
 »» Casse previdenziali  | :heavy_check_mark: | :heavy_check_mark: |:heavy_check_mark:|:heavy_check_mark:|-||
 »» IVA  | :heavy_check_mark: | :heavy_check_mark: |:heavy_check_mark:|:heavy_check_mark:|-||
 »» Modelli prima nota  | :heavy_check_mark: |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-||
 »» Banche  | :heavy_check_mark: |  :heavy_check_mark: |:heavy_check_mark:|:heavy_check_mark:|-||
 »» Ritenute acconto  | :heavy_check_mark: |:heavy_check_mark: |:heavy_check_mark:|:heavy_check_mark:|-||
 »» Categorie articoli  | :heavy_check_mark: | :heavy_check_mark: |:heavy_check_mark:|:heavy_check_mark:|-||
 »» Pagamenti  | :heavy_check_mark: | :heavy_check_mark: |:heavy_check_mark:|:heavy_check_mark:|-||
 »» Porto  | :heavy_check_mark: | :heavy_check_mark: |:heavy_check_mark:|:heavy_check_mark:|-||
 »» Unità di misura  | :heavy_check_mark: |:heavy_check_mark: |:heavy_check_mark:|:heavy_check_mark:|-||
 »» Aspetto beni  | :heavy_check_mark: | :heavy_check_mark: |:heavy_check_mark:|:heavy_check_mark:|-||
 »» Causali  | :heavy_check_mark: |:heavy_check_mark: |:heavy_check_mark:|:heavy_check_mark:|-||
 »» Mansioni referenti  | :heavy_check_mark: | :heavy_check_mark: |:heavy_check_mark:|:heavy_check_mark:|-||
 » Impostazioni  | :heavy_check_mark: |-|-|-|-||
 » Segmenti  | :heavy_check_mark: | :heavy_check_mark: |:heavy_check_mark:|:heavy_check_mark:|-||
 » Import  | :heavy_check_mark: ||-|-|-||
 » Stato dei servizi  | :heavy_check_mark: |-|-|-|-||
 » Checklists  | :heavy_check_mark: |:heavy_check_mark: |:heavy_check_mark:|:heavy_check_mark:|-||
 » Utenti e permessi  | :heavy_check_mark: |:heavy_check_mark: |:heavy_check_mark:|:heavy_check_mark:|-||
 » Viste  | :heavy_check_mark: |-|-|-|-||
 » Backup  | :heavy_check_mark: |:heavy_check_mark: |-|-|-||
 » Aggiornamenti  | :heavy_check_mark: | -|-|-|-||