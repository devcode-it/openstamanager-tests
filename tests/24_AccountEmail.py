from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from common.Test import Test


class AccountEmail(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Gestione email")

    def test_creazione_accountemail(self):
        self._creazione_account_email(
            "Account di Prova da Eliminare",
            self.getConfig('tests.email_user'),
            self.getConfig('tests.email_user')
        )
        self._modifica_account_email(
            self.getConfig('tests.email_user'),
            "smtps.aruba.it",
            "465"
        )
        self._elimina_account_email()
        self._verifica_account_email()
        self._invia_mail()

    def _creazione_account_email(self, nomeaccount=str, nomevisualizzato=str, emailmittente=str):
        self.navigate_to_and_wait("Account email")
        self.click_add_button()

        modal = self.wait_modal()
        self.input(modal, 'Nome account').setValue(nomeaccount)
        self.input(modal, 'Nome visualizzato').setValue(nomevisualizzato)
        self.input(modal, 'Email mittente').setValue(emailmittente)
        self.wait_for_element_and_click('button[type="submit"]', By.CSS_SELECTOR)

    def _modifica_account_email(self, emailmittente: str, server: str, porta: str):
        self.navigate_to_and_wait("Account email")

        self.search_by_th("th_Nome-account", 'Account Email da Impostazioni')
        self.click_first_table_row()

        self.input(None, 'Username SMTP').setValue(emailmittente)
        self.input(None, 'Server SMTP').setValue(server)
        self.input(None, 'Porta SMTP').setValue(porta)
        self.click_save_button()

        self.navigate_to_and_wait("Account email")
        self.clear_filters()

    def _elimina_account_email(self):
        self.navigate_to_and_wait("Account email")

        self.search_by_th_and_click_first("th_Nome-account", 'Account di Prova da Eliminare')

        self.delete_current_and_clear()

    def _verifica_account_email(self):
        self.navigate_to_and_wait("Account email")

        self.search_by_th("th_Nome-account", "Account email da Impostazioni")

        modificato = self.get_table_text(1, 3)
        self.assertEqual("Account email da Impostazioni", modificato)

        self.clear_filters()

        self.verify_deleted_by_th("th_Nome-account", "Account di Prova da Eliminare")

    def _invia_mail(self):
        self.navigate_to_and_wait("Account email")

        self.search_by_th_and_click_first("th_Nome-account", "Account email")

        self.wait_for_dropdown_and_select('//span[@id="select2-encryption-container"]', option_text='SSL')
        self.input(None, 'Password SMTP').setValue(self.getConfig('tests.email_password'))
        self.wait_for_element_and_click('//button[@id="save"]')

        self.navigate_to_and_wait("Anagrafiche")

        search_input = self.find(By.XPATH, '//th[@id="th_Ragione-sociale"]/input')
        self.send_keys_and_wait(search_input, "Cliente", wait_modal=False)
        self.click_first_table_row()
        self.input(None, 'Email').setValue(self.getConfig('tests.email_user'))
        self.wait_for_element_and_click('//button[@id="save"]')

        self.navigate_to_and_wait("Attività")
        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_element_and_click('//button[@data-toggle="dropdown"]')
        self.wait_for_element_and_click('//a[@data-op="send_mail"]')
        self.wait_for_dropdown_and_select('//span[@id="select2-id_template-container"]', option_text='Rapportino intervento')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-success"]')

        scritta = self.find(By.XPATH, '//tbody//tr//td[14]').text
        self.assertEqual(scritta, "Inviata via email")