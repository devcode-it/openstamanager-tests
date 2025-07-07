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
        wait = WebDriverWait(self.driver, 20)
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-15"]').click() #apro Ordini
        sleep(1)

        self.find(By.XPATH, '(//label[@class="btn btn-default active"])[1]').click() #disattivo impostazione
        sleep(1)

        self.expandSidebar("Vendite")
        self.navigateTo("Ordini cliente")
        self.wait_loader()

        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click()   #click su tasto +
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-idanagrafica-container"]').click()     #scelta di "Cliente" come anagrafica per l'ordine
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys('Cliente')
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(Keys.ENTER)
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click()   #click su tasto aggiungi
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="tab_0"]//a[@class="btn btn-primary"]').click()  #click su tasto aggiungi riga
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys('Test') #aggiunta descrizione riga
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys('1')   #aggiunta prezzo unitario
        self.find(By.XPATH, '//button[@class="btn btn-primary pull-right"]').click()    #click su aggiungi
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idstatoordine-container"]'))).click()   #cambio stato in Accettato
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys('Accettato', Keys.ENTER)
        self.find(By.XPATH, '//button[@id="save"]').click() #click su salva
        self.wait_loader()

        self.navigateTo("Ordini cliente")   #torna in pagina principale
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input'))).send_keys('02', Keys.ENTER) #cerco l'ordine 02     
        sleep(1)

        self.find(By.XPATH, '//tbody//tr//td').click()  #seleziono l'ordine
        self.find(By.XPATH, '//button[@data-toggle="dropdown"]').click() #click su azioni di gruppo
        self.find(By.XPATH, '//a[@data-op="crea_fattura"]').click() #click su fattura ordini clienti
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-raggruppamento-container"]').click() #ragruppa per cliente
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-raggruppamento-results"]//li[1]').click()
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-warning"]').click()
        self.wait_loader()

        stato=self.find(By.XPATH, '(//tr[1]//td[7]//span)[2]').text
        self.assertEqual(stato, "Accettato")    #check se lo stato non è cambiato
        self.find(By.XPATH, '//tbody//tr//td[2]').click()   #elimino ordine
        self.wait_loader()

        self.find(By.XPATH, '//a[@class="btn btn-danger ask"]').click()
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()

        self.find(By.XPATH, '//th[@id="th_Numero"]/i[@class="deleteicon fa fa-times"]').click() #cancello la ricerca
        sleep(1)

        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr[1]//td[2]').click() #elimino fattura
        self.wait_loader()

        self.find(By.XPATH, '//a[@id="elimina"]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click() #click di conferma
        self.wait_loader()
        #torno alle impostazioni di prima
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-15"]').click() #apro Ordini
        sleep(1)

        self.find(By.XPATH, '(//label[@class="btn btn-default active"])[1]').click() #attivo impostazione
        sleep(1)

    def conferma_quantita_ordini_cliente(self):
        wait = WebDriverWait(self.driver, 20)
        self.expandSidebar("Vendite")
        self.navigateTo("Ordini cliente")
        self.wait_loader()

        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click()   #click su tasto +
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-idanagrafica-container"]').click()     #scelta di "Cliente" come anagrafica per l'ordine
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys('Cliente')
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(Keys.ENTER)
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click()   #click su tasto aggiungi
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="tab_0"]//a[@class="btn btn-primary"]').click()  #click su tasto aggiungi riga
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys('Test') #aggiunta descrizione riga
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys('1')   #aggiunta prezzo unitario
        self.find(By.XPATH, '//button[@class="btn btn-primary pull-right"]').click()    #click su aggiungi
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '(//i[@class="fa fa-check text-success"])[1]'))) #check se la quantita è stata confermata automaticamente
        #elimino ordine
        self.find(By.XPATH, '//a[@class="btn btn-danger ask"]').click()
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-15"]').click() #apro Ordini
        sleep(1)

        self.find(By.XPATH, '(//label[@class="btn btn-default active"])[2]').click() #disattivo impostazione
        sleep(1)

        self.expandSidebar("Vendite")
        self.navigateTo("Ordini cliente")
        self.wait_loader()

        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click()   #click su tasto +
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-idanagrafica-container"]').click()     #scelta di "Cliente" come anagrafica per l'ordine
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys('Cliente')
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(Keys.ENTER)
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click()   #click su tasto aggiungi
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="tab_0"]//a[@class="btn btn-primary"]').click()  #click su tasto aggiungi riga
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys('Test') #aggiunta descrizione riga
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys('1')   #aggiunta prezzo unitario
        self.find(By.XPATH, '//button[@class="btn btn-primary pull-right"]').click()    #click su aggiungi
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//i[@class="fa fa-clock-o text-warning"]')))    #check se è stato confermata la quantita
        #elimino ordine
        self.find(By.XPATH, '//a[@class="btn btn-danger ask"]').click()
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()
        #torno alle impostazioni di prima
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-15"]').click() #apro Ordini
        sleep(1)

        self.find(By.XPATH, '(//label[@class="btn btn-default active"])[2]').click() #attivo impostazione
        sleep(1)

    def conferma_quantita_ordini_fornitore(self):
        wait = WebDriverWait(self.driver, 20)
        self.expandSidebar("Acquisti")
        self.navigateTo("Ordini fornitore")
        self.wait_loader()

        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click() #crea ordine fornitore
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-idanagrafica-container"]').click() #imposta fornitore
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-idanagrafica-results"]//li[1]').click()
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click()   #click su aggiungi
        self.wait_loader()

        self.find(By.XPATH, '//a[@class="btn btn-primary"]').click()    #aggiungi riga
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys('Test') #aggiunta descrizione riga
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys('1')   #aggiunta prezzo unitario
        self.find(By.XPATH, '//button[@class="btn btn-primary pull-right"]').click()    #click su aggiungi
        sleep(1)
        
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//i[@class="fa fa-check text-success"])[1]')))    #check se è stato confermata la quantita
        #elimino ordine
        self.find(By.XPATH, '//a[@class="btn btn-danger ask"]').click()
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-15"]').click() #apro Ordini
        sleep(1)

        self.find(By.XPATH, '(//label[@class="btn btn-default active"])[3]').click() #disattivo impostazione
        sleep(1)

        self.expandSidebar("Acquisti")
        self.navigateTo("Ordini fornitore")
        self.wait_loader()

        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click() #crea ordine fornitore
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-idanagrafica-container"]').click() #imposta fornitore
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-idanagrafica-results"]//li[1]').click()
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click()   #click su aggiungi
        self.wait_loader()

        self.find(By.XPATH, '//a[@class="btn btn-primary"]').click()    #aggiungi riga
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys('Test') #aggiunta descrizione riga
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys('1')   #aggiunta prezzo unitario
        self.find(By.XPATH, '//button[@class="btn btn-primary pull-right"]').click()    #click su aggiungi
        sleep(1)
        
        wait.until(EC.visibility_of_element_located((By.XPATH, '//i[@class="fa fa-clock-o text-warning"]')))    #check se è stato confermata la quantita
        #elimino ordine
        self.find(By.XPATH, '//a[@class="btn btn-danger ask"]').click()
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()

        #torno alle impostazioni di prima
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-15"]').click() #apro Ordini
        sleep(1)

        self.find(By.XPATH, '(//label[@class="btn btn-default active"])[3]').click() #attivo impostazione
        sleep(1)