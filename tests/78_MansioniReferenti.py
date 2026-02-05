from common.Test import Test
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class MansioniReferenti(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Strumenti")
        self.expandSidebar("Tabelle")
        self.navigateTo("Mansioni referenti")

    def test_creazione_mansioni_referenti(self):
        self.creazione_mansioni_referenti("Mansione Referente di Prova da Modificare")
        self.creazione_mansioni_referenti("Mansione Referente di Prova da Eliminare")
        self.modifica_mansione_referente("Mansione Referente di Prova")
        self.elimina_mansione_referente()
        self.verifica_mansione_referente()
        self.wait_for_element_and_click('//i[@class="fa fa-power-off nav-icon"]')
        
    def creazione_mansioni_referenti(self, mansione= str):
        self.wait_for_element_and_click('//i[@class="fa fa-plus"]')
        modal = self.wait_modal()

        self.input(modal, 'Mansione').setValue(mansione)
        self.wait_for_element_and_click('//div[@class="modal-footer"]//button[@type="submit"]')

    def modifica_mansione_referente(self, modifica = str):
        self.navigateTo("Mansioni referenti")
        self.wait_loader()

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input')))
        self.send_keys_and_wait(search_input, 'Mansione Referente di Prova da Modificare', wait_modal=False)
        self.wait_for_element_and_click('//tbody//tr//td[2]')

        self.input(None,'Nome').setValue(modifica)
        self.wait_for_element_and_click('//div[@id="tab_0"]//button[@id="save"]')

        self.navigateTo("Mansioni referenti")
        self.wait_loader()
        self.wait_for_element_and_click('//th[@id="th_Nome"]/i[@class="deleteicon fa fa-times"]')

    def elimina_mansione_referente(self):
        self.navigateTo("Mansioni referenti")
        self.wait_loader()

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input')))
        self.send_keys_and_wait(search_input, 'Mansione Referente di Prova da Eliminare', wait_modal=False)
        self.wait_for_element_and_click('//tbody//tr//td[2]')

        self.wait_for_element_and_click('//a[@class="btn btn-danger ask "]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')
        self.wait_for_element_and_click('//th[@id="th_Nome"]/i[@class="deleteicon fa fa-times"]')

    def verifica_mansione_referente(self):
        self.navigateTo("Mansioni referenti")
        self.wait_loader()

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input')))
        self.send_keys_and_wait(search_input, "Mansione Referente di Prova", wait_modal=False)
        modificato = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//tbody//tr[1]//td[2]'))).text
        self.assertEqual("Mansione Referente di Prova", modificato)
        self.wait_for_element_and_click('//i[@class="deleteicon fa fa-times"]')

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input')))
        self.send_keys_and_wait(search_input, "Mansione Referente di Prova da Eliminare", wait_modal=False)
        eliminato = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//tbody//tr[1]//td[@class="dataTables_empty"]'))).text
        self.assertEqual("Nessun dato presente nella tabella", eliminato)