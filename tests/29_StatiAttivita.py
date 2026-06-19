from selenium.webdriver.common.by import By
from common.Test import Test


class StatiAttivita(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Attività")
        self.wait_loader()

    def test_creazione_stati_attivita(self):
        self._creazione_stati_attivita("0001", "Stato di Prova da Modificare", "#9d2929")
        self._creazione_stati_attivita("0002", "Stato di Prova da Eliminare", "#38468f")
        self._modifica_stato_attivita("Stato di Attività di Prova")
        self._elimina_stato_attivita()
        self._verifica_stato_attivita()

    def _creazione_stati_attivita(self, codice: str, descrizione: str, colore: str):
        self.navigate_to_and_wait("Stati di attività")

        self.click_add_button()
        modal = self.wait_modal()

        self.input(modal, 'Colore').setValue(colore)
        self.input(modal, 'Codice').setValue(codice)
        self.input(modal, 'Descrizione').setValue(descrizione)
        self.wait_for_element_and_click('button[type="submit"]', By.CSS_SELECTOR)

    def _search_stato_attivita(self, nome: str):
        self.navigate_to_and_wait("Stati di attività")
        self.search_by_th("th_Descrizione", nome)

    def _modifica_stato_attivita(self, modifica: str):
        self._search_stato_attivita('Stato di Prova da Modificare')
        self.click_first_result()
        self.input(None, 'Descrizione').setValue(modifica)
        self.click_save_button()

        self.navigate_to_and_wait("Stati di attività")
        self.clear_filters()

    def _elimina_stato_attivita(self):
        self._search_stato_attivita('Stato di Prova da Eliminare')
        self.click_first_result()

        self.delete_current_and_clear()

    def _verifica_stato_attivita(self):
        self._search_stato_attivita("Stato di Attività di Prova")
        modificato = self.get_table_text(1, 3)
        self.assertEqual("Stato di Attività di Prova", modificato)
        self.clear_filters()

        self._search_stato_attivita("Stato di Attività di Prova da Eliminare")
        eliminato = self.get_empty_table_message()
        self.assertEqual("Nessun dato presente nella tabella", eliminato)
        self.clear_filters()