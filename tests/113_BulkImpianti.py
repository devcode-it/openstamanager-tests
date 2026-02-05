from common.Test import Test, get_html
from common.RowManager import RowManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Impianti(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Impianti")

    def test_bulk_impianti(self):
        #TODO: aggiorna cliente
        #self.aggiorna_cliente()
        #TODO: elimina selezionati
        #self.elimina_selezionati()
        #TODO: esporta
        self.esporta_selezionati()
        self.wait_for_element_and_click('//i[@class="fa fa-power-off nav-icon"]')