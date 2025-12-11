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

## Funzionamento

I test simulano i comportamenti di un utente che usa il gestionale. Ad esempio la compilazione dei campi, la scrittura, i click, la verifica di risultati e tanto altro.

### Scrittura

Il nome del file di test deve avere il numero del file seguito dal trattino basso e dal nome del modulo, ad esempio:

`02_Anagrafiche.py`

Ogni test è dentro ad una classe che eredita da `Test` funzioni come `navigateTo`, `wait_loader`, `find`, ecc.

Il metodo `setUp` viene eseguito prima di ogni test e serve per aprire il browser, entrare nel gestionale e fare il login.

Ogni metodo dei test deve avere un nome che inizia con `test_` così da essere eseguito da pytest. Ad esempio:

` def test_distinta_base(self): `

Le verifiche vengono fatte tramite `assert`. Ad esempio, se dobbiamo cambiare lo stato di una fattura da *Bozza* a *Emessa*, potremo verificare questo cambiamento nella modalità seguente:

```python
stato = self.find((//tbody//tr[1]//td[7]//span)[2]).text
self.assertEqual(stato, "Emessa")
```

### Ricerca tramite XPath

XPath è un linguaggio usato per cercare elementi di una pagina HTML. Questo viene usato nei test per individuare gli elementi da cliccare, modificare, eliminare e altro.

Sintassi base:

- `//tag` → trova tutti gli elementi `<tag>` ovunque nella pagina
- `//tag[@attr="val"]` → trova elementi `<tag>` con attributo `attr` uguale a `val`
- `//div[@id="main"]` → trova un `<div>` con `id="main"`
- `//ul//li[1]` → trova il primo `<li>` dentro ogni `<ul>`
- `//span[contains(text(), 'ok')]` → trova `<span>` che contiene il testo “ok”
- `[1]` → seleziona il primo elemento
- `(xpath)[2]` → prende il secondo elemento dell’intero xpath (tra parentesi)

### I tempi di attesa

Quando si esegue un test, il codice è più veloce della pagina, quindi potresti cliccare su un bottone prima ancora che esso venga caricato.

Per evitare questo problema, si dovrà aspettare che la pagina o un elemento sia pronto.

I metodi principali sono:

- `sleep(n)` ha un’attesa fissa, va bene solo per casi banali.
- `self.wait_loader()` aspetta che sparisca il loader della pagina.
- `wait.until(EC.visibility_of_element_located(...))` aspetta fino a 10 secondi che l’elemento diventi visibile; appena è pronto, continua senza aspettare inutilmente.
- `modal = self.wait_modal()` aspetta che compaia un popup/modal dopo un click.

### Esempio

```python
def modifica_attivita_tecnico(self):
    wait = WebDriverWait(self.driver, 20)
    self.navigateTo("Disponibilità tecnici")
    self.wait_loader()

    self.find(By.XPATH, '(//div[@class="fc-timeline-event-harness"]//div)[1]').click()
    self.wait_loader()

    element = self.find(By.XPATH, '//input[@id="codice"]')
    element.clear()
    element.send_keys("3")
    self.find(By.XPATH, '//button[@id="save"]').click()
    self.wait_loader()

    self.navigateTo("Disponibilità tecnici")
    self.wait_loader()

    attivita=self.find(By.XPATH, '(//div[@class="fc-timeline-event-harness"]//div)[1]').text 
    self.assertEqual(attivita, "Int. 3 Cliente")
```

### Spiegazione passo passo

1. **Inizializza un'attesa esplicita**  
   Crea un oggetto `WebDriverWait` per sincronizzare il test con il caricamento degli elementi.

2. **Naviga al modulo "Disponibilità tecnici"**  
   Usa `self.navigateTo("Disponibilità tecnici")` per aprire il modulo.

3. **Aspetta che il loader sparisca**  
   `self.wait_loader()` evita di procedere finché la pagina non è completamente caricata.

4. **Clicca sul primo evento del calendario**  
   Trova e clicca il primo elemento del calendario tramite XPath.

5. **Aspetta nuovamente il caricamento**  
   Attende che la pagina o il popup siano pronti.

6. **Modifica il codice dell’attività**  
   - Trova il campo input con id `codice`.  
   - Cancella il contenuto attuale con `clear()`.  
   - Inserisce il nuovo codice `"3"`.

7. **Salva la modifica**  
   Clicca il pulsante SALVA.

8. **Aspetta il completamento del salvataggio**  
   Attende che l’operazione sia terminata.

9. **Ritorna al modulo "Disponibilità tecnici"**  
   Ricarica la pagina per verificare la modifica.

10. **Aspetta il caricamento della pagina**  
    Attende che la pagina sia pronta.

11. **Verifica il risultato**  
    - Recupera il testo del primo evento nel calendario.  
    - Controlla che corrisponda a `"Int. 3 Cliente"` con un `assertEqual`.

