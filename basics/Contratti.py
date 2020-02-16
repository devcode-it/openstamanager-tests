from common.Test import Test, get_html, get_input
from common.RowManager import RowManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class Anagrafiche(Test):
    def setUp(self):
        super().setUp()

        self.expandSidebar("Vendite")
        self.navigateTo("Contratti")

    def test_creazione_contratto(self):
        ''' Crea una nuovo contratto per il cliente "Cliente". '''
        # Apre la schermata di nuovo elemento
        self.find(By.CSS_SELECTOR, '.btn-primary > .fa-plus').click()
        modal = self.wait_modal()

        # Completamento dei campi per il nuovo elemento
        get_input(modal, 'Nome').send_keys('Contratto di test')

        # Submit
        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        self.wait_loader()

        row_manager = RowManager(self)
        row_manager.compile('importi/base.json')
