from common.Test import Test, get_html
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Impostazioni(Test):
    def setUp(self):
        super().setUp()

    def test_impostazioni_generali(self):
        return True
        ## TODO: Azienda predefinita

        # Nascondere la barra sinistra di default (2)
        #self.nascondi_barra_sx()

        # Cambio cifre decimali per importi (3)
        #self.cifre_decimali_importi()

        ## TODO: CSS personalizzato

        ## TODO: Attiva notifica di presenza utenti sul record

        ## TODO: Timeout notifica di presenza (minuti)

        # Prima pagina
        #self.prima_pagina()

        # Cifre decimali per quantità
        #self.cifre_decimali_quantita()

        ## TODO: Tempo di attesa ricerche in secondi

        ## TODO: Logo stampe

        # Abilita esportazione Excel e PDF 
        #self.esportazione_excel_pdf

        # Cambio valuta 
        #self.valuta()

        # Visualizza riferimento su ogni riga in stampa 
        #self.riferimento_riga_stampa()

        ## TODO: Lunghezza in pagine del buffer Datatables

        # Autocompletamento form 
        #self.autocompletamento_form()   #da finire

        ## TODO: Filigrana stampe

        ## TODO: attiva scorciatoie da tastiera

        ## TODO: Modifica viste di default

        ## TODO: Totali delle tabelle ristretti alla selezione

        ## TODO: Nascondere barra dei plugin di default

        ## TODO: Soft quota
        
        # Permetti selezione articoli con quantità minore o uguale a zero in Documenti di Vendita 
        #self.quantita_minore_uguale_zero()

        # Cambio periodo calendario 
        #self.periodo_calendario()

        # Permetti il superamento della soglia quantità dei documenti di origine 
        #self.superamento_soglia_quantita()

        # Aggiungi riferimento tra documenti
        #self.aggiungi_riferimento_documenti()

        # Aggiungi riferimento tra tutti i documenti collegati 
        #self.aggiungi_riferimenti_tutti_documenti()

        # Aggiungi le note delle righe tra documenti 
        #self.aggiungi_note_documenti()

        # Dimensione widget predefinita 
        #self.dimensione_widget_predefinita()

        ## TODO: Posizione del simbolo valuta

        ## TODO: Tile server osm

        ## TODO: Sistema di firma

        # Tipo di sconto predefinito 
        #self.tipo_sconto_predefinito()

        # Cifre decimali per importi in stampa 
        #self.importi_stampa()

        # Cifre decimali per quantità in stampa 
        #self.quantita_stampa()

        # Cifre decimali per totali in stampa 
        #self.totali_stampa()

        # Listino cliente predefinito 
        #self.listino_predefinito()

        # Cambio lingua 
        #self.lingua()

        ## TODO: Ridimensiona automaticamente le immagini caricate

        ## TODO: Larghezza per ridimensionamento immagini

        ## TODO: Gestore mappa

        ## TODO: Tile server satellite

    def nascondi_barra_sx(self):
                self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="impostazioni-11"]'))
        ).click() #apro Generali

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//label[@class="btn btn-default active"])[1]'))
        ).click() #attivo impostazione

        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//body[@class="sidebar-mini layout-fixed  sidebar-collapse"]'))
        ) #controlla se trova la classe sidebar-collapse
        #torno alle impostazioni di prima
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="impostazioni-11"]'))
        ).click() #apro Generali

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//label[@class="btn btn-default active"])[1]'))
        ).click() #disattivo impostazione

        self.navigateTo("Impostazioni")
        self.wait_loader()

    def cifre_decimali_importi(self):
                self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="impostazioni-11"]'))
        ).click() #apro Generali

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-setting47-container"]'))
        ).click()    #seleziono 4 cifre decimali per gli importi
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys('4', Keys.ENTER)

        self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//i[@class="fa fa-plus"]'))
        ).click()   #click su +

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idanagrafica_add-container"]'))
        ).click() #seleziono Cliente come anagrafica
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente", Keys.ENTER)
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary"]'))
        ).click() #click su aggiungi
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-id_articolo-container"]'))
        ).click()  #aggiungo un articolo
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys('Articolo 1')

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(Keys.ENTER)
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary tip tooltipstered"]'))
        ).click() #click su aggiungi

        importo = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//tbody//tr[1]//td[9]'))
        ).text   #controllo se l'importo corrisponde a 20 euro con 4 cifre decimali
        self.assertEqual(importo, "20,0000 €")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@id="elimina"]'))
        ).click() #elimina fattura
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()
        self.wait_loader()
        #torno alle impostazioni di prima
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="impostazioni-11"]'))
        ).click() #apro Generali

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-setting47-container"]'))
        ).click()    #seleziono 2 cifre decimali per gli importi
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys('2', Keys.ENTER)

    def prima_pagina(self):
        wait = self.wait_driver  
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="impostazioni-11"]'))
        ).click() #apro Generali

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-setting59-container"]'))
        ).click()    #metto come prima pagina "Anagrafiche"

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Anagrafiche")

        wait.until(EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-setting59-results"]//li[2]'))).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="nav-link bg-danger"]'))
        ).click() #logout
        self.wait_loader()

        #login
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="form-control"]'))).send_keys(self.getConfig('login.username'))
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="password"]'))).send_keys(self.getConfig('login.password')) #password da mettere prima del test
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-danger btn-block btn-flat"]'))
        ).click()
        self.wait_loader()

        pagina = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="nav-link active"]'))
        ).text    #check se la prima pagina è quella delle Anagrafiche
        self.assertEqual(pagina[2:13], "Anagrafiche")
        #torno alle impostazioni di prima
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="impostazioni-11"]'))
        ).click() #apro Generali

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-setting59-container"]'))
        ).click()    #metto come prima pagina "Dashboard"

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Dashboard")

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(Keys.ENTER)

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="nav-link bg-danger"]'))
        ).click() #logout
        self.wait_loader()

        #login
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="form-control"]'))).send_keys(self.getConfig('login.username'))
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="password"]'))).send_keys(self.getConfig('login.password')) #password da mettere prima del test
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-danger btn-block btn-flat"]'))
        ).click()
        self.wait_loader()

    def cifre_decimali_quantita(self):
                self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//i[@class="fa fa-plus"]'))
        ).click()   #click su +

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idanagrafica_add-container"]'))
        ).click() #seleziono Cliente come anagrafica
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente", Keys.ENTER)
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary"]'))
        ).click() #click su aggiungi
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-id_articolo-container"]'))
        ).click()  #aggiungo un articolo
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys('Articolo 1')

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(Keys.ENTER)
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary tip tooltipstered"]'))
        ).click() #click su aggiungi

        quantita_element = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//tbody[@id="righe"]//input)[2]'))
        )   #check cifre decimali
        quantita = quantita_element.get_attribute("decimals")
        self.assertEqual(quantita, "2") 
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@id="elimina"]'))
        ).click() #elimina fattura
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()
        self.wait_loader()

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="impostazioni-11"]'))
        ).click() #apro Generali

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-setting60-container"]'))
        ).click()    #seleziono 4 cifre decimali per le quantità
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys('4', Keys.ENTER)

        self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//i[@class="fa fa-plus"]'))
        ).click()   #click su +

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idanagrafica_add-container"]'))
        ).click() #seleziono Cliente come anagrafica
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente", Keys.ENTER)
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary"]'))
        ).click() #click su aggiungi
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-id_articolo-container"]'))
        ).click()  #aggiungo un articolo
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys('Articolo 1')

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(Keys.ENTER)
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary tip tooltipstered"]'))
        ).click() #click su aggiungi

        quantita_element = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//tbody[@id="righe"]//input)[2]'))
        )   #check cifre decimali
        quantita = quantita_element.get_attribute("decimals")
        self.assertEqual(quantita, "4") 
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@id="elimina"]'))
        ).click() #elimina fattura
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()
        self.wait_loader()
        #torno alle impostazioni di prima
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="impostazioni-11"]'))
        ).click() #apro Generali

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-setting60-container"]'))
        ).click()    #seleziono 2 cifre decimali per le quanità
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys('2', Keys.ENTER)

    def esportazione_excel_pdf(self):
        wait = self.wait_driver  
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="impostazioni-11"]'))
        ).click() #apro Generali

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//label[@class="btn btn-default active"])[6]'))
        ).click()    #attiva impostazione

        self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.wait_for_element_and_click('//tbody//tr[1]//td[1]')    #seleziono prima fattura
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary table-btn dropdown-toggle"]'))
        ).click() #click su esporta

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@class="dropdown-menu show"]//a[1]'))
        ).click()

        self.driver.close() #chiude scheda
        self.driver.switch_to.window(self.driver.window_handles[0]) #torna alla prima

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary table-btn dropdown-toggle"]'))
        ).click() #click su esporta

        wait.until(EC.visibility_of_element_located((By.XPATH, '//ul[@class="dropdown-menu show"]//a[2]'))) #controllo se c'è l'esporta excel
        self.wait_for_element_and_click('//tbody//tr[1]//td[1]')    #diseleziono prima fattura
        #torno alle impostazioni di prima
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="impostazioni-11"]'))
        ).click() #apro Generali

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//label[@class="btn btn-default active"])[6]'))
        ).click()    #disattiva impostazione

    def valuta(self):
        wait = self.wait_driver  
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="impostazioni-11"]'))
        ).click() #apro Generali

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-setting83-container"]'))
        ).click() #cambio valuta in sterline
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys('Sterlina', Keys.ENTER)

        self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.wait_for_element_and_click('//tbody//tr//td[2]') #apro prima fattura
        self.wait_loader()

        nuova_valuta = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//tbody//tr[1]//td[5]//div//span'))
        ).text   #controllo se è cambiata la valuta
        self.assertEqual(nuova_valuta, "£")
        #torno alle impostazioni di prima
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="impostazioni-11"]'))
        ).click() #apro Generali

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-setting83-container"]'))
        ).click() #cambio valuta in euro
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys('Euro', Keys.ENTER)

    def riferimento_riga_stampa(self):
                self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="impostazioni-11"]'))
        ).click() #apro Generali

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//label[@class="btn btn-default active"])[4]'))
        ).click()   #disattivo impostazione

        #crea ordine
        self.expandSidebar("Vendite")
        self.navigateTo("Ordini cliente")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//i[@class="fa fa-plus"]'))
        ).click()   #click su tasto +

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idanagrafica-container"]'))
        ).click()     #scelta di "Cliente" come anagrafica per l'ordine
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys('Cliente')

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(Keys.ENTER)
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary"]'))
        ).click()   #click su tasto aggiungi
        self.wait_loader()
        #aggiungi articolo
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-id_articolo-container"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@class="select2-results__options select2-results__options--nested"]//li[1]'))
        ).click()
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary tip tooltipstered"]'))
        ).click() #click su aggiungi

        #aggiungi articolo
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-id_articolo-container"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@class="select2-results__options select2-results__options--nested"]//li[1]'))
        ).click()
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary tip tooltipstered"]'))
        ).click() #click su aggiungi
        #cambio stato
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idstatoordine-container"]'))
        ).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Accettato", Keys.ENTER)
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@id="save"]'))
        ).click()
        self.wait_loader()
        #crea ddt
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-info dropdown-toggle "]'))
        ).click() #click su crea

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@class="dropdown-menu dropdown-menu-right show"]//a[3]'))
        ).click()  #click su crea ddt

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-id_causale_trasporto-container"]'))
        ).click() #causale trasporto

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-id_causale_trasporto-results"]//li[1]'))
        ).click()
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-id_segment-container"]'))
        ).click()   #sezionale

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-id_segment-results"]//li[1]'))
        ).click()
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@id="submit_btn"]'))
        ).click()   #click su aggiungi
        self.wait_loader()
        #cambia stato
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idstatoddt-container"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-idstatoddt-results"]//li[2]'))
        ).click()    #stato evaso
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@id="save"]'))
        ).click()
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-info bound clickable"]'))
        ).click()  #crea fattura di vendita

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@id="submit_btn"]'))
        ).click()   #click su aggiungi
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@id="print-button_p"]'))
        ).click()    #stampa fattura

        self.driver.switch_to.window(self.driver.window_handles[1]) #cambia scheda

        primo_riferimento = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//div[@id="viewer"]//span)[38]'))
        ).text
        self.assertEqual(primo_riferimento[0:27], "Rif. ordine cliente num. 02")
        secondo_riferimento = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//div[@id="viewer"]//span)[39]'))
        ).text
        self.assertEqual(secondo_riferimento[0:27], "Ddt in uscita num. 02")
        self.driver.close() #chiude scheda
        self.driver.switch_to.window(self.driver.window_handles[0]) #torna alla prima
        #elimina fattura
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@id="elimina"]'))
        ).click()
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()
        self.wait_loader()
        #elimina ordine
        self.navigateTo("Ordini cliente")
        self.wait_loader()

        self.wait_for_element_and_click('//tbody//tr[1]//td[2]') 
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="btn btn-danger ask"]'))
        ).click()
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()
        self.wait_loader()
        #elimina ddt
        self.expandSidebar("Magazzino") 
        self.navigateTo("Ddt in uscita")
        self.wait_loader()

        self.wait_for_element_and_click('//tbody//tr[1]//td[2]')

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="btn btn-danger ask"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()
        self.wait_loader()
        #torna alle impostazioni di prima
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="impostazioni-11"]'))
        ).click() #apro Generali

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//label[@class="btn btn-default active"])[4]'))
        ).click()   #attivo impostazione

        #crea ordine
        self.expandSidebar("Vendite")
        self.navigateTo("Ordini cliente")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//i[@class="fa fa-plus"]'))
        ).click()   #click su tasto +

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idanagrafica-container"]'))
        ).click()     #scelta di "Cliente" come anagrafica per l'ordine
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys('Cliente')

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(Keys.ENTER)
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary"]'))
        ).click()   #click su tasto aggiungi
        self.wait_loader()
        #aggiungi articolo
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-id_articolo-container"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@class="select2-results__options select2-results__options--nested"]//li[1]'))
        ).click()
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary tip tooltipstered"]'))
        ).click() #click su aggiungi

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary"]'))
        ).click()   #click su tasto aggiungi
        self.wait_loader()
        #aggiungi articolo
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-id_articolo-container"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@class="select2-results__options select2-results__options--nested"]//li[1]'))
        ).click()
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary tip tooltipstered"]'))
        ).click() #click su aggiungi
        #cambio stato
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idstatoordine-container"]'))
        ).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Accettato", Keys.ENTER)
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@id="save"]'))
        ).click()
        self.wait_loader()
        #crea ddt
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-info dropdown-toggle "]'))
        ).click() #click su crea

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@class="dropdown-menu dropdown-menu-right show"]//a[3]'))
        ).click()  #click su crea ddt

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-id_causale_trasporto-container"]'))
        ).click() #causale trasporto

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-id_causale_trasporto-results"]//li[1]'))
        ).click()
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-id_segment-container"]'))
        ).click()   #sezionale

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-id_segment-results"]//li[1]'))
        ).click()
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@id="submit_btn"]'))
        ).click()   #click su aggiungi
        self.wait_loader()
        #cambia stato
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idstatoddt-container"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-idstatoddt-results"]//li[2]'))
        ).click()    #stato evaso
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@id="save"]'))
        ).click()
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-info bound clickable"]'))
        ).click()  #crea fattura di vendita

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@id="submit_btn"]'))
        ).click()   #click su aggiungi
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@id="print-button_p"]'))
        ).click()    #stampa fattura

        self.driver.switch_to.window(self.driver.window_handles[1]) #cambia scheda

        primo_riferimento = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//div[@id="viewer"]//span)[40]'))
        ).text
        self.assertEqual(primo_riferimento[0:27], "Rif. ordine cliente num. 02")

        self.driver.close() #chiude scheda
        self.driver.switch_to.window(self.driver.window_handles[0]) #torna alla prima
        #elimina fattura
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@id="elimina"]'))
        ).click()
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()
        self.wait_loader()
        #elimina ordine
        self.navigateTo("Ordini cliente")
        self.wait_loader()

        self.wait_for_element_and_click('//tbody//tr[1]//td[2]') 
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="btn btn-danger ask"]'))
        ).click()
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()
        self.wait_loader()
        #elimina ddt
        self.expandSidebar("Magazzino") 
        self.navigateTo("Ddt in uscita")
        self.wait_loader()

        self.wait_for_element_and_click('//tbody//tr[1]//td[2]')

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="btn btn-danger ask"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()
        self.wait_loader()

    def autocompletamento_form(self):
                self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="impostazioni-11"]'))
        ).click() #apro Generali

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-setting93-container"]'))
        ).click()    #autocopletamento on

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-setting93-results"]//li[1]'))
        ).click()

        self.navigateTo("Anagrafiche")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//i[@class="fa fa-plus"]'))
        ).click()   #click su +

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="ragione_sociale_add"]'))).send_keys('Prova')
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-selection select2-selection--multiple"]'))
        ).click()   #tipo anagrafica cliente

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-idtipoanagrafica_add-results"]//li[2]'))
        ).click()
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary"]'))
        ).click()
        self.wait_loader()

        #elimino anagrafica
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="btn btn-danger ask"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()
        self.wait_loader()

        self.navigateTo("Anagrafiche")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//i[@class="fa fa-plus"]'))
        ).click()   #click su +

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="ragione_sociale_add"]'))).send_keys('Pro')

        #controllo se appare il suggerimento
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="close"]'))
        ).click()
        #torno alle impostazioni di prima
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="impostazioni-11"]'))
        ).click() #apro Generali

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-setting93-container"]'))
        ).click()    #autocompletamento off

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-setting93-results"]//li[2]'))
        ).click()

    def quantita_minore_uguale_zero(self):
                self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//i[@class="fa fa-plus"]'))
        ).click()   #click su +

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idanagrafica_add-container"]'))
        ).click() #seleziono Cliente come anagrafica
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente", Keys.ENTER)
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary"]'))
        ).click() #click su aggiungi
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-id_articolo-container"]'))
        ).click()  #aggiungo un articolo
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys('Vestito')

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@class="select2-results__options select2-results__options--nested"]//li[1]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary tip tooltipstered"]'))
        ).click() #click su aggiungi 

        messaggio = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="swal2-content"]'))
        ).text    #check se esce l'errore
        self.assertEqual(messaggio, "Nessun articolo corrispondente a magazzino")
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-primary"]'))
        ).click()  #esce dal errore

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@id="elimina"]'))
        ).click() #elimina fattura
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()
        self.wait_loader()

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="impostazioni-11"]'))
        ).click() #apro Generali

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//label[@class="btn btn-default active"])[8]'))
        ).click() #attiva impostazione

        self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//i[@class="fa fa-plus"]'))
        ).click()   #click su +

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idanagrafica_add-container"]'))
        ).click() #seleziono Cliente come anagrafica
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente", Keys.ENTER)
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary"]'))
        ).click() #click su aggiungi
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-id_articolo-container"]'))
        ).click()  #aggiungo un articolo
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys('Vestito')

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@class="select2-results__options select2-results__options--nested"]//li[1]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary tip tooltipstered"]'))
        ).click() #click su aggiungi

        articolo = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//tbody[@id="righe"]//td[2]'))
        ).text    #check se l'articolo è stato aggiunto
        self.assertEqual(articolo, "1")
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@id="elimina"]'))
        ).click() #elimina fattura
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()
        self.wait_loader()
        #torno alle impostazioni di prima
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="impostazioni-11"]'))
        ).click() #apro Generali

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//label[@class="btn btn-default active"])[8]'))
        ).click() #disattiva impostazione

    def periodo_calendario(self):
        wait = self.wait_driver  
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="impostazioni-11"]'))
        ).click() #apro Generali

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//input[@id="setting135"]'))
        ).click()
        data_inizio = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//input[@id="setting135"]'))
        ) #cambio inizio periodo
        data_inizio.clear()
        data_inizio.send_keys("01/01/2026", Keys.ENTER)
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//input[@id="setting135"]'))
        ).click()
        data_fine = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//input[@id="setting136"]'))
        ) #cambio fine periodo
        data_fine.clear()
        data_fine.send_keys("30/06/2026", Keys.ENTER)

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="nav-link bg-danger"]'))
        ).click() #logout
        self.wait_loader()

        #login
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="form-control"]'))).send_keys(self.getConfig('login.username'))
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="password"]'))).send_keys('') #password da mettere prima del test
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-danger btn-block btn-flat"]'))
        ).click()
        self.wait_loader()

        data = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="nav-link text-danger"]'))
        ).text #controllo se la data è cambiata
        self.assertEqual(data, "01/01/2026 - 30/06/2026")
        #torno alle impostazioni di prima
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="impostazioni-11"]'))
        ).click() #apro Generali

        data_inizio = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//input[@id="setting135"]'))
        ) #cambio inizio periodo
        data_inizio.clear()
        data_inizio.send_keys("01/01/2026", Keys.ENTER)
        data_fine = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//input[@id="setting136"]'))
        ) #cambio fine periodo
        data_fine.clear()
        data_fine.send_keys("31/12/2026", Keys.ENTER)
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="nav-link bg-danger"]'))
        ).click() #logout
        self.wait_loader()

        #login
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="form-control"]'))).send_keys(self.getConfig('login.username'))
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="password"]'))).send_keys(self.getConfig('login.password')) #password da mettere prima del test
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-danger btn-block btn-flat"]'))
        ).click()
        self.wait_loader()

    def superamento_soglia_quantita(self):
                self.navigateTo("Impostazioni")
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="impostazioni-11"]'))
        ).click() #apro Generali

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//label[@class="btn btn-default active"])[9]'))
        ).click()    #attivo impostazione
        #crea attività
        self.navigateTo("Attività")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//i[@class="fa fa-plus"]'))
        ).click()  #click su +

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idanagrafica-container"]'))
        ).click() #seleziono Cliente come anagrafica
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-dropdown select2-dropdown--below"]//input'))).send_keys("Cliente", Keys.ENTER)
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idtipointervento-container"]'))
        ).click() #seleziono Generico come tipo di intervento
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys("Generico")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//li[@class="select2-results__option select2-results__option--highlighted"]'))
        ).click()  #click su primo risultato
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//iframe[@class="cke_wysiwyg_frame cke_reset"])[1]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//iframe[@class="cke_wysiwyg_frame cke_reset"])[1]'))).send_keys("Test")   #scrivo "Test" come richiesta
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary"]'))
        ).click()   #click su Aggiungi
        self.wait_loader()
        #aggiungi articolo
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-id_articolo-container"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@class="select2-results__options select2-results__options--nested"]//li[1]'))
        ).click()
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary tip tooltipstered"]'))
        ).click() #click su aggiungi
        #cambio stato
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idstatointervento-container"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-idstatointervento-results"]//li[1]'))
        ).click() #imposto stato "Completato"
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@id="save"]'))
        ).click() #click su salva
        self.wait_loader()

        #creo preventivo
        self.expandSidebar("Vendite")
        self.navigateTo("Preventivi")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//i[@class="fa fa-plus"]'))
        ).click()   #click su +
        #nome
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="nome"]'))).send_keys('Test')
        #cliente
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idanagrafica-container"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-idanagrafica-results"]//li[2]'))
        ).click()
        #tipo di attività
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idtipointervento-container"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-idtipointervento-results"]//li[1]'))
        ).click()
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary"]'))
        ).click()   #click su aggiungi
        self.wait_loader()
        #aggiungi articolo
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-id_articolo-container"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@class="select2-results__options select2-results__options--nested"]//li[1]'))
        ).click()
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary tip tooltipstered"]'))
        ).click() #click su aggiungi

        self.driver.execute_script('window.scrollTo(0,0)')

        #cambio stato
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idstato-container"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-idstato-results"]//li[1]'))
        ).click() #imposto stato "Accettato"
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@id="save"]'))
        ).click() #click su salva
        self.wait_loader()

        #crea contratto
        self.navigateTo("Contratti")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//i[@class="fa fa-plus"]'))
        ).click()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="nome"]'))).send_keys("Test")
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idanagrafica-container"]'))
        ).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente", Keys.ENTER)
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="data_accettazione"]'))).send_keys("01/01/2026")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="data_conclusione"]'))).send_keys("31/12/2026")
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary"]'))
        ).click()
        self.wait_loader()
        #aggiungi articolo
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-id_articolo-container"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@class="select2-results__options select2-results__options--nested"]//li[1]'))
        ).click()
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary tip tooltipstered"]'))
        ).click() #click su aggiungi
        #cambio stato
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idstato-container"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-idstato-results"]//li[1]'))
        ).click() #imposto stato "Accettato"
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@id="save"]'))
        ).click() #click su salva
        self.wait_loader()
        #creo ddt
        self.expandSidebar("Magazzino")
        self.navigateTo("Ddt in uscita")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//i[@class="fa fa-plus"]'))
        ).click() #click su +
        #seleziono destinatario
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idanagrafica_add-container"]'))
        ).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente")

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(Keys.ENTER)
        #seleziono causale trasporto
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idcausalet-container"]'))
        ).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Conto lavorazione")

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(Keys.ENTER)
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary"]'))
        ).click() #click su aggiungi
        self.wait_loader()

        #aggiungi articolo
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-id_articolo-container"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@class="select2-results__options select2-results__options--nested"]//li[1]'))
        ).click()
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary tip tooltipstered"]'))
        ).click() #click su aggiungi

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idstatoddt-container"]'))
        ).click() #cambio stato in evaso
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Evaso", Keys.ENTER)
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@id="save"]'))
        ).click()
        self.wait_loader()
        #crea ordine
        self.expandSidebar("Vendite")
        self.navigateTo("Ordini cliente")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//i[@class="fa fa-plus"]'))
        ).click()   #click su tasto +

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idanagrafica-container"]'))
        ).click()     #scelta di "Cliente" come anagrafica per l'ordine
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys('Cliente')

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(Keys.ENTER)
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary"]'))
        ).click()   #click su tasto aggiungi
        self.wait_loader()
        #aggiungi articolo
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-id_articolo-container"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@class="select2-results__options select2-results__options--nested"]//li[1]'))
        ).click()
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary tip tooltipstered"]'))
        ).click() #click su aggiungi
        #cambio stato
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idstatoordine-container"]'))
        ).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Accettato", Keys.ENTER)
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@id="save"]'))
        ).click()
        self.wait_loader()
        
        #crea fattura
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//i[@class="fa fa-plus"]'))
        ).click()   #click su +

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idanagrafica_add-container"]'))
        ).click() #seleziono Cliente come anagrafica
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente")

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(Keys.ENTER)
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary"]'))
        ).click() #click su aggiungi
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary dropdown-toggle"]'))
        ).click() #click su altro
        #attività
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@class="dropdown-menu dropdown-menu-right show"]//a[3]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idintervento-container"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-idintervento-results"]//li[2]'))
        ).click()  #seleziona attività creata prima
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary pull-right"]'))
        ).click()    #click su aggiungi
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//tbody[@id="righe"]//tr[2]//td[4]//input'))).send_keys("2", Keys.ENTER) #imposta quantità a 2

        qta_element = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//tbody[@id="righe"]//tr[2]//td[4]//input'))
        )    #controllo se la quantità è cambiata
        qta = qta_element.get_attribute("value")
        self.assertEqual(qta, "2,00") 
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//input[@id="check_all"]'))
        ).click() #elimino righe
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@id="elimina_righe"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-primary"]'))
        ).click()
        #preventivi
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary dropdown-toggle"]'))
        ).click() #click su altro
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@class="dropdown-menu dropdown-menu-right show"]//a[4]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-id_documento-container"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-id_documento-results"]//li[2]'))
        ).click()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//tbody[@id="righe_documento_importato"]//tr[1]//td[4]//input'))).send_keys("2", Keys.ENTER)

        qta_element = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//tbody[@id="righe"]//tr[1]//td[4]//input'))
        )    #controllo se la quantità è cambiata
        qta = qta_element.get_attribute("value")
        self.assertEqual(qta, "2,00") 
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//input[@id="check_all"]'))
        ).click() #elimino righe
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@id="elimina_righe"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-primary"]'))
        ).click()
        #contratti
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary dropdown-toggle"]'))
        ).click() #click su altro
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@class="dropdown-menu dropdown-menu-right show"]//a[5]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-id_documento-container"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-id_documento-results"]//li[3]'))
        ).click()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//tbody[@id="righe_documento_importato"]//tr[1]//td[4]//input'))).send_keys("2", Keys.ENTER)

        qta_element = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//tbody[@id="righe"]//tr[1]//td[4]//input'))
        )    #controllo se la quantità è cambiata
        qta = qta_element.get_attribute("value")
        self.assertEqual(qta, "2,00") 
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//input[@id="check_all"]'))
        ).click() #elimino righe
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@id="elimina_righe"]'))
        ).click()
        #ddt
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary dropdown-toggle"]'))
        ).click() #click su altro
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@class="dropdown-menu dropdown-menu-right show"]//a[6]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-id_documento-container"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-id_documento-results"]//li[1]'))
        ).click()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//tbody[@id="righe_documento_importato"]//tr[1]//td[4]//input'))).send_keys("2", Keys.ENTER)

        qta_element = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//tbody[@id="righe"]//tr[1]//td[4]//input'))
        )    #controllo se la quantità è cambiata
        qta = qta_element.get_attribute("value")
        self.assertEqual(qta, "2,00") 
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//input[@id="check_all"]'))
        ).click() #elimino righe
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@id="elimina_righe"]'))
        ).click()
        #ordine
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary dropdown-toggle"]'))
        ).click() #click su altro
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@class="dropdown-menu dropdown-menu-right show"]//a[7]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-id_documento-container"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-id_documento-results"]//li[1]'))
        ).click()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//tbody[@id="righe_documento_importato"]//tr[1]//td[4]//input'))).send_keys("2", Keys.ENTER)

        qta_element = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//tbody[@id="righe"]//tr[1]//td[4]//input'))
        )    #controllo se la quantità è cambiata
        qta = qta_element.get_attribute("value")
        self.assertEqual(qta, "2,00") 
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//input[@id="check_all"]'))
        ).click() #elimino righe
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@id="elimina_righe"]'))
        ).click()

        #torno alle impostazioni di prima
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="impostazioni-11"]'))
        ).click() #apro Generali

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//label[@class="btn btn-default active"])[9]'))
        ).click()    #disattivo impostazione
        
        self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.wait_for_element_and_click('//tbody//tr[1]//td[2]')    #apro fattura
        self.wait_loader()

        #attività
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@class="dropdown-menu dropdown-menu-right show"]//a[3]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idintervento-container"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-idintervento-results"]//li[3]'))
        ).click()  #seleziona attività creata prima
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary pull-right"]'))
        ).click()    #click su aggiungi
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//tbody[@id="righe"]//tr[2]//td[4]//input'))).send_keys("2", Keys.ENTER) #imposta quantità a 2

        qta_element = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//tbody[@id="righe"]//tr[2]//td[4]//input'))
        )    #controllo se la quantità è cambiata a 1 e non a 2
        qta = qta_element.get_attribute("value")
        self.assertEqual(qta, "1") 
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//input[@id="check_all"]'))
        ).click() #elimino righe
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@id="elimina_righe"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-primary"]'))
        ).click()

        #preventivi
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary dropdown-toggle"]'))
        ).click() #click su altro
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@class="dropdown-menu dropdown-menu-right show"]//a[4]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-id_documento-container"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-id_documento-results"]//li[2]'))
        ).click()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//tbody[@id="righe_documento_importato"]//tr[1]//td[4]//input'))).send_keys("2", Keys.ENTER)

        qta_element = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//tbody[@id="righe"]//tr[1]//td[4]//input'))
        )    #controllo se la quantità è cambiata a 1 e non a 2
        qta = qta_element.get_attribute("value")
        self.assertEqual(qta, "1")
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//input[@id="check_all"]'))
        ).click() #elimino righe
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@id="elimina_righe"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-primary"]'))
        ).click()
        #contratti
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary dropdown-toggle"]'))
        ).click() #click su altro
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@class="dropdown-menu dropdown-menu-right show"]//a[5]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-id_documento-container"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-id_documento-results"]//li[3]'))
        ).click()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//tbody[@id="righe_documento_importato"]//tr[1]//td[4]//input'))).send_keys("2", Keys.ENTER)

        qta_element = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//tbody[@id="righe"]//tr[1]//td[4]//input'))
        )    #controllo se la quantità è cambiata a 1 e non a 2
        qta = qta_element.get_attribute("value")
        self.assertEqual(qta, "1")
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//input[@id="check_all"]'))
        ).click() #elimino righe
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@id="elimina_righe"]'))
        ).click()
        #ddt
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary dropdown-toggle"]'))
        ).click() #click su altro
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@class="dropdown-menu dropdown-menu-right show"]//a[6]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-id_documento-container"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-id_documento-results"]//li[1]'))
        ).click()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//tbody[@id="righe_documento_importato"]//tr[1]//td[4]//input'))).send_keys("2", Keys.ENTER)

        qta_element = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//tbody[@id="righe"]//tr[1]//td[4]//input'))
        )    #controllo se la quantità è cambiata a 1 e non a 2
        qta = qta_element.get_attribute("value")
        self.assertEqual(qta, "1")
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//input[@id="check_all"]'))
        ).click() #elimino righe
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@id="elimina_righe"]'))
        ).click()
        #ordine
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary dropdown-toggle"]'))
        ).click() #click su altro
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@class="dropdown-menu dropdown-menu-right show"]//a[7]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-id_documento-container"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-id_documento-results"]//li[1]'))
        ).click()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//tbody[@id="righe_documento_importato"]//tr[1]//td[4]//input'))).send_keys("2", Keys.ENTER)

        qta_element = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//tbody[@id="righe"]//tr[1]//td[4]//input'))
        )    #controllo se la quantità è cambiata a 1 e non a 2
        qta = qta_element.get_attribute("value")
        self.assertEqual(qta, "1")
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//input[@id="check_all"]'))
        ).click() #elimino righe
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@id="elimina_righe"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@id="elimina"]'))
        ).click() #elimina fattura
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()
        self.wait_loader()
        #elimino attività
        self.navigateTo("Attività")
        self.wait_loader()

        self.wait_for_element_and_click('//tbody//tr[1]//td[2]')

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="btn btn-danger ask"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()
        self.wait_loader()
        #elimino preventivo
        self.expandSidebar("Vendite")
        self.navigateTo("Preventivi")
        self.wait_loader()

        self.wait_for_element_and_click('//tbody//tr[1]//td[2]')

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="btn btn-danger ask"]'))
        ).click()
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()
        self.wait_loader()
        #elimina contratto
        self.navigateTo("Contratti")
        self.wait_loader()

        self.wait_for_element_and_click('//tbody//tr[4]//td[2]') #apre contratto
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_0"]//a[@class="btn btn-danger ask"]'))).click()  #elimino contratto 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))).click()
        self.wait_loader()
        #elimina ddt
        self.expandSidebar("Magazzino") 
        self.navigateTo("Ddt in uscita")
        self.wait_loader()

        self.wait_for_element_and_click('//tbody//tr[1]//td[2]')

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="btn btn-danger ask"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()
        self.wait_loader()
        #elimina ordini
        self.expandSidebar("Vendite")
        self.navigateTo("Ordini cliente")
        self.wait_loader()

        self.wait_for_element_and_click('//tbody//tr[1]//td[2]') 
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="btn btn-danger ask"]'))
        ).click()
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()
        self.wait_loader()

    def aggiungi_riferimento_documenti(self):
                self.navigateTo("Impostazioni") #primo caso (no,no)
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="impostazioni-11"]'))
        ).click() #apro Generali

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//label[@class="btn btn-default active"])[10]'))
        ).click()   #disattiva impostazione
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//label[@class="btn btn-default active"])[11]'))
        ).click() #disattiva seconda impostazione da riattivare alla fine

        #creo ddt
        self.expandSidebar("Magazzino")
        self.navigateTo("Ddt in uscita")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//i[@class="fa fa-plus"]'))
        ).click() #click su +
        #seleziono destinatario
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idanagrafica_add-container"]'))
        ).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente")

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(Keys.ENTER)
        #seleziono causale trasporto
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idcausalet-container"]'))
        ).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Conto lavorazione")

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(Keys.ENTER)
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary"]'))
        ).click() #click su aggiungi
        self.wait_loader()

        #aggiungi articolo
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-id_articolo-container"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@class="select2-results__options select2-results__options--nested"]//li[1]'))
        ).click()
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary tip tooltipstered"]'))
        ).click() #click su aggiungi

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idstatoddt-container"]'))
        ).click() #cambio stato in evaso
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Evaso", Keys.ENTER)
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@id="save"]'))
        ).click()
        self.wait_loader()
        #crea fattura
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-info bound clickable"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@id="submit_btn"]'))
        ).click()   #click su aggiungi
        self.wait_loader()

        riferimento = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//tbody[@id="righe"]//tr[1]//td[3]//a)[2]'))
        ).text  #controllo se è presente il riferimento
        self.assertEqual(riferimento, "001 - Articolo 1")
        #elimina riga
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="btn btn-xs btn-danger"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-primary"]'))
        ).click()
        #rimetto stato in evaso del ddt
        self.expandSidebar("Magazzino")
        self.navigateTo("Ddt in uscita")
        self.wait_loader()

        self.wait_for_element_and_click('//tbody//tr[1]//td[2]')    #apri ddt
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idstatoddt-container"]'))
        ).click() #cambio stato in evaso
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Evaso", Keys.ENTER)
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@id="save"]'))
        ).click()
        self.wait_loader()

        self.navigateTo("Impianti")
        self.wait_loader()

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni") #secondo caso (si,no)
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="impostazioni-11"]'))
        ).click() #apro Generali

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//label[@class="btn btn-default active"])[10]'))
        ).click()   #attiva impostazione

        self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.wait_for_element_and_click('//tbody//tr[1]//td[2]')    #apri fattura
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary dropdown-toggle"]'))
        ).click() #click su altro
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@class="dropdown-menu dropdown-menu-right show"]//a[6]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-id_documento-container"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-id_documento-results"]//li[1]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@id="submit_btn"]'))
        ).click()   #click su aggiungi
        self.wait_loader()

        riferimento = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//tbody[@id="righe"]//tr[1]//td[3]//a)[2]'))
        ).text  #controllo se è presente il riferimento
        self.assertEqual(riferimento[17:43], "Rif. ddt in uscita num. 02")
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@id="elimina"]'))
        ).click() #elimina fattura
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()
        self.wait_loader()

        #elimino ddt
        self.expandSidebar("Magazzino")
        self.navigateTo("Ddt in uscita")
        self.wait_loader()

        self.wait_for_element_and_click('//tbody//tr[1]//td[2]')    #apro primo ddt
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="btn btn-danger ask"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()
        self.wait_loader()

        self.navigateTo("Impianti")
        self.wait_loader()

        #torno alle impostazioni di prima
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="impostazioni-11"]'))
        ).click() #apro Generali
        
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//label[@class="btn btn-default active"])[11]'))
        ).click() #attiva seconda impostazione

    def aggiungi_riferimenti_tutti_documenti(self):
                self.navigateTo("Impostazioni") #prima con opzione (no,si)
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="impostazioni-11"]'))
        ).click() #apro Generali

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//label[@class="btn btn-default active"])[10]'))
        ).click() #disattiva prima impostazione

        #creo preventivo
        self.expandSidebar("Vendite")
        self.navigateTo("Preventivi")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//i[@class="fa fa-plus"]'))
        ).click()   #click su +
        #nome
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="nome"]'))).send_keys('Test')
        #cliente
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idanagrafica-container"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-idanagrafica-results"]//li[2]'))
        ).click()
        #tipo di attività
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idtipointervento-container"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-idtipointervento-results"]//li[1]'))
        ).click()
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary"]'))
        ).click()   #click su aggiungi
        self.wait_loader()
        #aggiungi articolo
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-id_articolo-container"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@class="select2-results__options select2-results__options--nested"]//li[1]'))
        ).click()
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary tip tooltipstered"]'))
        ).click() #click su aggiungi

        self.driver.execute_script('window.scrollTo(0,0)')

        #cambio stato
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idstato-container"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-idstato-results"]//li[1]'))
        ).click() #imposto stato "Accettato"
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@id="save"]'))
        ).click() #click su salva
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-info dropdown-toggle "]'))
        ).click() #click su crea

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="dropdown-menu dropdown-menu-right show"]//a[5]'))
        ).click()
        #ddt
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-id_causale_trasporto-container"]'))).click()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//li[@class="select2-results__option select2-results__option--highlighted"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-id_segment-container"]'))).click()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//li[@class="select2-results__option select2-results__option--highlighted"]'))).click()
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@id="submit_btn"]'))
        ).click()
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idstatoddt-container"]'))
        ).click()   #cambio stato

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-idstatoddt-results"]//li[2]'))
        ).click()    #imposta stato "Evaso"
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@id="save"]'))
        ).click() #click su salva
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-info bound clickable"]'))
        ).click()  #crea fattura

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@id="submit_btn"]'))
        ).click()   #click su aggiungi
        self.wait_loader()

        riferimento1 = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//tbody[@id="righe"]//tr[1]//td[3]//a)[2]'))
        ).text
        self.assertEqual(riferimento1[17:39], "Rif. preventivo num. 2")
        riferimento2 = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//tbody[@id="righe"]//tr[1]//td[3]//a)[2]'))
        ).text
        self.assertEqual(riferimento2[55:81], "Rif. ddt in uscita num. 02")
        #elimina fattura
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@id="elimina"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()   #click di conferma
        self.wait_loader()
        #elimino ddt
        self.expandSidebar("Magazzino")
        self.navigateTo("Ddt in entrata")
        self.wait_loader()

        self.wait_for_element_and_click('//tbody//tr[1]//td[2]')

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="btn btn-danger ask"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()
        self.wait_loader()
        #elimino preventivo
        self.expandSidebar("Vendite")
        self.navigateTo("Preventivi")
        self.wait_loader()

        self.wait_for_element_and_click('//tbody//tr[1]//td[2]')

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="btn btn-danger ask"]'))
        ).click()
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()
        self.wait_loader()
        self.navigateTo("Impianti")
        self.wait_loader()

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni") #test con opzioni messe a (si,si)
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="impostazioni-11"]'))
        ).click() #apro Generali

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//label[@class="btn btn-default active"])[10]'))
        ).click() #attiva prima impostazione

        #creo preventivo
        self.expandSidebar("Vendite")
        self.navigateTo("Preventivi")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//i[@class="fa fa-plus"]'))
        ).click()   #click su +
        #nome
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="nome"]'))).send_keys('Test')
        #cliente
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idanagrafica-container"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-idanagrafica-results"]//li[2]'))
        ).click()
        #tipo di attività
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idtipointervento-container"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-idtipointervento-results"]//li[1]'))
        ).click()
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary"]'))
        ).click()   #click su aggiungi
        self.wait_loader()
        #aggiungi articolo
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-id_articolo-container"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@class="select2-results__options select2-results__options--nested"]//li[1]'))
        ).click()
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary tip tooltipstered"]'))
        ).click() #click su aggiungi

        self.driver.execute_script('window.scrollTo(0,0)')

        #cambio stato
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idstato-container"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-idstato-results"]//li[1]'))
        ).click() #imposto stato "Accettato"
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@id="save"]'))
        ).click() #click su salva
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-info dropdown-toggle "]'))
        ).click() #click su crea

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="dropdown-menu dropdown-menu-right show"]//a[5]'))
        ).click()
        #ddt
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-id_causale_trasporto-container"]'))).click()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//li[@class="select2-results__option select2-results__option--highlighted"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-id_segment-container"]'))).click()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//li[@class="select2-results__option select2-results__option--highlighted"]'))).click()
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@id="submit_btn"]'))
        ).click()
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idstatoddt-container"]'))
        ).click()   #cambio stato

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-idstatoddt-results"]//li[2]'))
        ).click()    #imposta stato "Evaso"
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@id="save"]'))
        ).click() #click su salva
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-info bound clickable"]'))
        ).click()  #crea fattura

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@id="submit_btn"]'))
        ).click()   #click su aggiungi
        self.wait_loader()

        riferimento1 = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//tbody[@id="righe"]//tr[1]//td[3]//a)[2]'))
        ).text
        self.assertEqual(riferimento1[17:39], "Rif. preventivo num. 2")
        riferimento2 = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//tbody[@id="righe"]//tr[1]//td[3]//a)[2]'))
        ).text
        self.assertEqual(riferimento2[55:81], "Rif. ddt in uscita num. 02")
        #elimina fattura
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@id="elimina"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()   #click di conferma
        self.wait_loader()
        #elimino ddt
        self.expandSidebar("Magazzino")
        self.navigateTo("Ddt in entrata")
        self.wait_loader()

        self.wait_for_element_and_click('//tbody//tr[1]//td[2]')

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="btn btn-danger ask"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()
        self.wait_loader()
        #elimino preventivo
        self.expandSidebar("Vendite")
        self.navigateTo("Preventivi")
        self.wait_loader()

        self.wait_for_element_and_click('//tbody//tr[1]//td[2]')

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="btn btn-danger ask"]'))
        ).click()
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()
        self.wait_loader()

    def aggiungi_note_documenti(self):
                self.navigateTo("Impostazioni")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="impostazioni-11"]'))
        ).click() #apro Generali

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//label[@class="btn btn-default active"])[12]'))
        ).click()   #attiva impostazione

        self.expandSidebar("Vendite")
        self.navigateTo("Preventivi")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//i[@class="fa fa-plus"]'))
        ).click()   #crea preventivo
        #nome
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="nome"]'))).send_keys('Test')
        #cliente
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idanagrafica-container"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-idanagrafica-results"]//li[2]'))
        ).click()
        #tipo di attività
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idtipointervento-container"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-idtipointervento-results"]//li[1]'))
        ).click()
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary"]'))
        ).click()   #click su aggiungi
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//a[@class="btn btn-primary"])[1]'))
        ).click()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("Test") #scrivo "Test" come descrizione riga
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("1") #scrivo 1 come prezzo unitario
        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("Nota di prova")   #aggiungo note
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary pull-right"]'))
        ).click()    #click su aggiungi

        #cambio stato
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idstato-container"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-idstato-results"]//li[1]'))
        ).click() #imposto stato "Accettato"
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@id="save"]'))
        ).click() #click su salva
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-info dropdown-toggle "]'))
        ).click() #click su crea
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="dropdown-menu dropdown-menu-right show"]//a[6]'))
        ).click() #crea fattura

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@id="submit_btn"]'))
        ).click()
        self.wait_loader()

        nota = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//tbody[@id="righe"]//td[3]//span'))
        ).text  #controllo se ha aggiunto la nota dal preventivo
        self.assertEqual(nota, "Nota di prova")
        #elimina fattura
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@id="elimina"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()   #click di conferma
        self.wait_loader()
        #elimino preventivo
        self.navigateTo("Preventivi")
        self.wait_loader()

        self.wait_for_element_and_click('//tbody//tr[1]//td[2]')

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="btn btn-danger ask"]'))
        ).click()
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()
        self.wait_loader()

        self.expandSidebar("Vendite")
        #torno alle impostazioni di prima
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="impostazioni-11"]'))
        ).click() #apro Generali 

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//label[@class="btn btn-default active"])[12]'))
        ).click()   #disattiva impostazione

        self.expandSidebar("Vendite")
        self.navigateTo("Preventivi")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//i[@class="fa fa-plus"]'))
        ).click()   #crea preventivo
        #nome
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="nome"]'))).send_keys('Test')
        #cliente
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idanagrafica-container"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-idanagrafica-results"]//li[2]'))
        ).click()
        #tipo di attività
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idtipointervento-container"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-idtipointervento-results"]//li[1]'))
        ).click()
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary"]'))
        ).click()   #click su aggiungi
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//a[@class="btn btn-primary"])[1]'))
        ).click()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("Test") #scrivo "Test" come descrizione riga
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("1") #scrivo 1 come prezzo unitario
        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("Nota di prova")   #aggiungo note
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary pull-right"]'))
        ).click()    #click su aggiungi

        #cambio stato
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idstato-container"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-idstato-results"]//li[1]'))
        ).click() #imposto stato "Accettato"
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@id="save"]'))
        ).click() #click su salva
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-info dropdown-toggle "]'))
        ).click() #click su crea
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="dropdown-menu dropdown-menu-right show"]//a[6]'))
        ).click() #crea fattura

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@id="submit_btn"]'))
        ).click()
        self.wait_loader()

        wait.until(EC.invisibility_of_element_located((By.XPATH, '//tbody[@id="righe"]//td[3]//span')))   #controllo se non ha aggiunto la nota dal preventivo
        
        #elimina fattura
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@id="elimina"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()   #click di conferma
        self.wait_loader()
        #elimino preventivo
        self.navigateTo("Preventivi")
        self.wait_loader()

        self.wait_for_element_and_click('//tbody//tr[1]//td[2]')

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="btn btn-danger ask"]'))
        ).click()
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()
        self.wait_loader()

    def dimensione_widget_predefinita(self):
                self.navigateTo("Impostazioni")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="impostazioni-11"]'))
        ).click() #apro Generali

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-setting166-container"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-setting166-results"]//li[1]'))
        ).click()    #metto dimensione col-md-1

        self.navigateTo("Dashboard")
        self.wait_loader()

        dimensione_element = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//div[@id="widget-top"]//div)[1]'))
        )    #controllo se la dimensione è cambiata
        dimensione = dimensione_element.get_attribute("class")
        self.assertEqual(dimensione[9:17], "col-md-1")
        self.navigateTo("Impianti")
        self.wait_loader()

        #torno alle impostazioni di prima
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="impostazioni-11"]'))
        ).click() #apro Generali

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-setting166-container"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-setting166-results"]//li[3]'))
        ).click()    #metto dimensione col-md-3

        self.navigateTo("Dashboard")
        self.wait_loader()

        dimensione_element = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//div[@id="widget-top"]//div)[1]'))
        )    #controllo se la dimensione è cambiata
        dimensione = dimensione_element.get_attribute("class")
        self.assertEqual(dimensione[9:17], "col-md-3")

    def tipo_sconto_predefinito(self):
                self.navigateTo("Impostazioni")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="impostazioni-11"]'))
        ).click() #apro Generali

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-setting189-container"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-setting189-results"]//li[2]'))
        ).click()    #sconto predefinito in eur

        self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//i[@class="fa fa-plus"]'))
        ).click()   #click su +

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idanagrafica_add-container"]'))
        ).click() #seleziono Cliente come anagrafica
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente", Keys.ENTER)
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary"]'))
        ).click() #click su aggiungi
        self.wait_loader()
        #aggiungo articolo
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-id_articolo-container"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@class="select2-results__options select2-results__options--nested"]//li[1]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary tip tooltipstered"]'))
        ).click()

        sconto_element = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//tbody[@id="righe"]//span[@class="select2-selection select2-selection--single"]//span[1]'))
        )    #check valore dello sconto
        sconto = sconto_element.get_attribute("title")
        self.assertEqual(sconto, "€")
        #torno alle impostazioni di prima
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="impostazioni-11"]'))
        ).click() #apro Generali

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-setting189-container"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-setting189-results"]//li[1]'))
        ).click()    #sconto predefinito in percentuale

        self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.wait_for_element_and_click('//tbody//tr[1]//td[2]')

        sconto_element = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//tbody[@id="righe"]//span[@class="select2-selection select2-selection--single"]//span[1]'))
        )    #check valore dello sconto
        sconto = sconto_element.get_attribute("title")
        self.assertEqual(sconto, "%")
        #elimina fattura
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@id="elimina"]'))
        ).click()
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()
        self.wait_loader()

    def importi_stampa(self):
                self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//i[@class="fa fa-plus"]'))
        ).click()   #click su +

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idanagrafica_add-container"]'))
        ).click() #seleziono Cliente come anagrafica
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente", Keys.ENTER)
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary"]'))
        ).click() #click su aggiungi
        self.wait_loader()
        # riga 1
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="btn btn-primary"]'))
        ).click() #click su aggiungi riga

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("1")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("26,10")
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary pull-right"]'))
        ).click() #click su aggiungi
        #riga 2
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="btn btn-primary"]'))
        ).click() #click su aggiungi riga

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("2")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("8,34")
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary pull-right"]'))
        ).click() #click su aggiungi
        #riga 3
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="btn btn-primary"]'))
        ).click() #click su aggiungi riga

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("3")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("8,35")
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary pull-right"]'))
        ).click() #click su aggiungi
        #riga 4
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="btn btn-primary"]'))
        ).click() #click su aggiungi riga

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("4")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("8,34")
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary pull-right"]'))
        ).click() #click su aggiungi
        #riga 5
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="btn btn-primary"]'))
        ).click() #click su aggiungi riga

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("5")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("8,35")
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary pull-right"]'))
        ).click() #click su aggiungi
        #riga 6
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="btn btn-primary"]'))
        ).click() #click su aggiungi riga

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("6")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("16,60")
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary pull-right"]'))
        ).click() #click su aggiungi
        #riga 7
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="btn btn-primary"]'))
        ).click() #click su aggiungi riga

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("7")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("28,81")
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary pull-right"]'))
        ).click() #click su aggiungi

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idstatodocumento-container"]'))
        ).click() #cambio stato in "Emessa"
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Emessa", Keys.ENTER)
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@id="save"]'))
        ).click()
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@id="print-button_p"]'))
        ).click()

        self.driver.switch_to.window(self.driver.window_handles[1]) #cambia scheda

        importo1 = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@style="left: 66.18%; top: 27.96%; font-size: calc(var(--scale-factor)*7.82px); font-family: sans-serif; transform: scaleX(0.901707);"]'))
        ).text
        self.assertEqual(importo1, "26,10 €")
        importo2 = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@style="left: 81.57%; top: 27.96%; font-size: calc(var(--scale-factor)*7.82px); font-family: sans-serif; transform: scaleX(0.901707);"]'))
        ).text
        self.assertEqual(importo2, "26,10 €")

        self.driver.close() #chiude scheda
        self.driver.switch_to.window(self.driver.window_handles[0]) #torna alla prima

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@id="elimina"]'))
        ).click() #elimina fattura
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()
        self.wait_loader()

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="impostazioni-11"]'))
        ).click() #apro Generali

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-setting193-container"]'))
        ).click()    #seleziono 4 cifre decimali per gli importi
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys('4', Keys.ENTER)

        self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//i[@class="fa fa-plus"]'))
        ).click()   #click su +

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idanagrafica_add-container"]'))
        ).click() #seleziono Cliente come anagrafica
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente", Keys.ENTER)
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary"]'))
        ).click() #click su aggiungi
        self.wait_loader()
        # riga 1
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="btn btn-primary"]'))
        ).click() #click su aggiungi riga

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("1")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("26,10")
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary pull-right"]'))
        ).click() #click su aggiungi
        #riga 2
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="btn btn-primary"]'))
        ).click() #click su aggiungi riga

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("2")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("8,34")
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary pull-right"]'))
        ).click() #click su aggiungi
        #riga 3
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="btn btn-primary"]'))
        ).click() #click su aggiungi riga

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("3")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("8,35")
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary pull-right"]'))
        ).click() #click su aggiungi
        #riga 4
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="btn btn-primary"]'))
        ).click() #click su aggiungi riga

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("4")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("8,34")
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary pull-right"]'))
        ).click() #click su aggiungi
        #riga 5
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="btn btn-primary"]'))
        ).click() #click su aggiungi riga

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("5")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("8,35")
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary pull-right"]'))
        ).click() #click su aggiungi
        #riga 6
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="btn btn-primary"]'))
        ).click() #click su aggiungi riga

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("6")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("16,60")
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary pull-right"]'))
        ).click() #click su aggiungi
        #riga 7
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="btn btn-primary"]'))
        ).click() #click su aggiungi riga

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("7")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("28,81")
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary pull-right"]'))
        ).click() #click su aggiungi

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idstatodocumento-container"]'))
        ).click() #cambio stato in "Emessa"
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Emessa", Keys.ENTER)
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@id="save"]'))
        ).click()
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@id="print-button_p"]'))
        ).click()

        self.driver.switch_to.window(self.driver.window_handles[1]) #cambia scheda

        importo1 = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@style="left: 64.67%; top: 27.96%; font-size: calc(var(--scale-factor)*7.82px); font-family: sans-serif; transform: scaleX(0.901707);"]'))
        ).text
        self.assertEqual(importo1, "26,1000 €")
        importo2 = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@style="left: 80.07%; top: 27.96%; font-size: calc(var(--scale-factor)*7.82px); font-family: sans-serif; transform: scaleX(0.901707);"]'))
        ).text
        self.assertEqual(importo2, "26,1000 €")

        self.driver.close() #chiude scheda
        self.driver.switch_to.window(self.driver.window_handles[0]) #torna alla prima

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@id="elimina"]'))
        ).click() #elimina fattura
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()
        self.wait_loader()

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="impostazioni-11"]'))
        ).click() #apro Generali

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-setting193-container"]'))
        ).click()    #seleziono 2 cifre decimali per gli importi
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys('2', Keys.ENTER)

    def quantita_stampa(self):
                self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//i[@class="fa fa-plus"]'))
        ).click()   #click su +

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idanagrafica_add-container"]'))
        ).click() #seleziono Cliente come anagrafica
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente", Keys.ENTER)
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary"]'))
        ).click() #click su aggiungi
        self.wait_loader()
        # riga 1
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="btn btn-primary"]'))
        ).click() #click su aggiungi riga

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("1")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("26,10")
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary pull-right"]'))
        ).click() #click su aggiungi
        #riga 2
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="btn btn-primary"]'))
        ).click() #click su aggiungi riga

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("2")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("8,34")
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary pull-right"]'))
        ).click() #click su aggiungi
        #riga 3
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="btn btn-primary"]'))
        ).click() #click su aggiungi riga

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("3")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("8,35")
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary pull-right"]'))
        ).click() #click su aggiungi
        #riga 4
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="btn btn-primary"]'))
        ).click() #click su aggiungi riga

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("4")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("8,34")
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary pull-right"]'))
        ).click() #click su aggiungi
        #riga 5
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="btn btn-primary"]'))
        ).click() #click su aggiungi riga

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("5")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("8,35")
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary pull-right"]'))
        ).click() #click su aggiungi
        #riga 6
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="btn btn-primary"]'))
        ).click() #click su aggiungi riga

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("6")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("16,60")
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary pull-right"]'))
        ).click() #click su aggiungi
        #riga 7
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="btn btn-primary"]'))
        ).click() #click su aggiungi riga

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("7")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("28,81")
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary pull-right"]'))
        ).click() #click su aggiungi

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idstatodocumento-container"]'))
        ).click() #cambio stato in "Emessa"
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Emessa", Keys.ENTER)
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@id="save"]'))
        ).click()
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@id="print-button_p"]'))
        ).click()

        self.driver.switch_to.window(self.driver.window_handles[1]) #cambia scheda

        quantita = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@style="left: 52.11%; top: 27.96%; font-size: calc(var(--scale-factor)*7.82px); font-family: sans-serif; transform: scaleX(0.901707);"]'))
        ).text
        self.assertEqual(quantita, "1,00")
        self.driver.close() #chiude scheda
        self.driver.switch_to.window(self.driver.window_handles[0]) #torna alla prima

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@id="elimina"]'))
        ).click() #elimina fattura
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()
        self.wait_loader()

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="impostazioni-11"]'))
        ).click() #apro Generali

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-setting194-container"]'))
        ).click()    #seleziono 4 cifre decimali per le quantità
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys('4', Keys.ENTER)

        self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//i[@class="fa fa-plus"]'))
        ).click()   #click su +

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idanagrafica_add-container"]'))
        ).click() #seleziono Cliente come anagrafica
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente", Keys.ENTER)
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary"]'))
        ).click() #click su aggiungi
        self.wait_loader()
        # riga 1
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="btn btn-primary"]'))
        ).click() #click su aggiungi riga

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("1")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("26,10")
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary pull-right"]'))
        ).click() #click su aggiungi
        #riga 2
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="btn btn-primary"]'))
        ).click() #click su aggiungi riga

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("2")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("8,34")
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary pull-right"]'))
        ).click() #click su aggiungi
        #riga 3
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="btn btn-primary"]'))
        ).click() #click su aggiungi riga

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("3")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("8,35")
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary pull-right"]'))
        ).click() #click su aggiungi
        #riga 4
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="btn btn-primary"]'))
        ).click() #click su aggiungi riga

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("4")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("8,34")
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary pull-right"]'))
        ).click() #click su aggiungi
        #riga 5
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="btn btn-primary"]'))
        ).click() #click su aggiungi riga

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("5")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("8,35")
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary pull-right"]'))
        ).click() #click su aggiungi
        #riga 6
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="btn btn-primary"]'))
        ).click() #click su aggiungi riga

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("6")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("16,60")
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary pull-right"]'))
        ).click() #click su aggiungi
        #riga 7
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="btn btn-primary"]'))
        ).click() #click su aggiungi riga

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("7")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("28,81")
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary pull-right"]'))
        ).click() #click su aggiungi

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idstatodocumento-container"]'))
        ).click() #cambio stato in "Emessa"
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Emessa", Keys.ENTER)
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@id="save"]'))
        ).click()
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@id="print-button_p"]'))
        ).click()

        self.driver.switch_to.window(self.driver.window_handles[1]) #cambia scheda

        quantita = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@style="left: 51.36%; top: 27.96%; font-size: calc(var(--scale-factor)*7.82px); font-family: sans-serif; transform: scaleX(0.901707);"]'))
        ).text
        self.assertEqual(quantita, "1,0000")
        self.driver.close() #chiude scheda
        self.driver.switch_to.window(self.driver.window_handles[0]) #torna alla prima

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@id="elimina"]'))
        ).click() #elimina fattura
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()
        self.wait_loader()

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="impostazioni-11"]'))
        ).click() #apro Generali

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-setting194-container"]'))
        ).click()    #seleziono 2 cifre decimali per le quantità
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys('2', Keys.ENTER)

    def totali_stampa(self):
                self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//i[@class="fa fa-plus"]'))
        ).click()   #click su +

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idanagrafica_add-container"]'))
        ).click() #seleziono Cliente come anagrafica
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente", Keys.ENTER)
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary"]'))
        ).click() #click su aggiungi
        self.wait_loader()
        # riga 1
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="btn btn-primary"]'))
        ).click() #click su aggiungi riga

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("1")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("26,10")
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary pull-right"]'))
        ).click() #click su aggiungi
        #riga 2
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="btn btn-primary"]'))
        ).click() #click su aggiungi riga

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("2")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("8,34")
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary pull-right"]'))
        ).click() #click su aggiungi
        #riga 3
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="btn btn-primary"]'))
        ).click() #click su aggiungi riga

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("3")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("8,35")
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary pull-right"]'))
        ).click() #click su aggiungi
        #riga 4
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="btn btn-primary"]'))
        ).click() #click su aggiungi riga

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("4")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("8,34")
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary pull-right"]'))
        ).click() #click su aggiungi
        #riga 5
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="btn btn-primary"]'))
        ).click() #click su aggiungi riga

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("5")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("8,35")
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary pull-right"]'))
        ).click() #click su aggiungi
        #riga 6
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="btn btn-primary"]'))
        ).click() #click su aggiungi riga

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("6")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("16,60")
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary pull-right"]'))
        ).click() #click su aggiungi
        #riga 7
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="btn btn-primary"]'))
        ).click() #click su aggiungi riga

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("7")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("28,81")
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary pull-right"]'))
        ).click() #click su aggiungi

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idstatodocumento-container"]'))
        ).click() #cambio stato in "Emessa"
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Emessa", Keys.ENTER)
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@id="save"]'))
        ).click()
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@id="print-button_p"]'))
        ).click()

        self.driver.switch_to.window(self.driver.window_handles[1]) #cambia scheda

        totale = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@style="left: 76.88%; top: 90.82%; font-size: calc(var(--scale-factor)*8.86px); font-family: sans-serif; transform: scaleX(0.900168);"]'))
        ).text
        self.assertEqual(totale, "127,97 €")
        self.driver.close() #chiude scheda
        self.driver.switch_to.window(self.driver.window_handles[0]) #torna alla prima

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@id="elimina"]'))
        ).click() #elimina fattura
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()
        self.wait_loader()

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="impostazioni-11"]'))
        ).click() #apro Generali

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-setting195-container"]'))
        ).click()    #seleziono 1 cifra decimali per le quantità
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys('1', Keys.ENTER)

        self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//i[@class="fa fa-plus"]'))
        ).click()   #click su +

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idanagrafica_add-container"]'))
        ).click() #seleziono Cliente come anagrafica
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente", Keys.ENTER)
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary"]'))
        ).click() #click su aggiungi
        self.wait_loader()
        # riga 1
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="btn btn-primary"]'))
        ).click() #click su aggiungi riga

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("1")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("26,10")
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary pull-right"]'))
        ).click() #click su aggiungi
        #riga 2
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="btn btn-primary"]'))
        ).click() #click su aggiungi riga

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("2")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("8,34")
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary pull-right"]'))
        ).click() #click su aggiungi
        #riga 3
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="btn btn-primary"]'))
        ).click() #click su aggiungi riga

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("3")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("8,35")
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary pull-right"]'))
        ).click() #click su aggiungi
        #riga 4
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="btn btn-primary"]'))
        ).click() #click su aggiungi riga

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("4")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("8,34")
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary pull-right"]'))
        ).click() #click su aggiungi
        #riga 5
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="btn btn-primary"]'))
        ).click() #click su aggiungi riga

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("5")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("8,35")
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary pull-right"]'))
        ).click() #click su aggiungi
        #riga 6
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="btn btn-primary"]'))
        ).click() #click su aggiungi riga

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("6")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("16,60")
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary pull-right"]'))
        ).click() #click su aggiungi
        #riga 7
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="btn btn-primary"]'))
        ).click() #click su aggiungi riga

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("7")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("28,81")
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary pull-right"]'))
        ).click() #click su aggiungi

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idstatodocumento-container"]'))
        ).click() #cambio stato in "Emessa"
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Emessa", Keys.ENTER)
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@id="save"]'))
        ).click()
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@id="print-button_p"]'))
        ).click()

        self.driver.switch_to.window(self.driver.window_handles[1]) #cambia scheda

        totale = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@style="left: 77.32%; top: 90.82%; font-size: calc(var(--scale-factor)*8.86px); font-family: sans-serif; transform: scaleX(0.900206);"]'))
        ).text
        self.assertEqual(totale, "128,0 €")
        self.driver.close() #chiude scheda
        self.driver.switch_to.window(self.driver.window_handles[0]) #torna alla prima

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@id="elimina"]'))
        ).click() #elimina fattura
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()
        self.wait_loader()

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="impostazioni-11"]'))
        ).click() #apro Generali

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-setting195-container"]'))
        ).click()    #seleziono 2 cifre decimali per le quantità
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys('2', Keys.ENTER)
        

    def listino_predefinito(self):
        wait = self.wait_driver  
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="impostazioni-11"]'))
        ).click() #apro Generali

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-setting196-container"]'))
        ).click()   #seleziona listino di prova

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-setting196-results"]//li'))
        ).click()

        self.navigateTo("Anagrafiche")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//i[@class="fa fa-plus"]'))
        ).click()   #click su +
        #creo anagrafica
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="ragione_sociale_add"]'))).send_keys('Test')    #nome anagrafica
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-selection select2-selection--multiple"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-idtipoanagrafica_add-results"]//li[2]'))
        ).click()  #tipo anagrafica cliente
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary"]'))
        ).click()   #click su aggiungi
        self.wait_loader()

        listino = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-id_listino-container"]'))
        ).text  #check se il listino è stato selezionato
        self.assertEqual(listino[2:26], "Listino cliente di Prova")
        #elimino anagrafica
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="btn btn-danger ask"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()
        self.wait_loader()

        self.expandSidebar("Strumenti") 
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="impostazioni-11"]'))
        ).click() #apro Generali

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-setting196-container"]//span'))
        ).click()

    def lingua(self):
        wait = self.wait_driver  
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="impostazioni-11"]'))
        ).click() #apro Generali

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-setting199-container"]'))
        ).click()   #metto la lingua in inglese
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys('English')

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(Keys.ENTER)
        self.navigateTo("Anagrafiche")
        self.wait_loader() 

        scritta = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//li[@id="2"]//p)[1]'))
        ).text   #controllo se ha cambiato lingua
        self.assertEqual(scritta, "Entities")
        #torno alle impostazioni di prima
        self.expandSidebar("Tools")
        self.navigateTo("Settings")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="impostazioni-11"]'))
        ).click() #apro Generali

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-setting199-container"]'))
        ).click()   #metto la lingua in italiano
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys('Italiano')

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(Keys.ENTER)
        self.navigateTo("Settings")
        self.wait_loader()

