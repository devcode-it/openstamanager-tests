from common.Test import Test, get_html
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class StatiPreventivi(Test):
    def setUp(self):
        super().setUp()

        self.expandSidebar("Strumenti")
        self.expandSidebar("Tabelle")
        

    def test_creazione_stati_preventivi(self):
        # Creazione stato preventivi    *Required*
        self.creazione_stati_preventivi("Stato Preventivi di Prova da Modificare", "fa fa-check text-success")
        self.creazione_stati_preventivi("Stato Preventivi di Prova da Eliminare", "fa fa-thumbs-down text-danger")

        # Modifica Stato dei preventivi
        self.modifica_stati_preventivi("Stato Preventivi di Prova")
        
        # Cancellazione Stato dei Preventivi
        self.elimina_stati_preventivi()
        

    def creazione_stati_preventivi(self, descrizione=str, icona=str):
        self.navigateTo("Stati dei preventivi")
        self.find(By.CSS_SELECTOR, '#tabs > li:first-child .btn-primary > .fa-plus').click()
        modal = self.wait_modal()

        self.input(modal, 'Descrizione').setValue(descrizione)
        self.input(modal, 'Icona').setValue(icona)

        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        self.wait_loader()

    def modifica_stati_preventivi(self, modifica=str):
        self.navigateTo("Stati dei preventivi")
        self.wait_loader()

        element=self.driver.find_element(By.XPATH,'//th[@id="th_Descrizione"]/input')
        element.send_keys('Stato Preventivi di Prova da Modificare')
        
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input'))).send_keys(Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//div[@id="tab_0"]//tbody//td[2]//div[1]').click()
        self.wait_loader()
        
        actions = webdriver.common.action_chains.ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element(By.XPATH,'//div[@class="col-md-12"]')).move_by_offset(0,0).perform()
        self.input(None,'Descrizione').setValue(modifica)

        self.find(By.XPATH, '//div[@id="tab_0"]//a[@id="save"]').click()
        self.wait_loader()

        self.navigateTo("Stati dei preventivi")
        self.wait_loader()    

        self.find(By.XPATH, '//th[@id="th_Descrizione"]/i[@class="deleteicon fa fa-times fa-2x"]').click()

    def elimina_stati_preventivi(self):
        self.navigateTo("Stati dei preventivi")
        self.wait_loader()    

        element=self.driver.find_element(By.XPATH,'//th[@id="th_Descrizione"]/input')
        element.send_keys('Stato Preventivi di Prova da Eliminare')
        
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input'))).send_keys(Keys.ENTER)

        sleep(2)
        self.find(By.XPATH, '//div[@id="tab_0"]//tbody//td[2]//div[1]').click()
        self.wait_loader()

        actions = webdriver.common.action_chains.ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element(By.XPATH,'//div[@class="col-md-12"]')).move_by_offset(0,0).perform()

        self.find(By.XPATH, '//div[@id="tab_0"]//a[@class="btn btn-danger ask"]').click()
        self.wait_loader()
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()        
