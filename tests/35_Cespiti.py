from common.Test import Test
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Cespiti(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Contabilità")

    def test_creazione_cespiti(self):
        self.navigateTo("Cespiti")
        self.wait_loader()
        ##TODO: test ammortamenti cespiti
        self.wait_for_element_and_click('//i[@class="fa fa-power-off nav-icon"]')