from common.Test import Test
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Dashboard(Test):
    def setUp(self):
        super().setUp()

    def test_Dashboard(self):
        self.navigateTo("Dashboard")
        self.wait_loader()

        actions = webdriver.common.action_chains.ActionChains(self.driver)
        calendar = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="calendar"]'))
        )
        actions.move_to_element(calendar).move_by_offset(300, 100).click().perform()
        modal = self.wait_modal()

        self.input(modal, 'Cliente').setByText("Cliente")
        self.input(modal, 'Tipo').setByIndex("1")
        expected_text = "Int. 1 Cliente\nStefano Bianchi"

        self.wait_for_element_and_click('//a[@id="tecnici-sessioni-tab"]')
        self.wait_for_element_and_click('(//div[@id="tab_tecnici_sessioni"]//i[@class="fa fa-plus"])[2]')
        modal = self.wait_modal()

        tecnico = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="ragione_sociale_add"]')))
        self.send_keys_and_wait(tecnico, "Stefano Bianchi")

        description_field = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '(//iframe[@class="cke_wysiwyg_frame cke_reset"])[1]')))
        description_field.click()
        self.send_keys_and_wait(description_field, "Test", wait_modal=False)

        self.wait_for_element_and_click('//div[@class="col-md-12 text-right"]//button[@type="button"]')

        self.navigateTo("Dashboard")
        self.wait_loader()

        self.wait_for_element_and_click('//div[@class="tab-content"]//div[@class="row"]//div[@id="dashboard_tecnici"]//button[@type="button"]')
        self.wait_for_element_and_click('//div[@id="dashboard_tecnici"]//button[@class="btn btn-primary btn-sm seleziona_tutto"]')

        activity_text = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="fc-event-main"]'))).text
        self.assertEqual(activity_text, expected_text)

        self.verifica_attività()
        self.wait_for_element_and_click('//i[@class="fa fa-power-off nav-icon"]')

    def verifica_attività(self):
        self.navigateTo("Attività")
        self.wait_loader()

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input')))
        self.send_keys_and_wait(search_input, "1", wait_modal=False)

        technician_name = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//tbody//tr[1]//td[12]'))).text
        self.assertEqual("Stefano Bianchi", technician_name)

        self.navigateTo("Attività")
        self.wait_loader()

        self.wait_for_element_and_click('//tbody//tr//td[2]')
        self.wait_for_element_and_click('//div[@id="tab_0"]//a[@class="btn btn-danger ask"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')

        self.navigateTo("Attività")
        self.wait_loader()

        empty_message = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//tbody//tr[1]//td[@class="dataTables_empty"]'))).text
        self.assertEqual("Nessun dato presente nella tabella", empty_message)
