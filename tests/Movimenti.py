from common.Test import Test, get_html
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class Movimenti(Test):
    def setUp(self):
        super().setUp()

        self.expandSidebar("Magazzino")
        self.navigateTo("Movimenti")

    def test_creazione_movimento(self):
        # Crea un nuovo movimento. 
        self.creazione_movimento("10", "Articolo")

    def creazione_movimento(self, qta: str, articolo: str):
        # Crea un nuovo movimento. 
        # Apre la schermata di nuovo elemento
        self.find(By.CSS_SELECTOR, '#tabs > li:first-child .btn-primary > .fa-plus').click()
        modal = self.wait_modal()

        self.input(modal, 'Articolo').setByText(articolo)
        self.input(modal, 'Quantità').setValue(qta)

        # Submit
        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        self.wait_loader()
        
        #toast = self.driver.find_elements(By.CLASS_NAME, 'toast-message')
        #self.assertIn('Aggiunto movimento', toast)
    
        
        