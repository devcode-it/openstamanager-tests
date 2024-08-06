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

    def test_impostazioni_ddt(self):
        # Cambia automaticamente stato ddt fatturati (1)
        self.cambia_stato_ddt_fatturati()

    def cambia_stato_ddt_fatturati(self):
        wait = WebDriverWait(self.driver, 20) 
        self.expandSidebar("Magazzino") #prima test con il ddt in entrata
        self.navigateTo("Ddt in entrata")
        self.wait_loader()

        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click() #click su +
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-idanagrafica_add-container"]').click() #seleziono "Admin spa" come mittente
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Admin spa", Keys.ENTER)
        self.find(By.XPATH, '//span[@id="select2-idcausalet-container"]').click()   #seleziono "Conto lavorazione" come causale
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Conto lavorazione", Keys.ENTER)
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click()   #click su procedi
        self.wait_loader()

        self.find(By.XPATH, '//span[@id="select2-idstatoddt-container"]').click() #cambio stato in evaso
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Evaso", Keys.ENTER)
        self.find(By.XPATH, '//button[@id="save"]').click()
        self.wait_loader()

        self.navigateTo("Ddt in entrata")
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr[1]//td[1]').click()    #seleziono primo ddt
        self.find(By.XPATH, '//button[@class="btn btn-primary btn-lg dropdown-toggle dropdown-toggle-split"]').click()  #apro azioni di gruppo
        self.find(By.XPATH, '//a[@data-op="crea_fattura"]').click()   #click su fattura ddt
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-raggruppamento-container"]').click()   
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente")    #ragruppa per Cliente
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(Keys.ENTER)
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-warning"]').click()  #click di conferma
        self.wait_loader()

        stato=self.find(By.XPATH, '(//tr[1]//td[11]//span)[2]').text    #controllo se lo stato è in fatturato
        self.assertEqual(stato, "Fatturato")
        #elimino ddt
        self.find(By.XPATH, '//tbody//tr[1]//td[2]').click()
        self.wait_loader()

        self.find(By.XPATH, '//a[@class="btn btn-danger ask"]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()
        #elimino fattura
        self.expandSidebar("Acquisti")
        self.navigateTo("Fatture di acquisto")
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr//td[2]').click()   #click sulla fattura in prima riga
        self.wait_loader()
    
        self.find(By.XPATH, '//a[@id="elimina"]').click()   #elimina fattura
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()   #click di conferma
        self.wait_loader()

        self.expandSidebar("Magazzino") #test con il ddt in uscita
        self.navigateTo("Ddt in uscita")
        self.wait_loader()

        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click() #click su +
        sleep(1)
        #seleziono destinatario
        self.find(By.XPATH, '//span[@id="select2-idanagrafica_add-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Admin spa")
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(Keys.ENTER)
        #seleziono causale trasporto
        self.find(By.XPATH, '//span[@id="select2-idcausalet-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Conto lavorazione")
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(Keys.ENTER)
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click() #click su aggiungi
        self.wait_loader()

        self.find(By.XPATH, '//span[@id="select2-idstatoddt-container"]').click() #cambio stato in evaso
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Evaso", Keys.ENTER)
        self.find(By.XPATH, '//button[@id="save"]').click()
        self.wait_loader()

        self.navigateTo("Ddt in uscita")
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr[1]//td[1]').click()    #seleziono primo ddt
        self.find(By.XPATH, '//button[@class="btn btn-primary btn-lg dropdown-toggle dropdown-toggle-split"]').click()  #apro azioni di gruppo
        self.find(By.XPATH, '//a[@data-op="crea_fattura"]').click()   #click su fattura ddt
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente")    #ragruppa per Cliente
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(Keys.ENTER)
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-warning"]').click()  #click di conferma
        self.wait_loader()

        stato2=self.find(By.XPATH, '(//tr[1]//td[11]//span)[2]').text    #controllo se lo stato è in fatturato
        self.assertEqual(stato2, "Fatturato")
        #elimino ddt
        self.find(By.XPATH, '//tbody//tr[1]//td[2]').click()
        self.wait_loader()

        self.find(By.XPATH, '//a[@class="btn btn-danger ask"]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()

        self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        #elimino fattura
        self.find(By.XPATH, '//tbody//tr//td[2]').click()   #click sulla fattura in prima riga
        self.wait_loader()
    
        self.find(By.XPATH, '//a[@id="elimina"]').click()   #elimina fattura
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()   #click di conferma
        self.wait_loader()