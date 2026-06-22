from common.Test import Test
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Pagamenti(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Strumenti")
        self.expandSidebar("Tabelle")

    def test_creazione_pagamenti(self):
        self.navigate_to_and_wait("Pagamenti")

        self.creazione_pagamenti("Pagamento di Prova da Modificare", "MP01 - Contanti")
        self.creazione_pagamenti("Pagamento di Prova da Eliminare", "MP01 - Contanti")
        self.modifica_pagamento("Pagamento di Prova")
        self.elimina_pagamento()
        self.verifica_pagamento()
        
    def creazione_pagamenti(self, descrizione= str, codice = str):
        self.click_add_button()
        modal = self.wait_modal()

        self.wait_for_dropdown_and_select('//span[@id="select2-codice_modalita_pagamento_fe_add-container"]', option_text=codice)
        self.input(modal, 'Descrizione').setValue(descrizione)
        self.wait_for_element_and_click('//div[@class="modal-footer"]//button[@type="submit"]')

    def modifica_pagamento(self, modifica = str):
        self.navigate_to_and_wait("Pagamenti")

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input')))
        self.send_keys_and_wait(search_input, 'Pagamento di Prova da Modificare', wait_modal=False)
        self.click_first_table_row()

        self.input(None,'Descrizione').setValue(modifica)
        percentuale_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="percentuale1"]')))
        self.send_keys_and_wait(percentuale_input, '100', wait_modal=False)

        self.navigate_to_and_wait("Pagamenti")
        self.wait_for_element_and_click('//th[@id="th_Descrizione"]/i[@class="deleteicon fa fa-times"]')

    def elimina_pagamento(self):
        self.navigate_to_and_wait("Pagamenti")

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input')))
        self.send_keys_and_wait(search_input, 'Pagamento di Prova da Eliminare', wait_modal=False)
        self.click_first_table_row()

        self.delete_current_and_clear()

    def verifica_pagamento(self):
        self.navigate_to_and_wait("Pagamenti")

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input')))
        self.send_keys_and_wait(search_input, "Pagamento di Prova", wait_modal=False)
        modificato = self.get_table_text(1, 2)
        self.assertEqual("Pagamento di Prova", modificato)
        self.clear_filters()

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input')))
        self.send_keys_and_wait(search_input, "Pagamento di Prova da Eliminare", wait_modal=False)
        eliminato = self.get_empty_table_message()
        self.assertEqual("Nessun dato presente nella tabella", eliminato)