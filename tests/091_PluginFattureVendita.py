from common.Test import Test
from common.RowManager import RowManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class FattureVendita(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Vendite")

    def test_plugin_fattura_vendita(self):
        self.movimenti_contabili()
        self.contabilizzazione()
        
    def movimenti_contabili(self):
        self.navigate_to_and_wait("Fatture di vendita")

        self.search_by_th("th_Tipo", "Fattura immediata di vendita", wait_modal=False)

        self.click_first_table_row()
        self.wait_for_element_and_click('//a[@id="link-tab_37"]')
        self.wait_for_element_and_click('//a[@class="btn btn-info btn-lg"]')

        dare_1 = self.driver.find_element(By.XPATH, '(//div[@id="tab_37"]//tbody//td)[3]').text
        avere_1 = self.driver.find_element(By.XPATH, '(//div[@id="tab_37"]//tbody//td)[9]').text
        avere_2 = self.driver.find_element(By.XPATH, '(//div[@id="tab_37"]//tbody//td)[14]').text

        self.assertEqual(dare_1, "323,06 €")
        self.assertEqual(avere_1, "264,80 €")
        self.assertEqual(avere_2, "58,26 €")

        self.navigate_to_and_wait("Fatture di vendita")
        self.clear_filters()

    def contabilizzazione(self):
        self.navigate_to_and_wait("Fatture di vendita")

        self.search_by_th("th_Tipo", "Fattura immediata di vendita", wait_modal=False)

        self.click_first_table_row()
        self.wait_for_element_and_click('//a[@id="link-tab_42"]')
        self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_42"]//tr[2]//td')))

        self.navigate_to_and_wait("Fatture di vendita")
        self.clear_filters()

