from common.Test import Test
from selenium.webdriver.common.by import By

class Cespiti(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Contabilità")

    def test_creazione_cespiti(self):
        self.navigate_to_and_wait("Cespiti")
        ##TODO: test ammortamenti cespiti
