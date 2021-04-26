from common.Test import Test, get_html
from selenium.webdriver.common.keys import Keys
from common.RowManager import RowManager
from selenium.webdriver.common.by import By


class Interventi(Test):
    def setUp(self):
        super().setUp()

        self.navigateTo("Attività")

    def test_creazione_intervento(self):
        # Crea un nuovo intervento. 
        importi = RowManager.list()
        self.creazione_intervento("Cliente", "1", "1", "Intervento n.1")

    def creazione_intervento(self, cliente: str, tipo: str, stato: str, richiesta: str):
        # Crea un nuovo intervento. 
        # Apre la schermata di nuovo elemento
        self.find(By.CSS_SELECTOR, '#tabs > li:first-child .btn-primary > .fa-plus').click()
        modal = self.wait_modal()

        self.input(modal, 'Cliente').setByText(cliente)
        self.input(modal, 'Tipo').setByIndex(tipo)
        self.input(modal, 'Stato').setByIndex(stato)
        self.input(modal, 'Richiesta').setValue(richiesta)

        # Submit
        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        self.wait_loader()

        
        
        #toast = self.driver.find_elements(By.CLASS_NAME, 'toast-message')
        #self.assertIn('Aggiunto intervento', toast)
    
        row_manager = RowManager(self)
        row_manager.compile(file_importi)

        