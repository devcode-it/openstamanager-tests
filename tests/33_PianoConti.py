from common.Test import Test
from selenium.webdriver.common.by import By

class PrimaNota(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Contabilità")

    def test_creazione_prima_nota(self):
        self.navigate_to_and_wait("Piano dei conti")
        ##TODO: test piano dei conti