from common.Test import Test, get_html
from common.RowManager import RowManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class OrdiniCliente(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Vendite")

    def test_plugin_ordine_cliente(self):
        self.consuntivi()


    def consuntivi(self):
        self.navigate_to_and_wait("Ordini cliente")

        self.click_first_table_row()
        self.wait_for_element_and_click('//a[@id="link-tab_29"]')
        budget = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="card-body text-center bg-success text-white"]'))
        ).text
        self.assertEqual(budget, "Rapporto budget/spesa:\n264,80 €")