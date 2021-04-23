from common.Test import Test, get_html
from common.RowManager import RowManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class DdtEntrata(Test):
    def setUp(self):
        super().setUp()

        self.expandSidebar("Magazzino")
        self.navigateTo("Ddt in entrata")

    def test_creazione_ddt_entrata(self):
        # Crea un nuovo ddt dal fornitore "Fornitore".
        importi = RowManager.list()
        self.creazione_ddt_entrata("Fornitore", "1", importi[0])

    def creazione_ddt_entrata(self, fornitore: str, causale: str, file_importi: str):
        # Crea un nuovo ddt del fornitore indicato.
        # Apre la schermata di nuovo elemento
        self.find(By.CSS_SELECTOR, '#tabs > li:first-child .btn-primary > .fa-plus').click()
        modal = self.wait_modal()

        select = self.input(modal, 'Mittente')
        select.setByText(fornitore)

        select = self.input(modal, 'Causale trasporto')
        select.setByIndex(causale)

        # Submit
        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        self.wait_loader()

        #toast = self.driver.find_elements(By.CLASS_NAME, 'toast-message')
        #self.assertIn('Aggiunto ddt', toast)

        row_manager = RowManager(self)
        row_manager.compile(file_importi)
