from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from common.Test import Test, get_html


class AccountEmail(Test):
    def setUp(self):
        super().setUp()

        self.expandSidebar("Gestione email")


    def test_creazione_accountemail(self):
        # Creazione account email   *Required* 
        self.creazione_account_email(nomeaccount= "Account di Prova da Modificare", nomevisualizzato="Nome Cognome", emailmittente="accountprova@email.com")
        self.creazione_account_email(nomeaccount= "Account di Prova da Eliminare", nomevisualizzato="Nome Cognome", emailmittente="accountprova@email.it")

        # Modifica account email
        self.modifica_account_email("Account Email di Prova", "1", "1")

        # Cancellazione account email
        self.elimina_account_email()

        # Verifica account email
        self.verifica_account_email()

    def creazione_account_email(self, nomeaccount=str, nomevisualizzato=str, emailmittente=str):
        self.navigateTo("Account email")

        self.find(By.CSS_SELECTOR, '#tabs > li:first-child .btn-primary > .fa-plus').click()
        modal = self.wait_modal()

        self.input(modal, 'Nome account').setValue(nomeaccount)
        self.input(modal, 'Nome visualizzato').setValue(nomevisualizzato)
        self.input(modal, 'Email mittente').setValue(emailmittente)

        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        self.wait_loader()

    def modifica_account_email(self, modifica:str, server:str, porta:str):
        self.navigateTo("Account email")
        self.wait_loader()

        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome-account"]/input'))).send_keys('Account di Prova da Modificare')        
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome-account"]/input'))).send_keys(Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//div[@id="tab_0"]//tbody//td[2]//div[1]').click()
        self.wait_loader()
        
        self.input(None,'Nome account').setValue(modifica)
        self.input(None, 'Server SMTP').setValue(server)
        self.input(None, 'Porta SMTP').setValue(porta)

        self.find(By.XPATH, '//div[@id="tab_0"]//a[@id="save"]').click()
        self.wait_loader()

        self.navigateTo("Account email")
        self.wait_loader()    

        self.find(By.XPATH, '//th[@id="th_Nome-account"]/i[@class="deleteicon fa fa-times fa-2x"]').click()

    def elimina_account_email(self):
        self.navigateTo("Account email")
        self.wait_loader()    

        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome-account"]/input'))).send_keys('Account di Prova da Eliminare')        
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome-account"]/input'))).send_keys(Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//div[@id="tab_0"]//tbody//td[2]//div[1]').click()
        sleep(1)
        
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_0"]//a[@class="btn btn-danger ask"]'))).click()
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))).click()
        self.wait_loader()

        self.find(By.XPATH, '//th[@id="th_Nome-account"]/i[@class="deleteicon fa fa-times fa-2x"]').click()

    def verifica_account_email(self):
        self.navigateTo("Account email")
        self.wait_loader()    

        #verifica elemento modificato
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome-account"]/input'))).send_keys("Account Email di Prova")
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome-account"]/input'))).send_keys(Keys.ENTER)
        sleep(1)

        modificato=self.driver.find_element(By.XPATH,'//tbody//tr[1]//td[3]').text
        self.assertEqual("Account Email di Prova",modificato)
        self.find(By.XPATH, '//i[@class="deleteicon fa fa-times fa-2x"]').click()

        #verifica elemento eliminato
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome-account"]/input'))).send_keys("Account di Prova da Eliminare")
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome-account"]/input'))).send_keys(Keys.ENTER)
        sleep(1)
        
        eliminato=self.driver.find_element(By.XPATH,'//tbody//tr[1]//td[@class="dataTables_empty"]').text
        self.assertEqual("La ricerca non ha portato alcun risultato.",eliminato)