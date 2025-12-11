from common.Test import Test
from common.RowManager import RowManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class Scadenzario(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Acquisti")

    def test_plugin_scadenzario(self):
        #TODO: presentazioni bancarie
        self.presentazioni_bancarie()