from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from common.Test import Test, get_html

class TemplateEmail(Test):
    def setUp(self):
        super().setUp()

        self.expandSidebar("Gestione email")
        

    def test_creazione_template_email(self):

        # Crea un nuovo template.   *Required* 
        self.add_template_email('Template di Prova da Modificare', 'Anagrafiche', '1')
        self.add_template_email('Template di Prova da Eliminare', 'Anagrafiche', '1')

        # Modifica template email
        self.modifica_template("Template di Prova")

        # Cancellazione template email
        self.elimina_template()

        # Verifica template email
        self.verifica_template_email()

    def add_template_email(self, nome: str, modulo: str, account: str):
        self.navigateTo("Template email")

        # Crea un nuovo template
        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click()
        modal = self.wait_modal()

        # Completamento dei campi per il nuovo elemento
        self.input(modal, 'Nome').setValue(nome)

        select = self.input(modal, 'Modulo del template')
        select.setByText(modulo)
    
        select = self.input(modal, 'Indirizzo email')
        select.setByIndex(account)

        # Submit
        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        self.wait_loader()

    def modifica_template(self, modifica:str):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Template email")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))).send_keys('Template di Prova da Modificare', Keys.ENTER)        
        sleep(1)

        self.find(By.XPATH, '//tbody//tr//td[2]').click()
        self.wait_loader()
        
        self.input(None,'Nome').setValue(modifica)
        self.find(By.XPATH, '//div[@id="tab_0"]//button[@id="save"]').click()
        self.wait_loader()

        self.navigateTo("Template email")
        self.wait_loader()    

        self.find(By.XPATH, '//th[@id="th_Nome"]/i[@class="deleteicon fa fa-times"]').click()
        sleep(2)

    def elimina_template(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Template email")
        self.wait_loader()    

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))).send_keys('Template di Prova da Eliminare', Keys.ENTER)       
        sleep(1)

        self.find(By.XPATH, '//tbody//tr//td[2]').click()
        sleep(1)
        
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_0"]//a[@class="btn btn-danger ask"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))).click()
        self.wait_loader()

        self.find(By.XPATH, '//th[@id="th_Nome"]/i[@class="deleteicon fa fa-times"]').click()
        sleep(2)
        
    def verifica_template_email(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Template email")
        self.wait_loader()    

        #verifica elemento modificato
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))).send_keys("Template di Prova", Keys.ENTER)
        sleep(1)

        modificato=self.driver.find_element(By.XPATH,'//tbody//tr[1]//td[3]').text
        self.assertEqual("Template di Prova",modificato)
        self.find(By.XPATH, '//i[@class="deleteicon fa fa-times"]').click()
        sleep(2)

        #verifica elemento eliminato
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))).send_keys("Template di Prova da Eliminare", Keys.ENTER)
        sleep(1)
        
        eliminato=self.driver.find_element(By.XPATH,'//tbody//tr[1]//td[@class="dataTables_empty"]').text
        self.assertEqual("La ricerca non ha portato alcun risultato.",eliminato)