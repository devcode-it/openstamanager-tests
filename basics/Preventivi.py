from common.Test import Test, get_html
from common.RowManager import RowManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class Preventivi(Test):
    def setUp(self):
        super().setUp()

        self.expandSidebar("Vendite")
        self.navigateTo("Preventivi")

    def test_creazione_preventivo(self):
        ''' Crea una nuovo preventivo per il cliente "Cliente". '''
        importi = RowManager.list()
        self.creazione_preventivo("Cliente", importi[0])

    def creazione_preventivo(self, cliente: str, file_importi: str):
        ''' Crea una nuovo preventivo per il cliente indicato. '''
        # Apre la schermata di nuovo elemento
        self.find(By.CSS_SELECTOR, '#tabs > li:first-child .btn-primary > .fa-plus').click()
        modal = self.wait_modal()

        # Completamento dei campi per il nuovo elemento
        self.input(modal, 'Nome').setValue('Preventivo di test')

        select = self.input(modal, 'Cliente')
        select.setByText(cliente)

        select = self.input(modal, 'Tipo di Attività')
        select.setByIndex("1")

        # Submit
        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        self.wait_loader()

        #toast = self.driver.find_elements(By.CLASS_NAME, 'toast-message')
        #self.assertIn('Aggiunto preventivo', toast)

        row_manager = RowManager(self)
        row_manager.compile(file_importi)
