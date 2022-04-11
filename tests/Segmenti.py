from common.Test import Test, get_html
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class Segmenti(Test):
    def setUp(self):
        super().setUp()

        self.expandSidebar("Strumenti")
        self.navigateTo("Segmenti")

    def test_creazione_segmenti(self):
        self.creazione_segmenti(nome= "Segmento di prova", maschera="1234/2022", modulo= "Articoli", note="Prova nota segmenti")

    def creazione_segmenti(self, nome=str, segmenti= str, maschera=str, modulo=str, note=str):

        self.find(By.CSS_SELECTOR, '#tabs > li:first-child .btn-primary > .fa-plus').click()
        modal = self.wait_modal()

        self.input(modal, 'Nome').setValue(nome)
        self.input(modal, 'Maschera').setValue(maschera)
        self.input(modal, 'Note').setValue(note)

        select = self.input(modal, 'Modulo')
        select.setByText(modulo)

        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        self.wait_loader()