from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from common.Test import Test
from common.functions import TestHelperMixin


class Viste(Test, TestHelperMixin):
    def setUp(self):
        super().setUp()

    def test_viste(self):
        self.navigate_to_and_wait("Anagrafiche")
        self.controllo_viste("Admin spa")

        self.navigate_to_and_wait("Attività")
        self.controllo_viste("2")

        self.expandSidebar("Vendite")

        self.navigate_to_and_wait("Preventivi")
        self.controllo_viste("1")

        self.navigate_to_and_wait("Contratti")
        self.controllo_viste("1")

        self.navigate_to_and_wait("Ordini cliente")
        self.controllo_viste("01")

        self.navigate_to_and_wait("Fatture di vendita")
        self.controllo_viste("0002/2026")

        self.expandSidebar("Acquisti")
        self.navigate_to_and_wait("Ordini fornitore")
        self.controllo_viste("1")

        self.navigate_to_and_wait("Fatture di acquisto")
        self.controllo_viste("02")

        self.expandSidebar("Contabilità")
        self.navigate_to_and_wait("Scadenzario")
        self.controllo_viste("Integrazione/autofattura per acquisto servizi dall'estero numero 0001")

        self.expandSidebar("Magazzino")
        self.navigate_to_and_wait("Articoli")
        self.controllo_viste("Articolo 1")

        self.navigate_to_and_wait("Movimenti")
        self.controllo_viste("001 - Articolo 1")

        self.navigate_to_and_wait("Ddt in uscita")
        self.controllo_viste("02")

        self.navigate_to_and_wait("Ddt in entrata")
        self.controllo_viste("1")
        
    def controllo_viste(self, test: str):
        self.wait_for_search_results()
        verifica = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//tbody//tr[1]//td[2]'))
        ).text
        self.assertEqual(verifica, test)

