from common.Test import Test
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class TipiDocumento(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Strumenti")
        self.expandSidebar("Tabelle")

    def test_creazione_tipi_documento(self):
        self.creazione_tipi_documento(descrizione="Tipo di Documento di Prova da Modificare", direzione="Entrata", codice="TD01 - Fattura" )
        self.creazione_tipi_documento(descrizione="Tipo di Documento di Prova da Eliminare", direzione="Entrata", codice="TD01 - Fattura" )
        self.modifica_documento("Tipo di Documento di Prova")
        self.elimina_documento()
        self.verifica_tipo_documento()
        
    def creazione_tipi_documento(self, descrizione = str, direzione = str, codice = str):
        self.navigate_to_and_wait("Tipi documento")
        self.click_add_button()
        modal = self.wait_modal()

        self.input(modal, 'Descrizione').setValue(descrizione)
        select = self.input(modal, 'Direzione')
        select.setByText(direzione)
        select = self.input(modal, 'Codice tipo documento FE')
        select.setByText(codice)
        self.wait_for_element_and_click('button[type="submit"]', By.CSS_SELECTOR)

    def modifica_documento(self, modifica):
        self.navigate_to_and_wait("Tipi documento")

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input')))
        self.send_keys_and_wait(search_input, 'Tipo di Documento di Prova da Modificare', wait_modal=False)
        self.click_first_table_row()

        self.input(None,'Descrizione').setValue(modifica)
        self.input(None, 'Sezionale predefinito').setByText('Autofatture')
        self.click_save_button()

        self.navigate_to_and_wait("Tipi documento")
        self.wait_for_element_and_click('//th[@id="th_Descrizione"]/i[@class="deleteicon fa fa-times"]')

    def elimina_documento(self):
        self.navigate_to_and_wait("Tipi documento")

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input')))
        self.send_keys_and_wait(search_input, 'Tipo di Documento di Prova da Eliminare', wait_modal=False)
        self.click_first_table_row()

        self.delete_current_and_clear()

    def verifica_tipo_documento(self):
        self.navigate_to_and_wait("Tipi documento")

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input')))
        self.send_keys_and_wait(search_input, "Tipo di Documento di Prova", wait_modal=False)
        modificato = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//tbody//tr[1]//td[2]'))).text
        self.assertEqual("Tipo di Documento di Prova", modificato)
        self.clear_filters()

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input')))
        self.send_keys_and_wait(search_input, "Tipo di Documento di Prova da Eliminare", wait_modal=False)
        eliminato = self.get_empty_table_message()
        self.assertEqual("Nessun dato presente nella tabella", eliminato)