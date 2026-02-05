from common.Test import Test
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class PrimaNota(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Strumenti")
        self.expandSidebar("Gestione accessi")

    def test_creazione_prima_nota(self):
        self.navigateTo("Accesso con OAuth")
        self.wait_loader()
        ##TODO: test accesso con oauth
        self.wait_for_element_and_click('//i[@class="fa fa-power-off nav-icon"]')