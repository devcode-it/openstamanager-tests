from common.Test import Test, get_html
from common.RowManager import RowManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class OrdiniFornitore(Test):
    def setUp(self):
        super().setUp()

        self.expandSidebar("Acquisti")
        self.navigateTo("Ordini fornitore")

    def test_creazione_ordine_fornitore(self):
        ''' Crea una nuovo ordine fornitore per il fornitore "Fornitore". '''
        importi = RowManager.list()
        self.creazione_ordine_fornitore("Fornitore", importi[0])

    def creazione_ordine_fornitore(self, fornitore: str, file_importi: str):
        ''' Crea un nuovo ordine fornitore per il fornitore indicato. '''
        # Apre la schermata di nuovo elemento
        self.find(By.CSS_SELECTOR, '#tabs > li:first-child .btn-primary > .fa-plus').click()
        modal = self.wait_modal()

        select = self.input(modal, 'Fornitore')
        select.setByText(fornitore)

        # Submit
        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        self.wait_loader()

        #toast = self.driver.find_elements(By.CLASS_NAME, 'toast-message')
        #self.assertIn('Aggiunto ordine fornitore', toast)

        row_manager = RowManager(self)
        row_manager.compile(file_importi)
