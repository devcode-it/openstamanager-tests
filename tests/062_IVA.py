from common.Test import Test
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class IVA(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Strumenti")
        self.expandSidebar("Tabelle")

    def test_creazione_iva(self):
        self.creazione_iva("IVA di Prova da Modificare", "9,00", "2,00", "Scissione dei pagamenti")
        self.creazione_iva("IVA di Prova da Eliminare", "9,00", "2,00", "Scissione dei pagamenti")
        self.modifica_iva("IVA di Prova")
        self.elimina_iva()
        self.verifica_iva()
        
    def creazione_iva(self, descrizione = str, percentuale = str, indetraibile = str, esigibilita = str):
        self.navigate_to_and_wait("IVA")
        self.click_add_button()
        modal = self.wait_modal()

        self.input(modal, 'Descrizione').setValue(descrizione)
        self.input(modal, 'Percentuale').setValue(percentuale)
        self.input(modal, 'Indetraibile').setValue(indetraibile)
        select = self.input(modal, 'Esigibilità')
        select.setByText(esigibilita)
        self.wait_for_element_and_click('button[type="submit"]', By.CSS_SELECTOR)

    def modifica_iva(self, modifica = str):
        self.navigate_to_and_wait("IVA")

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input')))
        self.send_keys_and_wait(search_input, 'IVA di Prova da Modificare', wait_modal=False)
        self.click_first_table_row()

        self.input(None,'Descrizione').setValue(modifica)
        self.click_save_button()

        self.navigate_to_and_wait("IVA")
        self.wait_for_element_and_click('//th[@id="th_Descrizione"]/i[@class="deleteicon fa fa-times"]')

    def elimina_iva(self):
        self.navigate_to_and_wait("IVA")

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input')))
        self.send_keys_and_wait(search_input, 'IVA di Prova da Eliminare', wait_modal=False)
        self.click_first_table_row()

        self.delete_current_and_clear()

    def verifica_iva(self):
        self.navigate_to_and_wait("IVA")

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input')))
        self.send_keys_and_wait(search_input, "IVA di Prova", wait_modal=False)
        modificato = self.get_table_text(1, 3)
        self.assertEqual("IVA di Prova", modificato)
        self.clear_filters()

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input')))
        self.send_keys_and_wait(search_input, "IVA di Prova da Eliminare", wait_modal=False)
        eliminato = self.get_empty_table_message()
        self.assertEqual("Nessun dato presente nella tabella", eliminato)