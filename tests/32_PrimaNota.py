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



class PrimaNota(Test):
    def setUp(self):
        super().setUp()

        self.expandSidebar("Contabilità")

    def test_creazione_prima_nota(self):
        # Creazione prima nota *Required*
        self.creazione_prima_nota(causale = "Prima Nota da Modificare")
        self.creazione_prima_nota(causale = "Prima Nota da Eliminare")

       # Modifica Prima Nota
        self.modifica_prima_nota("Prima Nota di Prova (Fatt. n.1 del 01/01/2024)")
     
        # Cancellazione Prima nota
        self.elimina_prima_nota()

        # Verifica Fasce orarie
        self.verifica_prima_nota()
       
    def creazione_prima_nota(self,  causale = str):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Prima nota")
        self.wait_loader() 

        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click()
        modal = self.wait_modal()

        self.input(modal, 'Causale').setValue(causale)
        modal = self.wait_modal()
        
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-conto0-container"]'))).click()
        sleep(1)
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("100.000010", Keys.ENTER)
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-conto1-container"]'))).click()
        sleep(1)
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("700.000010")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//li[@class="select2-results__option select2-results__option--highlighted"]'))).click()
        sleep(1) 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="avere0"]'))).send_keys("100,00")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="dare1"]'))).send_keys("100,00")
        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        self.wait_loader()
    
    def modifica_prima_nota(self, modifica=str):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Prima nota")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Causale"]/input'))).send_keys('Prima Nota da Modificare', Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//tbody//tr//td[2]').click()
        self.wait_loader()
        
        self.input(None,'Causale').setValue(modifica)
        self.find(By.XPATH, '//div[@id="tab_0"]//button[@id="save"]').click()
        self.wait_loader()

        self.navigateTo("Prima nota")
        self.wait_loader()  

        self.find(By.XPATH, '//th[@id="th_Causale"]/i[@class="deleteicon fa fa-times"]').click()
        sleep(2)

    def elimina_prima_nota(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Prima nota")
        self.wait_loader()  

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Causale"]/input'))).send_keys('Prima Nota da Eliminare', Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//tbody//tr//td[2]').click()
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_0"]//a[@class="btn btn-danger ask"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))).click()
        self.wait_loader()

        self.find(By.XPATH, '//th[@id="th_Causale"]/i[@class="deleteicon fa fa-times"]').click()
        sleep(2)

    def verifica_prima_nota(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Prima nota")
        self.wait_loader()    

        #verifica elemento modificato
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Causale"]/input'))).send_keys("Prima Nota di Prova (Fatt. n.1 del 01/01/2024)", Keys.ENTER)
        sleep(1)

        modificato=self.driver.find_element(By.XPATH,'//tbody//tr[1]//td[4]').text
        self.assertEqual("Prima Nota di Prova (Fatt. n.1 del 01/01/2024)",modificato)
        self.find(By.XPATH, '//i[@class="deleteicon fa fa-times"]').click()
        sleep(2)

        #verifica elemento eliminato
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Causale"]/input'))).send_keys("Prima nota da Eliminare", Keys.ENTER)
        sleep(1)
        
        eliminato=self.driver.find_element(By.XPATH,'//tbody//tr[1]//td[@class="dataTables_empty"]').text
        self.assertEqual("La ricerca non ha portato alcun risultato.",eliminato)

