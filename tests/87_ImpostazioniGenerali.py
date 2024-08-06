from common.Test import Test, get_html
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Impostazioni(Test):
    def setUp(self):
        super().setUp()

    def test_impostazioni_generali(self):
        # Nascondere la barra sinistra di default (2)
        self.nascondi_barra_sx()

        # Cambio cifre decimali per importi (3)
        self.cifre_decimali_importi()

        # Prima pagina (7)
        self.prima_pagina()

        # Cifre decimali per quantità (8)
        self.cifre_decimali_quantita()

        # Abilita esportazione Excel e PDF (11)
        self.esportazione_excel_pdf

        # Cambio valuta (12)
        self.valuta()

        # Visualizza riferimento su ogni riga in stampa (13)
        self.riferimento_riga_stampa()

        # Autocompletamento form (15)
        self.autocompletamento_form()   #da finire
        
        # Permetti selezione articoli con quantità minore o uguale a zero in Documenti di Vendita (22)
        self.quantita_minore_uguale_zero()

        # Cambio periodo calendario (23-24)
        self.periodo_calendario()

        # Permetti il superamento della soglia quantità dei documenti di origine (25)
        self.superamento_soglia_quantita()

        # Aggiungi riferimento tra documenti (26)
        self.aggiungi_riferimento_documenti()

        # Aggiungi riferimento tra tutti i documenti collegati (27)
        self.aggiungi_riferimenti_tutti_documenti()

        # Aggiungi le note delle righe tra documenti (28)
        self.aggiungi_note_documenti()

        # Dimensione widget predefinita (29)
        self.dimensione_widget_predefinita()

        # Tipo di sconto predefinito (33)
        self.tipo_sconto_predefinito()

        # Cifre decimali per importi in stampa (34)
        self.importi_stampa()

        # Cifre decimali per quantità in stampa (35)
        self.quantita_stampa()

        # Cifre decimali per totali in stampa (36)
        self.totali_stampa()

        # Listino cliente predefinito (37)
        self.listino_predefinito()

        # Cambio lingua (38)
        self.lingua()


    def nascondi_barra_sx(self):
        wait = WebDriverWait(self.driver, 20)
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-11"]').click() #apro Generali
        sleep(1)

        self.find(By.XPATH, '(//label[@class="btn btn-default active"])[1]').click() #attivo impostazione
        sleep(1)

        self.navigateTo("Impostazioni")
        self.wait_loader()
        sleep(2)

        self.find(By.XPATH, '//body[@class="sidebar-mini layout-fixed  sidebar-collapse"]') #controlla se trova la classe sidebar-collapse
        #torno alle impostazioni di prima
        self.find(By.XPATH, '//div[@id="impostazioni-11"]').click() #apro Generali
        sleep(1)

        self.find(By.XPATH, '(//label[@class="btn btn-default active"])[1]').click() #disattivo impostazione
        sleep(1)

        self.navigateTo("Impostazioni")
        self.wait_loader()
        sleep(1)

    def cifre_decimali_importi(self):
        wait = WebDriverWait(self.driver, 20)
        self.find(By.XPATH, '//div[@id="impostazioni-11"]').click() #apro Generali
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-setting47-container"]').click()    #seleziono 4 cifre decimali per gli importi
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys('4', Keys.ENTER)
        sleep(1)

        self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.find(By.XPATH, '//button[@class="btn btn-primary bound clickable"]').click()   #click su +
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-idanagrafica_add-container"]').click() #seleziono Cliente come anagrafica
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente", Keys.ENTER)
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click() #click su aggiungi
        self.wait_loader()

        self.find(By.XPATH, '//span[@id="select2-id_articolo-container"]').click()  #aggiungo un articolo
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys('Articolo 1')
        sleep(2)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(Keys.ENTER)
        self.find(By.XPATH, '//button[@class="btn btn-primary tip tooltipstered"]').click() #click su aggiungi
        sleep(1)

        importo=self.find(By.XPATH, '//tbody//tr[1]//td[9]').text   #controllo se l'importo corrisponde a 20 euro con 4 cifre decimali
        self.assertEqual(importo, "20,0000 €")

        self.find(By.XPATH, '//a[@id="elimina"]').click() #elimina fattura
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()
        #torno alle impostazioni di prima
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.find(By.XPATH, '//div[@id="impostazioni-11"]').click() #apro Generali
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-setting47-container"]').click()    #seleziono 2 cifre decimali per gli importi
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys('2', Keys.ENTER)
        sleep(1)

    def prima_pagina(self):
        wait = WebDriverWait(self.driver, 20)  
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-11"]').click() #apro Generali
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-setting59-container"]').click()    #metto come prima pagina "Anagrafiche"
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Anagrafiche")
        sleep(2)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-setting59-results"]//li[2]'))).click()
        sleep(2)

        self.find(By.XPATH, '//a[@class="nav-link bg-danger"]').click() #logout
        self.wait_loader()
        sleep(2)

        #login
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="form-control"]'))).send_keys(self.getConfig('login.username'))
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="password"]'))).send_keys(self.getConfig('login.password')) #password da mettere prima del test
        self.find(By.XPATH, '//button[@class="btn btn-danger btn-block btn-flat"]').click() 
        sleep(2)
        self.wait_loader()

        pagina=self.find(By.XPATH, '//a[@class="nav-link active"]').text    #check se la prima pagina è quella delle Anagrafiche
        self.assertEqual(pagina[2:13], "Anagrafiche")
        #torno alle impostazioni di prima
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-11"]').click() #apro Generali
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-setting59-container"]').click()    #metto come prima pagina "Dashboard"
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Dashboard")
        sleep(2)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(Keys.ENTER)
        sleep(2)

        self.find(By.XPATH, '//a[@class="nav-link bg-danger"]').click() #logout
        self.wait_loader()
        sleep(2)

        #login
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="form-control"]'))).send_keys(self.getConfig('login.username'))
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="password"]'))).send_keys(self.getConfig('login.password')) #password da mettere prima del test
        self.find(By.XPATH, '//button[@class="btn btn-danger btn-block btn-flat"]').click() 
        sleep(2)
        self.wait_loader()

    def cifre_decimali_quantita(self):
        wait = WebDriverWait(self.driver, 20)
        self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")
        self.wait_loader()
        sleep(1)

        self.find(By.XPATH, '//button[@class="btn btn-primary bound clickable"]').click()   #click su +
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-idanagrafica_add-container"]').click() #seleziono Cliente come anagrafica
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente", Keys.ENTER)
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click() #click su aggiungi
        self.wait_loader()

        self.find(By.XPATH, '//span[@id="select2-id_articolo-container"]').click()  #aggiungo un articolo
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys('Articolo 1')
        sleep(2)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(Keys.ENTER)
        self.find(By.XPATH, '//button[@class="btn btn-primary tip tooltipstered"]').click() #click su aggiungi
        sleep(1)

        quantita_element = self.find(By.XPATH, '(//tbody[@id="righe"]//input)[2]')   #check cifre decimali
        quantita = quantita_element.get_attribute("decimals")
        self.assertEqual(quantita, "2") 
        self.find(By.XPATH, '//a[@id="elimina"]').click() #elimina fattura
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-11"]').click() #apro Generali
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-setting60-container"]').click()    #seleziono 4 cifre decimali per le quantità
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys('4', Keys.ENTER)
        sleep(1)

        self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")
        self.wait_loader()
        sleep(1)

        self.find(By.XPATH, '//button[@class="btn btn-primary bound clickable"]').click()   #click su +
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-idanagrafica_add-container"]').click() #seleziono Cliente come anagrafica
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente", Keys.ENTER)
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click() #click su aggiungi
        self.wait_loader()

        self.find(By.XPATH, '//span[@id="select2-id_articolo-container"]').click()  #aggiungo un articolo
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys('Articolo 1')
        sleep(2)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(Keys.ENTER)
        self.find(By.XPATH, '//button[@class="btn btn-primary tip tooltipstered"]').click() #click su aggiungi
        sleep(1)

        quantita_element = self.find(By.XPATH, '(//tbody[@id="righe"]//input)[2]')   #check cifre decimali
        quantita = quantita_element.get_attribute("decimals")
        self.assertEqual(quantita, "4") 
        self.find(By.XPATH, '//a[@id="elimina"]').click() #elimina fattura
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()
        #torno alle impostazioni di prima
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.find(By.XPATH, '//div[@id="impostazioni-11"]').click() #apro Generali
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-setting60-container"]').click()    #seleziono 2 cifre decimali per le quanità
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys('2', Keys.ENTER)
        sleep(1)

    def esportazione_excel_pdf(self):
        wait = WebDriverWait(self.driver, 20)  
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-11"]').click() #apro Generali
        sleep(1)

        self.find(By.XPATH, '(//label[@class="btn btn-default active"])[6]').click()    #attiva impostazione
        sleep(2)

        self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr[1]//td[1]').click()    #seleziono prima fattura
        self.find(By.XPATH, '//button[@class="btn btn-primary table-btn dropdown-toggle"]').click() #click su esporta
        sleep(1)

        self.find(By.XPATH, '//ul[@class="dropdown-menu show"]//a[1]').click()
        sleep(2)

        self.driver.close() #chiude scheda
        self.driver.switch_to.window(self.driver.window_handles[0]) #torna alla prima
        sleep(1)

        self.find(By.XPATH, '//button[@class="btn btn-primary table-btn dropdown-toggle"]').click() #click su esporta
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//ul[@class="dropdown-menu show"]//a[2]'))) #controllo se c'è l'esporta excel
        self.find(By.XPATH, '//tbody//tr[1]//td[1]').click()    #diseleziono prima fattura
        #torno alle impostazioni di prima
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-11"]').click() #apro Generali
        sleep(1)

        self.find(By.XPATH, '(//label[@class="btn btn-default active"])[6]').click()    #disattiva impostazione
        sleep(2)


    def valuta(self):
        wait = WebDriverWait(self.driver, 20)  
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-11"]').click() #apro Generali
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-setting83-container"]').click() #cambio valuta in sterline
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys('Sterlina', Keys.ENTER)
        sleep(1)

        self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr//td[2]').click() #apro prima fattura
        self.wait_loader()

        nuova_valuta=self.find(By.XPATH, '//tbody//tr[1]//td[5]//div//span').text   #controllo se è cambiata la valuta
        self.assertEqual(nuova_valuta, "£")
        #torno alle impostazioni di prima
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.find(By.XPATH, '//div[@id="impostazioni-11"]').click() #apro Generali
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-setting83-container"]').click() #cambio valuta in euro
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys('Euro', Keys.ENTER)
        sleep(1)

    def riferimento_riga_stampa(self):
        wait = WebDriverWait(self.driver, 20)
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-11"]').click() #apro Generali
        sleep(1)

        self.find(By.XPATH, '(//label[@class="btn btn-default active"])[4]').click()   #disattivo impostazione
        sleep(2)

        #crea ordine
        self.expandSidebar("Vendite")
        self.navigateTo("Ordini cliente")
        self.wait_loader()

        self.find(By.XPATH, '//button[@class="btn btn-primary bound clickable"]').click()   #click su tasto +
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-idanagrafica-container"]').click()     #scelta di "Cliente" come anagrafica per l'ordine
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys('Cliente')
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(Keys.ENTER)
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click()   #click su tasto aggiungi
        self.wait_loader()
        #aggiungi articolo
        self.find(By.XPATH, '//span[@id="select2-id_articolo-container"]').click()
        sleep(1)

        self.find(By.XPATH, '//ul[@class="select2-results__options select2-results__options--nested"]//li[1]').click()
        self.find(By.XPATH, '//button[@class="btn btn-primary tip tooltipstered"]').click() #click su aggiungi
        sleep(2)

        #aggiungi articolo
        self.find(By.XPATH, '//span[@id="select2-id_articolo-container"]').click()
        sleep(1)

        self.find(By.XPATH, '//ul[@class="select2-results__options select2-results__options--nested"]//li[1]').click()
        self.find(By.XPATH, '//button[@class="btn btn-primary tip tooltipstered"]').click() #click su aggiungi
        sleep(2)
        #cambio stato
        self.find(By.XPATH, '//span[@id="select2-idstatoordine-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Accettato", Keys.ENTER)
        self.find(By.XPATH, '//button[@id="save"]').click()
        self.wait_loader()
        #crea ddt
        self.find(By.XPATH, '//button[@class="btn btn-info dropdown-toggle "]').click() #click su crea
        sleep(1)

        self.find(By.XPATH, '//ul[@class="dropdown-menu dropdown-menu-right show"]//a[3]').click()  #click su crea ddt
        sleep(2)

        self.find(By.XPATH, '//span[@id="select2-id_causale_trasporto-container"]').click() #causale trasporto
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-id_causale_trasporto-results"]//li[1]').click()
        self.find(By.XPATH, '//span[@id="select2-id_segment-container"]').click()   #sezionale
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-id_segment-results"]//li[1]').click()
        self.find(By.XPATH, '//button[@id="submit_btn"]').click()   #click su aggiungi
        self.wait_loader()
        #cambia stato
        self.find(By.XPATH, '//span[@id="select2-idstatoddt-container"]').click()
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-idstatoddt-results"]//li[2]').click()    #stato evaso
        self.find(By.XPATH, '//button[@id="save"]').click()
        self.wait_loader()

        self.find(By.XPATH, '//button[@class="btn btn-info bound clickable"]').click()  #crea fattura di vendita
        sleep(2)

        self.find(By.XPATH, '//button[@id="submit_btn"]').click()   #click su aggiungi
        self.wait_loader()

        self.find(By.XPATH, '//a[@id="print-button_p"]').click()    #stampa fattura
        sleep(2)

        self.driver.switch_to.window(self.driver.window_handles[1]) #cambia scheda
        sleep(2)

        primo_riferimento=self.find(By.XPATH, '(//div[@id="viewer"]//span)[38]').text
        self.assertEqual(primo_riferimento[0:27], "Rif. ordine cliente num. 02")
        secondo_riferimento=self.find(By.XPATH, '(//div[@id="viewer"]//span)[39]').text
        self.assertEqual(secondo_riferimento[0:27], "Ddt in uscita num. 02")
        self.driver.close() #chiude scheda
        self.driver.switch_to.window(self.driver.window_handles[0]) #torna alla prima
        sleep(1)
        #elimina fattura
        self.find(By.XPATH, '//a[@id="elimina"]').click()
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()
        #elimina ordine
        self.navigateTo("Ordini cliente")
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr[1]//td[2]').click() 
        self.wait_loader()

        self.find(By.XPATH, '//a[@class="btn btn-danger ask"]').click()
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()
        #elimina ddt
        self.expandSidebar("Magazzino") 
        self.navigateTo("Ddt in uscita")
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr[1]//td[2]').click()
        self.wait_loader()

        self.find(By.XPATH, '//a[@class="btn btn-danger ask"]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()
        #torna alle impostazioni di prima
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-11"]').click() #apro Generali
        sleep(1)

        self.find(By.XPATH, '(//label[@class="btn btn-default active"])[4]').click()   #attivo impostazione
        sleep(2)

        #crea ordine
        self.expandSidebar("Vendite")
        self.navigateTo("Ordini cliente")
        self.wait_loader()

        self.find(By.XPATH, '//button[@class="btn btn-primary bound clickable"]').click()   #click su tasto +
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-idanagrafica-container"]').click()     #scelta di "Cliente" come anagrafica per l'ordine
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys('Cliente')
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(Keys.ENTER)
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click()   #click su tasto aggiungi
        self.wait_loader()
        #aggiungi articolo
        self.find(By.XPATH, '//span[@id="select2-id_articolo-container"]').click()
        sleep(1)

        self.find(By.XPATH, '//ul[@class="select2-results__options select2-results__options--nested"]//li[1]').click()
        self.find(By.XPATH, '//button[@class="btn btn-primary tip tooltipstered"]').click() #click su aggiungi
        sleep(2)

        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click()   #click su tasto aggiungi
        self.wait_loader()
        #aggiungi articolo
        self.find(By.XPATH, '//span[@id="select2-id_articolo-container"]').click()
        sleep(1)

        self.find(By.XPATH, '//ul[@class="select2-results__options select2-results__options--nested"]//li[1]').click()
        self.find(By.XPATH, '//button[@class="btn btn-primary tip tooltipstered"]').click() #click su aggiungi
        sleep(2)
        #cambio stato
        self.find(By.XPATH, '//span[@id="select2-idstatoordine-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Accettato", Keys.ENTER)
        self.find(By.XPATH, '//button[@id="save"]').click()
        self.wait_loader()
        #crea ddt
        self.find(By.XPATH, '//button[@class="btn btn-info dropdown-toggle "]').click() #click su crea
        sleep(1)

        self.find(By.XPATH, '//ul[@class="dropdown-menu dropdown-menu-right show"]//a[3]').click()  #click su crea ddt
        sleep(2)

        self.find(By.XPATH, '//span[@id="select2-id_causale_trasporto-container"]').click() #causale trasporto
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-id_causale_trasporto-results"]//li[1]').click()
        self.find(By.XPATH, '//span[@id="select2-id_segment-container"]').click()   #sezionale
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-id_segment-results"]//li[1]').click()
        self.find(By.XPATH, '//button[@id="submit_btn"]').click()   #click su aggiungi
        self.wait_loader()
        #cambia stato
        self.find(By.XPATH, '//span[@id="select2-idstatoddt-container"]').click()
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-idstatoddt-results"]//li[2]').click()    #stato evaso
        self.find(By.XPATH, '//button[@id="save"]').click()
        self.wait_loader()

        self.find(By.XPATH, '//button[@class="btn btn-info bound clickable"]').click()  #crea fattura di vendita
        sleep(2)

        self.find(By.XPATH, '//button[@id="submit_btn"]').click()   #click su aggiungi
        self.wait_loader()

        self.find(By.XPATH, '//a[@id="print-button_p"]').click()    #stampa fattura
        sleep(2)

        self.driver.switch_to.window(self.driver.window_handles[1]) #cambia scheda
        sleep(2)

        primo_riferimento=self.find(By.XPATH, '(//div[@id="viewer"]//span)[40]').text
        self.assertEqual(primo_riferimento[0:27], "Rif. ordine cliente num. 02")

        self.driver.close() #chiude scheda
        self.driver.switch_to.window(self.driver.window_handles[0]) #torna alla prima
        sleep(1)
        #elimina fattura
        self.find(By.XPATH, '//a[@id="elimina"]').click()
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()
        #elimina ordine
        self.navigateTo("Ordini cliente")
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr[1]//td[2]').click() 
        self.wait_loader()

        self.find(By.XPATH, '//a[@class="btn btn-danger ask"]').click()
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()
        #elimina ddt
        self.expandSidebar("Magazzino") 
        self.navigateTo("Ddt in uscita")
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr[1]//td[2]').click()
        self.wait_loader()

        self.find(By.XPATH, '//a[@class="btn btn-danger ask"]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()



    def autocompletamento_form(self):
        wait = WebDriverWait(self.driver, 20)
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-11"]').click() #apro Generali
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-setting93-container"]').click()    #autocopletamento on
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-setting93-results"]//li[1]').click()
        sleep(2)

        self.navigateTo("Anagrafiche")
        self.wait_loader()

        self.find(By.XPATH, '//button[@class="btn btn-primary bound clickable"]').click()   #click su +
        sleep(2)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="ragione_sociale_add"]'))).send_keys('Prova')
        self.find(By.XPATH, '//span[@class="select2-selection select2-selection--multiple"]').click()   #tipo anagrafica cliente
        sleep(1)

        self.find(By.XPATH,'//ul[@id="select2-idtipoanagrafica_add-results"]//li[2]').click()
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click()
        self.wait_loader()

        #elimino anagrafica
        self.find(By.XPATH, '//a[@class="btn btn-danger ask"]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()

        self.navigateTo("Anagrafiche")
        self.wait_loader()

        self.find(By.XPATH, '//button[@class="btn btn-primary bound clickable"]').click()   #click su +
        sleep(2)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="ragione_sociale_add"]'))).send_keys('Pro')
        sleep(1)

        #controllo se appare il suggerimento
        self.find(By.XPATH, '//button[@class="close"]').click()
        sleep(1)
        #torno alle impostazioni di prima
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-11"]').click() #apro Generali
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-setting93-container"]').click()    #autocompletamento off
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-setting93-results"]//li[2]').click()
        sleep(2)


    def quantita_minore_uguale_zero(self):
        wait = WebDriverWait(self.driver, 20)
        self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")
        self.wait_loader()
        sleep(1)

        self.find(By.XPATH, '//button[@class="btn btn-primary bound clickable"]').click()   #click su +
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-idanagrafica_add-container"]').click() #seleziono Cliente come anagrafica
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente", Keys.ENTER)
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click() #click su aggiungi
        self.wait_loader()

        self.find(By.XPATH, '//span[@id="select2-id_articolo-container"]').click()  #aggiungo un articolo
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys('Vestito')
        sleep(2)

        self.find(By.XPATH, '//ul[@class="select2-results__options select2-results__options--nested"]//li[1]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@class="btn btn-primary tip tooltipstered"]').click() #click su aggiungi
        sleep(1) 

        messaggio=self.find(By.XPATH, '//div[@id="swal2-content"]').text    #check se esce l'errore
        self.assertEqual(messaggio, "Nessun articolo corrispondente a magazzino")
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-primary"]').click()  #esce dal errore
        sleep(1)

        self.find(By.XPATH, '//a[@id="elimina"]').click() #elimina fattura
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-11"]').click() #apro Generali
        sleep(1)

        self.find(By.XPATH, '(//label[@class="btn btn-default active"])[8]').click() #attiva impostazione
        sleep(1)

        self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")
        self.wait_loader()
        sleep(1)

        self.find(By.XPATH, '//button[@class="btn btn-primary bound clickable"]').click()   #click su +
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-idanagrafica_add-container"]').click() #seleziono Cliente come anagrafica
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente", Keys.ENTER)
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click() #click su aggiungi
        self.wait_loader()

        self.find(By.XPATH, '//span[@id="select2-id_articolo-container"]').click()  #aggiungo un articolo
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys('Vestito')
        sleep(2)

        self.find(By.XPATH, '//ul[@class="select2-results__options select2-results__options--nested"]//li[1]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@class="btn btn-primary tip tooltipstered"]').click() #click su aggiungi
        sleep(1)

        articolo=self.find(By.XPATH, '//tbody[@id="righe"]//td[2]').text    #check se l'articolo è stato aggiunto
        self.assertEqual(articolo, "1")
        self.find(By.XPATH, '//a[@id="elimina"]').click() #elimina fattura
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()
        #torno alle impostazioni di prima
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.find(By.XPATH, '//div[@id="impostazioni-11"]').click() #apro Generali
        sleep(1)

        self.find(By.XPATH, '(//label[@class="btn btn-default active"])[8]').click() #disattiva impostazione
        sleep(1)



    def periodo_calendario(self):
        wait = WebDriverWait(self.driver, 20)  
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-11"]').click() #apro Generali
        sleep(1)

        self.find(By.XPATH, '//input[@id="setting135"]').click()
        data_inizio=self.find(By.XPATH, '//input[@id="setting135"]') #cambio inizio periodo
        data_inizio.clear()
        data_inizio.send_keys("01/01/2024", Keys.ENTER)
        self.find(By.XPATH, '//input[@id="setting135"]').click()
        data_fine=self.find(By.XPATH, '//input[@id="setting136"]') #cambio fine periodo
        data_fine.clear()
        data_fine.send_keys("30/06/2024", Keys.ENTER)
        sleep(2)

        self.find(By.XPATH, '//a[@class="nav-link bg-danger"]').click() #logout
        self.wait_loader()
        sleep(2)

        #login
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="form-control"]'))).send_keys(self.getConfig('login.username'))
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="password"]'))).send_keys('') #password da mettere prima del test
        self.find(By.XPATH, '//button[@class="btn btn-danger btn-block btn-flat"]').click() 
        sleep(2)
        self.wait_loader()

        data=self.find(By.XPATH, '//a[@class="nav-link text-danger"]').text #controllo se la data è cambiata
        self.assertEqual(data, "01/01/2024 - 30/06/2024")
        #torno alle impostazioni di prima
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.find(By.XPATH, '//div[@id="impostazioni-11"]').click() #apro Generali
        sleep(1)

        data_inizio=self.find(By.XPATH, '//input[@id="setting135"]') #cambio inizio periodo
        data_inizio.clear()
        data_inizio.send_keys("01/01/2024", Keys.ENTER)
        data_fine=self.find(By.XPATH, '//input[@id="setting136"]') #cambio fine periodo
        data_fine.clear()
        data_fine.send_keys("31/12/2024", Keys.ENTER)
        self.find(By.XPATH, '//a[@class="nav-link bg-danger"]').click() #logout
        self.wait_loader()

        #login
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="form-control"]'))).send_keys(self.getConfig('login.username'))
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="password"]'))).send_keys(self.getConfig('login.password')) #password da mettere prima del test
        self.find(By.XPATH, '//button[@class="btn btn-danger btn-block btn-flat"]').click() 
        sleep(2)
        self.wait_loader()

    def superamento_soglia_quantita(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Impostazioni")
        self.find(By.XPATH, '//div[@id="impostazioni-11"]').click() #apro Generali
        sleep(1)

        self.find(By.XPATH, '(//label[@class="btn btn-default active"])[9]').click()    #attivo impostazione
        sleep(2)
        #crea attività
        self.navigateTo("Attività")
        self.wait_loader()

        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click()  #click su +
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-idanagrafica-container"]').click() #seleziono Cliente come anagrafica
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-dropdown select2-dropdown--below"]//input'))).send_keys("Cliente", Keys.ENTER)
        self.find(By.XPATH, '//span[@id="select2-idtipointervento-container"]').click() #seleziono Generico come tipo di intervento
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys("Generico")
        sleep(1)

        self.find(By.XPATH, '//li[@class="select2-results__option select2-results__option--highlighted"]').click()  #click su primo risultato
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//iframe[@class="cke_wysiwyg_frame cke_reset"])[1]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//iframe[@class="cke_wysiwyg_frame cke_reset"])[1]'))).send_keys("Test")   #scrivo "Test" come richiesta
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click()   #click su Aggiungi
        self.wait_loader()
        sleep(2)
        #aggiungi articolo
        self.find(By.XPATH, '//span[@id="select2-id_articolo-container"]').click()
        sleep(1)

        self.find(By.XPATH, '//ul[@class="select2-results__options select2-results__options--nested"]//li[1]').click()
        self.find(By.XPATH, '//button[@class="btn btn-primary tip tooltipstered"]').click() #click su aggiungi
        sleep(2)
        #cambio stato
        self.find(By.XPATH, '//span[@id="select2-idstatointervento-container"]').click()
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-idstatointervento-results"]//li[1]').click() #imposto stato "Completato"
        self.find(By.XPATH, '//button[@id="save"]').click() #click su salva
        self.wait_loader()

        #creo preventivo
        self.expandSidebar("Vendite")
        self.navigateTo("Preventivi")
        self.wait_loader()

        self.find(By.XPATH, '//button[@class="btn btn-primary bound clickable"]').click()   #click su +
        sleep(1)
        #nome
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="nome"]'))).send_keys('Test')
        #cliente
        self.find(By.XPATH, '//span[@id="select2-idanagrafica-container"]').click()
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-idanagrafica-results"]//li[2]').click()
        #tipo di attività
        self.find(By.XPATH, '//span[@id="select2-idtipointervento-container"]').click()
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-idtipointervento-results"]//li[1]').click()
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click()   #click su aggiungi
        self.wait_loader()
        #aggiungi articolo
        self.find(By.XPATH, '//span[@id="select2-id_articolo-container"]').click()
        sleep(1)

        self.find(By.XPATH, '//ul[@class="select2-results__options select2-results__options--nested"]//li[1]').click()
        self.find(By.XPATH, '//button[@class="btn btn-primary tip tooltipstered"]').click() #click su aggiungi
        sleep(2)

        self.driver.execute_script('window.scrollTo(0,0)')
        sleep(1)

        #cambio stato
        self.find(By.XPATH, '//span[@id="select2-idstato-container"]').click()
        sleep(2)

        self.find(By.XPATH, '//ul[@id="select2-idstato-results"]//li[1]').click() #imposto stato "Accettato"
        self.find(By.XPATH, '//button[@id="save"]').click() #click su salva
        self.wait_loader()

        #crea contratto
        self.navigateTo("Contratti")
        self.wait_loader()

        self.find(By.XPATH, '//button[@class="btn btn-primary bound clickable"]').click()
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="nome"]'))).send_keys("Test")
        self.find(By.XPATH, '//span[@id="select2-idanagrafica-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente", Keys.ENTER)
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="data_accettazione"]'))).send_keys("01/01/2024")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="data_conclusione"]'))).send_keys("31/12/2024")
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click()
        self.wait_loader()
        #aggiungi articolo
        self.find(By.XPATH, '//span[@id="select2-id_articolo-container"]').click()
        sleep(1)

        self.find(By.XPATH, '//ul[@class="select2-results__options select2-results__options--nested"]//li[1]').click()
        self.find(By.XPATH, '//button[@class="btn btn-primary tip tooltipstered"]').click() #click su aggiungi
        sleep(2)
        #cambio stato
        self.find(By.XPATH, '//span[@id="select2-idstato-container"]').click()
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-idstato-results"]//li[1]').click() #imposto stato "Accettato"
        self.find(By.XPATH, '//button[@id="save"]').click() #click su salva
        self.wait_loader()
        #creo ddt
        self.expandSidebar("Magazzino")
        self.navigateTo("Ddt in uscita")
        self.wait_loader()

        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click() #click su +
        sleep(1)
        #seleziono destinatario
        self.find(By.XPATH, '//span[@id="select2-idanagrafica_add-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente")
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(Keys.ENTER)
        #seleziono causale trasporto
        self.find(By.XPATH, '//span[@id="select2-idcausalet-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Conto lavorazione")
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(Keys.ENTER)
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click() #click su aggiungi
        self.wait_loader()

        #aggiungi articolo
        self.find(By.XPATH, '//span[@id="select2-id_articolo-container"]').click()
        sleep(1)

        self.find(By.XPATH, '//ul[@class="select2-results__options select2-results__options--nested"]//li[1]').click()
        self.find(By.XPATH, '//button[@class="btn btn-primary tip tooltipstered"]').click() #click su aggiungi
        sleep(2)

        self.find(By.XPATH, '//span[@id="select2-idstatoddt-container"]').click() #cambio stato in evaso
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Evaso", Keys.ENTER)
        self.find(By.XPATH, '//button[@id="save"]').click()
        self.wait_loader()
        #crea ordine
        self.expandSidebar("Vendite")
        self.navigateTo("Ordini cliente")
        self.wait_loader()

        self.find(By.XPATH, '//button[@class="btn btn-primary bound clickable"]').click()   #click su tasto +
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-idanagrafica-container"]').click()     #scelta di "Cliente" come anagrafica per l'ordine
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys('Cliente')
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(Keys.ENTER)
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click()   #click su tasto aggiungi
        self.wait_loader()
        #aggiungi articolo
        self.find(By.XPATH, '//span[@id="select2-id_articolo-container"]').click()
        sleep(1)

        self.find(By.XPATH, '//ul[@class="select2-results__options select2-results__options--nested"]//li[1]').click()
        self.find(By.XPATH, '//button[@class="btn btn-primary tip tooltipstered"]').click() #click su aggiungi
        sleep(2)
        #cambio stato
        self.find(By.XPATH, '//span[@id="select2-idstatoordine-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Accettato", Keys.ENTER)
        self.find(By.XPATH, '//button[@id="save"]').click()
        self.wait_loader()
        
        #crea fattura
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.find(By.XPATH, '//button[@class="btn btn-primary bound clickable"]').click()   #click su +
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-idanagrafica_add-container"]').click() #seleziono Cliente come anagrafica
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente")
        sleep(2)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(Keys.ENTER)
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click() #click su aggiungi
        self.wait_loader()

        self.find(By.XPATH, '//button[@class="btn btn-primary dropdown-toggle"]').click() #click su altro
        #attività
        self.find(By.XPATH, '//ul[@class="dropdown-menu dropdown-menu-right show"]//a[3]').click()
        sleep(2)

        self.find(By.XPATH, '//span[@id="select2-idintervento-container"]').click()
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-idintervento-results"]//li[2]').click()  #seleziona attività creata prima
        self.find(By.XPATH, '//button[@class="btn btn-primary pull-right"]').click()    #click su aggiungi
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//tbody[@id="righe"]//tr[2]//td[4]//input'))).send_keys("2", Keys.ENTER) #imposta quantità a 2
        sleep(2)

        qta_element = self.find(By.XPATH, '//tbody[@id="righe"]//tr[2]//td[4]//input')    #controllo se la quantità è cambiata
        qta = qta_element.get_attribute("value")
        self.assertEqual(qta, "2,00") 
        self.find(By.XPATH, '//input[@id="check_all"]').click() #elimino righe
        self.find(By.XPATH, '//button[@id="elimina_righe"]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-primary"]').click()
        sleep(2)
        #preventivi
        self.find(By.XPATH, '//button[@class="btn btn-primary dropdown-toggle"]').click() #click su altro
        self.find(By.XPATH, '//ul[@class="dropdown-menu dropdown-menu-right show"]//a[4]').click()
        sleep(2)

        self.find(By.XPATH, '//span[@id="select2-id_documento-container"]').click()
        sleep(2)

        self.find(By.XPATH, '//ul[@id="select2-id_documento-results"]//li[2]').click()
        sleep(2)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//tbody[@id="righe_documento_importato"]//tr[1]//td[4]//input'))).send_keys("2", Keys.ENTER)
        sleep(3)

        qta_element = self.find(By.XPATH, '//tbody[@id="righe"]//tr[1]//td[4]//input')    #controllo se la quantità è cambiata
        qta = qta_element.get_attribute("value")
        self.assertEqual(qta, "2,00") 
        self.find(By.XPATH, '//input[@id="check_all"]').click() #elimino righe
        self.find(By.XPATH, '//button[@id="elimina_righe"]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-primary"]').click()
        sleep(2)
        #contratti
        self.find(By.XPATH, '//button[@class="btn btn-primary dropdown-toggle"]').click() #click su altro
        self.find(By.XPATH, '//ul[@class="dropdown-menu dropdown-menu-right show"]//a[5]').click()
        sleep(2)

        self.find(By.XPATH, '//span[@id="select2-id_documento-container"]').click()
        sleep(2)

        self.find(By.XPATH, '//ul[@id="select2-id_documento-results"]//li[3]').click()
        sleep(2)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//tbody[@id="righe_documento_importato"]//tr[1]//td[4]//input'))).send_keys("2", Keys.ENTER)
        sleep(3)

        qta_element = self.find(By.XPATH, '//tbody[@id="righe"]//tr[1]//td[4]//input')    #controllo se la quantità è cambiata
        qta = qta_element.get_attribute("value")
        self.assertEqual(qta, "2,00") 
        self.find(By.XPATH, '//input[@id="check_all"]').click() #elimino righe
        self.find(By.XPATH, '//button[@id="elimina_righe"]').click()
        sleep(1)
        #ddt
        self.find(By.XPATH, '//button[@class="btn btn-primary dropdown-toggle"]').click() #click su altro
        self.find(By.XPATH, '//ul[@class="dropdown-menu dropdown-menu-right show"]//a[6]').click()
        sleep(2)

        self.find(By.XPATH, '//span[@id="select2-id_documento-container"]').click()
        sleep(2)

        self.find(By.XPATH, '//ul[@id="select2-id_documento-results"]//li[1]').click()
        sleep(2)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//tbody[@id="righe_documento_importato"]//tr[1]//td[4]//input'))).send_keys("2", Keys.ENTER)
        sleep(3)

        qta_element = self.find(By.XPATH, '//tbody[@id="righe"]//tr[1]//td[4]//input')    #controllo se la quantità è cambiata
        qta = qta_element.get_attribute("value")
        self.assertEqual(qta, "2,00") 
        self.find(By.XPATH, '//input[@id="check_all"]').click() #elimino righe
        self.find(By.XPATH, '//button[@id="elimina_righe"]').click()
        sleep(1)
        #ordine
        self.find(By.XPATH, '//button[@class="btn btn-primary dropdown-toggle"]').click() #click su altro
        self.find(By.XPATH, '//ul[@class="dropdown-menu dropdown-menu-right show"]//a[7]').click()
        sleep(2)

        self.find(By.XPATH, '//span[@id="select2-id_documento-container"]').click()
        sleep(2)

        self.find(By.XPATH, '//ul[@id="select2-id_documento-results"]//li[1]').click()
        sleep(2)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//tbody[@id="righe_documento_importato"]//tr[1]//td[4]//input'))).send_keys("2", Keys.ENTER)
        sleep(3)

        qta_element = self.find(By.XPATH, '//tbody[@id="righe"]//tr[1]//td[4]//input')    #controllo se la quantità è cambiata
        qta = qta_element.get_attribute("value")
        self.assertEqual(qta, "2,00") 
        self.find(By.XPATH, '//input[@id="check_all"]').click() #elimino righe
        self.find(By.XPATH, '//button[@id="elimina_righe"]').click()
        sleep(1)

        #torno alle impostazioni di prima
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-11"]').click() #apro Generali
        sleep(1)

        self.find(By.XPATH, '(//label[@class="btn btn-default active"])[9]').click()    #disattivo impostazione
        sleep(2)
        
        self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr[1]//td[2]').click()    #apro fattura
        self.wait_loader()

        #attività
        self.find(By.XPATH, '//ul[@class="dropdown-menu dropdown-menu-right show"]//a[3]').click()
        sleep(2)

        self.find(By.XPATH, '//span[@id="select2-idintervento-container"]').click()
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-idintervento-results"]//li[3]').click()  #seleziona attività creata prima
        self.find(By.XPATH, '//button[@class="btn btn-primary pull-right"]').click()    #click su aggiungi
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//tbody[@id="righe"]//tr[2]//td[4]//input'))).send_keys("2", Keys.ENTER) #imposta quantità a 2
        sleep(3)

        qta_element = self.find(By.XPATH, '//tbody[@id="righe"]//tr[2]//td[4]//input')    #controllo se la quantità è cambiata a 1 e non a 2
        qta = qta_element.get_attribute("value")
        self.assertEqual(qta, "1") 
        self.find(By.XPATH, '//input[@id="check_all"]').click() #elimino righe
        self.find(By.XPATH, '//button[@id="elimina_righe"]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-primary"]').click()
        sleep(2)

        #preventivi
        self.find(By.XPATH, '//button[@class="btn btn-primary dropdown-toggle"]').click() #click su altro
        self.find(By.XPATH, '//ul[@class="dropdown-menu dropdown-menu-right show"]//a[4]').click()
        sleep(2)

        self.find(By.XPATH, '//span[@id="select2-id_documento-container"]').click()
        sleep(2)

        self.find(By.XPATH, '//ul[@id="select2-id_documento-results"]//li[2]').click()
        sleep(2)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//tbody[@id="righe_documento_importato"]//tr[1]//td[4]//input'))).send_keys("2", Keys.ENTER)
        sleep(3)

        qta_element = self.find(By.XPATH, '//tbody[@id="righe"]//tr[1]//td[4]//input')    #controllo se la quantità è cambiata a 1 e non a 2
        qta = qta_element.get_attribute("value")
        self.assertEqual(qta, "1")
        self.find(By.XPATH, '//input[@id="check_all"]').click() #elimino righe
        self.find(By.XPATH, '//button[@id="elimina_righe"]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-primary"]').click()
        sleep(2)
        #contratti
        self.find(By.XPATH, '//button[@class="btn btn-primary dropdown-toggle"]').click() #click su altro
        self.find(By.XPATH, '//ul[@class="dropdown-menu dropdown-menu-right show"]//a[5]').click()
        sleep(2)

        self.find(By.XPATH, '//span[@id="select2-id_documento-container"]').click()
        sleep(2)

        self.find(By.XPATH, '//ul[@id="select2-id_documento-results"]//li[3]').click()
        sleep(2)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//tbody[@id="righe_documento_importato"]//tr[1]//td[4]//input'))).send_keys("2", Keys.ENTER)
        sleep(3)

        qta_element = self.find(By.XPATH, '//tbody[@id="righe"]//tr[1]//td[4]//input')    #controllo se la quantità è cambiata a 1 e non a 2
        qta = qta_element.get_attribute("value")
        self.assertEqual(qta, "1")
        self.find(By.XPATH, '//input[@id="check_all"]').click() #elimino righe
        self.find(By.XPATH, '//button[@id="elimina_righe"]').click()
        sleep(1)
        #ddt
        self.find(By.XPATH, '//button[@class="btn btn-primary dropdown-toggle"]').click() #click su altro
        self.find(By.XPATH, '//ul[@class="dropdown-menu dropdown-menu-right show"]//a[6]').click()
        sleep(2)

        self.find(By.XPATH, '//span[@id="select2-id_documento-container"]').click()
        sleep(2)

        self.find(By.XPATH, '//ul[@id="select2-id_documento-results"]//li[1]').click()
        sleep(2)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//tbody[@id="righe_documento_importato"]//tr[1]//td[4]//input'))).send_keys("2", Keys.ENTER)
        sleep(3)

        qta_element = self.find(By.XPATH, '//tbody[@id="righe"]//tr[1]//td[4]//input')    #controllo se la quantità è cambiata a 1 e non a 2
        qta = qta_element.get_attribute("value")
        self.assertEqual(qta, "1")
        self.find(By.XPATH, '//input[@id="check_all"]').click() #elimino righe
        self.find(By.XPATH, '//button[@id="elimina_righe"]').click()
        sleep(1)
        #ordine
        self.find(By.XPATH, '//button[@class="btn btn-primary dropdown-toggle"]').click() #click su altro
        self.find(By.XPATH, '//ul[@class="dropdown-menu dropdown-menu-right show"]//a[7]').click()
        sleep(2)

        self.find(By.XPATH, '//span[@id="select2-id_documento-container"]').click()
        sleep(2)

        self.find(By.XPATH, '//ul[@id="select2-id_documento-results"]//li[1]').click()
        sleep(2)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//tbody[@id="righe_documento_importato"]//tr[1]//td[4]//input'))).send_keys("2", Keys.ENTER)
        sleep(3)

        qta_element = self.find(By.XPATH, '//tbody[@id="righe"]//tr[1]//td[4]//input')    #controllo se la quantità è cambiata a 1 e non a 2
        qta = qta_element.get_attribute("value")
        self.assertEqual(qta, "1")
        self.find(By.XPATH, '//input[@id="check_all"]').click() #elimino righe
        self.find(By.XPATH, '//button[@id="elimina_righe"]').click()
        sleep(1)

        self.find(By.XPATH, '//a[@id="elimina"]').click() #elimina fattura
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()
        #elimino attività
        self.navigateTo("Attività")
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr[1]//td[2]').click()
        self.wait_loader()

        self.find(By.XPATH, '//a[@class="btn btn-danger ask"]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()
        #elimino preventivo
        self.expandSidebar("Vendite")
        self.navigateTo("Preventivi")
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr[1]//td[2]').click()
        self.wait_loader()

        self.find(By.XPATH, '//a[@class="btn btn-danger ask"]').click()
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()
        #elimina contratto
        self.navigateTo("Contratti")
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr[4]//td[2]').click() #apre contratto
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_0"]//a[@class="btn btn-danger ask"]'))).click()  #elimino contratto 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))).click()
        self.wait_loader()
        #elimina ddt
        self.expandSidebar("Magazzino") 
        self.navigateTo("Ddt in uscita")
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr[1]//td[2]').click()
        self.wait_loader()

        self.find(By.XPATH, '//a[@class="btn btn-danger ask"]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()
        #elimina ordini
        self.expandSidebar("Vendite")
        self.navigateTo("Ordini cliente")
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr[1]//td[2]').click() 
        self.wait_loader()

        self.find(By.XPATH, '//a[@class="btn btn-danger ask"]').click()
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()

    def aggiungi_riferimento_documenti(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Impostazioni") #primo caso (no,no)
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-11"]').click() #apro Generali
        sleep(1)

        self.find(By.XPATH, '(//label[@class="btn btn-default active"])[10]').click()   #disattiva impostazione
        self.find(By.XPATH, '(//label[@class="btn btn-default active"])[11]').click() #disattiva seconda impostazione da riattivare alla fine
        sleep(2)

        #creo ddt
        self.expandSidebar("Magazzino")
        self.navigateTo("Ddt in uscita")
        self.wait_loader()

        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click() #click su +
        sleep(1)
        #seleziono destinatario
        self.find(By.XPATH, '//span[@id="select2-idanagrafica_add-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente")
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(Keys.ENTER)
        #seleziono causale trasporto
        self.find(By.XPATH, '//span[@id="select2-idcausalet-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Conto lavorazione")
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(Keys.ENTER)
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click() #click su aggiungi
        self.wait_loader()

        #aggiungi articolo
        self.find(By.XPATH, '//span[@id="select2-id_articolo-container"]').click()
        sleep(1)

        self.find(By.XPATH, '//ul[@class="select2-results__options select2-results__options--nested"]//li[1]').click()
        self.find(By.XPATH, '//button[@class="btn btn-primary tip tooltipstered"]').click() #click su aggiungi
        sleep(2)

        self.find(By.XPATH, '//span[@id="select2-idstatoddt-container"]').click() #cambio stato in evaso
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Evaso", Keys.ENTER)
        self.find(By.XPATH, '//button[@id="save"]').click()
        self.wait_loader()
        #crea fattura
        self.find(By.XPATH, '//button[@class="btn btn-info bound clickable"]').click()
        sleep(2)

        self.find(By.XPATH, '//button[@id="submit_btn"]').click()   #click su aggiungi
        self.wait_loader()

        riferimento=self.find(By.XPATH, '(//tbody[@id="righe"]//tr[1]//td[3]//a)[2]').text  #controllo se è presente il riferimento
        self.assertEqual(riferimento, "001 - Articolo 1")
        #elimina riga
        self.find(By.XPATH, '//a[@class="btn btn-xs btn-danger"]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-primary"]').click()
        sleep(3)
        #rimetto stato in evaso del ddt
        self.expandSidebar("Magazzino")
        self.navigateTo("Ddt in uscita")
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr[1]//td[2]').click()    #apri ddt
        self.wait_loader()

        self.find(By.XPATH, '//span[@id="select2-idstatoddt-container"]').click() #cambio stato in evaso
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Evaso", Keys.ENTER)
        self.find(By.XPATH, '//button[@id="save"]').click()
        self.wait_loader()

        self.navigateTo("Impianti")
        self.wait_loader()

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni") #secondo caso (si,no)
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-11"]').click() #apro Generali
        sleep(1)

        self.find(By.XPATH, '(//label[@class="btn btn-default active"])[10]').click()   #attiva impostazione
        sleep(2)

        self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr[1]//td[2]').click()    #apri fattura
        self.wait_loader()

        self.find(By.XPATH, '//button[@class="btn btn-primary dropdown-toggle"]').click() #click su altro
        self.find(By.XPATH, '//ul[@class="dropdown-menu dropdown-menu-right show"]//a[6]').click()
        sleep(2)

        self.find(By.XPATH, '//span[@id="select2-id_documento-container"]').click()
        sleep(2)

        self.find(By.XPATH, '//ul[@id="select2-id_documento-results"]//li[1]').click()
        sleep(2)

        self.find(By.XPATH, '//button[@id="submit_btn"]').click()   #click su aggiungi
        self.wait_loader()

        riferimento=self.find(By.XPATH, '(//tbody[@id="righe"]//tr[1]//td[3]//a)[2]').text  #controllo se è presente il riferimento
        self.assertEqual(riferimento[17:43], "Rif. ddt in uscita num. 02")
        self.find(By.XPATH, '//a[@id="elimina"]').click() #elimina fattura
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()

        #elimino ddt
        self.expandSidebar("Magazzino")
        self.navigateTo("Ddt in uscita")
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr[1]//td[2]').click()    #apro primo ddt
        self.wait_loader()

        self.find(By.XPATH, '//a[@class="btn btn-danger ask"]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()

        self.navigateTo("Impianti")
        self.wait_loader()

        #torno alle impostazioni di prima
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-11"]').click() #apro Generali
        sleep(1)
        
        self.find(By.XPATH, '(//label[@class="btn btn-default active"])[11]').click() #attiva seconda impostazione
        sleep(2)


    def aggiungi_riferimenti_tutti_documenti(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Impostazioni") #prima con opzione (no,si)
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-11"]').click() #apro Generali  
        sleep(1)

        self.find(By.XPATH, '(//label[@class="btn btn-default active"])[10]').click() #disattiva prima impostazione
        sleep(2)

        #creo preventivo
        self.expandSidebar("Vendite")
        self.navigateTo("Preventivi")
        self.wait_loader()

        self.find(By.XPATH, '//button[@class="btn btn-primary bound clickable"]').click()   #click su +
        sleep(1)
        #nome
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="nome"]'))).send_keys('Test')
        #cliente
        self.find(By.XPATH, '//span[@id="select2-idanagrafica-container"]').click()
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-idanagrafica-results"]//li[2]').click()
        #tipo di attività
        self.find(By.XPATH, '//span[@id="select2-idtipointervento-container"]').click()
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-idtipointervento-results"]//li[1]').click()
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click()   #click su aggiungi
        self.wait_loader()
        #aggiungi articolo
        self.find(By.XPATH, '//span[@id="select2-id_articolo-container"]').click()
        sleep(1)

        self.find(By.XPATH, '//ul[@class="select2-results__options select2-results__options--nested"]//li[1]').click()
        self.find(By.XPATH, '//button[@class="btn btn-primary tip tooltipstered"]').click() #click su aggiungi
        sleep(2)

        self.driver.execute_script('window.scrollTo(0,0)')
        sleep(1)

        #cambio stato
        self.find(By.XPATH, '//span[@id="select2-idstato-container"]').click()
        sleep(2)

        self.find(By.XPATH, '//ul[@id="select2-idstato-results"]//li[1]').click() #imposto stato "Accettato"
        self.find(By.XPATH, '//button[@id="save"]').click() #click su salva
        self.wait_loader()

        self.find(By.XPATH, '//button[@class="btn btn-info dropdown-toggle "]').click() #click su crea
        sleep(1)

        self.find(By.XPATH, '//div[@class="dropdown-menu dropdown-menu-right show"]//a[5]').click()
        sleep(2)
        #ddt
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-id_causale_trasporto-container"]'))).click()
        sleep(2)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//li[@class="select2-results__option select2-results__option--highlighted"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-id_segment-container"]'))).click()
        sleep(2)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//li[@class="select2-results__option select2-results__option--highlighted"]'))).click()
        self.find(By.XPATH, '//button[@id="submit_btn"]').click()
        self.wait_loader()

        self.find(By.XPATH, '//span[@id="select2-idstatoddt-container"]').click()   #cambio stato
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-idstatoddt-results"]//li[2]').click()    #imposta stato "Evaso"
        self.find(By.XPATH, '//button[@id="save"]').click() #click su salva
        self.wait_loader()

        self.find(By.XPATH, '//button[@class="btn btn-info bound clickable"]').click()  #crea fattura
        sleep(1)

        self.find(By.XPATH, '//button[@id="submit_btn"]').click()   #click su aggiungi
        self.wait_loader()

        riferimento1=self.find(By.XPATH, '(//tbody[@id="righe"]//tr[1]//td[3]//a)[2]').text
        self.assertEqual(riferimento1[17:39], "Rif. preventivo num. 2")
        riferimento2=self.find(By.XPATH, '(//tbody[@id="righe"]//tr[1]//td[3]//a)[2]').text
        self.assertEqual(riferimento2[55:81], "Rif. ddt in uscita num. 02")
        #elimina fattura
        self.find(By.XPATH, '//a[@id="elimina"]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()   #click di conferma
        self.wait_loader()
        #elimino ddt
        self.expandSidebar("Magazzino")
        self.navigateTo("Ddt in entrata")
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr[1]//td[2]').click()
        self.wait_loader()

        self.find(By.XPATH, '//a[@class="btn btn-danger ask"]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()
        #elimino preventivo
        self.expandSidebar("Vendite")
        self.navigateTo("Preventivi")
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr[1]//td[2]').click()
        self.wait_loader()

        self.find(By.XPATH, '//a[@class="btn btn-danger ask"]').click()
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()
        self.navigateTo("Impianti")
        self.wait_loader()

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni") #test con opzioni messe a (si,si)
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-11"]').click() #apro Generali
        sleep(1)

        self.find(By.XPATH, '(//label[@class="btn btn-default active"])[10]').click() #attiva prima impostazione
        sleep(2)

        #creo preventivo
        self.expandSidebar("Vendite")
        self.navigateTo("Preventivi")
        self.wait_loader()

        self.find(By.XPATH, '//button[@class="btn btn-primary bound clickable"]').click()   #click su +
        sleep(1)
        #nome
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="nome"]'))).send_keys('Test')
        #cliente
        self.find(By.XPATH, '//span[@id="select2-idanagrafica-container"]').click()
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-idanagrafica-results"]//li[2]').click()
        #tipo di attività
        self.find(By.XPATH, '//span[@id="select2-idtipointervento-container"]').click()
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-idtipointervento-results"]//li[1]').click()
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click()   #click su aggiungi
        self.wait_loader()
        #aggiungi articolo
        self.find(By.XPATH, '//span[@id="select2-id_articolo-container"]').click()
        sleep(1)

        self.find(By.XPATH, '//ul[@class="select2-results__options select2-results__options--nested"]//li[1]').click()
        self.find(By.XPATH, '//button[@class="btn btn-primary tip tooltipstered"]').click() #click su aggiungi
        sleep(2)

        self.driver.execute_script('window.scrollTo(0,0)')
        sleep(1)

        #cambio stato
        self.find(By.XPATH, '//span[@id="select2-idstato-container"]').click()
        sleep(2)

        self.find(By.XPATH, '//ul[@id="select2-idstato-results"]//li[1]').click() #imposto stato "Accettato"
        self.find(By.XPATH, '//button[@id="save"]').click() #click su salva
        self.wait_loader()

        self.find(By.XPATH, '//button[@class="btn btn-info dropdown-toggle "]').click() #click su crea
        sleep(1)

        self.find(By.XPATH, '//div[@class="dropdown-menu dropdown-menu-right show"]//a[5]').click()
        sleep(2)
        #ddt
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-id_causale_trasporto-container"]'))).click()
        sleep(2)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//li[@class="select2-results__option select2-results__option--highlighted"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-id_segment-container"]'))).click()
        sleep(2)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//li[@class="select2-results__option select2-results__option--highlighted"]'))).click()
        self.find(By.XPATH, '//button[@id="submit_btn"]').click()
        self.wait_loader()

        self.find(By.XPATH, '//span[@id="select2-idstatoddt-container"]').click()   #cambio stato
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-idstatoddt-results"]//li[2]').click()    #imposta stato "Evaso"
        self.find(By.XPATH, '//button[@id="save"]').click() #click su salva
        self.wait_loader()

        self.find(By.XPATH, '//button[@class="btn btn-info bound clickable"]').click()  #crea fattura
        sleep(1)

        self.find(By.XPATH, '//button[@id="submit_btn"]').click()   #click su aggiungi
        self.wait_loader()

        riferimento1=self.find(By.XPATH, '(//tbody[@id="righe"]//tr[1]//td[3]//a)[2]').text
        self.assertEqual(riferimento1[17:39], "Rif. preventivo num. 2")
        riferimento2=self.find(By.XPATH, '(//tbody[@id="righe"]//tr[1]//td[3]//a)[2]').text
        self.assertEqual(riferimento2[55:81], "Rif. ddt in uscita num. 02")
        #elimina fattura
        self.find(By.XPATH, '//a[@id="elimina"]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()   #click di conferma
        self.wait_loader()
        #elimino ddt
        self.expandSidebar("Magazzino")
        self.navigateTo("Ddt in entrata")
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr[1]//td[2]').click()
        self.wait_loader()

        self.find(By.XPATH, '//a[@class="btn btn-danger ask"]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()
        #elimino preventivo
        self.expandSidebar("Vendite")
        self.navigateTo("Preventivi")
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr[1]//td[2]').click()
        self.wait_loader()

        self.find(By.XPATH, '//a[@class="btn btn-danger ask"]').click()
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()

    def aggiungi_note_documenti(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-11"]').click() #apro Generali
        sleep(1)

        self.find(By.XPATH, '(//label[@class="btn btn-default active"])[12]').click()   #attiva impostazione
        sleep(2)

        self.expandSidebar("Vendite")
        self.navigateTo("Preventivi")
        self.wait_loader()

        self.find(By.XPATH, '//button[@class="btn btn-primary bound clickable"]').click()   #crea preventivo
        sleep(1)
        #nome
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="nome"]'))).send_keys('Test')
        #cliente
        self.find(By.XPATH, '//span[@id="select2-idanagrafica-container"]').click()
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-idanagrafica-results"]//li[2]').click()
        #tipo di attività
        self.find(By.XPATH, '//span[@id="select2-idtipointervento-container"]').click()
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-idtipointervento-results"]//li[1]').click()
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click()   #click su aggiungi
        self.wait_loader()

        self.find(By.XPATH, '(//a[@class="btn btn-primary"])[1]').click()
        sleep(2)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("Test") #scrivo "Test" come descrizione riga
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("1") #scrivo 1 come prezzo unitario
        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("Nota di prova")   #aggiungo note
        self.find(By.XPATH, '//button[@class="btn btn-primary pull-right"]').click()    #click su aggiungi
        sleep(2)

        #cambio stato
        self.find(By.XPATH, '//span[@id="select2-idstato-container"]').click()
        sleep(2)

        self.find(By.XPATH, '//ul[@id="select2-idstato-results"]//li[1]').click() #imposto stato "Accettato"
        self.find(By.XPATH, '//button[@id="save"]').click() #click su salva
        self.wait_loader()

        self.find(By.XPATH, '//button[@class="btn btn-info dropdown-toggle "]').click() #click su crea
        self.find(By.XPATH, '//div[@class="dropdown-menu dropdown-menu-right show"]//a[6]').click() #crea fattura
        sleep(2)

        self.find(By.XPATH, '//button[@id="submit_btn"]').click()
        self.wait_loader()

        nota=self.find(By.XPATH, '//tbody[@id="righe"]//td[3]//span').text  #controllo se ha aggiunto la nota dal preventivo
        self.assertEqual(nota, "Nota di prova")
        #elimina fattura
        self.find(By.XPATH, '//a[@id="elimina"]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()   #click di conferma
        self.wait_loader()
        #elimino preventivo
        self.navigateTo("Preventivi")
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr[1]//td[2]').click()
        self.wait_loader()

        self.find(By.XPATH, '//a[@class="btn btn-danger ask"]').click()
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()

        self.expandSidebar("Vendite")
        #torno alle impostazioni di prima
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-11"]').click() #apro Generali
        sleep(1) 

        self.find(By.XPATH, '(//label[@class="btn btn-default active"])[12]').click()   #disattiva impostazione
        sleep(2)

        self.expandSidebar("Vendite")
        self.navigateTo("Preventivi")
        self.wait_loader()

        self.find(By.XPATH, '//button[@class="btn btn-primary bound clickable"]').click()   #crea preventivo
        sleep(1)
        #nome
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="nome"]'))).send_keys('Test')
        #cliente
        self.find(By.XPATH, '//span[@id="select2-idanagrafica-container"]').click()
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-idanagrafica-results"]//li[2]').click()
        #tipo di attività
        self.find(By.XPATH, '//span[@id="select2-idtipointervento-container"]').click()
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-idtipointervento-results"]//li[1]').click()
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click()   #click su aggiungi
        self.wait_loader()

        self.find(By.XPATH, '(//a[@class="btn btn-primary"])[1]').click()
        sleep(2)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("Test") #scrivo "Test" come descrizione riga
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("1") #scrivo 1 come prezzo unitario
        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("Nota di prova")   #aggiungo note
        self.find(By.XPATH, '//button[@class="btn btn-primary pull-right"]').click()    #click su aggiungi
        sleep(2)

        #cambio stato
        self.find(By.XPATH, '//span[@id="select2-idstato-container"]').click()
        sleep(2)

        self.find(By.XPATH, '//ul[@id="select2-idstato-results"]//li[1]').click() #imposto stato "Accettato"
        self.find(By.XPATH, '//button[@id="save"]').click() #click su salva
        self.wait_loader()

        self.find(By.XPATH, '//button[@class="btn btn-info dropdown-toggle "]').click() #click su crea
        self.find(By.XPATH, '//div[@class="dropdown-menu dropdown-menu-right show"]//a[6]').click() #crea fattura
        sleep(2)

        self.find(By.XPATH, '//button[@id="submit_btn"]').click()
        self.wait_loader()

        wait.until(EC.invisibility_of_element_located((By.XPATH, '//tbody[@id="righe"]//td[3]//span')))   #controllo se non ha aggiunto la nota dal preventivo
        
        #elimina fattura
        self.find(By.XPATH, '//a[@id="elimina"]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()   #click di conferma
        self.wait_loader()
        #elimino preventivo
        self.navigateTo("Preventivi")
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr[1]//td[2]').click()
        self.wait_loader()

        self.find(By.XPATH, '//a[@class="btn btn-danger ask"]').click()
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()

    def dimensione_widget_predefinita(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-11"]').click() #apro Generali
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-setting166-container"]').click()
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-setting166-results"]//li[1]').click()    #metto dimensione col-md-1
        sleep(2)

        self.navigateTo("Dashboard")
        self.wait_loader()

        dimensione_element = self.find(By.XPATH, '(//div[@id="widget-top"]//div)[1]')    #controllo se la dimensione è cambiata
        dimensione = dimensione_element.get_attribute("class")
        self.assertEqual(dimensione[9:17], "col-md-1")
        self.navigateTo("Impianti")
        self.wait_loader()

        #torno alle impostazioni di prima
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-11"]').click() #apro Generali
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-setting166-container"]').click()
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-setting166-results"]//li[3]').click()    #metto dimensione col-md-3
        sleep(2)

        self.navigateTo("Dashboard")
        self.wait_loader()

        dimensione_element = self.find(By.XPATH, '(//div[@id="widget-top"]//div)[1]')    #controllo se la dimensione è cambiata
        dimensione = dimensione_element.get_attribute("class")
        self.assertEqual(dimensione[9:17], "col-md-3")


    def tipo_sconto_predefinito(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-11"]').click() #apro Generali
        sleep(1)

        self.find(By.XPATH,'//span[@id="select2-setting189-container"]').click()
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-setting189-results"]//li[2]').click()    #sconto predefinito in eur
        sleep(2)

        self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.find(By.XPATH, '//button[@class="btn btn-primary bound clickable"]').click()   #click su +
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-idanagrafica_add-container"]').click() #seleziono Cliente come anagrafica
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente", Keys.ENTER)
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click() #click su aggiungi
        self.wait_loader()
        #aggiungo articolo
        self.find(By.XPATH, '//span[@id="select2-id_articolo-container"]').click()
        sleep(1)

        self.find(By.XPATH, '//ul[@class="select2-results__options select2-results__options--nested"]//li[1]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@class="btn btn-primary tip tooltipstered"]').click()
        sleep(2)

        sconto_element = self.find(By.XPATH, '//tbody[@id="righe"]//span[@class="select2-selection select2-selection--single"]//span[1]')    #check valore dello sconto
        sconto = sconto_element.get_attribute("title")
        self.assertEqual(sconto, "€")
        #torno alle impostazioni di prima
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-11"]').click() #apro Generali
        sleep(1)

        self.find(By.XPATH,'//span[@id="select2-setting189-container"]').click()
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-setting189-results"]//li[1]').click()    #sconto predefinito in percentuale
        sleep(2)

        self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr[1]//td[2]').click()
        self.wait_loader()

        sconto_element = self.find(By.XPATH, '//tbody[@id="righe"]//span[@class="select2-selection select2-selection--single"]//span[1]')    #check valore dello sconto
        sconto = sconto_element.get_attribute("title")
        self.assertEqual(sconto, "%")
        #elimina fattura
        self.find(By.XPATH, '//a[@id="elimina"]').click()
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()


    def importi_stampa(self):
        wait = WebDriverWait(self.driver, 20)
        self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")
        self.wait_loader()
        sleep(1)

        self.find(By.XPATH, '//button[@class="btn btn-primary bound clickable"]').click()   #click su +
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-idanagrafica_add-container"]').click() #seleziono Cliente come anagrafica
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente", Keys.ENTER)
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click() #click su aggiungi
        self.wait_loader()
        # riga 1
        self.find(By.XPATH, '//a[@class="btn btn-primary"]').click() #click su aggiungi riga
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("1")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("26,10")
        self.find(By.XPATH, '//button[@class="btn btn-primary pull-right"]').click() #click su aggiungi
        sleep(1)
        #riga 2
        self.find(By.XPATH, '//a[@class="btn btn-primary"]').click() #click su aggiungi riga
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("2")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("8,34")
        self.find(By.XPATH, '//button[@class="btn btn-primary pull-right"]').click() #click su aggiungi
        sleep(1)
        #riga 3
        self.find(By.XPATH, '//a[@class="btn btn-primary"]').click() #click su aggiungi riga
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("3")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("8,35")
        self.find(By.XPATH, '//button[@class="btn btn-primary pull-right"]').click() #click su aggiungi
        sleep(1)
        #riga 4
        self.find(By.XPATH, '//a[@class="btn btn-primary"]').click() #click su aggiungi riga
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("4")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("8,34")
        self.find(By.XPATH, '//button[@class="btn btn-primary pull-right"]').click() #click su aggiungi
        sleep(1)
        #riga 5
        self.find(By.XPATH, '//a[@class="btn btn-primary"]').click() #click su aggiungi riga
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("5")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("8,35")
        self.find(By.XPATH, '//button[@class="btn btn-primary pull-right"]').click() #click su aggiungi
        sleep(1)
        #riga 6
        self.find(By.XPATH, '//a[@class="btn btn-primary"]').click() #click su aggiungi riga
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("6")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("16,60")
        self.find(By.XPATH, '//button[@class="btn btn-primary pull-right"]').click() #click su aggiungi
        sleep(1)
        #riga 7
        self.find(By.XPATH, '//a[@class="btn btn-primary"]').click() #click su aggiungi riga
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("7")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("28,81")
        self.find(By.XPATH, '//button[@class="btn btn-primary pull-right"]').click() #click su aggiungi
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-idstatodocumento-container"]').click() #cambio stato in "Emessa"
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Emessa", Keys.ENTER)
        self.find(By.XPATH, '//button[@id="save"]').click()
        self.wait_loader()

        self.find(By.XPATH, '//a[@id="print-button_p"]').click()
        sleep(2)

        self.driver.switch_to.window(self.driver.window_handles[1]) #cambia scheda
        sleep(2)

        importo1=self.find(By.XPATH, '//span[@style="left: 66.18%; top: 27.96%; font-size: calc(var(--scale-factor)*7.82px); font-family: sans-serif; transform: scaleX(0.901707);"]').text
        self.assertEqual(importo1, "26,10 €")
        importo2=self.find(By.XPATH, '//span[@style="left: 81.57%; top: 27.96%; font-size: calc(var(--scale-factor)*7.82px); font-family: sans-serif; transform: scaleX(0.901707);"]').text
        self.assertEqual(importo2, "26,10 €")

        self.driver.close() #chiude scheda
        self.driver.switch_to.window(self.driver.window_handles[0]) #torna alla prima
        sleep(2)

        self.find(By.XPATH, '//a[@id="elimina"]').click() #elimina fattura
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-11"]').click() #apro Generali
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-setting193-container"]').click()    #seleziono 4 cifre decimali per gli importi
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys('4', Keys.ENTER)
        sleep(1)

        self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")
        self.wait_loader()
        sleep(1)

        self.find(By.XPATH, '//button[@class="btn btn-primary bound clickable"]').click()   #click su +
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-idanagrafica_add-container"]').click() #seleziono Cliente come anagrafica
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente", Keys.ENTER)
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click() #click su aggiungi
        self.wait_loader()
        # riga 1
        self.find(By.XPATH, '//a[@class="btn btn-primary"]').click() #click su aggiungi riga
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("1")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("26,10")
        self.find(By.XPATH, '//button[@class="btn btn-primary pull-right"]').click() #click su aggiungi
        sleep(1)
        #riga 2
        self.find(By.XPATH, '//a[@class="btn btn-primary"]').click() #click su aggiungi riga
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("2")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("8,34")
        self.find(By.XPATH, '//button[@class="btn btn-primary pull-right"]').click() #click su aggiungi
        sleep(1)
        #riga 3
        self.find(By.XPATH, '//a[@class="btn btn-primary"]').click() #click su aggiungi riga
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("3")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("8,35")
        self.find(By.XPATH, '//button[@class="btn btn-primary pull-right"]').click() #click su aggiungi
        sleep(1)
        #riga 4
        self.find(By.XPATH, '//a[@class="btn btn-primary"]').click() #click su aggiungi riga
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("4")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("8,34")
        self.find(By.XPATH, '//button[@class="btn btn-primary pull-right"]').click() #click su aggiungi
        sleep(1)
        #riga 5
        self.find(By.XPATH, '//a[@class="btn btn-primary"]').click() #click su aggiungi riga
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("5")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("8,35")
        self.find(By.XPATH, '//button[@class="btn btn-primary pull-right"]').click() #click su aggiungi
        sleep(1)
        #riga 6
        self.find(By.XPATH, '//a[@class="btn btn-primary"]').click() #click su aggiungi riga
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("6")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("16,60")
        self.find(By.XPATH, '//button[@class="btn btn-primary pull-right"]').click() #click su aggiungi
        sleep(1)
        #riga 7
        self.find(By.XPATH, '//a[@class="btn btn-primary"]').click() #click su aggiungi riga
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("7")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("28,81")
        self.find(By.XPATH, '//button[@class="btn btn-primary pull-right"]').click() #click su aggiungi
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-idstatodocumento-container"]').click() #cambio stato in "Emessa"
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Emessa", Keys.ENTER)
        self.find(By.XPATH, '//button[@id="save"]').click()
        self.wait_loader()

        self.find(By.XPATH, '//a[@id="print-button_p"]').click()
        sleep(2)

        self.driver.switch_to.window(self.driver.window_handles[1]) #cambia scheda
        sleep(2)

        importo1=self.find(By.XPATH, '//span[@style="left: 64.67%; top: 27.96%; font-size: calc(var(--scale-factor)*7.82px); font-family: sans-serif; transform: scaleX(0.901707);"]').text
        self.assertEqual(importo1, "26,1000 €")
        importo2=self.find(By.XPATH, '//span[@style="left: 80.07%; top: 27.96%; font-size: calc(var(--scale-factor)*7.82px); font-family: sans-serif; transform: scaleX(0.901707);"]').text
        self.assertEqual(importo2, "26,1000 €")

        self.driver.close() #chiude scheda
        self.driver.switch_to.window(self.driver.window_handles[0]) #torna alla prima
        sleep(2)

        self.find(By.XPATH, '//a[@id="elimina"]').click() #elimina fattura
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-11"]').click() #apro Generali
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-setting193-container"]').click()    #seleziono 2 cifre decimali per gli importi
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys('2', Keys.ENTER)
        sleep(1)

    def quantita_stampa(self):
        wait = WebDriverWait(self.driver, 20)
        self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")
        self.wait_loader()
        sleep(1)

        self.find(By.XPATH, '//button[@class="btn btn-primary bound clickable"]').click()   #click su +
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-idanagrafica_add-container"]').click() #seleziono Cliente come anagrafica
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente", Keys.ENTER)
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click() #click su aggiungi
        self.wait_loader()
        # riga 1
        self.find(By.XPATH, '//a[@class="btn btn-primary"]').click() #click su aggiungi riga
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("1")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("26,10")
        self.find(By.XPATH, '//button[@class="btn btn-primary pull-right"]').click() #click su aggiungi
        sleep(1)
        #riga 2
        self.find(By.XPATH, '//a[@class="btn btn-primary"]').click() #click su aggiungi riga
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("2")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("8,34")
        self.find(By.XPATH, '//button[@class="btn btn-primary pull-right"]').click() #click su aggiungi
        sleep(1)
        #riga 3
        self.find(By.XPATH, '//a[@class="btn btn-primary"]').click() #click su aggiungi riga
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("3")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("8,35")
        self.find(By.XPATH, '//button[@class="btn btn-primary pull-right"]').click() #click su aggiungi
        sleep(1)
        #riga 4
        self.find(By.XPATH, '//a[@class="btn btn-primary"]').click() #click su aggiungi riga
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("4")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("8,34")
        self.find(By.XPATH, '//button[@class="btn btn-primary pull-right"]').click() #click su aggiungi
        sleep(1)
        #riga 5
        self.find(By.XPATH, '//a[@class="btn btn-primary"]').click() #click su aggiungi riga
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("5")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("8,35")
        self.find(By.XPATH, '//button[@class="btn btn-primary pull-right"]').click() #click su aggiungi
        sleep(1)
        #riga 6
        self.find(By.XPATH, '//a[@class="btn btn-primary"]').click() #click su aggiungi riga
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("6")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("16,60")
        self.find(By.XPATH, '//button[@class="btn btn-primary pull-right"]').click() #click su aggiungi
        sleep(1)
        #riga 7
        self.find(By.XPATH, '//a[@class="btn btn-primary"]').click() #click su aggiungi riga
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("7")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("28,81")
        self.find(By.XPATH, '//button[@class="btn btn-primary pull-right"]').click() #click su aggiungi
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-idstatodocumento-container"]').click() #cambio stato in "Emessa"
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Emessa", Keys.ENTER)
        self.find(By.XPATH, '//button[@id="save"]').click()
        self.wait_loader()

        self.find(By.XPATH, '//a[@id="print-button_p"]').click()
        sleep(2)

        self.driver.switch_to.window(self.driver.window_handles[1]) #cambia scheda
        sleep(2)

        quantita=self.find(By.XPATH, '//span[@style="left: 52.11%; top: 27.96%; font-size: calc(var(--scale-factor)*7.82px); font-family: sans-serif; transform: scaleX(0.901707);"]').text
        self.assertEqual(quantita, "1,00")
        self.driver.close() #chiude scheda
        self.driver.switch_to.window(self.driver.window_handles[0]) #torna alla prima
        sleep(2)

        self.find(By.XPATH, '//a[@id="elimina"]').click() #elimina fattura
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-11"]').click() #apro Generali
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-setting194-container"]').click()    #seleziono 4 cifre decimali per le quantità
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys('4', Keys.ENTER)
        sleep(1)

        self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")
        self.wait_loader()
        sleep(1)

        self.find(By.XPATH, '//button[@class="btn btn-primary bound clickable"]').click()   #click su +
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-idanagrafica_add-container"]').click() #seleziono Cliente come anagrafica
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente", Keys.ENTER)
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click() #click su aggiungi
        self.wait_loader()
        # riga 1
        self.find(By.XPATH, '//a[@class="btn btn-primary"]').click() #click su aggiungi riga
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("1")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("26,10")
        self.find(By.XPATH, '//button[@class="btn btn-primary pull-right"]').click() #click su aggiungi
        sleep(1)
        #riga 2
        self.find(By.XPATH, '//a[@class="btn btn-primary"]').click() #click su aggiungi riga
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("2")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("8,34")
        self.find(By.XPATH, '//button[@class="btn btn-primary pull-right"]').click() #click su aggiungi
        sleep(1)
        #riga 3
        self.find(By.XPATH, '//a[@class="btn btn-primary"]').click() #click su aggiungi riga
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("3")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("8,35")
        self.find(By.XPATH, '//button[@class="btn btn-primary pull-right"]').click() #click su aggiungi
        sleep(1)
        #riga 4
        self.find(By.XPATH, '//a[@class="btn btn-primary"]').click() #click su aggiungi riga
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("4")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("8,34")
        self.find(By.XPATH, '//button[@class="btn btn-primary pull-right"]').click() #click su aggiungi
        sleep(1)
        #riga 5
        self.find(By.XPATH, '//a[@class="btn btn-primary"]').click() #click su aggiungi riga
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("5")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("8,35")
        self.find(By.XPATH, '//button[@class="btn btn-primary pull-right"]').click() #click su aggiungi
        sleep(1)
        #riga 6
        self.find(By.XPATH, '//a[@class="btn btn-primary"]').click() #click su aggiungi riga
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("6")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("16,60")
        self.find(By.XPATH, '//button[@class="btn btn-primary pull-right"]').click() #click su aggiungi
        sleep(1)
        #riga 7
        self.find(By.XPATH, '//a[@class="btn btn-primary"]').click() #click su aggiungi riga
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("7")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("28,81")
        self.find(By.XPATH, '//button[@class="btn btn-primary pull-right"]').click() #click su aggiungi
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-idstatodocumento-container"]').click() #cambio stato in "Emessa"
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Emessa", Keys.ENTER)
        self.find(By.XPATH, '//button[@id="save"]').click()
        self.wait_loader()

        self.find(By.XPATH, '//a[@id="print-button_p"]').click()
        sleep(2)

        self.driver.switch_to.window(self.driver.window_handles[1]) #cambia scheda
        sleep(2)

        quantita=self.find(By.XPATH, '//span[@style="left: 51.36%; top: 27.96%; font-size: calc(var(--scale-factor)*7.82px); font-family: sans-serif; transform: scaleX(0.901707);"]').text
        self.assertEqual(quantita, "1,0000")
        self.driver.close() #chiude scheda
        self.driver.switch_to.window(self.driver.window_handles[0]) #torna alla prima
        sleep(2)

        self.find(By.XPATH, '//a[@id="elimina"]').click() #elimina fattura
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-11"]').click() #apro Generali
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-setting194-container"]').click()    #seleziono 2 cifre decimali per le quantità
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys('2', Keys.ENTER)
        sleep(1)

    def totali_stampa(self):
        wait = WebDriverWait(self.driver, 20)
        self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")
        self.wait_loader()
        sleep(1)

        self.find(By.XPATH, '//button[@class="btn btn-primary bound clickable"]').click()   #click su +
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-idanagrafica_add-container"]').click() #seleziono Cliente come anagrafica
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente", Keys.ENTER)
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click() #click su aggiungi
        self.wait_loader()
        # riga 1
        self.find(By.XPATH, '//a[@class="btn btn-primary"]').click() #click su aggiungi riga
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("1")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("26,10")
        self.find(By.XPATH, '//button[@class="btn btn-primary pull-right"]').click() #click su aggiungi
        sleep(1)
        #riga 2
        self.find(By.XPATH, '//a[@class="btn btn-primary"]').click() #click su aggiungi riga
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("2")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("8,34")
        self.find(By.XPATH, '//button[@class="btn btn-primary pull-right"]').click() #click su aggiungi
        sleep(1)
        #riga 3
        self.find(By.XPATH, '//a[@class="btn btn-primary"]').click() #click su aggiungi riga
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("3")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("8,35")
        self.find(By.XPATH, '//button[@class="btn btn-primary pull-right"]').click() #click su aggiungi
        sleep(1)
        #riga 4
        self.find(By.XPATH, '//a[@class="btn btn-primary"]').click() #click su aggiungi riga
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("4")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("8,34")
        self.find(By.XPATH, '//button[@class="btn btn-primary pull-right"]').click() #click su aggiungi
        sleep(1)
        #riga 5
        self.find(By.XPATH, '//a[@class="btn btn-primary"]').click() #click su aggiungi riga
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("5")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("8,35")
        self.find(By.XPATH, '//button[@class="btn btn-primary pull-right"]').click() #click su aggiungi
        sleep(1)
        #riga 6
        self.find(By.XPATH, '//a[@class="btn btn-primary"]').click() #click su aggiungi riga
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("6")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("16,60")
        self.find(By.XPATH, '//button[@class="btn btn-primary pull-right"]').click() #click su aggiungi
        sleep(1)
        #riga 7
        self.find(By.XPATH, '//a[@class="btn btn-primary"]').click() #click su aggiungi riga
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("7")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("28,81")
        self.find(By.XPATH, '//button[@class="btn btn-primary pull-right"]').click() #click su aggiungi
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-idstatodocumento-container"]').click() #cambio stato in "Emessa"
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Emessa", Keys.ENTER)
        self.find(By.XPATH, '//button[@id="save"]').click()
        self.wait_loader()

        self.find(By.XPATH, '//a[@id="print-button_p"]').click()
        sleep(2)

        self.driver.switch_to.window(self.driver.window_handles[1]) #cambia scheda
        sleep(2)

        totale=self.find(By.XPATH, '//span[@style="left: 76.88%; top: 90.82%; font-size: calc(var(--scale-factor)*8.86px); font-family: sans-serif; transform: scaleX(0.900168);"]').text
        self.assertEqual(totale, "127,97 €")
        self.driver.close() #chiude scheda
        self.driver.switch_to.window(self.driver.window_handles[0]) #torna alla prima
        sleep(2)

        self.find(By.XPATH, '//a[@id="elimina"]').click() #elimina fattura
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-11"]').click() #apro Generali
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-setting195-container"]').click()    #seleziono 1 cifra decimali per le quantità
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys('1', Keys.ENTER)
        sleep(1)

        self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")
        self.wait_loader()
        sleep(1)

        self.find(By.XPATH, '//button[@class="btn btn-primary bound clickable"]').click()   #click su +
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-idanagrafica_add-container"]').click() #seleziono Cliente come anagrafica
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente", Keys.ENTER)
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click() #click su aggiungi
        self.wait_loader()
        # riga 1
        self.find(By.XPATH, '//a[@class="btn btn-primary"]').click() #click su aggiungi riga
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("1")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("26,10")
        self.find(By.XPATH, '//button[@class="btn btn-primary pull-right"]').click() #click su aggiungi
        sleep(1)
        #riga 2
        self.find(By.XPATH, '//a[@class="btn btn-primary"]').click() #click su aggiungi riga
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("2")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("8,34")
        self.find(By.XPATH, '//button[@class="btn btn-primary pull-right"]').click() #click su aggiungi
        sleep(1)
        #riga 3
        self.find(By.XPATH, '//a[@class="btn btn-primary"]').click() #click su aggiungi riga
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("3")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("8,35")
        self.find(By.XPATH, '//button[@class="btn btn-primary pull-right"]').click() #click su aggiungi
        sleep(1)
        #riga 4
        self.find(By.XPATH, '//a[@class="btn btn-primary"]').click() #click su aggiungi riga
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("4")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("8,34")
        self.find(By.XPATH, '//button[@class="btn btn-primary pull-right"]').click() #click su aggiungi
        sleep(1)
        #riga 5
        self.find(By.XPATH, '//a[@class="btn btn-primary"]').click() #click su aggiungi riga
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("5")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("8,35")
        self.find(By.XPATH, '//button[@class="btn btn-primary pull-right"]').click() #click su aggiungi
        sleep(1)
        #riga 6
        self.find(By.XPATH, '//a[@class="btn btn-primary"]').click() #click su aggiungi riga
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("6")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("16,60")
        self.find(By.XPATH, '//button[@class="btn btn-primary pull-right"]').click() #click su aggiungi
        sleep(1)
        #riga 7
        self.find(By.XPATH, '//a[@class="btn btn-primary"]').click() #click su aggiungi riga
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("7")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("28,81")
        self.find(By.XPATH, '//button[@class="btn btn-primary pull-right"]').click() #click su aggiungi
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-idstatodocumento-container"]').click() #cambio stato in "Emessa"
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Emessa", Keys.ENTER)
        self.find(By.XPATH, '//button[@id="save"]').click()
        self.wait_loader()

        self.find(By.XPATH, '//a[@id="print-button_p"]').click()
        sleep(2)

        self.driver.switch_to.window(self.driver.window_handles[1]) #cambia scheda
        sleep(2)

        totale=self.find(By.XPATH, '//span[@style="left: 77.32%; top: 90.82%; font-size: calc(var(--scale-factor)*8.86px); font-family: sans-serif; transform: scaleX(0.900206);"]').text
        self.assertEqual(totale, "128,0 €")
        self.driver.close() #chiude scheda
        self.driver.switch_to.window(self.driver.window_handles[0]) #torna alla prima
        sleep(2)

        self.find(By.XPATH, '//a[@id="elimina"]').click() #elimina fattura
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-11"]').click() #apro Generali
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-setting195-container"]').click()    #seleziono 2 cifre decimali per le quantità
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys('2', Keys.ENTER)
        sleep(1)
        

    def listino_predefinito(self):
        wait = WebDriverWait(self.driver, 20)  
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-11"]').click() #apro Generali
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-setting196-container"]').click()   #seleziona listino di prova
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-setting196-results"]//li').click()
        sleep(2)

        self.navigateTo("Anagrafiche")
        self.wait_loader()

        self.find(By.XPATH, '//button[@class="btn btn-primary bound clickable"]').click()   #click su +
        sleep(2)
        #creo anagrafica
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="ragione_sociale_add"]'))).send_keys('Test')    #nome anagrafica
        self.find(By.XPATH, '//span[@class="select2-selection select2-selection--multiple"]').click()
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-idtipoanagrafica_add-results"]//li[2]').click()  #tipo anagrafica cliente
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click()   #click su aggiungi
        self.wait_loader()

        listino=self.find(By.XPATH, '//span[@id="select2-id_listino-container"]').text  #check se il listino è stato selezionato
        self.assertEqual(listino[2:26], "Listino cliente di Prova")
        #elimino anagrafica
        self.find(By.XPATH, '//a[@class="btn btn-danger ask"]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()

        self.expandSidebar("Strumenti") 
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-11"]').click() #apro Generali
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-setting196-container"]//span').click()
        sleep(2)


    def lingua(self):
        wait = WebDriverWait(self.driver, 20)  
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-11"]').click() #apro Generali
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-setting199-container"]').click()   #metto la lingua in inglese
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys('English')
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(Keys.ENTER)
        self.navigateTo("Anagrafiche")
        self.wait_loader() 

        scritta=self.find(By.XPATH, '(//li[@id="2"]//p)[1]').text   #controllo se ha cambiato lingua
        self.assertEqual(scritta, "Entities")
        #torno alle impostazioni di prima
        self.expandSidebar("Tools")
        self.navigateTo("Settings")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-11"]').click() #apro Generali
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-setting199-container"]').click()   #metto la lingua in italiano
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys('Italiano')
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(Keys.ENTER)
        self.navigateTo("Settings")
        self.wait_loader()
        sleep(2)

