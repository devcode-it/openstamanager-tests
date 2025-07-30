from common.Test import Test, get_html
from selenium.webdriver.common.keys import Keys
from common.RowManager import RowManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

class Attivita_Dashboard(Test):
    def setUp(self):
        super().setUp()

    def test_attivita_dashboard(self):
        self.navigateTo("Dashboard")
        self.wait_loader()

        actions = webdriver.common.action_chains.ActionChains(self.driver)
        attivita = self.find(By.XPATH, '//div[@class="fc-event fc-event-primary"]')
        actions.drag_and_drop_by_offset(attivita, -1000, 0).perform()

        self.wait_for_element_and_click('(//span[@class="select2-selection select2-selection--multiple"])[4]')
        self.wait_for_element_and_click('//li[@class="select2-results__option select2-results__option--highlighted"]')
        self.wait_for_element_and_click('//div[@class="modal-content"]//button[@onclick="salva(this)"]')

        self.navigateTo("Dashboard")
        self.wait_loader()

        self.wait_for_element_and_click('//button[@class="btn btn-block counter_object btn-danger"]')
        self.wait_for_element_and_click('//input[@class="dashboard_tecnico"]')

        att = "Int. 2 Cliente\nTecnici: Stefano Bianchi"
        trova = self.find(By.XPATH, '//div[@class="fc-event-main"]').text
        self.assertEqual(trova, att)