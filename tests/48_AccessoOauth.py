from common.Test import Test
from selenium.webdriver.common.by import By

class PrimaNota(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Strumenti")
        self.expandSidebar("Gestione accessi")

    def test_creazione_prima_nota(self):
        self.navigateTo("Accesso con OAuth")
        self.wait_loader()
        ##TODO: test accesso con oauth
