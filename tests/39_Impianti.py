from common.Test import Test, get_html
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class Impianti(Test):
    def setUp(self):
        super().setUp()

        self.navigateTo("Impianti")

    def test_creazione_impianto(self):

        # Crea un nuovo impianto.   
        self.add_impianto('01', 'Impianto di prova', 'Cliente')

    def add_impianto(self, nome: str, matricola: str, cliente: str):
        # Crea un nuovo impianto
        # Apre la schermata di nuovo elemento
        self.find(By.CSS_SELECTOR, '#tabs > li:first-child .btn-primary > .fa-plus').click()
        modal = self.wait_modal()

        # Completamento dei campi per il nuovo elemento
        self.input(modal, 'Matricola').setValue(matricola)

        self.input(modal, 'Nome').setValue(nome)

        select = self.input(modal, 'Cliente')
        select.setByText(cliente)

        # Submit
        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        self.wait_loader()