## Moduli

Legenda:
- :heavy_plus_sign: Crea
- :pencil: Modifica
- :wastebasket: Elimina
- :bookmark_tabs: Righe
- ☑️ Verifica

|N°| Modulo  | :heavy_plus_sign:| :pencil:|:wastebasket:|:bookmark_tabs: | ☑️ | Altro |
|--|-------- | :---------------:|:-------:|:-----------:|:--------------:|:--:|:-----:|
|00| Backup | :heavy_check_mark: |-|:x:|-|:x:|:x:|
|01| Stato dei servizi |-|:heavy_check_mark:|-|-|-|-|
|02| Anagrafiche | :heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-|:heavy_check_mark:| + creazione documenti |
|03| Dashboard |:heavy_check_mark:|-|-|-|:heavy_check_mark:|-|
|04| Articoli |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-|:heavy_check_mark:|-|
|05| Attività |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:| + duplica|
|06| Fatture di acquisto |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:| + autofattura|
|07| Fatture di vendita |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:| + nota di credito, duplica e autofattura
|08| DDT in entrata |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:| + duplica|
|09| DDT in uscita |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:| +duplica|
|10| Ordini fornitore |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-|
|11| Ordini cliente |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-|
|12| Contratti |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|+ duplica|
|13| Preventivi |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:| +duplica e creazione documenti|
|14| Movimenti |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-|:heavy_check_mark:|-|
|15| Attività - Dashboard |:heavy_check_mark:|-|-|-|:heavy_check_mark:| +trascinamento|
|16| Tipi anagrafiche |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-|:heavy_check_mark:|-|
|17| Relazioni |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-|:heavy_check_mark:|-|
|18| Zone |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-|:heavy_check_mark:|-|
|19| Provenienze clienti |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-|:heavy_check_mark:|-|
|20| Settori merceologici |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-|:heavy_check_mark:|-|
|21| Newsletter |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-|:heavy_check_mark:|-|
|22| Liste |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-|:heavy_check_mark:|-|
|23| Template email |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-|:heavy_check_mark:|-|
|24| Account email |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-|:heavy_check_mark:|-|
|25| Gestione documentale |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-|:heavy_check_mark:|-|
|26| Categorie documenti |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-|:heavy_check_mark:|-|
|27| Tipi attività |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-|:heavy_check_mark:|-|
|28| Fasce orarie |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-|:heavy_check_mark:|-|
|29| Stati attività |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-|:heavy_check_mark:|-|
|30| Tecnici tariffe |-|:heavy_check_mark:|-|-|:heavy_check_mark:|-|
|31| Stampe contabili | -|-|-|-|:heavy_check_mark:|-|
|32| Prima nota |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-|:heavy_check_mark:|-|
|33| Piano dei conti |:x:|:x:|:x:|:x:|:x:|:x:|
|34| Scadenzario |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-|:heavy_check_mark:|-|
|35| Ammortamenti / Cespiti |:x:|:x:|:x:|:x:|:x:|:x:|
|36| Piani sconto maggiorazione |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-|:heavy_check_mark:|-|
|37| Listini |:x:|:x:|:x:|:x:|:x:|:x:|
|38| Listini clienti |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-|:heavy_check_mark:|+ aggiorna listino e aggiungi a listino|
|39| Giacenze sedi|:heavy_check_mark:|:heavy_check_mark:|-|:heavy_check_mark:|:heavy_check_mark:|+spostamento tra sedi|
|40| Attributi combinazioni |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-|:heavy_check_mark:|-|
|41| Combinazioni |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-|:heavy_check_mark:|-|
|42| Automezzi |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:| -|:heavy_check_mark:|-|
|43| Impianti |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-|:heavy_check_mark:|-|
|44| Statistiche |-|-|-|-|:heavy_check_mark:|-|
|45| Mappa |-|-|-|-|:heavy_check_mark:|-|
|46| Accesso con Token/OTP |:x:|:x:|:x:|:x:|:x:|:x:|
|47| Utenti permessi |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-|:heavy_check_mark:|-|
|48| Accesso con OAuth |:x:|:x:|:x:|:x:|:x:|:x:|
|49| Checklists |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-|:heavy_check_mark:|-|
|50| Viste |-|-|-|-|:heavy_check_mark:|-|
|51| Tipi scadenze |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-|:heavy_check_mark:|-|
|52| Categorie contratti |:x:|:x:|:x:|:x:|:x:|:x:|
|53| Stati fatture |-|:heavy_check_mark:|-|-|:heavy_check_mark:|-|
|54| Stati degli ordini |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-|:heavy_check_mark:|-|
|55| Eventi |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-|:heavy_check_mark:|-|
|56| Tipi documento |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-|:heavy_check_mark:|-|
|57| Causali movimenti |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-|:heavy_check_mark:|-|
|58| Stati contratti |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-|:heavy_check_mark:|-|
|59| Stati preventivi |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-|:heavy_check_mark:|-|
|60| Ritenute previdenziali |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-|:heavy_check_mark:|-|
|61| Tipi spedizione |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-|:heavy_check_mark:|-|
|62| IVA |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-|:heavy_check_mark:|-|
|63| Causali trasporto |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-|:heavy_check_mark:|-|
|64| Aspetto beni |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-|:heavy_check_mark:|-|
|65| Unità misura |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-|:heavy_check_mark:|-|
|66| Porto |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-|:heavy_check_mark:|-|
|67| Pagamenti |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-|:heavy_check_mark:|-|
|68| Categorie |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-|:heavy_check_mark:|-|
|69| Ritenute acconto |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-|:heavy_check_mark:|-|
|70| Banche |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-|:heavy_check_mark:|-|
|71| Modelli prima nota |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-|:heavy_check_mark:|-|
|72| Casse previdenziali |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-|:heavy_check_mark:|-|
|73| Tags |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:| -|:heavy_check_mark:|-|
|74| Marche |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-|:heavy_check_mark:|-|
|75| Stati dei DDT |:x:|:x:|:x:|:x:|:x:|:x:|
|76| Descrizioni predefinite |:x:|:x:|:x:|:x:|:x:|:x:|
|77| Categorie file |:x:|:x:|:x:|:x:|:x:|:x:|
|78| Mansioni referenti |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-|:heavy_check_mark:|-|
|79| Segmenti |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-|:heavy_check_mark:|-|
|80| Import |:x:|:x:|:x:|:x:|:x:|:x:|
|81| Campi personalizzati |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-|:heavy_check_mark:|-|
|83| Stampe |-|-|-|-|:heavy_check_mark:|-|
|84| Adattatori di archiviazione |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-|:heavy_check_mark:|-|
|85| Gestione task |-|:heavy_check_mark:|-|-|:heavy_check_mark:|-|
|86| Aggiornamenti |-|-|-|-|:heavy_check_mark:|-|
|87| Widgets |-|-|-|-|:heavy_check_mark:|-|


