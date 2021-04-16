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
        ''' Crea un nuovo articolo. '''
        # Apre la schermata di nuovo elemento
        self.find(By.CSS_SELECTOR, '#tabs > li:first-child .btn-primary > .fa-plus').click()
        modal = self.wait_modal()

        self.input(modal, 'Codice').setValue(codice)
        self.input(modal, 'Descrizione').setValue(descrizione)

        # Submit
        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        self.wait_loader()
        
        #toast = self.driver.find_elements(By.CLASS_NAME, 'toast-message')
        #self.assertIn('Aggiunto articolo', toast)

        check = self.input(self.find(By.XPATH, '//input[@id="qta_manuale"]'), 'Modifica quantità')
        self.driver.execute_script("arguments[0].click();", check)

        self.input(By.XPATH, '//input[@id ="qta"]').setValue(qta)

        self.find(By.XPATH, '//a[@id ="save"]').click()

    
        
        