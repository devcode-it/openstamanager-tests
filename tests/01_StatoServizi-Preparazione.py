from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from common.Test import Test, get_html

class StatoServizi(Test):
    def setUp(self):
        super().setUp()

        
    def test_stato_servizi(self):

        #Attivazione moduli nascosti
        self.attiva_moduli()

        #Aggiunta P.IVA e dati anagrafica azienda   
        self.compila_azienda()
        self.creazione_fornitore_estero()
        self.creazione_cliente_estero()

    def click_element(self, xpath):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, xpath))).click()

    def attiva_moduli(self):
        self.expandSidebar("Strumenti")   
        self.navigateTo("Stato dei servizi")

        for _ in range(3):
            self.click_element('//button[@onclick="abilitaSottoModuli(this)"]')
            self.click_element('//button[@class="swal2-confirm btn btn-lg btn-primary"]')
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//div[@class="toast-message"]'))).click()

    def compila_azienda(self):
        self.navigateTo("Anagrafiche")

        self.find(By.XPATH, '//tbody//tr//td[2]').click()
        self.wait_loader()
        
        self.input(None, 'Partita IVA').setValue("05024030289")
        self.input(None, 'Codice fiscale').setValue("05024030289")
        self.input(None, 'Tipologia').setValue("Azienda")
        self.driver.find_element(By.XPATH,'//input[@id="indirizzo"]').send_keys("Via Rovigo, 51")
        self.input(None, 'C.A.P.').setValue("35042")
        self.input(None, 'Città').setValue("Este")
        self.find(By.XPATH, '//button[@id="save"]').click()
        self.wait_loader()

    def creazione_fornitore_estero(self):
        wait = WebDriverWait(self.driver, 20)
        self.expandSidebar("Anagrafiche")

        # Crea una nuova anagrafica estera
        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click()
        modal = self.wait_modal()

        # Completamento dei campi per il nuovo elemento
        self.input(modal, 'Denominazione').setValue("Fornitore Estero")
        self.input(modal, 'Tipo di anagrafica').setByText("Fornitore")
        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        self.wait_loader() 

        # Completamento anagrafica  
        self.navigateTo("Anagrafiche")
        self.wait_loader()  
 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Ragione-sociale"]/input'))).send_keys("Fornitore Estero", Keys.ENTER)    
        sleep(1)

        self.find(By.XPATH, '//tbody//tr//td[2]').click()
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-id_nazione-container"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input[@type="search"]'))).send_keys("Germania")
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//li[@class="select2-results__option select2-results__option--highlighted"]'))).click()
        self.input(None, 'Partita IVA').setValue("05024030286")
        self.input(None, 'Tipologia').setValue("Azienda")
        self.input(None, 'Codice fiscale').setValue("05024030286")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="indirizzo"]'))).send_keys("Via controllo caratteri speciali: &\"<>èéàòùì?'`")
        self.input(None, 'C.A.P.').setValue("35042")
        self.input(None, 'Città').setValue("Berlino")
        self.find(By.XPATH, '//button[@id="save"]').click()
        self.wait_loader()

        self.navigateTo("Anagrafiche")
        self.wait_loader()

        self.find(By.XPATH, '//th[@id="th_Ragione-sociale"]/i[@class="deleteicon fa fa-times"]').click()
        sleep(1)

    def creazione_cliente_estero(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Anagrafiche")
        self.wait_loader()

        # Crea una nuova anagrafica estera
        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click()
        modal = self.wait_modal()

        # Completamento dei campi per il nuovo elemento
        self.input(modal, 'Denominazione').setValue("Cliente Estero")
        self.input(modal, 'Tipo di anagrafica').setByText("Cliente")
        
        # Submit
        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        sleep(1)

        self.navigateTo("Anagrafiche")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Ragione-sociale"]/input'))).send_keys("Cliente Estero", Keys.ENTER)  
        sleep(1)

        self.find(By.XPATH, '//tbody//tr//td[2]').click()
        self.wait_loader()

        # Modifica dati
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-id_nazione-container"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input[@type="search"]'))).send_keys("Germania")
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//li[@class="select2-results__option select2-results__option--highlighted"]'))).click()
        self.wait_loader()

        self.input(None, 'Partita IVA').setValue("05024030288")
        self.input(None, 'Codice fiscale').setValue("05024030288")
        self.input(None, 'Tipologia').setValue("Azienda")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="indirizzo"]'))).send_keys("Via controllo caratteri speciali: &\"<>èéàòùì?'`")
        self.input(None, 'C.A.P.').setValue("35042")
        self.input(None, 'Città').setValue("Piacenza d'Adige")
        self.find(By.XPATH, '//button[@id="save"]').click()
        self.wait_loader()