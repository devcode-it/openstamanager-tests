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

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")

    def test_impostazioni_generali(self):
        # Nascondere la barra sinistra di default (2)
        self.nascondi_barra_sx()

        # Cambio cifre decimali per importi (3)
        self.cifre_decimali_importi()

        # Prima pagina (7)
        self.prima_pagina()

        # Cifre decimali per quantità (8)
        self.cifre_decimali_quantita()

        # Cambio valuta (12)
        self.valuta()
        
        # Permetti selezione articoli con quantità minore o uguale a zero in Documenti di Vendita (22)
        self.quantita_minore_uguale_zero()

        # Cambio periodo calendario (23-24)
        self.periodo_calendario()

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
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="form-control"]'))).send_keys('admin')
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="password"]'))).send_keys('adminadmin') #password da mettere prima del test
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
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="form-control"]'))).send_keys('admin')
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="password"]'))).send_keys('adminadmin') #password da mettere prima del test
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
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="form-control"]'))).send_keys('admin')
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
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="form-control"]'))).send_keys('admin')
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="password"]'))).send_keys('') #password da mettere prima del test
        self.find(By.XPATH, '//button[@class="btn btn-danger btn-block btn-flat"]').click() 
        sleep(2)
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

