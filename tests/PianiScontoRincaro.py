from common.Test import Test, get_html
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class PianiScontoRincaro(Test):
    def setUp(self):
        super().setUp()

        self.expandSidebar("Magazzino")
        self.navigateTo("Piani di sconto/rincaro")

    def test_creazione_piano_sconto_rincaro(self):
        # Crea un nuovo piano. 
        self.creazione_piano_sconto_rincaro("Piano di sconto 1", "10")

    def creazione_piano_sconto_rincaro(self, nome: str, sconto: str):
        # Crea un nuovo piano. 
        # Apre la schermata di nuovo elemento
        self.find(By.CSS_SELECTOR, '#tabs > li:first-child .btn-primary > .fa-plus').click()
        modal = self.wait_modal()

        self.input(modal, 'Nome').setValue(nome)
        self.input(modal, 'Sconto/rincaro').setValue(sconto)

        # Submit
        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        self.wait_loader()
        
        #toast = self.driver.find_elements(By.CLASS_NAME, 'toast-message')
        #self.assertIn('Aggiunto piano', toast)
    
        
        