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
| Modulo | Descrizione | Stato |
|--------|-------------|:-------:|
| Anagrafiche | Crea nuova anagrafica per ogni tipologia |:heavy_check_mark: |
| - Relazioni | 
| - Zone | 
| Gestione email |
| - Newsletter | Crea una nuova Newsletter | :heavy_check_mark: |
| - Coda di invio |
| - Template email | Crea un nuovo template email | :heavy_check_mark: |
| - Account email | 
| Gestione documentale | Crea un nuovo documento | :heavy_check_mark: |
| - Categorie documenti | Crea una nuova categoria documenti |:heavy_check_mark: |
| Attività | Crea un nuovo intervento | :heavy_check_mark: |
| - Tipi di attività |
| - Fasce orarie |
| - Stati di attività |
| - Tecnici e tariffe |
| Vendite | 
| - Preventivi | Crea un preventivo |:heavy_check_mark: |
| - Contratti | Crea un nuovo contratto |:heavy_check_mark: |
| - Ordini cliente | Crea un nuovo ordine cliente | :heavy_check_mark: |
| - Fatture di vendita | Crea una nuova fattura di vendita e una nota di credito |:heavy_check_mark: |
| Acquisti |
| - Ordini fornitore | Crea un nuovo ordine fornitore| :heavy_check_mark: |
| - Fatture di acquisto |Crea una nuova fattura di acquisto| :heavy_check_mark: |
| Contabilità |
| - Stampe contabili |
| - Prima nota |
| - Piano dei conti |
| - Scadenzario | Crea una nuova scadenza | :heavy_check_mark: |
| Magazzino |
| - Articoli | Crea un nuovo articolo | :heavy_check_mark: |
| - Movimenti | Crea un nuovo movimento | :heavy_check_mark: |
| - Listini |
| - Piani di sconto/magg. | Crea un nuovo piano | :heavy_check_mark: |
| - Ddt in uscita | Crea un nuovo Ddt|:heavy_check_mark: |
| - Ddt in entrata | Crea un nuovo Ddt|:heavy_check_mark: |
| - Giacenza sedi |
| - Attributi Combinazioni |
| - Combinazioni |
| Impianti | Crea un nuovo impianto | :heavy_check_mark: |
| - Categorie impianti |
| Strumenti |
| - Tabelle |
| -- Tipi di spedizione |
| -- Eventi |
| -- Tipi documento |
| -- Causali movimenti |
| -- Tipi scadenze |
| -- Stati dei contratti |
| -- Stati dei preventivi |
| -- Ritenute previdenziali |
| -- Casse previdenziali |
| -- IVA |
| -- Modelli prima nota |
| -- Banche | Crea una nuova banca | :heavy_check_mark: |
| -- Ritenute acconto |
| -- Categorie articoli |
| -- Pagamenti |
| -- Porto |
| -- Unità di misura |
| -- Aspetto beni |
| -- Causali |
| -- Mansioni referenti |
| - Segmenti |
| - Import |
| - Checklists |
| - Utenti e permessi |
| - Backup |
| - Aggiornamenti |