## Plugin

Legenda:
- :heavy_plus_sign: Aggiunta
- :pencil: Modifica
- :wastebasket: Eliminazione
- ☑️ Verifica

|N°| Modulo | Plugin | :heavy_plus_sign: | :pencil: | :wastebasket: | ☑️ | Altro |
|--|--------|--------|:-----------------:|:--------:|:-------------:|:--:|:----------:|
|88| Anagrafiche | Impianti del cliente |:x:|:x:|:x:|:x:|:x:|
|88| Anagrafiche | Referenti |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-|
|88| Anagrafiche | Sedi aggiuntive |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-|
|88| Anagrafiche | Statistiche |-|-|-|:heavy_check_mark:|-|
|88| Anagrafiche | Ddt del cliente |-|-|-|:x:|:x:|
|88| Anagrafiche | Dichiarazione d'intento |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:| Fattura di vendita |
|88| Anagrafiche | Storico attività |-|-|-|:heavy_check_mark:|-|
|88| Anagrafiche | Allegati |-|-|-|:heavy_check_mark:|-|
|88| Anagrafiche | Contratti del cliente |:x:|:x:|:x:|:x:|:x:|
|88| Anagrafiche | Movimenti contabili |-|-|-|:heavy_check_mark:|-|
|88| Anagrafiche | Regole pagamenti |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-|
|88| Anagrafiche | Assicurazione crediti |:heavy_check_mark:|:heavy_check_mark:| :heavy_check_mark:| :heavy_check_mark:| Fattura di vendita |
|89| Attività | Mostra su mappa |:x:|:x:|:x:|:x:|:x:|
|89| Attività | Impianti |:x:|:x:|:x:|:x:|:x:|
|90| Preventivi | Consuntivo |-|-|-|:heavy_check_mark:|-|
|90| Preventivi | Revisioni |-|-|-|:heavy_check_mark:|-|
|91| Fatture di vendita | Movimenti contabilili |-|-|-|:heavy_check_mark:|-|
|91| Fatture di vendita | Ricevute FE |:x:|:x:|:x:|:x:|:x:|
|91| Fatture di vendita | Fatturazione elettronica |:x:|:x:|:x:|:x:|:x:|
|91| Fatture di vendita | Registrazioni |-|-|-|:heavy_check_mark:|-|
|91| Fatture di vendita | Importazione FE |:x:|:x:|:x:|:x:|:x:|
|92| Fatture di acquisto | Movimenti contabilili |-|-|-|:heavy_check_mark:|-|
|92| Fatture di acquisto | Fatturazione elettronica |:x:|:x:|:x:|:x:|:x:|
|92| Fatture di acquisto | Registrazioni |-|-|-|:heavy_check_mark:|-|
|93| Scadenzario | Presentazioni bancarie |:x:|:x:|:x:|:x:|:x:|
|94| Articoli | Barcode |:x:|:x:|:x:|:x:|:x:|
|94| Articoli | Provvigioni |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-|
|94| Articoli | Varianti articolo |:x:|:x:|:x:|:x:|:x:|
|94| Articoli | Piani di sconto/maggiorazione |:x:|:x:|:x:|:x:|:x:|
|94| Articoli | Listino fornitori |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|-|
|94| Articoli | Netto clienti |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|Fattura di vendita|
|94| Articoli | Statistiche |-|-|-|:heavy_check_mark:|-|
|94| Articoli | Giacenze |-|-|-|:heavy_check_mark:|-|
|94| Articoli | Serial |:heavy_check_mark:|-|:heavy_check_mark:|:heavy_check_mark:|-|
|94| Articoli | Movimenti |:x:|:x:|:x:|:x:|:x:|
|95| Ordini cliente | Consuntivo |-|-|-|:heavy_check_mark:|-|
|96| Impianti | Componenti |:x:|:x:|:x:|:x:|:x:|
|97| Contratti | Pianificazione fatturazione |:heavy_check_mark:|-|-|:heavy_check_mark:|controllo in Fatture e widget Dashboard|
|97| Contratti | Rinnovi |:x:|:x:|:x:|:x:|:x:|
|97| Contratti | Pianificazione attività |:heavy_check_mark:|:x:|:x:|:heavy_check_mark:|-|
|97| Contratti | Consuntivo |-|-|-|:heavy_check_mark:|-|
|98| Banche | Mandati SEPA |:x:|:x:|:x:|:x:|:x:|


