from common.Test import Test, get_html
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class UtentiPermessi(Test):
    def setUp(self):
        super().setUp()

        self.expandSidebar("Strumenti")


    def test_creazione_utenti_permessi(self):
        # Creazione utenti e permessi
        self.creazione_utenti_permessi(nome="Tipo Utente di Prova")

        # Modifica Utenti e Permessi
        self.modifica_utenti_permessi("Test","Admin spa","1qa2ws3ed!","Lettura e Scrittura")
        
        # Cancellazione Utenti e Permessi
        self.elimina_utenti_permessi()
        
        # Verifica Utenti e Permessi
        self.verifica_utenti_permessi()

    def creazione_utenti_permessi(self, nome):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Utenti e permessi")
        self.find(By.CSS_SELECTOR, '#tabs > li:first-child .btn-primary > .fa-plus').click()
        modal = self.wait_modal()

        self.input(modal, 'Nome').setValue(nome)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@id='form_38-']//button[@type='button']"))).click()
        self.wait_loader()

    def modifica_utenti_permessi(self, user=str, anag=str, passw=str, modifica=str):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Utenti e permessi")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Gruppo"]/input'))).send_keys('Tipo Utente di Prova', Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//div[@id="tab_0"]//tbody//td[2]//div[1]').click()
        self.wait_loader()

        self.find(By.XPATH, '//a[@class="pull-right btn btn-primary bound clickable"]').click()
        self.wait_loader()

        self.input(None, 'Username').setValue(user)
        sleep(1)

        self.find(By.XPATH,'//span[@id="select2-idanag-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]/input[@class="select2-search__field"]'))).send_keys(anag)
        sleep(1)
        wait.until(EC.visibility_of_element_located((By.XPATH, '//li[@class="select2-results__option select2-results__option--highlighted"]'))).click()
        sleep(1)

        self.input(None, 'Password').setValue(passw)
        self.find(By.XPATH, '//button[@id="submit-button"]').click()
        sleep(2)

        self.find(By.XPATH, '//span[@id="select2-permesso_1-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(modifica, Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-permesso_2-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(modifica, Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-permesso_8-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(modifica, Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-permesso_38-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(modifica, Keys.ENTER)

        self.navigateTo("Utenti e permessi")
        self.wait_loader()    

        self.find(By.XPATH, '//th[@id="th_Gruppo"]/i[@class="deleteicon fa fa-times fa-2x"]').click()

    def elimina_utenti_permessi(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Utenti e permessi")
        self.wait_loader()    

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Gruppo"]/input'))).send_keys('Tipo Utente di Prova', Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//div[@id="tab_0"]//tbody//td[2]//div[1]').click()
        sleep(1)
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_0"]//a[@class="btn btn-danger ask "]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))).click()
        self.wait_loader() 

        self.find(By.XPATH, '//th[@id="th_Gruppo"]/i[@class="deleteicon fa fa-times fa-2x"]').click()     

    def verifica_utenti_permessi(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Utenti e permessi")
        self.wait_loader()    

        #verifica elemento eliminato
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Gruppo"]/input'))).send_keys("Tipo Utente di Prova", Keys.ENTER)
        sleep(1)
        
        eliminato=self.driver.find_element(By.XPATH,'//tbody//tr[1]//td[@class="dataTables_empty"]').text
        self.assertEqual("La ricerca non ha portato alcun risultato.",eliminato)