from common.Test import Test, get_html
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class FasceOrarie(Test):
    def setUp(self):
        super().setUp()

        self.navigateTo("Attività")
        self.navigateTo("Fasce orarie")

    def test_creazione_fasceorarie(self):
        self.creazione_fasceorarie(nome= "Prova Fascia Oraria")

    def creazione_fasceorarie(self,nome = str):

        self.find(By.CSS_SELECTOR, '#tabs > li:first-child .btn-primary > .fa-plus').click()
        modal = self.wait_modal()

        self.input(modal, 'Nome').setValue(nome)
        
        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        self.wait_loader()
