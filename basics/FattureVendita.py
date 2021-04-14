from common.Test import Test, get_html
from common.RowManager import RowManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class FattureVendita(Test):
    def setUp(self):
        super().setUp()

        self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")

    def test_creazione_fattura_vendita(self):
        ''' Crea una nuova fattura per il cliente "Cliente". '''
        importi = RowManager.list()
        self.creazione_fattura_vendita("Cliente", importi[0])

    def creazione_fattura_vendita(self, cliente: str, file_importi: str):
        ''' Crea una nuova fattura per il cliente indicato. '''
        # Apre la schermata di nuovo elemento
        self.find(By.CSS_SELECTOR, '#tabs > li:first-child .btn-primary > .fa-plus').click()
        modal = self.wait_modal()

        select = self.input(modal, 'Cliente')
        select.setByText(cliente)

        # Submit
        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        self.wait_loader()

        #toast = self.driver.find_elements(By.CLASS_NAME, 'toast-message')
        #self.assertIn('Aggiunto fattura', toast)

        row_manager = RowManager(self)
        row_manager.compile(file_importi)
