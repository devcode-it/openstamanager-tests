from common.Test import Test, get_html
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Dashboard(Test):
      
    def test_Dashboard(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Dashboard")
        
        actions = webdriver.common.action_chains.ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element(By.XPATH,'//div[@id="calendar"]')).move_by_offset(300,100).click().perform()
        modal = self.wait_modal()

        self.input(modal, 'Cliente').setByText("Cliente")
        self.input(modal, 'Tipo').setByIndex("1")
        ora="Int. 1 Cliente\nTecnici: Stefano Bianchi"
        
        self.driver.find_element(By.XPATH,'//div[@class="box box-info collapsable "]//span[@class="input-group-addon after no-padding"]//i[@class="fa fa-plus"]').click()
        sleep(1)

        self.input(self.driver.find_element(By.XPATH,'//div[@class="modal-dialog modal-lg"]'),'Denominazione').setValue("Stefano Bianchi")
        modal.find_element(By.XPATH, '//div[@class="col-md-12 text-right"]//button[@type="submit"]').click()
        sleep(1)

        self.find(By.XPATH, '(//iframe[@class="cke_wysiwyg_frame cke_reset"])[1]').click()  
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//iframe[@class="cke_wysiwyg_frame cke_reset"])[1]'))).send_keys("Test")
        self.find(By.XPATH, '//div[@class="col-md-12 text-right"]//button[@type="button"]').click()
        sleep(1)

        self.navigateTo("Dashboard")
        self.wait_loader()

        self.find(By.XPATH, '//div[@class="tab-content"]//div[@class="row"]//div[@id="dashboard_tecnici"]//button[@type="button"]').click()
        self.wait_loader()
        self.find(By.XPATH, '//div[@id="dashboard_tecnici"]//button[@class="btn btn-primary btn-sm seleziona_tutto"]').click()
        sleep(1)

        trova=self.find(By.XPATH, '//div[@class="fc-event-main"]').text
        self.assertEqual(trova,ora)

        # Verifica Attività
        self.verifica_attività()

    def verifica_attività(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Attività")
        self.wait_loader()    

        #verifica elemento modificato
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input'))).send_keys("1", Keys.ENTER)
        sleep(1)
        
        modificato=self.driver.find_element(By.XPATH,'//tbody//tr[1]//td[10]').text
        self.assertEqual("Stefano Bianchi",modificato)

        #rimuovi elemento
        self.navigateTo("Attività")
        self.wait_loader()  

        self.find(By.XPATH, '//div[@id="tab_0"]//tbody//td[2]//div[1]').click()
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_0"]//a[@class="btn btn-danger ask"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))).click()
        self.wait_loader()
        
        #verifica elemento eliminato
        self.navigateTo("Attività")
        self.wait_loader()  
        
        eliminato=self.driver.find_element(By.XPATH,'//tbody//tr[1]//td[@class="dataTables_empty"]').text
        self.assertEqual("Nessun dato presente nella tabella", eliminato)