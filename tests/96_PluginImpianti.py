from common.Test import Test, get_html
from common.RowManager import RowManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Impianti(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Impianti")

    def test_plugin_impianti(self):
        #TODO: Componenti
        self.componenti()
        self.wait_for_element_and_click('//i[@class="fa fa-power-off nav-icon"]')