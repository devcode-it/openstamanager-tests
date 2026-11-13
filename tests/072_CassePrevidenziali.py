from common.Test import Test
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class CassePrevidenziali(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Strumenti")
        self.expandSidebar("Tabelle")

    def test_creazione_casse_previdenziali(self):
        self.creazione_casse_previdenziali("Cassa Previdenziale di Prova da Modificare","80,00", "60,00")
        self.creazione_casse_previdenziali("Cassa Previdenziale di Prova da Eliminare", "20,00", "40,00")
        self.modifica_casse_previdenziali("Cassa Previdenziale di Prova")
        self.elimina_casse_previdenziali()
        self.verifica_casse_previdenziali()
        
    def creazione_casse_previdenziali(self, descrizione = str, percentuale = str, indetraibile = str):
        self.navigate_to_and_wait("Casse previdenziali")
        self.click_add_button()
        modal = self.wait_modal()

        self.input(modal, 'Descrizione').setValue(descrizione)
        self.input(modal, 'Percentuale').setValue(percentuale)
        self.input(modal, 'Indetraibile').setValue(indetraibile)
        self.wait_for_element_and_click('button[type="submit"]', By.CSS_SELECTOR)

    def modifica_casse_previdenziali(self, modifica = str):
        self.navigate_to_and_wait("Casse previdenziali")

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input')))
        self.send_keys_and_wait(search_input, 'Cassa Previdenziale di Prova da Modificare', wait_modal=False)
        self.click_first_table_row()

        self.input(None,'Descrizione').setValue(modifica)
        self.click_save_button()

        self.navigate_to_and_wait("Casse previdenziali")
        self.wait_for_element_and_click('//th[@id="th_Descrizione"]/i[@class="deleteicon fa fa-times"]')

    def elimina_casse_previdenziali(self):
        self.navigate_to_and_wait("Casse previdenziali")

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input')))
        self.send_keys_and_wait(search_input, 'Cassa Previdenziale di Prova da Eliminare', wait_modal=False)
        self.click_first_table_row()

        self.delete_current_and_clear()

    def verifica_casse_previdenziali(self):
        self.navigate_to_and_wait("Casse previdenziali")

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input')))
        self.send_keys_and_wait(search_input, "Cassa Previdenziale di Prova", wait_modal=False)
        modificato = self.get_table_text(1, 2)
        self.assertEqual("Cassa Previdenziale di Prova", modificato)
        self.clear_filters()

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input')))
        self.send_keys_and_wait(search_input, "Cassa Previdenziale di Prova da Eliminare", wait_modal=False)
        eliminato = self.get_empty_table_message()
        self.assertEqual("Nessun dato presente nella tabella", eliminato)