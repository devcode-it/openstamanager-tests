from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from common.Test import Test


class Provenienze_clienti(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Anagrafiche")
        self.wait_loader()

    def test_creazione_provenienze_clienti(self):
        self._creazione_provenienze_clienti("Provenienza Clienti di Prova da Modificare", "#9d2929")
        self._creazione_provenienze_clienti("Provenienza Clienti di Prova da Eliminare", "#3737db")
        self._modifica_provenienze_clienti("Provenienza Clienti di Prova")
        self._elimina_provenienze_clienti()
        self._verifica_provenienze_clienti()

    def _creazione_provenienze_clienti(self, descrizione, colore):
        self.navigate_to_and_wait("Provenienze clienti")

        self.click_add_button()
        modal = self.wait_modal()

        self.input(modal, 'Colore').setValue(colore)
        self.input(modal, 'Descrizione').setValue(descrizione)
        self.wait_for_element_and_click('button[type="submit"]', By.CSS_SELECTOR)

    def _modifica_provenienze_clienti(self, modifica):
        self.navigate_to_and_wait("Provenienze clienti")

        search_input = self.wait_for_element_and_click('//th[@id="th_descrizione"]/input')
        self.send_keys_and_wait(search_input, 'Provenienza Clienti di Prova da Modificare', wait_modal=False)
        self.click_first_table_row()

        self.driver.execute_script('window.scrollTo(0,0)')
        self.input(None, 'Descrizione').setValue(modifica)
        self.click_save_button()

        self.navigate_to_and_wait("Provenienze clienti")
        self.clear_filters()

    def _elimina_provenienze_clienti(self):
        search_input = self.wait_for_element_and_click('//th[@id="th_descrizione"]/input')
        self.send_keys_and_wait(search_input, 'Provenienza Clienti di Prova da Eliminare', wait_modal=False)
        self.click_first_table_row()

        self.driver.execute_script('window.scrollTo(0,0)')
        self.delete_current_and_clear()
        
    def _verifica_provenienze_clienti(self):
        search_input = self.wait_for_element_and_click('//th[@id="th_descrizione"]/input')
        self.send_keys_and_wait(search_input, "Provenienza Clienti di Prova", wait_modal=False)
        modificato = self.get_table_text(1, 3)
        self.assertEqual("Provenienza Clienti di Prova", modificato)
        self.clear_filters()

        search_input = self.wait_for_element_and_click('//th[@id="th_descrizione"]/input')
        self.send_keys_and_wait(search_input, "Provenienza Clienti di Prova da Eliminare", wait_modal=False)
        eliminato = self.get_empty_table_message()
        self.assertEqual("Nessun dato presente nella tabella", eliminato)