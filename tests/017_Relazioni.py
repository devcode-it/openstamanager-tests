from selenium.webdriver.common.by import By
from common.Test import Test
from selenium.webdriver.support import expected_conditions as EC

class Relazioni(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Anagrafiche")
        self.wait_loader()

    def test_creazione_relazioni(self):
        self._creazione_relazioni("Relazione di Prova da Modificare", "#9d2929")
        self._creazione_relazioni("Relazione di Prova da Eliminare", "#3737db")
        self._modifica_relazioni("Relazione di Prova")
        self._elimina_relazioni()
        self._verifica_relazione()

    def _creazione_relazioni(self, descrizione, colore):
        self.navigate_to_and_wait("Relazioni")

        self.click_add_button()
        modal = self.wait_modal()

        self.input(modal, 'Colore').setValue(colore)
        self.input(modal, 'Descrizione').setValue(descrizione)
        self.wait_for_element_and_click('button[type="submit"]', By.CSS_SELECTOR)

    def _modifica_relazioni(self, modifica):
        self.navigate_to_and_wait("Relazioni")

        search_input = self.wait_for_element_and_click('//th[@id="th_Descrizione"]/input')
        self.send_keys_and_wait(search_input, 'Relazione di Prova da Modificare', wait_modal=False)
        self.click_first_table_row()

        colore = self.wait_for_element_and_click('//input[@id="colore"]')
        colore.clear()
        colore.send_keys("#436935")
        self.input(None, 'Descrizione').setValue(modifica)
        self.click_save_button()

        self.navigate_to_and_wait("Relazioni")
        self.wait_for_element_and_click('//th[@id="th_Descrizione"]/i[@class="deleteicon fa fa-times"]')

    def _elimina_relazioni(self):
        self.navigate_to_and_wait("Relazioni")

        search_input = self.wait_for_element_and_click('//th[@id="th_Descrizione"]/input')
        self.send_keys_and_wait(search_input, 'Relazione di Prova da Eliminare', wait_modal=False)
        self.click_first_table_row()
        self.delete_current_and_clear()

    def _verifica_relazione(self):
        self.navigate_to_and_wait("Relazioni")

        search_input = self.wait_for_element_and_click('//th[@id="th_Descrizione"]/input')
        self.send_keys_and_wait(search_input, "Relazione di Prova", wait_modal=False)
        modificato = self.get_table_text(1, 2)
        self.assertEqual("Relazione di Prova", modificato)
        self.clear_filters()

        search_input = self.wait_for_element_and_click('//th[@id="th_Descrizione"]/input')
        self.send_keys_and_wait(search_input, "Relazione di Prova da Eliminare", wait_modal=False)
        eliminato = self.get_table_text(1, 1)
        self.assertEqual("Nessun dato presente nella tabella", eliminato)
