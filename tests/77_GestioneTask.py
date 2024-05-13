from common.Test import Test, get_html
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class GestioneTask (Test):
    def setUp(self):
        super().setUp()

        self.expandSidebar("Strumenti")

    def test_creazione_task(self):
        # Modifica Task
        self.modifica_task("Backup")
                
        # Verifica Task
        self.verifica_task()

    def modifica_task(self, modifica=str):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Gestione task")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))).send_keys('Backup automatico', Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//div[@id="tab_0"]//tbody//td[2]//div[1]').click()
        sleep(1)          

        self.driver.execute_script('window.scrollTo(0,0)')
        self.input(None,'Nome').setValue(modifica)
        self.find(By.XPATH, '//div[@id="tab_0"]//a[@id="save"]').click()
        self.wait_loader()

        self.navigateTo("Gestione task")
        self.wait_loader()    

        self.find(By.XPATH, '//th[@id="th_Nome"]/i[@class="deleteicon fa fa-times fa-2x"]').click()

    
    def verifica_task(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Gestione task")
        self.wait_loader()    

        #verifica elemento modificato
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))).send_keys("Backup", Keys.ENTER)
        sleep(1)

        modificato=self.driver.find_element(By.XPATH,'//tbody//tr[1]//td[2]').text
        self.assertEqual("Backup",modificato)
        self.find(By.XPATH, '//i[@class="deleteicon fa fa-times fa-2x"]').click()
