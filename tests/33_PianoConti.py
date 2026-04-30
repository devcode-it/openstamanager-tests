from common.Test import Test
from selenium.webdriver.common.by import By

class PrimaNota(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Contabilità")

    def test_creazione_prima_nota(self):
        self.navigateTo("Piano dei conti")
        self.wait_loader()
        ##TODO: test piano dei conti