## Azioni di gruppo

Legenda:
- ☑️ Verifica

|N°| Modulo  | Azioni di gruppo | ☑️ |
|--| ------- | ---------------- |:--:|
|99| Anagrafiche | Cambia relazione |:heavy_check_mark:|
|99| Anagrafiche | Elimina |:heavy_check_mark:|
|99| Anagrafiche | Esporta |:x:|
|99| Anagrafiche | Imposta listino |:x:|
|99| Anagrafiche | Ricerca coordinate |:heavy_check_mark:|
|100| Liste | Aggiorna liste |:x:|
|101| Attività | Cambia stato |:heavy_check_mark:|
|101| Attività | Duplica |:heavy_check_mark:|
|101| Attività | Elimina |:heavy_check_mark:|
|101| Attività | Esporta stampe |:x:|
|101| Attività | Fattura attività |:heavy_check_mark:|
|101| Attività | Firma interventi  |:heavy_check_mark:|
|101| Attività | Invia mail |:x:|
|101| Attività | Stampa riepilogo |:heavy_check_mark:|
|102| Contratti | Cambia stato |:heavy_check_mark:|
|102| Contratti | Cambia metodo di pagamento |:x:|
|102| Contratti | Fattura contratti |:heavy_check_mark:|
|102| Contratti | Rinnova contratti |:heavy_check_mark:|
|103| Preventivi | Cambia stato |:heavy_check_mark:|
|103| Preventivi | Fattura preventivi |:heavy_check_mark:|
|104| Ordini cliente | Cambia stato |:heavy_check_mark:|
|104| Ordini cliente | Fattura ordini cliente |:heavy_check_mark:|
|105| Fatture di vendita | Aggiorna banca |:x:|
|105| Fatture di vendita | Cambia sezionale |:heavy_check_mark:|
|105| Fatture di vendita | Controlla fatture elettroniche |:heavy_check_mark:|
|105| Fatture di vendita | Duplica |:heavy_check_mark:|
|105| Fatture di vendita | Elimina |:heavy_check_mark:|
|105| Fatture di vendita | Emetti fatture |:heavy_check_mark:|
|105| Fatture di vendita | Esporta |:x:|
|105| Fatture di vendita | Esporta stampe |:x:|
|105| Fatture di vendita | Esporta stampe FE |:x:|
|105| Fatture di vendita | Esporta ricevute |:x:|
|105| Fatture di vendita | Esporta XML |:x:|
|105| Fatture di vendita | Genera fatture elettroniche |:heavy_check_mark:|
|105| Fatture di vendita | Invia fatture |:x:|
|105| Fatture di vendita | Registrazione contabile |:heavy_check_mark:|
|106| Ordini fornitore | Cambia stato |:heavy_check_mark:|
|107| Fatture di acquisto | Aggiorna banca |:x:|
|107| Fatture di acquisto | Cambia sezionale |:heavy_check_mark:|
|107| Fatture di acquisto | Duplica |:heavy_check_mark:|
|107| Fatture di acquisto | Elimina |:heavy_check_mark:|
|107| Fatture di acquisto | Esporta |:x:|
|107| Fatture di acquisto | Esporta stampe FE |:x:|
|107| Fatture di acquisto | Esporta ricevute |:x:|
|107| Fatture di acquisto | Esporta XML |:x:|
|107| Fatture di acquisto | Invia fatture |:x:|
|107| Fatture di acquisto | Registrazione contabile |:heavy_check_mark:|
|108| Scadenzario | Aggiorna banca |:x:|
|108| Scadenzario | Info distinta |:x:|
|108| Scadenzario | Invia mail sollecito |:x:|
|108| Scadenzario | Registrazione contabile |:x:|
|109| Articoli | Aggiorna aliquota iva |:heavy_check_mark:|
|109| Articoli | Aggiorna categoria e sottocategoria |:x:|
|109| Articoli | Aggiorna coefficiente di vendita |:heavy_check_mark:|
|109| Articoli | Aggiorna conto predefinito di acquisto |:heavy_check_mark:|
|109| Articoli | Aggiorna conto predefinito di vendita |:heavy_check_mark:|
|109| Articoli | Aggiorna prezzo di acquisto |:heavy_check_mark:|
|109| Articoli | Aggiorna prezzo di vendita |:heavy_check_mark:|
|109| Articoli | Aggiorna quantità |:heavy_check_mark:|
|109| Articoli | Aggiorna unità di misura |:heavy_check_mark:|
|109| Articoli | Aggiungi a listino cliente |:x:|
|109| Articoli | Attiva/Disattiva articoli |:x:|
|109| Articoli | Elimina |:heavy_check_mark:|
|109| Articoli | Esporta |:x:|
|109| Articoli | Crea preventivo |:heavy_check_mark:|
|109| Articoli | Genera barcode |:x:|
|109| Articoli | Imposta prezzo di acquisto da fattura |:heavy_check_mark:|
|109| Articoli | Imposta una provvigione |:heavy_check_mark:|
|109| Articoli | Stampa barcode |:heavy_check_mark:|
|110| Listini | Copia listini |:heavy_check_mark:|
|110| Listini | Aggiorna prezzo unitario |:heavy_check_mark:|
|111| Ddt in uscita | Cambia stato |:heavy_check_mark:|
|111| Ddt in uscita | Elimina |:heavy_check_mark:|
|111| Ddt in uscita | Fattura ddt in uscita |:heavy_check_mark:|
|112| Ddt in entrata | Cambia stato |:heavy_check_mark:|
|112| Ddt in entrata | Elimina |:heavy_check_mark:|
|112| Ddt in entrata | Fattura ddt in entrata |:heavy_check_mark:|
|113| Impianti | Aggiorna cliente |:x:|
|113| Impianti | Elimina |:x:|
|113| Impianti | Esporta |:x:|

