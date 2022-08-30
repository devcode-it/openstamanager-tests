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


class Articoli(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Magazzino")


    def test_creazione_articolo(self):
        # Crea un nuovo articolo. *Required*
        self.creazione_articolo("01", "Articolo di Prova",)
        self.creazione_articolo("02", "Articolo di Prova da Eliminare")
        
        # Modifica articolo
        self.modifica_articolo("10,00")
        
        # Cancellazione articolo
        self.elimina_articolo()
        
        # Verifica articolo
        self.verifica_articolo()

    def creazione_articolo(self, codice: str, descrizione: str):
        self.navigateTo("Articoli")
        sleep(2)
        # #
        # 1/2 Crea un nuovo articolo. 
        # #
        # Apre la schermata di nuovo elemento
        self.find(By.CSS_SELECTOR, '#tabs > li:first-child .btn-primary > .fa-plus').click()
        modal = self.wait_modal()

        self.input(modal, 'Codice').setValue(codice)
        self.input(modal, 'Descrizione').setValue(descrizione)

        # Submit
        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        self.wait_loader()
       
    def modifica_articolo(self, qta=str):
        self.navigateTo("Articoli")
        self.wait_loader()

        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH,'//th[@id="th_Descrizione"]/input'))).send_keys('Articolo di Prova')
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input'))).send_keys(Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//div[@id="tab_0"]//tbody//td[2]//div[1]').click()
        self.wait_loader()

        self.find(By.XPATH, '//label[@class="btn btn-default"][@for="qta_manuale"]').click()
        self.input(None, 'Quantità').setValue(qta)
        self.input(None, 'Descrizione movimento').setValue("Movimento di prova")

        self.find(By.XPATH, '//div[@id="tab_0"]//a[@id="save"]').click()
        sleep(2)

        # Controllo quantità 
        self.find(By.XPATH, '//a[@id="back"]').click()
        sleep(1)
        
        verificaqta = self.find(By.XPATH, '//div[@id="tab_0"]//tbody//td[10]//div[1][1]').text
        self.assertEqual(verificaqta, qta)

        self.find(By.XPATH, '//th[@id="th_Descrizione"]/i[@class="deleteicon fa fa-times fa-2x"]').click()

    def elimina_articolo(self):
        self.navigateTo("Articoli")
        self.wait_loader()  

        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH,'//th[@id="th_Descrizione"]/input'))).send_keys('Articolo di Prova da Eliminare')
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input'))).send_keys(Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//div[@id="tab_0"]//tbody//td[2]//div[1]').click()
        self.wait_loader()
        self.find(By.XPATH, '//div[@id="tab_0"]//a[@class="btn btn-danger ask"]').click()
        sleep(1)
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        sleep(1)

        self.find(By.XPATH, '//th[@id="th_Descrizione"]/i[@class="deleteicon fa fa-times fa-2x"]').click()
        sleep(1)

    def verifica_articolo(self):
        self.navigateTo("Articoli")
        self.wait_loader()    

        #verifica elemento modificato
        element=self.driver.find_element(By.XPATH,'//th[@id="th_Qtà"]/input')
        element.send_keys("10,00")
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Qtà"]/input'))).send_keys(Keys.ENTER)
        sleep(1)
        modificato=self.driver.find_element(By.XPATH,'//tbody//tr[1]//td[10]').text
        self.assertEqual("10,00",modificato)
        self.find(By.XPATH, '//i[@class="deleteicon fa fa-times fa-2x"]').click()
        sleep(1)

        #verifica elemento eliminato
        element=self.driver.find_element(By.XPATH,'//th[@id="th_Descrizione"]/input')
        element.send_keys("Articolo di prova da Eliminare")
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input'))).send_keys(Keys.ENTER)
        sleep(2)
        eliminato=self.driver.find_element(By.XPATH,'//tbody//tr[1]//td[1]').text
        self.assertEqual("La ricerca non ha portato alcun risultato.",eliminato)
