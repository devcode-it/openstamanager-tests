from common.Test import Test, get_html
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class RitenutePrevidenziali(Test):
    def setUp(self):
        super().setUp()

        self.expandSidebar("Strumenti")
        self.expandSidebar("Tabelle")
        

    def test_creazione_ritenuteprevidenziali(self, modifica="Ritenuta Previdenziale di Prova"):
        self.creazione_ritenuteprevidenziali(descrizione= "Ritenuta Previdenziale di Prova da Modificare", percentuale="80,00", percentualeimp="60,00")
        self.creazione_ritenuteprevidenziali(descrizione= "Ritenuta Previdenziale di Prova da Eliminare", percentuale="20,00", percentualeimp="40,00")

        # Modifica Ritenuta Previdenziale
        self.navigateTo("Ritenute previdenziali")
        self.wait_loader()

        element=self.driver.find_element(By.XPATH,'//th[@id="th_Descrizione"]/input')
        element.send_keys('Ritenuta Previdenziale di Prova da Modificare')
        
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input'))).send_keys(Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//div[@id="tab_0"]//tbody//td[2]//div[1]').click()
        self.wait_loader()
        
        self.input(None,'Descrizione').setValue(modifica)

        self.find(By.XPATH, '//div[@id="tab_0"]//a[@id="save"]').click()
        self.wait_loader()


        # Cancellazione Ritenuta Previdenziale
        self.navigateTo("Ritenute previdenziali")
        self.wait_loader()    

        self.find(By.XPATH, '//th[@id="th_Descrizione"]/i[@class="deleteicon fa fa-times fa-2x"]').click()

        element=self.driver.find_element(By.XPATH,'//th[@id="th_Descrizione"]/input')
        element.send_keys('Ritenuta Previdenziale di Prova da Eliminare')
        
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input'))).send_keys(Keys.ENTER)

        sleep(2)
        self.find(By.XPATH, '//div[@id="tab_0"]//tbody//td[2]//div[1]').click()
        self.wait_loader()
        self.find(By.XPATH, '//div[@id="tab_0"]//a[@class="btn btn-danger ask"]').click()
        self.wait_loader()
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()        



    def creazione_ritenuteprevidenziali(self, descrizione=str, percentuale=str, percentualeimp=str):
        self.navigateTo("Ritenute previdenziali")
        self.find(By.CSS_SELECTOR, '#tabs > li:first-child .btn-primary > .fa-plus').click()
        modal = self.wait_modal()

        self.input(modal, 'Descrizione').setValue(descrizione)
        self.input(modal, 'Percentuale').setValue(percentuale)
        self.input(modal, 'Percentuale imponibile').setValue(percentualeimp)

        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        self.wait_loader()
