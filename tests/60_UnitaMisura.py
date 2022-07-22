from common.Test import Test, get_html
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class UnitaMisura(Test):
    def setUp(self):
        super().setUp()

        self.expandSidebar("Strumenti")
        self.expandSidebar("Tabelle")

    def test_creazione_unita_misura(self):
        # Creazione unita di misura     *Required*
        self.creazione_unita_misura("UdMdPdM")
        self.creazione_unita_misura("UdMdPdE")

        # Modifica Unità di Misura
        self.modifica_unita_misura("UdMdP")
        
        # Cancellazione Unità di Misura
        self.elimina_unita_misura()

        # Verifica Unità di Misura
        self.verifica_unita_misura()

    def creazione_unita_misura(self, valore= str):

        self.navigateTo("Unità di misura")

        self.find(By.CSS_SELECTOR, '#tabs > li:first-child .btn-primary > .fa-plus').click()
        modal = self.wait_modal()

        self.input(modal, 'Valore').setValue(valore)

        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        self.wait_loader()

    def modifica_unita_misura(self, modifica=str):
        self.navigateTo("Unità di misura")
        self.wait_loader()

        element=self.driver.find_element(By.XPATH,'//th[@id="th_Valore"]/input')
        element.send_keys('UdMdPdM')
        
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Valore"]/input'))).send_keys(Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//div[@id="tab_0"]//tbody//td[2]//div[1]').click()
        
        sleep(2)          
        self.driver.execute_script('window.scrollTo(0,0)')

        self.input(None,'Valore').setValue(modifica)

        self.find(By.XPATH, '//div[@id="tab_0"]//a[@id="save"]').click()
        self.wait_loader()

        self.navigateTo("Unità di misura")
        self.wait_loader()    

        self.find(By.XPATH, '//th[@id="th_Valore"]/i[@class="deleteicon fa fa-times fa-2x"]').click()

    def elimina_unita_misura(self):
        self.navigateTo("Unità di misura")
        self.wait_loader()    

        element=self.driver.find_element(By.XPATH,'//th[@id="th_Valore"]/input')
        element.send_keys('UdMdPdE')
        
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Valore"]/input'))).send_keys(Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//div[@id="tab_0"]//tbody//td[2]//div[1]').click()

        sleep(2)          
        self.driver.execute_script('window.scrollTo(0,0)')


        self.find(By.XPATH, '//div[@id="tab_0"]//a[@class="btn btn-danger ask"]').click()
        self.wait_loader()
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()    

        self.find(By.XPATH, '//th[@id="th_Valore"]/i[@class="deleteicon fa fa-times fa-2x"]').click()

    def verifica_unita_misura(self):
        self.navigateTo("Unità di misura")
        self.wait_loader()    

        #verifica elemento modificato
        element=self.driver.find_element(By.XPATH,'//th[@id="th_Valore"]/input')
        element.send_keys("UdMdP")
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Valore"]/input'))).send_keys(Keys.ENTER)
        sleep(1)
        modificato=self.driver.find_element(By.XPATH,'//tbody//tr[1]//td[2]').text
        self.assertEqual("UdMdP",modificato)
        self.find(By.XPATH, '//i[@class="deleteicon fa fa-times fa-2x"]').click()
        sleep(1)

        #verifica elemento eliminato
        element=self.driver.find_element(By.XPATH,'//th[@id="th_Valore"]/input')
        element.send_keys("UdMdPdE")
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Valore"]/input'))).send_keys(Keys.ENTER)
        sleep(1)
        eliminato=self.driver.find_element(By.XPATH,'//tbody//tr[1]//td[@class="dataTables_empty"]').text
        self.assertEqual("La ricerca non ha portato alcun risultato.",eliminato)