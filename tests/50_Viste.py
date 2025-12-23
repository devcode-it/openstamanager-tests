from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from common.Test import Test
from common.functions import TestHelperMixin


class Viste(Test, TestHelperMixin):
    def setUp(self):
        super().setUp()

    def test_viste(self):
        self.navigateTo("Anagrafiche")
        self.wait_loader()
        self.controllo_viste("Admin spa")

        self.navigateTo("Attività")
        self.wait_loader()
        self.controllo_viste("3")

        self.expandSidebar("Vendite")

        self.navigateTo("Preventivi")
        self.wait_loader()
        self.controllo_viste("1")

        self.navigateTo("Contratti")
        self.wait_loader()
        self.controllo_viste("1")

        self.navigateTo("Ordini cliente")
        self.wait_loader()
        self.controllo_viste("01")

        self.navigateTo("Fatture di vendita")
        self.wait_loader()
        self.controllo_viste("0002/2025")

        self.expandSidebar("Acquisti")
        self.navigateTo("Ordini fornitore")
        self.wait_loader()
        self.controllo_viste("1")

        self.navigateTo("Fatture di acquisto")
        self.wait_loader()
        self.controllo_viste("02")

        self.expandSidebar("Contabilità")
        self.navigateTo("Scadenzario")
        self.wait_loader()
        self.controllo_viste("Integrazione/autofattura per acquisto servizi dall'estero numero 0001")

        self.expandSidebar("Magazzino")
        self.navigateTo("Articoli")
        self.wait_loader()
        self.controllo_viste("Articolo 1")

        self.navigateTo("Movimenti")
        self.wait_loader()
        self.controllo_viste("001 - Articolo 1")

        self.navigateTo("Ddt in uscita")
        self.wait_loader()
        self.controllo_viste("02")

        self.navigateTo("Ddt in entrata")
        self.wait_loader()
        self.controllo_viste("2")

    def controllo_viste(self, test: str):
        self.wait_for_search_results()
        verifica = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//tbody//tr[1]//td[2]'))
        ).text
        self.assertEqual(verifica, test)

