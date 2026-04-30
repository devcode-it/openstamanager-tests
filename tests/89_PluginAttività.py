from common.Test import Test, get_html
from common.RowManager import RowManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Attivita(Test):
    def setUp(self):
        super().setUp()

    def test_plugin_attivita(self):      
        #TODO: Mostra su mappa
        #self.mostra_su_mappa()
        #TODO: Impianti
        #self.impianti()
        self.test()