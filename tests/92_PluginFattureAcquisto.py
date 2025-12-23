from common.Test import Test
from common.RowManager import RowManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class FattureAcquisto(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Acquisti")

    def test_plugin_fattura_acquisto(self):
        self.movimenti_contabili()
        #TODO: fatturazione elettronica
        #self.fatturazione_elettronica()
        self.registrazioni()

    def movimenti_contabili(self):
        self.navigateTo("Fatture di acquisto")
        self.click_first_result()

        self.wait_for_element_and_click('//a[@id="link-tab_36"]')
        self.wait_for_element_and_click('//a[@class="btn btn-info btn-lg"]')

        avere = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_36"]//tr//td[4]'))
        ).text
        self.assertEqual(avere, "264,80 €")

    def registrazioni(self):
        self.navigateTo("Fatture di acquisto")
        self.click_first_result()

        self.wait_for_element_and_click('//a[@id="link-tab_41"]')
        self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_41"]//tr[5]//td[1]')))

 