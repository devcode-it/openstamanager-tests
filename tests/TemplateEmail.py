from common.Test import Test, get_html
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class TemplateEmail(Test):
    def setUp(self):
        super().setUp()

        self.navigateTo("Gestione email")
        self.navigateTo("Template email")

    def test_creazione_template_email(self):

        # Crea un nuovo template.   
        self.add_template_email('Template di prova', 'Anagrafiche', '1')

    def add_template_email(self, nome: str, modulo: str, account: str):
        # Crea un nuovo template
        # Apre la schermata di nuovo elemento
        self.find(By.CSS_SELECTOR, '#tabs > li:first-child .btn-primary > .fa-plus').click()
        modal = self.wait_modal()

        # Completamento dei campi per il nuovo elemento
        self.input(modal, 'Nome').setValue(nome)

        select = self.input(modal, 'Modulo del template')
        select.setByText(modulo)
    
        select = self.input(modal, 'Indirizzo email')
        select.setByIndex(account)

        # Submit
        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        self.wait_loader()
