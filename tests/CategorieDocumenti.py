from common.Test import Test, get_html
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class CategorieDocumenti(Test):
    def setUp(self):
        super().setUp()

        self.navigateTo("Gestione documentale")
        self.navigateTo("Categorie documenti")

    def test_creazione_categorie_documenti(self):

        # Crea una nuova categoria documenti.   
        self.add_categorie_documenti('Categoria di prova')

    def add_categorie_documenti(self, descrizione: str):
        # Crea una nuova  categoria documenti.   
        # Apre la schermata di nuovo elemento
        self.find(By.CSS_SELECTOR, '#tabs > li:first-child .btn-primary > .fa-plus').click()
        modal = self.wait_modal()

        # Completamento dei campi per il nuovo elemento
        self.input(modal, 'Descrizione').setValue(descrizione)
    

        # Submit
        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        self.wait_loader()
