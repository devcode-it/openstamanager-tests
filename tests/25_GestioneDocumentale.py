from common.Test import Test
from selenium.webdriver.common.by import By


class GestioneDocumentale(Test):
    def setUp(self):
        super().setUp()

    def test_creazione_gestione_documentale(self):
        self._add_documento_di_prova('Documento di Prova da Modificare', 'Documenti società')
        self._add_documento_di_prova('Documento di Prova da Eliminare', 'Documenti società')
        self._modifica_documento("Documento di prova")
        self._elimina_documento()
        self._verifica_documento()

    def _add_documento_di_prova(self, nome: str, categoria: str):
        self.navigate_to_and_wait("Gestione documentale")

        self.click_add_button()
        modal = self.wait_modal()

        self.input(modal, 'Nome').setValue(nome)
        self.input(modal, 'Categoria').setByText(categoria)
        self.wait_for_element_and_click('button[type="submit"]', By.CSS_SELECTOR)

    def _modifica_documento(self, modifica: str):
        self.navigate_to_and_wait("Gestione documentale")

        self.search_by_th_and_click_first("th_Nome", 'Documento di Prova da Modificare')

        self.input(None, 'Nome').setValue(modifica)
        self.click_save_button()

        self.navigate_to_and_wait("Gestione documentale")
        self.clear_filters()

    def _elimina_documento(self):
        self.navigate_to_and_wait("Gestione documentale")

        self.search_by_th_and_click_first("th_Nome", 'Documento di Prova da Eliminare')

        self.delete_current_and_clear()

    def _verifica_documento(self):
        self.navigate_to_and_wait("Gestione documentale")

        self.search_by_th("th_Nome", "Documento di prova")
        modificato = self.get_table_text(1, 3)
        self.assertEqual("Documento di prova", modificato)
        self.clear_filters()

        self.verify_deleted_by_th("th_Nome", "Documento di prova da Eliminare")