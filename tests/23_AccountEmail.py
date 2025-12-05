from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from common.Test import Test


class AccountEmail(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Gestione email")

    def test_creazione_accountemail(self):
        self.creazione_account_email(
            "Account di Prova da Eliminare",
            self.getConfig('tests.email_user'),
            self.getConfig('tests.email_user')
        )
        self.modifica_account_email(
            self.getConfig('tests.email_user'),
            "smtps.aruba.it",
            "465"
        )
        self.elimina_account_email()
        self.verifica_account_email()
        self.invia_mail()

    def creazione_account_email(self, nomeaccount=str, nomevisualizzato=str, emailmittente=str):
        self.navigateTo("Account email")
        self.wait_loader()
        self.wait_for_element_and_click('//i[@class="fa fa-plus"]')

        modal = self.wait_modal()
        self.input(modal, 'Nome account').setValue(nomeaccount)
        self.input(modal, 'Nome visualizzato').setValue(nomevisualizzato)
        self.input(modal, 'Email mittente').setValue(emailmittente)
        self.wait_for_element_and_click('button[type="submit"]', By.CSS_SELECTOR)

    def modifica_account_email(self, emailmittente: str, server: str, porta: str):
        self.navigateTo("Account email")
        self.wait_loader()

        search_input = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome-account"]/input'))
        )
        self.send_keys_and_wait(search_input, 'Account Email da Impostazioni', wait_modal=False)
        self.wait_for_element_and_click('//tbody//tr//td[2]')

        self.input(None, 'Username SMTP').setValue(emailmittente)
        self.input(None, 'Server SMTP').setValue(server)
        self.input(None, 'Porta SMTP').setValue(porta)
        self.wait_for_element_and_click('//div[@id="tab_0"]//button[@id="save"]')

        self.navigateTo("Account email")
        self.wait_loader()
        self.clear_filters()

    def elimina_account_email(self):
        self.navigateTo("Account email")
        self.wait_loader()

        search_input = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome-account"]/input'))
        )
        self.send_keys_and_wait(search_input, 'Account di Prova da Eliminare', wait_modal=False)
        self.wait_for_element_and_click('//tbody//tr//td[2]')
        self.wait_for_element_and_click('//div[@id="tab_0"]//a[@class="btn btn-danger ask"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')
        self.clear_filters()

    def verifica_account_email(self):
        self.navigateTo("Account email")
        self.wait_loader()

        search_input = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome-account"]/input'))
        )
        self.send_keys_and_wait(search_input, "Account email da Impostazioni", wait_modal=False)

        modificato = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//tbody//tr[1]//td[3]'))
        ).text
        self.assertEqual("Account email da Impostazioni", modificato)

        self.clear_filters()

        search_input = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome-account"]/input'))
        )
        self.send_keys_and_wait(search_input, "Account di Prova da Eliminare", wait_modal=False)

        eliminato = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//tbody//tr[1]//td[@class="dataTables_empty"]'))
        ).text
        self.assertEqual("La ricerca non ha portato alcun risultato.", eliminato)

        self.clear_filters()

    def invia_mail(self):
        self.navigateTo("Account email")
        self.wait_loader()

        search_input = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome-account"]/input'))
        )
        self.send_keys_and_wait(search_input, "Account email", wait_modal=False)
        self.wait_for_element_and_click('//tbody//tr//td[2]')
        self.wait_for_dropdown_and_select('//span[@id="select2-encryption-container"]', option_text='SSL')
        self.input(None, 'Password SMTP').setValue(self.getConfig('tests.email_password'))
        self.wait_for_element_and_click('//button[@id="save"]')

        self.navigateTo("Anagrafiche")
        self.wait_loader()

        search_input = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Ragione-sociale"]/input'))
        )
        self.send_keys_and_wait(search_input, "Cliente", wait_modal=False)
        self.wait_for_element_and_click('//tbody//tr//td[2]')
        self.input(None, 'Email').setValue(self.getConfig('tests.email_user'))
        self.wait_for_element_and_click('//button[@id="save"]')

        self.navigateTo("Attività")
        self.wait_loader()
        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_element_and_click('//button[@data-toggle="dropdown"]')
        self.wait_for_element_and_click('//a[@data-op="send_mail"]')
        self.wait_for_dropdown_and_select('//span[@id="select2-id_template-container"]', option_text='Rapportino intervento')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-warning"]')

        scritta = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//tbody//tr//td[14]'))
        ).text
        self.assertEqual(scritta, "Inviata via email")