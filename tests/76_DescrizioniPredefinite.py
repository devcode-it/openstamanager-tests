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
        self.wait_for_element_and_click('//i[@class="fa fa-power-off nav-icon"]')
        
    def creazione_descrizione_predefinita(self, nome = str, moduli = str, descrizione = str):
        self.navigateTo("Descrizioni predefinite")
        self.wait_for_element_and_click('//i[@class="fa fa-plus"]')
        modal = self.wait_modal()

        self.input(modal, 'Nome').setValue(nome)
        self.input(modal, 'Moduli').setByText(moduli)
        self.input(modal, 'Descrizione').setValue(descrizione)

        self.wait_for_element_and_click('button[type="submit"]', By.CSS_SELECTOR)

    def modifica_descrizione_predefinita(self, modifica = str):
        self.navigateTo("Descrizioni predefinite")
        self.wait_loader()

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input')))
        self.send_keys_and_wait(search_input, 'Descrizione Predefinita di Prova da Modificare', wait_modal=False)   
        self.wait_for_element_and_click('//tbody//tr//td[2]')

        self.input(None,'Descrizione').setValue(modifica)
        self.wait_for_element_and_click('//div[@id="tab_0"]//button[@id="save"]')

        self.navigateTo("Descrizioni predefinite")
        self.wait_loader()
        self.wait_for_element_and_click('//th[@id="th_Descrizione"]/i[@class="deleteicon fa fa-times"]')    

    def elimina_descrizione_predefinita(self):
        self.navigateTo("Descrizioni predefinite")
        self.wait_loader()

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input')))
        self.send_keys_and_wait(search_input, 'Descrizione Predefinita di Prova da Eliminare', wait_modal=False)
        self.wait_for_element_and_click('//tbody//tr//td[2]')

        self.wait_for_element_and_click('//div[@id="tab_0"]//a[@class="btn btn-danger ask"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')
        self.wait_for_element_and_click('//th[@id="th_Descrizione"]/i[@class="deleteicon fa fa-times"]')    

    def verifica_descrizione_predefinita(self):
        self.navigateTo("Descrizioni predefinite")
        self.wait_loader()

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input')))
        self.send_keys_and_wait(search_input, "Descrizione Predefinita di Prova", wait_modal=False)
        modificato = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//tbody//tr[1]//td[3]'))).text
        self.assertEqual("Descrizione Predefinita di Prova", modificato)
        self.wait_for_element_and_click('//i[@class="deleteicon fa fa-times"]')
