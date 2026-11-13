from common.Test import Test
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class DescrizioniPredefinite(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Strumenti")
        self.expandSidebar("Tabelle")

    def test_creazione_descrizioni_predefinite(self):
        self.creazione_descrizione_predefinita("Descrizione Predefinita di Prova da Modificare", "Preventivi", "Descrizione Predefinita di Prova da Modificare")
        self.creazione_descrizione_predefinita("Descrizione Predefinita di Prova da Eliminare", "Preventivi", "Descrizione Predefinita di Prova da Eliminare")
        self.modifica_descrizione_predefinita("Descrizione Predefinita di Prova")
        self.elimina_descrizione_predefinita()
        self.verifica_descrizione_predefinita()
        
    def creazione_descrizione_predefinita(self, nome = str, moduli = str, descrizione = str):
        self.navigate_to_and_wait("Descrizioni predefinite")
        self.click_add_button()
        modal = self.wait_modal()

        self.input(modal, 'Nome').setValue(nome)
        self.input(modal, 'Moduli').setByText(moduli)
        self.input(modal, 'Descrizione').setValue(descrizione)

        self.wait_for_element_and_click('button[type="submit"]', By.CSS_SELECTOR)

    def modifica_descrizione_predefinita(self, modifica = str):
        self.navigate_to_and_wait("Descrizioni predefinite")

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input')))
        self.send_keys_and_wait(search_input, 'Descrizione Predefinita di Prova da Modificare', wait_modal=False)   
        self.click_first_table_row()

        self.input(None,'Descrizione').setValue(modifica)
        self.click_save_button()

        self.navigate_to_and_wait("Descrizioni predefinite")
        self.wait_for_element_and_click('//th[@id="th_Descrizione"]/i[@class="deleteicon fa fa-times"]')    

    def elimina_descrizione_predefinita(self):
        self.navigate_to_and_wait("Descrizioni predefinite")

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input')))
        self.send_keys_and_wait(search_input, 'Descrizione Predefinita di Prova da Eliminare', wait_modal=False)
        self.click_first_table_row()

        self.delete_current_and_clear()

    def verifica_descrizione_predefinita(self):
        self.navigate_to_and_wait("Descrizioni predefinite")

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input')))
        self.send_keys_and_wait(search_input, "Descrizione Predefinita di Prova", wait_modal=False)
        modificato = self.get_table_text(1, 3)
        self.assertEqual("Descrizione Predefinita di Prova", modificato)
        self.clear_filters()
