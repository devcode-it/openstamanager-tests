from common.Test import Test
from selenium.webdriver.common.by import By

class Automezzi(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Magazzino")

    def test_creazione_automezzi(self):
        self.creazione_automezzo("Automezzo di Prova da Modificare", "aabbcc")
        self.creazione_automezzo("Automezzo di Prova da Eliminare", "ccbbaa")
        self.modifica_automezzo("Automezzo di Prova")
        self.elimina_automezzo()
        self.verifica_automezzo()

    def creazione_automezzo(self, descrizione: str, targa: str):
        self.navigate_to_and_wait("Automezzi")

        self.click_add_button()
        modal = self.wait_modal()

        self.input(modal, 'Nome').setValue(descrizione)
        self.input(modal, 'Targa').setValue(targa)
        self.wait_for_element_and_click('button[type="submit"]', By.CSS_SELECTOR)

    def modifica_automezzo(self, modifica:str):
        self.navigate_to_and_wait("Automezzi")

        self.search_by_th_and_click_first("th_Nome", 'Automezzo di Prova da Modificare')

        self.input(None,'Nome').setValue(modifica)
        self.click_save_button()

        self.navigate_to_and_wait("Automezzi")
        self.clear_filters()

    def elimina_automezzo(self):
        self.navigate_to_and_wait("Automezzi")

        self.search_by_th_and_click_first("th_Nome", 'Automezzo di Prova da Eliminare')

        self.delete_current_and_clear()

    def verifica_automezzo(self):
        self.navigate_to_and_wait("Automezzi")

        self.search_by_th("th_Nome", "Automezzo di Prova")
        modificato = self.get_table_text(1, 2)
        self.assertEqual("Automezzo di Prova", modificato)
        self.clear_filters()

        self.verify_deleted_by_th("th_Nome", "Automezzo di Prova da Eliminare")