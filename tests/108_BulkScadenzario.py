from common.Test import Test
from common.RowManager import RowManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
class Scadenzario(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Acquisti")

    def test_bulk_scadenzario(self):
        #TODO: aggiorna banca
        #self.aggiorna_banca()
        #TODO: info distinta
        #self.info_distinta()
        #TODO: invia mail sollecito
        #self.invia_mail_sollecito()
        #TODO: registrazione contabile
        self.registrazione_contabile()
        self.wait_for_element_and_click('//i[@class="fa fa-power-off nav-icon"]')