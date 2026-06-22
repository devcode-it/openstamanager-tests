from common.Test import Test
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class AspettoBeni(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Strumenti")
        self.expandSidebar("Tabelle")

    def test_creazione_aspetto_beni(self):
        self.creazione_aspetto_beni("Aspetto Beni di Prova da Modificare")
        self.creazione_aspetto_beni("Aspetto Beni di Prova da Eliminare")
        self.modifica_aspetto_beni("Aspetto Beni di Prova")
        self.elimina_aspetto_beni()
        self.verifica_aspetto_beni()
        
    def creazione_aspetto_beni(self, descrizione = str):
        self.navigate_to_and_wait("Aspetto beni")
        self.click_add_button()
        modal = self.wait_modal()

        self.input(modal, 'Descrizione').setValue(descrizione)
        self.wait_for_element_and_click('button[type="submit"]', By.CSS_SELECTOR)

    def modifica_aspetto_beni(self, modifica = str):
        self.navigate_to_and_wait("Aspetto beni")

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input')))
        self.send_keys_and_wait(search_input, 'Aspetto Beni di Prova da Modificare', wait_modal=False)
        self.click_first_table_row()

        self.input(None,'Descrizione').setValue(modifica)
        self.click_save_button()

        self.navigate_to_and_wait("Aspetto beni")
        self.wait_for_element_and_click('//th[@id="th_Descrizione"]/i[@class="deleteicon fa fa-times"]')

    def elimina_aspetto_beni(self):
        self.navigate_to_and_wait("Aspetto beni")

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input')))
        self.send_keys_and_wait(search_input, 'Aspetto Beni di Prova da Eliminare', wait_modal=False)
        self.click_first_table_row()

        self.delete_current_and_clear()

    def verifica_aspetto_beni(self):
        self.navigate_to_and_wait("Aspetto beni")

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input')))
        self.send_keys_and_wait(search_input, "Aspetto Beni di Prova", wait_modal=False)
        modificato = self.get_table_text(1, 2)
        self.assertEqual("Aspetto Beni di Prova", modificato)
        self.clear_filters()

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input')))
        self.send_keys_and_wait(search_input, "Aspetto Beni di Prova da Eliminare", wait_modal=False)
        eliminato = self.get_empty_table_message()
        self.assertEqual("Nessun dato presente nella tabella", eliminato)