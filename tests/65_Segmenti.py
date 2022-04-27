from common.Test import Test, get_html
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Segmenti(Test):
    def setUp(self):
        super().setUp()

        self.expandSidebar("Strumenti")
        self.navigateTo("Segmenti")

    def test_creazione_segmenti(self, modifica="Segmento di Prova da Eliminare"):
        self.creazione_segmenti(nome= "Segmento di Prova da Modificare", maschera="1234/2022", modulo= "Articoli", note="Nota di Prova")

        # Modifica Segmenti
        self.navigateTo("Segmenti")
        self.wait_loader()

        element=self.driver.find_element(By.XPATH,'//th[@id="th_Nome"]/input')
        element.send_keys('Segmento di Prova da Modificare')
        
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))).send_keys(Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//div[@id="tab_0"]//tbody//td[2]//div[1]').click()
        self.wait_loader()
        
        self.input(None,'Nome').setValue(modifica)

        self.find(By.XPATH, '//div[@id="tab_0"]//a[@id="save"]').click()
        self.wait_loader()


        # Cancellazione Segmenti
        self.navigateTo("Segmenti")
        self.wait_loader()    

        self.find(By.XPATH, '//th[@id="th_Nome"]/i[@class="deleteicon fa fa-times fa-2x"]').click()

        element=self.driver.find_element(By.XPATH,'//th[@id="th_Nome"]/input')
        element.send_keys('Segmento di Prova da Eliminare')
        
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))).send_keys(Keys.ENTER)

        sleep(2)
        self.find(By.XPATH, '//div[@id="tab_0"]//tbody//td[2]//div[1]').click()
        self.wait_loader()
        self.find(By.XPATH, '//div[@id="tab_0"]//a[@class="btn btn-danger ask"]').click()
        self.wait_loader()
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()      


    def creazione_segmenti(self, nome=str, segmenti= str, maschera=str, modulo=str, note=str):

        self.find(By.CSS_SELECTOR, '#tabs > li:first-child .btn-primary > .fa-plus').click()
        modal = self.wait_modal()

        self.input(modal, 'Nome').setValue(nome)
        self.input(modal, 'Maschera').setValue(maschera)
        self.input(modal, 'Note').setValue(note)
        
        select = self.input(modal, 'Modulo')
        select.setByText(modulo)

        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        self.wait_loader()