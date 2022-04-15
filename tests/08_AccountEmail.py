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


    def test_creazione_accountemail(self, modifica = "Account Email di Prova", server="1", porta="1"):
        self.creazione_accountemail(nomeaccount= "Account di Prova da Modificare", nomevisualizzato="Nome Cognome", emailmittente="accountprova@email.com")
        self.creazione_accountemail(nomeaccount= "Account di Prova da Eliminare", nomevisualizzato="Nome Cognome", emailmittente="accountprova@email.it")

        # Modifica email
        self.navigateTo("Account email")
        self.wait_loader()

        element=self.driver.find_element(By.XPATH,'//th[@id="th_Nome-account"]/input')
        element.send_keys('Account di Prova da Modificare')
        
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome-account"]/input'))).send_keys(Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//div[@id="tab_0"]//tbody//td[2]//div[1]').click()
        self.wait_loader()
        
        self.input(None,'Nome account').setValue(modifica)
        self.input(None, 'Server SMTP').setValue(server)
        self.input(None, 'Porta SMTP').setValue(porta)

        self.find(By.XPATH, '//div[@id="tab_0"]//a[@id="save"]').click()
        self.wait_loader()


        # Cancellazione email
        self.navigateTo("Account email")
        self.wait_loader()    

        self.find(By.XPATH, '//th[@id="th_Nome-account"]/i[@class="deleteicon fa fa-times fa-2x"]').click()

        element=self.driver.find_element(By.XPATH,'//th[@id="th_Nome-account"]/input')
        element.send_keys('Account di Prova da Eliminare')
        
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome-account"]/input'))).send_keys(Keys.ENTER)

        sleep(2)
        self.find(By.XPATH, '//div[@id="tab_0"]//tbody//td[2]//div[1]').click()
        self.wait_loader()
        self.find(By.XPATH, '//div[@id="tab_0"]//a[@class="btn btn-danger ask"]').click()
        self.wait_loader()
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()


    def creazione_accountemail(self, nomeaccount=str, nomevisualizzato=str, emailmittente=str):
        self.navigateTo("Account email")

        self.find(By.CSS_SELECTOR, '#tabs > li:first-child .btn-primary > .fa-plus').click()
        modal = self.wait_modal()

        self.input(modal, 'Nome account').setValue(nomeaccount)
        self.input(modal, 'Nome visualizzato').setValue(nomevisualizzato)
        self.input(modal, 'Email mittente').setValue(emailmittente)

        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        self.wait_loader()
