from common.Test import Test, get_html
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class CategorieImpianti(Test):
    def setUp(self):
        super().setUp()

        self.navigateTo("Impianti")
        self.navigateTo("Categorie impianti")

    def test_creazione_categorieimpianti(self):
        self.creazione_categorieimpianti(nome= "Prova1", colore="#9d2929", nota= "Prova")

    def creazione_categorieimpianti(self, nome=str, colore=str, nota=str):

        self.find(By.CSS_SELECTOR, '#tabs > li:first-child .btn-primary > .fa-plus').click()
        modal = self.wait_modal()

        self.input(modal, 'Colore').setValue(colore)
        self.input(modal, 'Nome').setValue(nome)
        self.input(modal, 'Nota').setValue(nota)

        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        self.wait_loader()