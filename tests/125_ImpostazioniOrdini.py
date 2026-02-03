from common.Test import Test, get_html
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Impostazioni(Test):
    def setUp(self):
        super().setUp()

    def test_impostazioni_ordini(self):
        return True
        # Cambia automaticamente stato ordini fatturati (1)
        #self.cambia_stato_ordini()

        # Conferma automaticamente le quantità negli ordini cliente (2)
        #self.conferma_quantita_ordini_cliente()

        # Conferma automaticamente le quantità negli ordini fornitore (3)
        #self.conferma_quantita_ordini_fornitore()
        
        ## TODO: Visualizza numero ordine cliente

    def cambia_stato_ordini(self):
                self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="impostazioni-15"]'))
        ).click() #apro Ordini

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//label[@class="btn btn-default active"])[1]'))
        ).click() #disattivo impostazione

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

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_0"]//a[@class="btn btn-primary"]'))
        ).click()  #click su tasto aggiungi riga

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys('Test') #aggiunta descrizione riga
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys('1')   #aggiunta prezzo unitario
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary pull-right"]'))
        ).click()    #click su aggiungi

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idstatoordine-container"]'))).click()   #cambio stato in Accettato
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys('Accettato', Keys.ENTER)
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@id="save"]'))
        ).click() #click su salva
        self.wait_loader()

        self.navigateTo("Ordini cliente")   #torna in pagina principale
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input'))).send_keys('02', Keys.ENTER) #cerco l'ordine 02

        self.wait_for_element_and_click('//tbody//tr//td')  #seleziono l'ordine
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@data-toggle="dropdown"]'))
        ).click() #click su azioni di gruppo
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@data-op="crea_fattura"]'))
        ).click() #click su fattura ordini clienti

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-raggruppamento-container"]'))
        ).click() #ragruppa per cliente

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-raggruppamento-results"]//li[1]'))
        ).click()
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-warning"]'))
        ).click()
        self.wait_loader()

        stato = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//tr[1]//td[7]//span)[2]'))
        ).text
        self.assertEqual(stato, "Accettato")    #check se lo stato non è cambiato
        self.wait_for_element_and_click('//tbody//tr//td[2]')   #elimino ordine
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="btn btn-danger ask"]'))
        ).click()
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/i[@class="deleteicon fa fa-times"]'))
        ).click() #cancello la ricerca

        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.wait_for_element_and_click('//tbody//tr[1]//td[2]') #elimino fattura
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@id="elimina"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click() #click di conferma
        self.wait_loader()
        #torno alle impostazioni di prima
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="impostazioni-15"]'))
        ).click() #apro Ordini

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//label[@class="btn btn-default active"])[1]'))
        ).click() #attivo impostazione

    def conferma_quantita_ordini_cliente(self):
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

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_0"]//a[@class="btn btn-primary"]'))
        ).click()  #click su tasto aggiungi riga

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys('Test') #aggiunta descrizione riga
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys('1')   #aggiunta prezzo unitario
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary pull-right"]'))
        ).click()    #click su aggiungi

        wait.until(EC.visibility_of_element_located((By.XPATH, '(//i[@class="fa fa-check text-success"])[1]'))) #check se la quantita è stata confermata automaticamente
        #elimino ordine
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
            EC.visibility_of_element_located((By.XPATH, '//div[@id="impostazioni-15"]'))
        ).click() #apro Ordini

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//label[@class="btn btn-default active"])[2]'))
        ).click() #disattivo impostazione

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

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_0"]//a[@class="btn btn-primary"]'))
        ).click()  #click su tasto aggiungi riga

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys('Test') #aggiunta descrizione riga
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys('1')   #aggiunta prezzo unitario
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary pull-right"]'))
        ).click()    #click su aggiungi

        wait.until(EC.visibility_of_element_located((By.XPATH, '//i[@class="fa fa-clock-o text-warning"]')))    #check se è stato confermata la quantita
        #elimino ordine
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="btn btn-danger ask"]'))
        ).click()
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()
        self.wait_loader()
        #torno alle impostazioni di prima
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="impostazioni-15"]'))
        ).click() #apro Ordini

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//label[@class="btn btn-default active"])[2]'))
        ).click() #attivo impostazione

    def conferma_quantita_ordini_fornitore(self):
                self.expandSidebar("Acquisti")
        self.navigateTo("Ordini fornitore")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//i[@class="fa fa-plus"]'))
        ).click() #crea ordine fornitore

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idanagrafica-container"]'))
        ).click() #imposta fornitore

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-idanagrafica-results"]//li[1]'))
        ).click()
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary"]'))
        ).click()   #click su aggiungi
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="btn btn-primary"]'))
        ).click()    #aggiungi riga

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys('Test') #aggiunta descrizione riga
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys('1')   #aggiunta prezzo unitario
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary pull-right"]'))
        ).click()    #click su aggiungi
        
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//i[@class="fa fa-check text-success"])[1]')))    #check se è stato confermata la quantita
        #elimino ordine
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
            EC.visibility_of_element_located((By.XPATH, '//div[@id="impostazioni-15"]'))
        ).click() #apro Ordini

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//label[@class="btn btn-default active"])[3]'))
        ).click() #disattivo impostazione

        self.expandSidebar("Acquisti")
        self.navigateTo("Ordini fornitore")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//i[@class="fa fa-plus"]'))
        ).click() #crea ordine fornitore

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idanagrafica-container"]'))
        ).click() #imposta fornitore

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-idanagrafica-results"]//li[1]'))
        ).click()
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary"]'))
        ).click()   #click su aggiungi
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="btn btn-primary"]'))
        ).click()    #aggiungi riga

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys('Test') #aggiunta descrizione riga
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys('1')   #aggiunta prezzo unitario
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary pull-right"]'))
        ).click()    #click su aggiungi
        
        wait.until(EC.visibility_of_element_located((By.XPATH, '//i[@class="fa fa-clock-o text-warning"]')))    #check se è stato confermata la quantita
        #elimino ordine
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="btn btn-danger ask"]'))
        ).click()
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()
        self.wait_loader()

        #torno alle impostazioni di prima
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="impostazioni-15"]'))
        ).click() #apro Ordini

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//label[@class="btn btn-default active"])[3]'))
        ).click() #attivo impostazione