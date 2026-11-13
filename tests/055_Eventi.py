from common.Test import Test
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Eventi(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Strumenti")
        self.expandSidebar("Tabelle")

    def test_creazione_eventi(self):
        self.creazione_eventi("Evento di Prova da Modificare", "20/02/2026", "IT - Italia")
        self.creazione_eventi("Evento di Prova da Eliminare", "20/02/2026", "IT - Italia")
        self.modifica_evento("Evento di Prova")
        self.elimina_evento()
        self.verifica_evento()
        
    def creazione_eventi(self, nome = str, data = str, nazione = str):
        self.navigate_to_and_wait("Eventi")
        self.click_add_button()
        modal = self.wait_modal()

        self.input(modal, 'Nome').setValue(nome)
        self.input(None, 'Data').setValue(data)
        select = self.input(modal, 'Nazione')
        select.setByText(nazione)
        self.wait_for_element_and_click('button[type="submit"]', By.CSS_SELECTOR)

    def modifica_evento(self, modifica):
        self.navigate_to_and_wait("Eventi")

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input')))
        self.send_keys_and_wait(search_input, 'Evento di Prova da Modificare', wait_modal=False)
        self.click_first_table_row()

        self.input(None,'Nome').setValue(modifica)
        self.click_save_button()

        self.navigate_to_and_wait("Eventi")
        self.clear_filters()

    def elimina_evento(self):
        self.navigate_to_and_wait("Eventi")

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input')))
        self.send_keys_and_wait(search_input, 'Evento di Prova da Eliminare', wait_modal=False)
        self.click_first_table_row()

        self.delete_current_and_clear()
        
    def verifica_evento(self):
        self.navigate_to_and_wait("Eventi")

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input')))
        self.send_keys_and_wait(search_input, "Evento di Prova", wait_modal=False)
        modificato = self.get_table_text(1, 2)
        self.assertEqual("Evento di Prova", modificato)
        self.clear_filters()

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input')))
        self.send_keys_and_wait(search_input, "Evento di Prova da Eliminare", wait_modal=False)
        eliminato = self.get_empty_table_message()
        self.assertEqual("Nessun dato presente nella tabella", eliminato)