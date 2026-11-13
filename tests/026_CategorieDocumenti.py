from selenium.webdriver.common.by import By
from common.Test import Test


class CategorieDocumenti(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Gestione documentale")
        self.wait_loader()

    def test_creazione_categorie_documenti(self):
        self._add_categorie_documenti('Categoria di Prova da Modificare')
        self._add_categorie_documenti('Categoria di Prova da Eliminare')
        self._modifica_categoria_documenti("Categoria Documenti di Prova")
        self._elimina_categoria_documenti()
        self._verifica_categoria_documento()

    def _add_categorie_documenti(self, descrizione: str):
        self.navigate_to_and_wait("Categorie documenti")

        self.click_add_button()
        modal = self.wait_modal()
        self.input(modal, 'Descrizione').setValue(descrizione)
        self.wait_for_element_and_click('button[type="submit"]', By.CSS_SELECTOR)

    def _search_categoria(self, nome: str):
        self.navigate_to_and_wait("Categorie documenti")
        self.search_by_th("th_Descrizione", nome)

    def _modifica_categoria_documenti(self, modifica: str):
        self._search_categoria('Categoria di Prova da Modificare')
        self.click_first_result()
        self.input(None, 'Descrizione').setValue(modifica)
        self.click_save_button()

        self.navigate_to_and_wait("Categorie documenti")
        self.clear_filters()

    def _elimina_categoria_documenti(self):
        self._search_categoria('Categoria di Prova da Eliminare')
        self.click_first_result()

        self.delete_current_and_clear()

    def _verifica_categoria_documento(self):
        self._search_categoria("Categoria Documenti di Prova")
        modificato = self.get_table_text(1, 2)
        self.assertEqual("Categoria Documenti di Prova", modificato)
        self.clear_filters()

        self.verify_deleted_by_th("th_Descrizione", "Categoria Documenti di Prova da Eliminare")