from common.Test import Test
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Dashboard(Test):
    def setUp(self):
        super().setUp()
        self.wait_driver = WebDriverWait(self.driver, 20)
      
    def test_Dashboard(self):
        try:
            self.navigateTo("Dashboard")
            self.wait_loader() 

            actions = webdriver.common.action_chains.ActionChains(self.driver)
            calendar = self.driver.find_element(By.XPATH,'//div[@id="calendar"]')
            actions.move_to_element(calendar).move_by_offset(300,100).click().perform()
            modal = self.wait_modal()

            self.input(modal, 'Cliente').setByText("Cliente")
            self.input(modal, 'Tipo').setByIndex("1")
            expected_text = "Int. 1 Cliente\nTecnici: Stefano Bianchi"
            
            add_button = self.driver.find_element(By.XPATH,'//div[@class="card card-info collapsable "]//span[@class="input-group-text after no-padding"]//i[@class="fa fa-plus"]')
            add_button.click()
            time.sleep(1)

            technician_modal = self.driver.find_element(By.XPATH,'//div[@class="modal-dialog modal-lg"]')
            self.input(technician_modal, 'Denominazione').setValue("Stefano Bianchi")
            submit_button = modal.find_element(By.XPATH, '//div[@class="col-md-12 text-right"]//button[@type="submit"]')
            submit_button.click()
            time.sleep(1)

            description_field = self.find(By.XPATH, '(//iframe[@class="cke_wysiwyg_frame cke_reset"])[1]')
            description_field.click()  
            self.wait_driver.until(EC.visibility_of_element_located(
                (By.XPATH, '(//iframe[@class="cke_wysiwyg_frame cke_reset"])[1]')
            )).send_keys("Test")
            
            save_button = self.find(By.XPATH, '//div[@class="col-md-12 text-right"]//button[@type="button"]')
            save_button.click()
            time.sleep(1)

            self.navigateTo("Dashboard")
            self.wait_loader()

            filter_button = self.find(By.XPATH, '//div[@class="tab-content"]//div[@class="row"]//div[@id="dashboard_tecnici"]//button[@type="button"]')
            filter_button.click()
            self.wait_loader()
            
            select_all_button = self.find(By.XPATH, '//div[@id="dashboard_tecnici"]//button[@class="btn btn-primary btn-sm seleziona_tutto"]')
            select_all_button.click()
            time.sleep(1)

            activity_text = self.find(By.XPATH, '//div[@class="fc-event-main"]').text
            self.assertEqual(activity_text, expected_text)

            self.verifica_attività()
        except Exception as e:
            self.driver.save_screenshot("dashboard_test_error.png")
            raise Exception(f"Dashboard test failed: {str(e)}")

    def verifica_attività(self):
        try:
            self.navigateTo("Attività")
            self.wait_loader()    

            search_input = self.wait_driver.until(EC.visibility_of_element_located(
                (By.XPATH, '//th[@id="th_Numero"]/input')
            ))
            search_input.send_keys("1", Keys.ENTER)
            time.sleep(1)
            
            technician_name = self.driver.find_element(By.XPATH,'//tbody//tr[1]//td[12]').text
            self.assertEqual("Stefano Bianchi", technician_name)

            self.navigateTo("Attività")
            self.wait_loader()  

            activity_row = self.find(By.XPATH, '//tbody//tr//td[2]')
            activity_row.click()
            time.sleep(1)

            delete_button = self.wait_driver.until(EC.visibility_of_element_located(
                (By.XPATH, '//div[@id="tab_0"]//a[@class="btn btn-danger ask"]')
            ))
            delete_button.click()
            
            confirm_button = self.wait_driver.until(EC.visibility_of_element_located(
                (By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]')
            ))
            confirm_button.click()
            self.wait_loader()
            
            self.navigateTo("Attività")
            self.wait_loader()  
            
            empty_message = self.driver.find_element(By.XPATH,'//tbody//tr[1]//td[@class="dataTables_empty"]').text
            self.assertEqual("Nessun dato presente nella tabella", empty_message)
        except Exception as e:
            self.driver.save_screenshot("verify_activity_error.png")
            raise Exception(f"Activity verification failed: {str(e)}")
