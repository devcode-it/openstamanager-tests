from common.Test import Test
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class RitenuteAcconto(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Strumenti")
        self.expandSidebar("Tabelle")

    def test_creazione_ritenute_acconto(self):
        self.navigate_to_and_wait("Ritenute acconto")

        self.creazione_ritenute_acconto("Ritenuta Acconto di Prova da Modificare", "80,00", "60,00")
        self.creazione_ritenute_acconto("Ritenuta Acconto di Prova da Eliminare", "20,00", "40,00")
        self.modifica_ritenuta_acconto("Ritenuta Acconto di Prova")
        self.elimina_ritenuta_acconto()
        self.verifica_ritenuta_acconto()
        
    def creazione_ritenute_acconto(self, descrizione = str, percentuale = str, percentualeimp = str):
        self.click_add_button()
        modal = self.wait_modal()

        self.input(modal, 'Descrizione').setValue(descrizione)
        self.input(modal, 'Percentuale').setValue(percentuale)
        self.input(modal, 'Percentuale imponibile').setValue(percentualeimp)
        self.wait_for_element_and_click('//div[@class="modal-footer"]//button[@type="submit"]')

    def modifica_ritenuta_acconto(self, modifica):
        self.navigate_to_and_wait("Ritenute acconto")

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input')))
        self.send_keys_and_wait(search_input, 'Ritenuta Acconto di Prova da Modificare', wait_modal=False)
        self.click_first_table_row()

        self.input(None,'Descrizione').setValue(modifica)
        self.click_save_button()

        self.navigate_to_and_wait("Ritenute acconto")
        self.wait_for_element_and_click('//th[@id="th_Descrizione"]/i[@class="deleteicon fa fa-times"]')

    def elimina_ritenuta_acconto(self):
        self.navigate_to_and_wait("Ritenute acconto")

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input')))
        self.send_keys_and_wait(search_input, 'Ritenuta Acconto di Prova da Eliminare', wait_modal=False)
        self.click_first_table_row()

        self.delete_current_and_clear()

    def verifica_ritenuta_acconto(self):
        self.navigate_to_and_wait("Ritenute acconto")

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input')))
        self.send_keys_and_wait(search_input, "Ritenuta Acconto di Prova", wait_modal=False)
        modificato = self.get_table_text(1, 2)
        self.assertEqual("Ritenuta Acconto di Prova", modificato)
        self.clear_filters()

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input')))
        self.send_keys_and_wait(search_input, "Ritenuta Acconto di Prova da Eliminare", wait_modal=False)
        eliminato = self.get_empty_table_message()
        self.assertEqual("Nessun dato presente nella tabella", eliminato)