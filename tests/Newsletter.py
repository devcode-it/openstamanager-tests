from common.Test import Test, get_html
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class Newsletter(Test):
    def setUp(self):
        super().setUp()

        self.navigateTo("Gestione email")
        self.navigateTo("Newsletter")

    def test_creazione_newsletter(self):

        # Crea una nuova newsletter.   
        self.add_newsletter('Template di prova', 'Ddt')

    def add_newsletter(self, nome: str, modulo: str):
        # Crea una nuova newsletter
        # Apre la schermata di nuovo elemento
        self.find(By.CSS_SELECTOR, '#tabs > li:first-child .btn-primary > .fa-plus').click()
        modal = self.wait_modal()

        # Completamento dei campi per il nuovo elemento
        self.input(modal, 'Nome').setValue(nome)

        select = self.input(modal, 'Template email')
        select.setByText(modulo)
    
        

        # Submit
        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        self.wait_loader()
