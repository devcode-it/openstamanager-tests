from common.Test import Test, get_html
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class Articoli(Test):
    def setUp(self):
        super().setUp()

        self.expandSidebar("Magazzino")
        self.navigateTo("Articoli")

    def test_creazione_articolo(self):
        ''' Crea un nuovo articolo. '''
        self.creazione_articolo("01", "Articolo")

    def creazione_articolo(self, codice: str, descrizione: str):
        ''' '''
        ''' 1/2 Crea un nuovo articolo. '''
        ''' '''
        # Apre la schermata di nuovo elemento
        self.find(By.CSS_SELECTOR, '#tabs > li:first-child .btn-primary > .fa-plus').click()
        modal = self.wait_modal()

        self.input(modal, 'Codice').setValue(codice)
        self.input(modal, 'Descrizione').setValue(descrizione)

        # Submit
        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        self.wait_loader()
       


        ''' '''
        ''' 2/2 Modifica articolo. '''
        ''' '''
        self.input(self.find(By.XPATH, '//div[@id="tab_0"]'), 'Modifica quantità').clickFlag()

        ''' Q.tà '''
        self.input(self.find(By.XPATH, '//div[@id="tab_0"]'), 'Quantità').setValue("1")

        ''' Causale movimento '''
        self.input(self.find(By.XPATH, '//div[@id="tab_0"]'), 'Descrizione movimento').setValue("Movimento di test")

        ''' Salvataggio '''
        self.find(By.XPATH, '//div[@id="tab_0"]//a[@id="save"]').click()
