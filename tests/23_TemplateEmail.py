from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from common.Test import Test


class TemplateEmail(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Gestione email")

    def test_creazione_template_email(self):
        self._add_template_email('Template di Prova da Modificare', 'Anagrafiche', '1')
        self._add_template_email('Template di Prova da Eliminare', 'Anagrafiche', '1')
        self._modifica_template("Template di Prova")
        self._elimina_template()
        self._verifica_template_email()

    def _add_template_email(self, nome: str, modulo: str, account: str):
        self.navigate_to_and_wait("Template email")
        self.click_add_button()
        modal = self.wait_modal()
        self.input(modal, 'Nome').setValue(nome)
        select = self.input(modal, 'Modulo del template')
        select.setByText(modulo)
        select = self.input(modal, 'Indirizzo email')
        select.setByIndex(account)
        self.wait_for_element_and_click('button[type="submit"]', By.CSS_SELECTOR)

    def _modifica_template(self, modifica: str):
        self.navigate_to_and_wait("Template email")
        self.search_by_th_and_click_first("th_Nome", 'Template di Prova da Modificare')
        self.input(None, 'Nome').setValue(modifica)
        self.click_save_button()
        self.navigate_to_and_wait("Template email")
        self.clear_filters()

    def _elimina_template(self):
        self.navigate_to_and_wait("Template email")
        self.search_by_th_and_click_first("th_Nome", 'Template di Prova da Eliminare')

        self.delete_current_and_clear()

    def _verifica_template_email(self):
        self.navigate_to_and_wait("Template email")
        self.search_by_th("th_Nome", "Template di Prova")
        modificato = self.get_table_text(1, 3)
        self.assertEqual("Template di Prova", modificato)
        self.clear_filters()

        self.verify_deleted_by_th("th_Nome", "Template di Prova da Eliminare")