from common.Test import Test
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class StatiContratti(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Strumenti")
        self.expandSidebar("Tabelle")

    def test_creazione_stati_contratti(self):
        self.creazione_stato_contratti("Stato dei Contratti di Prova da Modificare", "fa fa-check text-success", "#9d2929" )
        self.creazione_stato_contratti("Stato dei Contratti di Prova da Eliminare", "fa fa-thumbs-down text-danger", "#38468f")
        self.modifica_stato_contratti("Stato dei Contratti di Prova")
        self.elimina_stato_contratti()
        self.verifica_stato_contratti()
        
    def creazione_stato_contratti(self, descrizione = str, icona = str, colore = str):
        self.navigate_to_and_wait("Stati dei contratti")
        self.click_add_button()
        modal = self.wait_modal()

        self.input(modal, 'Descrizione').setValue(descrizione)
        self.input(modal, 'Colore').setValue(colore)
        self.input(modal, 'Icona').setValue(icona)
        self.wait_for_element_and_click('button[type="submit"]', By.CSS_SELECTOR)

    def modifica_stato_contratti(self, modifica = str):
        self.navigate_to_and_wait("Stati dei contratti")

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input')))
        self.send_keys_and_wait(search_input, 'Stato dei Contratti di Prova da Modificare', wait_modal=False)
        self.click_first_table_row()

        self.input(None,'Descrizione').setValue(modifica)
        self.click_save_button()

        self.navigate_to_and_wait("Stati dei contratti")
        self.wait_for_element_and_click('//th[@id="th_Descrizione"]/i[@class="deleteicon fa fa-times"]')

    def elimina_stato_contratti(self):
        self.navigate_to_and_wait("Stati dei contratti")

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input')))
        self.send_keys_and_wait(search_input, 'Stato dei Contratti di Prova da Eliminare', wait_modal=False)
        self.click_first_table_row()

        self.delete_current_and_clear()

    def verifica_stato_contratti(self):
        self.navigate_to_and_wait("Stati dei contratti")

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input')))
        self.send_keys_and_wait(search_input, "Stato dei Contratti di Prova", wait_modal=False)
        modificato = self.get_table_text(1, 2)
        self.assertEqual("Stato dei Contratti di Prova", modificato)
        self.clear_filters()

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input')))
        self.send_keys_and_wait(search_input, "Stato dei Contratti di Prova da Eliminare", wait_modal=False)
        eliminato = self.get_empty_table_message()
        self.assertEqual("Nessun dato presente nella tabella", eliminato)