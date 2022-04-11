from common.Test import Test, get_html
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class AccountEmail(Test):
    def setUp(self):
        super().setUp()

        self.expandSidebar("Gestione email")
        self.navigateTo("Account email")

    def test_creazione_accountemail(self):
        self.creazione_accountemail(nomeaccount= "Account Prova", nomevisualizzato="Mario Rossi", emailmittente="accountprova@prova.com")

    def creazione_accountemail(self, nomeaccount=str, nomevisualizzato=str, emailmittente=str):

        self.find(By.CSS_SELECTOR, '#tabs > li:first-child .btn-primary > .fa-plus').click()
        modal = self.wait_modal()

        self.input(modal, 'Nome account').setValue(nomeaccount)
        self.input(modal, 'Nome visualizzato').setValue(nomevisualizzato)
        self.input(modal, 'Email mittente').setValue(emailmittente)

        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        self.wait_loader()
