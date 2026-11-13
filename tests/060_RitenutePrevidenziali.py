from common.Test import Test
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class RitenutePrevidenziali(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Strumenti")
        self.expandSidebar("Tabelle")

    def test_creazione_ritenute_previdenziali(self):
        self.creazione_ritenute_previdenziali(descrizione= "Ritenuta Previdenziale di Prova da Modificare", percentuale="80,00", percentualeimp="60,00")
        self.creazione_ritenute_previdenziali(descrizione= "Ritenuta Previdenziale di Prova da Eliminare", percentuale="20,00", percentualeimp="40,00")
        self.modifica_ritenute_previdenziali("Ritenuta Previdenziale di Prova")
        self.elimina_ritenute_previdenziali()
        self.verifica_ritenuta_previdenziale()
        
    def creazione_ritenute_previdenziali(self, descrizione = str, percentuale = str, percentualeimp = str):
        self.navigate_to_and_wait("Ritenute previdenziali")
        self.click_add_button()
        modal = self.wait_modal()

        self.input(modal, 'Descrizione').setValue(descrizione)
        self.input(modal, 'Percentuale').setValue(percentuale)
        self.input(modal, 'Causale ritenuta').setValue("A")
        self.input(modal, 'Tipo ritenuta').setValue("RT01")
        self.input(modal, 'Percentuale imponibile').setValue(percentualeimp)
        self.wait_for_element_and_click('button[type="submit"]', By.CSS_SELECTOR)

    def modifica_ritenute_previdenziali(self, modifica = str):
        self.navigate_to_and_wait("Ritenute previdenziali")

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input')))
        self.send_keys_and_wait(search_input, 'Ritenuta Previdenziale di Prova da Modificare', wait_modal=False)
        self.click_first_table_row()

        self.input(None,'Descrizione').setValue(modifica)
        self.click_save_button()

        self.navigate_to_and_wait("Ritenute previdenziali")
        self.wait_for_element_and_click('//th[@id="th_Descrizione"]/i[@class="deleteicon fa fa-times"]')

    def elimina_ritenute_previdenziali(self):
        self.navigate_to_and_wait("Ritenute previdenziali")

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input')))
        self.send_keys_and_wait(search_input, 'Ritenuta Previdenziale di Prova da Eliminare', wait_modal=False)
        self.click_first_table_row()

        self.delete_current_and_clear()

    def verifica_ritenuta_previdenziale(self):
        self.navigate_to_and_wait("Ritenute previdenziali")

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input')))
        self.send_keys_and_wait(search_input, "Ritenuta Previdenziale di Prova", wait_modal=False)
        modificato = self.get_table_text(1, 3)
        self.assertEqual("Ritenuta Previdenziale di Prova", modificato)
        self.clear_filters()

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input')))
        self.send_keys_and_wait(search_input, "Ritenuta Previdenziale di Prova da Eliminare", wait_modal=False)
        eliminato = self.get_empty_table_message()
        self.assertEqual("Nessun dato presente nella tabella", eliminato)