from common.Test import Test
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class Attivita_Dashboard(Test):
    def setUp(self):
        super().setUp()

    def test_attivita_dashboard(self):
        self.navigateTo("Dashboard")
        self.wait_loader()

        actions = ActionChains(self.driver)
        attivita = self.wait_for_element_and_click('//div[@class="fc-event fc-event-primary"]')
        actions.drag_and_drop_by_offset(attivita, -1000, 0).perform()
        modal = self.wait_modal()

        description_field = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '(//iframe[@class="cke_wysiwyg_frame cke_reset"])[1]')))
        description_field.click()
        self.send_keys_and_wait(description_field, "Test", wait_modal=False)

        self.wait_for_element_and_click('//a[@id="tecnici-sessioni-tab"]')
        self.wait_for_dropdown_and_select(
            '(//span[@class="select2-selection select2-selection--multiple"])[4]',
            option_text='Stefano Bianchi'
        )

        self.wait_for_element_and_click('//div[@class="modal-content"]//button[@onclick="salva(this)"]')

        self.navigateTo("Dashboard")
        self.wait_loader()

        self.wait_for_element_and_click('//button[@class="btn btn-block counter_object btn-danger"]')
        self.wait_for_element_and_click('//input[@class="dashboard_tecnico"]')

        att = "Int. 2 Cliente\nTecnici: Stefano Bianchi"
        trova_element = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="fc-event-main"]')))
        trova = trova_element.text
        self.assertEqual(trova, att)