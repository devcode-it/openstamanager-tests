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
        self.wait_for_element_and_click('//i[@class="fa fa-power-off nav-icon"]')
        
    def creazione_unita_misura(self, valore= str):
        self.navigateTo("Unità di misura")
        self.wait_for_element_and_click('//i[@class="fa fa-plus"]')
        modal = self.wait_modal()

        self.input(modal, 'Valore').setValue(valore)
        self.wait_for_element_and_click('//div[@class="modal-footer"]//button[@type="submit"]')

    def modifica_unita_misura(self, modifica = str):
        self.navigateTo("Unità di misura")
        self.wait_loader()

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Valore"]/input')))
        self.send_keys_and_wait(search_input, 'UdMdPdM', wait_modal=False)
        self.wait_for_element_and_click('//tbody//tr//td[2]')

        self.input(None,'Valore').setValue(modifica)
        self.wait_for_element_and_click('//div[@id="tab_0"]//button[@id="save"]')

        self.navigateTo("Unità di misura")
        self.wait_loader()
        self.wait_for_element_and_click('//th[@id="th_Valore"]/i[@class="deleteicon fa fa-times"]')

    def elimina_unita_misura(self):
        self.navigateTo("Unità di misura")
        self.wait_loader()

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Valore"]/input')))
        self.send_keys_and_wait(search_input, 'UdMdPdE', wait_modal=False)
        self.wait_for_element_and_click('//tbody//tr//td[2]')

        self.wait_for_element_and_click('//div[@id="tab_0"]//a[@class="btn btn-danger ask"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')
        self.wait_for_element_and_click('//th[@id="th_Valore"]/i[@class="deleteicon fa fa-times"]')

    def verifica_unita_misura(self):
        self.navigateTo("Unità di misura")
        self.wait_loader()

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Valore"]/input')))
        self.send_keys_and_wait(search_input, "UdMdP", wait_modal=False)
        modificato = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//tbody//tr[1]//td[2]'))).text
        self.assertEqual("UdMdP", modificato)
        self.wait_for_element_and_click('//i[@class="deleteicon fa fa-times"]')

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Valore"]/input')))
        self.send_keys_and_wait(search_input, "UdMdPdE", wait_modal=False)
        eliminato = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//tbody//tr[1]//td[@class="dataTables_empty"]'))).text
        self.assertEqual("Nessun dato presente nella tabella", eliminato)