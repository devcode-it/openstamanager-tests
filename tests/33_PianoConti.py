from common.Test import Test
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class PrimaNota(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Contabilità")

    def test_creazione_prima_nota(self):
        self.navigateTo("Piano dei conti")
        self.wait_loader()
        ##TODO: test piano dei conti
        self.wait_for_element_and_click('//i[@class="fa fa-power-off nav-icon"]')