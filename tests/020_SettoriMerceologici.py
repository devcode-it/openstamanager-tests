from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from common.Test import Test


class SettoriMerceologici(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Anagrafiche")
        self.wait_loader()

    def test_creazione_settori_merceologici(self):
        self._creazione_settori_merceologici("Settore Merceologico di Prova da Modificare")
        self._modifica_settori_merceologici("Settore Merceologico di Prova")
        self._creazione_settori_merceologici("Settore Merceologico di Prova da Eliminare")
        self._elimina_settore_merceologico()
        self._verifica_settore_merceologico()

    def _creazione_settori_merceologici(self, descrizione):
        self.navigate_to_and_wait("Settori merceologici")

        self.click_add_button()
        modal = self.wait_modal()

        self.input(modal, 'Descrizione').setValue(descrizione)
        self.wait_for_element_and_click('//button[@class="btn btn-primary"][@type="submit"]')

    def _modifica_settori_merceologici(self, modifica):
        self.navigate_to_and_wait("Settori merceologici")

        self.search_by_th_and_click_first("th_descrizione", 'Settore Merceologico di Prova da Modificare')

        self.driver.execute_script('window.scrollTo(0,0)')
        self.input(None, 'Descrizione').setValue(modifica)
        self.click_save_button()

        self.navigate_to_and_wait("Settori merceologici")
        self.clear_filters()

    def _elimina_settore_merceologico(self):
        self.navigate_to_and_wait("Settori merceologici")
        self.search_by_th_and_click_first("th_descrizione", 'Settore Merceologico di Prova da Eliminare')

        self.driver.execute_script('window.scrollTo(0,0)')
        self.delete_current_and_clear()

    def _verifica_settore_merceologico(self):
        self.search_by_th("th_descrizione", "Settore Merceologico di Prova")
        modificato = self.get_table_text(1, 3)
        self.assertEqual("Settore Merceologico di Prova", modificato)
        self.clear_filters()

        self.verify_deleted_by_th("th_descrizione", "Settore Merceologico di Prova da Eliminare")