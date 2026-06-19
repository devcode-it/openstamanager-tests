from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from common.Test import Test


class Liste(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Gestione email")

    def test_creazione_lista(self):
        self._creazione_lista(nome="Lista di Prova da Modificare")
        self._creazione_lista(nome="Lista di Prova da Eliminare")
        self._modifica_lista("Lista di Prova")
        self._elimina_lista()
        self._verifica_lista()

    def _creazione_lista(self, nome=str):
        self.navigate_to_and_wait("Liste")
        self.click_add_button()
        modal = self.wait_modal()
        self.input(modal, 'Nome').setValue(nome)
        self.wait_for_element_and_click('button[type="submit"]', By.CSS_SELECTOR)

    def _modifica_lista(self, modifica: str):
        self.navigate_to_and_wait("Liste")
        self.search_by_th_and_click_first("th_Nome", 'Lista di Prova da Modificare')
        self.input(None, 'Nome').setValue(modifica)
        self.click_save_button()
        self.navigate_to_and_wait("Liste")
        self.clear_filters()

    def _elimina_lista(self):
        self.navigate_to_and_wait("Liste")
        self.search_by_th_and_click_first("th_Nome", 'Lista di Prova da Eliminare')

        self.delete_current_and_clear()

    def _verifica_lista(self):
        self.navigate_to_and_wait("Liste")
        self.search_by_th("th_Nome", "Lista di Prova")
        modificato = self.get_table_text(1, 2)
        self.assertEqual("Lista di Prova", modificato)
        self.clear_filters()

        self.verify_deleted_by_th("th_Nome", "Lista di Prova da Eliminare")