## Impostazioni

Legenda:
- ☑️ Verifica

|Test| Sezione | Nome | ☑️ | Altro |
|----|---------|------|:--:|:-----:| 
|114| Anagrafiche | Formato codice anagrafica |:heavy_check_mark:|Crea anagrafica| 
|114| Anagrafiche | Geolocalizzazione automatica |:x:|:x:| 
|115| Attività | Mostra i prezzi al tecnico |:heavy_check_mark:|Crea utente e attività|
|115| Attività | Stampa per anteprima e firma |:heavy_check_mark:|-|
|115| Attività | Permetti inserimento sessioni degli altri tecnici |:heavy_check_mark:|Crea attività|
|115| Attività | Giorni lavorativi |:heavy_check_mark:|Dashboard|
|115| Attività | Notifica al tecnico l'aggiunta della sessione nell'attività |:heavy_check_mark:|Aggiungi sessione di lavoro|
|115| Attività | Notifica al tecnico la rimozione della sessione dall'attività |:heavy_check_mark:|Elimina sessione di lavoro|
|115| Attività | Stato dell'attività dopo la firma |:heavy_check_mark:|Crea attività e firma attività|
|115| Attività | Espandi automaticamente la sezione "Dettagli aggiuntivi" |:heavy_check_mark:|Crea attività|
|115| Attività | Alert occupazione tecnici |:heavy_check_mark:|Crea attività|
|115| Attività | Verifica numero intervento |:heavy_check_mark:|Crea attività|
|115| Attività | Formato ore in stampa |:heavy_check_mark:|Stampa intervento|
|115| Attività | Notifica al tecnico l'assegnazione all'attività |:heavy_check_mark:|Aggiungi assegnazione|
|115| Attività | Notifica al tecnico la rimozione dell'assegnazione dall'attività |:heavy_check_mark:|Elimina assegnazione|
|115| Attività | Descrizione personalizzata in fatturazione |:heavy_check_mark:|Fattura attività|
|115| Attività | Stato predefinito dell'attività da Dashboard |:heavy_check_mark:|Crea attività|
|115| Attività | Stato predefinito dell'attività |:heavy_check_mark:|Crea attività|
|115| Attività | Numero di minuti di avanzamento delle sessioni delle attività |:x:|:x:|
|115| Attività | Cambia automaticamente stato attività fatturate |:x:|:x:|
|115| Attività | Raggruppamento fatturazione massiva attività |:x:|:x:|
|116| Contratti | Condizioni generali di fornitura contratti |:heavy_check_mark:|Crea contratto|
|116| Contratti | Crea contratto rinnovabile di default |:heavy_check_mark:|-|
|116| Contratti | Giorni di preavviso di default |:heavy_check_mark:|-|
|116| Contratti | Cambia automaticamente stato contratti fatturati |:x:|:x:| 
|116| Contratti | Raggruppamento fatturazione massiva contratti |:x:|:x:|
|117| Dashboard | Utilizzare i tooltip sul calendario |:x:|:x:|
|117| Dashboard | Visualizzare la domenica sul calendario |:heavy_check_mark:|-|
|117| Dashboard | Vista dashboard |:heavy_check_mark:|-|
|117| Dashboard | Ora inizio sul calendario |:heavy_check_mark:|-|
|117| Dashboard | Ora fine sul calendario |:heavy_check_mark:|-|
|117| Dashboard | Visualizza informazioni aggiuntive sul calendario |:heavy_check_mark:|-|
|117| Dashboard | Visualizzazione colori sessioni |:heavy_check_mark:|-|
|117| Dashboard | Tempo predefinito di snap attività sul calendario | ||
|118| Ddt| Cambia automaticamente stato ddt fatturati |:heavy_check_mark:|Crea ddt sia in entrata che in uscita|
|118| Ddt| Raggruppamento fatturazione massiva ddt |:x:||
|118| Ddt| Raggruppa gli articoli con stesso barcode nei DDT |:x:||
|119| Fatturazione | Iva predefinita |:heavy_check_mark:|Crea fattura|
|119| Fatturazione | Tipo di pagamento predefinito |:heavy_check_mark:|Crea fattura|
|119| Fatturazione | Ritenuta d'acconto predefinita |:heavy_check_mark:|Aggiungi riga|
|119| Fatturazione | Cassa previdenziale predefinita |:heavy_check_mark:|Crea anagrafica|
|119| Fatturazione | Importo marca da bollo |:heavy_check_mark:|Aggiungi riga|
|119| Fatturazione | Soglia minima per l'applicazione della marca da bollo |:heavy_check_mark:|Aggiungi riga|
|119| Fatturazione | Conto aziendale predefinito |:x:|:x:|
|119| Fatturazione | Conto predefinito fatture di vendita |:heavy_check_mark:|Aggiungi riga|
|119| Fatturazione | Conto predefinito fatture di acquisto |:heavy_check_mark:|Aggiungi riga|
|119| Fatturazione | Dicitura fissa fattura |:heavy_check_mark:||
|119| Fatturazione | Metodologia calcolo ritenuta d'acconto predefinito |:x:|:x:|
|119| Fatturazione | Ritenuta previdenziale predefinita |:heavy_check_mark:|Crea fattura|
|119| Fatturazione | Descrizione addebito bollo |:heavy_check_mark:|Crea fattura|
|119| Fatturazione | Conto predefinito per la marca da bollo |:heavy_check_mark:|Crea fattura|
|119| Fatturazione | Iva per lettere d'intento |:heavy_check_mark:|Crea fattura|
|119| Fatturazione | Utilizza prezzi di vendita comprensivi di IVA |:heavy_check_mark:|Crea articolo e fatturazione|
|119| Fatturazione | Liquidazione iva |:heavy_check_mark:|Stampe contabili|
|119| Fatturazione | Conto anticipo clienti |:x:|:x:|
|119| Fatturazione | Conto anticipo fornitori |:x:|:x:|
|119| Fatturazione | Descrizione fattura pianificata |:heavy_check_mark:|Crea fattura pianificata|
|119| Fatturazione | Aggiorna info di acquisto |:x:|:x:|
|119| Fatturazione | Bloccare i prezzi inferiori al minimo di vendita |:x:|:x:|
|119| Fatturazione | Permetti fatturazione delle attività collegate a contratti |:heavy_check_mark:|Fattura attività|
|119| Fatturazione | Data emissione fattura automatica |:x:|:x:|
|119| Fatturazione | Permetti fatturazione delle attività collegate a ordini |:heavy_check_mark:|Fattura attività|
|119| Fatturazione | Permetti fatturazione delle attività collegate a preventivi |:x:|:x:|
|119| Fatturazione | Data inizio verifica contatore fattura di vendita |:x:|:x:|
|119| Fatturazione | Raggruppa attività per tipologia in fattura |:x:|:x:|
|119| Fatturazione | Metodo di importazione XML fatture di vendita |:x:|:x:|
|119| Fatturazione | Conto predefinito per le spese d'incasso |:x:|:x:|
|120| Fatturazione Elettronica | Allega stampa per fattura verso Privati |:heavy_check_mark:|Crea fattura|
|120| Fatturazione Elettronica | Allega stampa per fattura verso Aziende |:heavy_check_mark:|Crea fattura|
|120| Fatturazione Elettronica | Allega stampa per fattura verso PA |:heavy_check_mark:|Crea fattura|
|120| Fatturazione Elettronica | Regime Fiscale |:heavy_check_mark:|Apri fattura elettronica|
|120| Fatturazione Elettronica | Tipo Cassa Previdenziale |:heavy_check_mark:|Apri fattura elettronica|
|120| Fatturazione Elettronica | Causale ritenuta d'acconto |:heavy_check_mark:|Apri fattura elettronica|
|120| Fatturazione Elettronica | Authorization ID Indice PA | ||
|120| Fatturazione Elettronica | OSMCloud Services API Token | ||
|120| Fatturazione Elettronica | Terzo intermediario | ||
|120| Fatturazione Elettronica | Riferimento dei documenti in Fattura Elettronica |:heavy_check_mark:|Apri fattura elettronica|
|120| Fatturazione Elettronica | OSMCloud Services API URL | ||
|120| Fatturazione Elettronica | OSMCloud Services API Version | ||
|120| Fatturazione Elettronica | Data inizio controlli su stati FE | ||
|120| Fatturazione Elettronica | Movimenta magazzino da fatture di acquisto | ||
|120| Fatturazione Elettronica | Rimuovi avviso fatture estere | ||
|120| Fatturazione Elettronica | Creazione seriali in import FE | ||
|120| Fatturazione Elettronica | Giorni validità fattura scartata | ||
|121| Generali | Azienda predefinita | ||
|121| Generali | Nascondere la barra sinistra di default |:heavy_check_mark:|Impostazioni|
|121| Generali | Cifre decimali per importi |:heavy_check_mark:|Crea fattura|
|121| Generali | CSS Personalizzato | ||
|121| Generali | Attiva notifica di presenza utenti sul record | ||
|121| Generali | Timeout notifica di presenza (minuti) | ||
|121| Generali | Prima pagina |:heavy_check_mark:|Anagrafiche|
|121| Generali | Cifre decimali per quantità |:heavy_check_mark:|Crea fattura|
|121| Generali | Tempo di attesa ricerche in secondi | ||
|121| Generali | Logo stampe | ||
|121| Generali | Abilita esportazione Excel e PDF |:heavy_check_mark:|Esporta fattura|
|121| Generali | Valuta |:heavy_check_mark:|Apro fattura|
|121| Generali | Visualizza riferimento su ogni riga in stampa |:heavy_check_mark:|Stampa fattura|
|121| Generali | Lunghezza in pagine del buffer Datatables | ||
|121| Generali | Autocompletamento form | ||
|121| Generali | Filigrana stampe | ||
|121| Generali | Attiva scorciatoie da tastiera | ||
|121| Generali | Modifica Viste di default | ||
|121| Generali | Totali delle tabelle ristretti alla selezione |:heavy_check_mark:|Seleziona fattura|
|121| Generali | Nascondere la barra dei plugin di default |:x:|:x:|
|121| Generali | Soft quota | ||
|121| Generali | Permetti selezione articoli con quantità minore o uguale a zero in Documenti di Vendita |:heavy_check_mark:|Crea fattura|
|121| Generali | Inizio periodo calendario |:heavy_check_mark:|Dashboard||
|121| Generali | Fine periodo calendario |:heavy_check_mark:|Dashboard||
|121| Generali | Permetti il superamento della soglia quantità dei documenti di origine |:heavy_check_mark:|Crea attività, preventivo, contratto, |ddt, ordine, fattura|
|121| Generali | Aggiungi riferimento tra documenti |:heavy_check_mark:|Aggiungi ddt in fattura||
|121| Generali | Mantieni riferimenti tra tutti i documenti collegati | |||
|121| Generali | Aggiungi le note delle righe tra documenti |:heavy_check_mark:|Fattura preventivo||
|121| Generali | Dimensione widget predefinita |:heavy_check_mark:|Dashboard||
|121| Generali | Posizione del simbolo valuta |:heavy_check_mark:|Crea fattura||
|121| Generali | Tile server OpenStreetMap | |||
|121| Generali | Sistema di firma | |||
|121| Generali | Tipo di sconto predefinito |:heavy_check_mark:|Crea fattura||
|121| Generali | Cifre decimali per importi in stampa |:heavy_check_mark:|Stampa fattura||
|121| Generali | Cifre decimali per quantità in stampa |:heavy_check_mark:|Stampa fattura||
|121| Generali | Cifre decimali per totali in stampa |:heavy_check_mark:|Stampa fattura||
|121| Generali | Listino cliente predefinito |:heavy_check_mark:|Crea anagrafica||
|121| Generali | Lingua |:heavy_check_mark:|Impostazioni||
|121| Generali | Ridimensiona automaticamente le immagini caricate | |||
|121| Generali | Larghezza per ridimensionamento immagini | |||
|121| Generali | Gestore mappa | |||
|121| Generali | Tile server satellite | |||
|121| Generali | Rendi casuale il nome dei file allegati | |||
|121| Generali | Template email richiesta codice OTP | |||
|121| Generali | Base URL | |||
|122| Magazzino | Movimenta il magazzino durante l'inserimento o eliminazione dei lotti/serial number | |||
|122| Magazzino | Serial number abilitato di default |:heavy_check_mark:|Crea articolo||
|122| Magazzino | Magazzino cespiti | |||
|123| Mail | Numero di giorni mantenimento coda di invio | |||
|123| Newsletter | Numero massimo di tentativi | ||
|123| Newsletter | Numero email da inviare in contemporanea per account | ||
|125| Ordini | Cambia automaticamente stato ordini fatturati |:heavy_check_mark:|Fattura ordine|
|125| Ordini | Conferma automaticamente le quantità negli ordini cliente |:heavy_check_mark:|Crea ordine cliente|
|125| Ordini | Conferma automaticamente le quantità negli ordini fornitore |:heavy_check_mark:|Crea ordine fornitore|
|125| Ordini | Visualizza numero ordine cliente | ||
|125| Ordini | Raggruppamento fatturazione massiva ordini | ||
|126| Piano dei conti | Conto per Riepilogativo fornitori |:heavy_check_mark:|Piano dei conti|
|126| Piano dei conti | Conto per Riepilogativo clienti |:heavy_check_mark:|Piano dei conti|
|126| Piano dei conti | Conto per Iva indetraibile |:heavy_check_mark:|Piano dei conti|
|126| Piano dei conti | Conto per Iva su vendite |:heavy_check_mark:|Piano dei conti|
|126| Piano dei conti | Conto per Iva su acquisti |:heavy_check_mark:|Piano dei conti|
|126| Piano dei conti | Conto per Erario c/ritenute d'acconto |:heavy_check_mark:|Piano dei conti|
|126| Piano dei conti | Conto per Erario c/INPS |:heavy_check_mark:|Piano dei conti|
|126| Piano dei conti | Conto per Erario c/enasarco |:heavy_check_mark:|Piano dei conti|
|126| Piano dei conti | Conto per Apertura conti patrimoniali |:heavy_check_mark:|Piano dei conti|
|126| Piano dei conti | Conto per Chiusura conti patrimoniali |:heavy_check_mark:|Piano dei conti|
|126| Piano dei conti | Conto per autofattura |:heavy_check_mark:|Piano dei conti|
|126| Piano dei conti | Conto di secondo livello per i crediti clienti |:heavy_check_mark:|Piano dei conti|
|126| Piano dei conti | Conto di secondo livello per i debiti fornitori |:heavy_check_mark:|Piano dei conti|
|127| Preventivi | Condizioni generali di fornitura preventivi |:heavy_check_mark:|Stampa preventivo|
|127| Preventivi | Conferma automaticamente le quantità nei preventivi |:heavy_check_mark:|Aggiungi articolo|
|127| Preventivi | Esclusioni default preventivi |:heavy_check_mark:|Crea preventivo|
|127| Preventivi | Raggruppamento fatturazione massiva preventivi |:x:||
|128| Scadenzario | Invio solleciti in automatico | ||
|128| Scadenzario | Template email primo sollecito | ||
|128| Scadenzario | Ritardo in giorni della scadenza della fattura per invio sollecito pagamento | ||
|128| Scadenzario | Ritardo in giorni dall'ultima email per invio sollecito pagamento | ||
|128| Scadenzario | Template email secondo sollecito | ||
|128| Scadenzario | Template email terzo sollecito | ||
|128| Scadenzario | Template email mancato pagamento dopo i solleciti | ||
|128| Scadenzario | Indirizzo email mancato pagamento dopo i solleciti | ||
|128| Scadenzario | Template email promemoria scadenza | ||
|128| Scadenzario | Intervallo di giorni in anticipo per invio promemoria scadenza | ||
|129| Tavoletta Wacom | Licenza Wacom SDK - Key|-|-|
|129| Tavoletta Wacom | Sfondo firma tavoletta Wacom|-|-|
|129| Tavoletta Wacom | Luminosità firma tavoletta Wacom|-|-|
|129| Tavoletta Wacom | Contrasto firma tavoletta Wacom|-|-|
|129| Tavoletta Wacom | Secondi timeout tavoletta Wacom|-|-|
|129| Tavoletta Wacom | Licenza Wacom SDK - Secret |-|-|
