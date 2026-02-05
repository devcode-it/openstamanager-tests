from common.Test import Test
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Adattatori(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Strumenti")

    def test_creazione_adattatore(self):
        self.navigateTo("Adattatori di archiviazione")

        self.creazione_adattatore("Adattatore di Prova da Modificare", "Archiviazione FTP")
        self.creazione_adattatore("Adattatore di Prova da Eliminare", "Archiviazione FTP")
        self.modifica_adattatore("Adattatore di Prova")
        self.elimina_adattatore()
        self.verifica_adattatore()
        self.wait_for_element_and_click('//i[@class="fa fa-power-off nav-icon"]')
        
    def creazione_adattatore(self, nome: str, tipo: str):
        self.wait_for_element_and_click('//i[@class="fa fa-plus"]')
        modal = self.wait_modal()

        self.input(modal, 'Nome').setValue(nome)
        self.wait_for_dropdown_and_select('//span[@id="select2-class_add-container"]', option_text=tipo)
        self.wait_for_element_and_click('//div[@class="modal-footer"]//button[@type="submit"]')

    def modifica_adattatore(self, modifica = str):
        self.navigateTo("Adattatori di archiviazione")
        self.wait_loader()

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input')))
        self.send_keys_and_wait(search_input, 'Adattatore di Prova da Modificare', wait_modal=False)
        self.click_first_result()

        self.input(None,'Nome').setValue(modifica)
        self.wait_for_element_and_click('//div[@id="tab_0"]//button[@id="save"]')

        self.navigateTo("Adattatori di archiviazione")
        self.wait_loader()
        self.wait_for_element_and_click('//th[@id="th_Nome"]/i[@class="deleteicon fa fa-times"]')

    def elimina_adattatore(self):
        self.navigateTo("Adattatori di archiviazione")
        self.wait_loader()

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input')))
        self.send_keys_and_wait(search_input, 'Adattatore di Prova da Eliminare', wait_modal=False)
        self.click_first_result()

        self.wait_for_element_and_click('//div[@id="tab_0"]//a[@class="btn btn-danger ask"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')
        self.wait_for_element_and_click('//th[@id="th_Nome"]/i[@class="deleteicon fa fa-times"]')

    def verifica_adattatore(self):
        self.navigateTo("Adattatori di archiviazione")
        self.wait_loader()

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input')))
        self.send_keys_and_wait(search_input, "Adattatore di Prova", wait_modal=False)
        modificato = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//tbody//tr[1]//td[2]'))).text
        self.assertEqual("Adattatore di Prova", modificato)
        self.wait_for_element_and_click('//i[@class="deleteicon fa fa-times"]')

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input')))
        self.send_keys_and_wait(search_input, "Adattatore di Prova da Eliminare", wait_modal=False)
        eliminato = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//tbody//tr[1]//td[@class="dataTables_empty"]'))).text
        self.assertEqual("Nessun dato presente nella tabella", eliminato)