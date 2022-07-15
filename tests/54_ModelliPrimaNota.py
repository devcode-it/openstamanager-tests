from common.Test import Test, get_html
from selenium.webdriver.common.keys import Keys
from common.RowManager import RowManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class ModelliPrimaNota(Test):
    def setUp(self):
        super().setUp()

        self.expandSidebar("Strumenti")
        self.expandSidebar("Tabelle")
        

    def test_creazione_modelli_prima_nota(self):
        # Creazione modello prima nota      *Required*
        self.creazione_modelli_prima_nota(nome="Modello Prima Nota di Prova da Modificare", causale="Prova anticipo fattura num. {numero} del {data}")
        self.creazione_modelli_prima_nota(nome="Modello Prima Nota di Prova da Eliminare", causale="Prova anticipo fattura num. {numero} del {data}")

        # Modifica Modello Prima Nota
        self.modifica_modello_prima_nota("Modello Prima Nota di Prova")
        
        # Cancellazione Modello Prima nota
        self.elimina_modello_prima_nota()
        

    def creazione_modelli_prima_nota(self, nome=str, causale=str):
        self.navigateTo("Modelli prima nota")

        actions = webdriver.common.action_chains.ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element(By.XPATH,'//div[@class="col-md-12"]')).move_by_offset(0,0).perform()


        self.find(By.CSS_SELECTOR, '#tabs > li:first-child .btn-primary > .fa-plus').click()
        modal = self.wait_modal()

        self.input(modal, 'Nome').setValue(nome)
        self.input(modal, 'Causale').setValue(causale)

        self.find(By.XPATH, '//span[@id="select2-conto0-container"]').click()
        sleep(1)
        self.find(By.XPATH, '//input[@class="select2-search__field"]').send_keys("100.000010", Keys.ENTER)
        sleep(1)
        self.find(By.XPATH, '//input[@id="avere0"]').send_keys("100,00")


        self.find(By.XPATH, '//span[@id="select2-conto1-container"]').click()
        self.find(By.XPATH, '//input[@class="select2-search__field"]').send_keys("700.000010")
        sleep(1)
        self.find(By.XPATH, '//li[@class="select2-results__option select2-results__option--highlighted"]').click() 
        sleep(1)
        self.find(By.XPATH, '//input[@id="dare1"]').send_keys("100,00")


        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        self.wait_loader()

    def modifica_modello_prima_nota(self, modifica=str):
        self.navigateTo("Modelli prima nota")
        self.wait_loader()

        element=self.driver.find_element(By.XPATH,'//th[@id="th_Nome"]/input')
        element.send_keys('Modello Prima Nota di Prova da Modificare')
        
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))).send_keys(Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//div[@id="tab_0"]//tbody//td[2]//div[1]').click()
        self.wait_loader()
        
        actions = webdriver.common.action_chains.ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element(By.XPATH,'//div[@id="module-edit"]')).move_by_offset(0,0).perform()

        self.input(None,'Nome').setValue(modifica)

        self.find(By.XPATH, '//div[@id="tab_0"]//a[@id="save"]').click()
        self.wait_loader()

        self.navigateTo("Modelli prima nota")
        self.wait_loader()  

        self.find(By.XPATH, '//th[@id="th_Nome"]/i[@class="deleteicon fa fa-times fa-2x"]').click()

    def elimina_modello_prima_nota(self):
        self.navigateTo("Modelli prima nota")
        self.wait_loader()

        element=self.driver.find_element(By.XPATH,'//th[@id="th_Nome"]/input')
        element.send_keys('Modello Prima Nota di Prova da Eliminare')
        
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))).send_keys(Keys.ENTER)

        sleep(2)
        self.find(By.XPATH, '//div[@id="tab_0"]//tbody//td[2]//div[1]').click()
        self.wait_loader()

        actions = webdriver.common.action_chains.ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element(By.XPATH,'//div[@id="module-edit"]')).move_by_offset(0,0).perform()

        self.find(By.XPATH, '//div[@id="tab_0"]//a[@class="btn btn-danger ask"]').click()
        self.wait_loader()
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()
