from common.Test import Test, get_html
from common.RowManager import RowManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


class PrimaNota(Test):
    def setUp(self):
        super().setUp()

        self.expandSidebar("Contabilità")
        self.navigateTo("Prima nota")

    def test_creazione_primanota(self):
        self.creazione_primanota(modelloprimanota="Anticipo fattura")

    def creazione_primanota(self, modelloprimanota= str):

        self.find(By.CSS_SELECTOR, '#tabs > li:first-child .btn-primary > .fa-plus').click()
        modal = self.wait_modal()

        select = self.input(modal, 'Modello prima nota')
        select.setByText(modelloprimanota)
        modal = self.wait_modal()


        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        self.wait_loader()
    

