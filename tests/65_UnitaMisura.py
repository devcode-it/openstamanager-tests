from common.Test import Test
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class UnitaMisura(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Strumenti")
        self.expandSidebar("Tabelle")

    def test_creazione_unita_misura(self):
        self.creazione_unita_misura("UdMdPdM")
        self.creazione_unita_misura("UdMdPdE")
        self.modifica_unita_misura("UdMdP")
        self.elimina_unita_misura()
        self.verifica_unita_misura()
        
    def creazione_unita_misura(self, valore= str):
        self.navigate_to_and_wait("Unità di misura")
        self.click_add_button()
        modal = self.wait_modal()

        self.input(modal, 'Valore').setValue(valore)
        self.wait_for_element_and_click('//div[@class="modal-footer"]//button[@type="submit"]')

    def modifica_unita_misura(self, modifica = str):
        self.navigate_to_and_wait("Unità di misura")

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Valore"]/input')))
        self.send_keys_and_wait(search_input, 'UdMdPdM', wait_modal=False)
        self.click_first_table_row()

        self.input(None,'Valore').setValue(modifica)
        self.click_save_button()

        self.navigate_to_and_wait("Unità di misura")
        self.wait_for_element_and_click('//th[@id="th_Valore"]/i[@class="deleteicon fa fa-times"]')

    def elimina_unita_misura(self):
        self.navigate_to_and_wait("Unità di misura")

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Valore"]/input')))
        self.send_keys_and_wait(search_input, 'UdMdPdE', wait_modal=False)
        self.click_first_table_row()

        self.delete_current_and_clear()

    def verifica_unita_misura(self):
        self.navigate_to_and_wait("Unità di misura")

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Valore"]/input')))
        self.send_keys_and_wait(search_input, "UdMdP", wait_modal=False)
        modificato = self.get_table_text(1, 2)
        self.assertEqual("UdMdP", modificato)
        self.clear_filters()

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Valore"]/input')))
        self.send_keys_and_wait(search_input, "UdMdPdE", wait_modal=False)
        eliminato = self.get_empty_table_message()
        self.assertEqual("Nessun dato presente nella tabella", eliminato)