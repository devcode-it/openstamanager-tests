from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from common.Test import Test


class Newsletter(Test):
    def setUp(self):
        super().setUp()

    def test_creazione_newsletter(self):
        self.expandSidebar("Gestione email")
        self._add_newsletter('Newsletter di Prova da Modificare', "Contratto")
        self._add_newsletter('Newsletter di Prova da Eliminare', "Ddt")
        self._modifica_newsletter("Newsletter di Prova")
        self._elimina_newsletter()
        self._verifica_newsletter()

    def _add_newsletter(self, nome: str, modulo: str):
        self.navigate_to_and_wait("Newsletter")

        self.click_add_button()
        modal = self.wait_modal()

        select = self.input(modal, 'Template email')
        select.setByText(modulo)
        self.input(modal, 'Nome').setValue(nome)
        self.wait_for_element_and_click('button[type="submit"]', By.CSS_SELECTOR)

    def _modifica_newsletter(self, modifica: str):
        self.navigate_to_and_wait("Newsletter")

        self.search_by_th_and_click_first("th_Nome", 'Newsletter di Prova da Modificare')

        self.input(None, 'Nome').setValue(modifica)
        self.click_save_button()

        self.navigate_to_and_wait("Newsletter")
        self.clear_filters()

    def _elimina_newsletter(self):
        self.search_by_th_and_click_first("th_Nome", 'Newsletter di Prova da Eliminare')

        self.delete_current_and_clear()

    def _verifica_newsletter(self):
        self.search_by_th("th_Nome", "Newsletter di Prova")
        modificato = self.get_table_text(1, 2)
        self.assertEqual("Newsletter di Prova", modificato)
        self.clear_filters()

        self.verify_deleted_by_th("th_Nome", "Newsletter di Prova da Eliminare")