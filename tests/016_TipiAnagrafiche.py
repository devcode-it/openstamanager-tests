from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from common.Test import Test


class TipiAnagrafiche(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Anagrafiche")
        self.wait_loader()

    def test_creazione_tipo_anagrafiche(self):
        self.navigate_to_and_wait("Tipi di anagrafiche")

        self._creazione_tipo_anagrafiche("Tipo di anagrafica di Prova da Modificare")
        self._creazione_tipo_anagrafiche("Tipo di anagrafica di Prova da Eliminare")
        self._modifica_tipo_anagrafiche("Tipo di anagrafica di Prova")
        self._elimina_tipo_anagrafiche()
        self._verifica_tipo_anagrafiche()

    def _creazione_tipo_anagrafiche(self, descrizione):
        self.click_add_button()
        modal = self.wait_modal()
        self.input(modal, 'Descrizione').setValue(descrizione)
        self.submit_modal(modal)

    def _modifica_tipo_anagrafiche(self, modifica):
        self.navigate_to_and_wait("Tipi di anagrafiche")

        self.search_by_th_and_click_first("th_Descrizione", 'Tipo di anagrafica di Prova da Modificare')
        self.input(None, 'Descrizione').setValue(modifica)
        self.click_save_button()

        self.navigate_to_and_wait("Tipi di anagrafiche")
        self.clear_filters()

    def _elimina_tipo_anagrafiche(self):
        self.navigate_to_and_wait("Tipi di anagrafiche")

        self.search_by_th_and_click_first("th_Descrizione", 'Tipo di anagrafica di Prova da Eliminare')

        self.delete_current_and_clear()

    def _verifica_tipo_anagrafiche(self):
        self.navigate_to_and_wait("Tipi di anagrafiche")

        self.search_by_th("th_Descrizione", "Tipo di anagrafica di Prova")
        modificato = self.get_table_text(1, 2)
        self.assertEqual("Tipo di anagrafica di Prova", modificato)
        self.clear_filters()

        self.verify_deleted_by_th("th_Descrizione", "Tipo di anagrafica di Prova da Eliminare")
