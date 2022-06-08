from common.Test import Test, get_html
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

class Dashboard(Test):
      
    def test_Dashboard(self):
        self.navigateTo("Dashboard")
        
        actions = webdriver.common.action_chains.ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element(By.XPATH,'//div[@id="calendar"]')).move_by_offset(300,100).click().perform()
        modal = self.wait_modal()


        self.input(modal, 'Cliente').setByText("Cliente")
        self.input(modal, 'Tipo').setByIndex("1")
        self.input(modal, 'Stato').setByIndex("2")
        ora="8:30 - 9:30"
        
        self.driver.find_element(By.XPATH,'//div[@class="box box-info collapsable "]//span[@class="input-group-addon after no-padding"]//i[@class="fa fa-plus"]').click()
        sleep(1)

        self.input(self.driver.find_element(By.XPATH,'//div[@class="modal-dialog modal-lg"]'),'Denominazione').setValue("Mario Rossi")
        modal.find_element(By.XPATH, '//div[@class="col-md-12 text-right"]//button[@type="submit"]').click()
        sleep(1)
        modal.find_element(By.XPATH, '//div[@class="col-md-12 text-right"]//button[@type="button"]').click()

        self.navigateTo("Dashboard")
        self.wait_loader()

        self.find(By.XPATH, '//div[@class="tab-content"]//div[@class="row"]//div[@id="dashboard_tecnici"]//button[@type="button"]').click()
        self.wait_loader()
        self.find(By.XPATH, '//div[@id="dashboard_tecnici"]//button[@class="btn btn-primary btn-sm seleziona_tutto"]').click()
        sleep(2)

        trova=self.find(By.XPATH, '//div[@class="fc-content-col"]//div[@data-start="8:30"]').text
        self.assertEqual(trova,ora)