from selenium.webdriver.common.by import By
from common.Test import Test
from selenium.webdriver.support import expected_conditions as EC

class Zone(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Anagrafiche")
        self.wait_loader()

    def test_creazione_zone(self):
        self._creazione_zone(nome="0001", descrizione="Zona di Prova da Modificare")
        self._creazione_zone(nome="0002", descrizione="Zona di Prova da Eliminare")
        self._modifica_zone("Zona di Prova")
        self._elimina_zone()
        self._verifica_zone()

    def _creazione_zone(self, nome, descrizione):
        self.navigate_to_and_wait("Zone")

        self.click_add_button()
        modal = self.wait_modal()

        self.input(modal, 'Nome').setValue(nome)
        self.input(modal, 'Descrizione').setValue(descrizione)
        self.wait_for_element_and_click('button[type="submit"]', By.CSS_SELECTOR)

    def _modifica_zone(self, modifica):
        self.navigate_to_and_wait("Zone")

        search_input = self.wait_for_element_and_click('//th[@id="th_Descrizione"]/input')
        self.send_keys_and_wait(search_input, 'Zona di Prova da Modificare', wait_modal=False)
        self.click_first_table_row()

        self.input(None, 'Descrizione').setValue(modifica)
        self.click_save_button()

        self.navigate_to_and_wait("Zone")
        self.clear_filters()

    def _elimina_zone(self):
        search_input = self.wait_for_element_and_click('//th[@id="th_Descrizione"]/input')
        self.send_keys_and_wait(search_input, 'Zona di Prova da Eliminare', wait_modal=False)
        self.click_first_table_row()

        self.delete_current_and_clear()
    def _verifica_zone(self):
        search_input = self.wait_for_element_and_click('//th[@id="th_Descrizione"]/input')
        self.send_keys_and_wait(search_input, "Zona di Prova", wait_modal=False)
        modificato = self.get_table_text(1, 3)
        self.assertEqual("Zona di Prova", modificato)

        self.clear_filters()

        search_input = self.wait_for_element_and_click('//th[@id="th_Descrizione"]/input')
        self.send_keys_and_wait(search_input, "Zona di Prova da Eliminare", wait_modal=False)
        eliminato = self.get_empty_table_message()
        self.assertEqual("Nessun dato presente nella tabella", eliminato)
