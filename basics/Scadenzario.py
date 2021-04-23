from common.Test import Test, get_html
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class Scadenzario(Test):
    def setUp(self):
        super().setUp()

        self.expandSidebar("Contabilità")
        self.navigateTo("Scadenzario")

    def test_creazione_scadenzario(self):
        # Crea una nuova scadenza. 
        self.creazione_scadenzario("Scadenze generiche", "10", "Scadenza n.1")

    def creazione_scadenzario(self, tipo: str, importo: str, descrizione: str):
        # Crea una nuova scadenza. 
        # Apre la schermata di nuovo elemento
        self.find(By.CSS_SELECTOR, '#tabs > li:first-child .btn-primary > .fa-plus').click()
        modal = self.wait_modal()

        self.input(modal, 'Tipo').setByText(tipo)
        self.input(modal, 'Importo').setValue(importo)
        self.input(modal, 'Descrizione').setValue(descrizione)

        # Submit
        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        self.wait_loader()

        
        
        #toast = self.driver.find_elements(By.CLASS_NAME, 'toast-message')
        #self.assertIn('Aggiunta scadenza', toast)
    
        
        