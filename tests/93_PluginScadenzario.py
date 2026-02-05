from common.Test import Test
from common.RowManager import RowManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Scadenzario(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Acquisti")

    def test_plugin_scadenzario(self):
        #TODO: presentazioni bancarie
        self.presentazioni_bancarie()
        self.wait_for_element_and_click('//i[@class="fa fa-power-off nav-icon"]')