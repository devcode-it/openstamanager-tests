from common.Test import Test
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class TipiSpedizione(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Strumenti")
        self.expandSidebar("Tabelle")

    def test_creazione_tipi_spedizione(self):
        self.creazione_tipi_spedizione("Tipo di Spedizione di Prova da Modificare")
        self.creazione_tipi_spedizione("Tipo di Spedizione di Prova da Eliminare")
        self.modifica_tipi_spedizione("Tipo di Spedizione di Prova")
        self.elimina_tipi_spedizione()
        self.verifica_tipi_spedizione()
        
    def creazione_tipi_spedizione(self, descrizione = str):
        self.navigate_to_and_wait("Tipi di spedizione")
        self.click_add_button()
        modal = self.wait_modal()
        self.input(modal, 'Descrizione').setValue(descrizione)
        self.wait_for_element_and_click('button[type="submit"]', By.CSS_SELECTOR)

    def modifica_tipi_spedizione(self, modifica = str):
        self.navigate_to_and_wait("Tipi di spedizione")
        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input')))
        self.send_keys_and_wait(search_input, 'Tipo di Spedizione di Prova da Modificare', wait_modal=False)
        self.click_first_table_row()
        self.input(None,'Descrizione').setValue(modifica)
        self.click_save_button()
        self.navigate_to_and_wait("Tipi di spedizione")
        self.wait_for_element_and_click('//th[@id="th_Descrizione"]/i[@class="deleteicon fa fa-times"]')

    def elimina_tipi_spedizione(self):
        self.navigate_to_and_wait("Tipi di spedizione")
        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input')))
        self.send_keys_and_wait(search_input, 'Tipo di Spedizione di Prova da Eliminare', wait_modal=False)
        self.click_first_table_row()
        self.delete_current_and_clear()

    def verifica_tipi_spedizione(self):
        self.navigate_to_and_wait("Tipi di spedizione")
        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input')))
        self.send_keys_and_wait(search_input, "Tipo di Spedizione di Prova", wait_modal=False)
        modificato = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//tbody//tr[1]//td[2]'))).text
        self.assertEqual("Tipo di Spedizione di Prova", modificato)
        self.clear_filters()
        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input')))
        self.send_keys_and_wait(search_input, "Tipo di Spedizione di Prova da Eliminare", wait_modal=False)
        eliminato = self.get_empty_table_message()
        self.assertEqual("Nessun dato presente nella tabella", eliminato)