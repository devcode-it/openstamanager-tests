from common.Test import Test, get_html
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class PrimaNota(Test):
    def setUp(self):
        super().setUp()

        self.expandSidebar("Contabilità")
        self.navigateTo("Prima nota")

    def test_creazione_prima_nota(self):
        # Crea un nuovo movimento di prima nota. 
        self.creazione_prima_nota("Pag. 1", "10")

    def creazione_prima_nota(self, causale: str, sconto: str):
        # Crea un nuovo movimento di prima nota. 
        # Apre la schermata di nuovo elemento
        self.find(By.CSS_SELECTOR, '#tabs > li:first-child .btn-primary > .fa-plus').click()
        modal = self.wait_modal()

        self.input(modal, 'Causale').setValue(causale)

        self.driver.find_element(By.XPATH, '//div[@class="modal-content"]//select[@id="conto0"]').click()

        # Submit
        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        self.wait_loader()

        
        
        #toast = self.driver.find_elements(By.CLASS_NAME, 'toast-message')
        #self.assertIn('Aggiunto movimento', toast)
    
        
        