from common.Test import Test
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Segmenti(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Strumenti")

    def test_creazione_segmenti(self):
        self.navigateTo("Segmenti")

        self.creazione_segmenti("Segmento di Prova da Modificare", "1234/2025", "Articoli")
        self.creazione_segmenti("Segmento di Prova da Eliminare", "1234/2025", "Articoli")
        self.modifica_segmento("Segmento di Prova")
        self.elimina_segmento()
        self.verifica_segmento()

    def creazione_segmenti(self, nome = str, maschera = str, modulo = str):
        self.wait_for_element_and_click('//i[@class="fa fa-plus"]')
        modal = self.wait_modal()

        self.input(modal, 'Nome').setValue(nome)
        self.input(modal, 'Maschera').setValue(maschera)
        self.wait_for_dropdown_and_select('//span[@id="select2-module_add-container"]', option_text=modulo)
        self.wait_for_element_and_click('//div[@class="modal-footer"]//button[@type="submit"]')
        self.wait_loader()

    def modifica_segmento(self, modifica = str):
        self.navigateTo("Segmenti")

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input')))
        self.send_keys_and_wait(search_input, 'Segmento di Prova da Modificare', wait_modal=False)
        self.wait_for_element_and_click('//tbody//tr//td[2]')

        self.input(None,'Nome').setValue(modifica)
        self.wait_for_element_and_click('//div[@id="tab_0"]//button[@id="save"]')

        self.navigateTo("Segmenti")
        self.wait_loader()
        self.wait_for_element_and_click('//th[@id="th_Nome"]/i[@class="deleteicon fa fa-times"]')

    def elimina_segmento(self):
        self.navigateTo("Segmenti")
        self.wait_loader()

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input')))
        self.send_keys_and_wait(search_input, 'Segmento di Prova da Eliminare', wait_modal=False)
        self.wait_for_element_and_click('//tbody//tr//td[2]')

        self.wait_for_element_and_click('//div[@id="tab_0"]//a[@class="btn btn-danger ask"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')
        self.wait_for_element_and_click('//th[@id="th_Nome"]/i[@class="deleteicon fa fa-times"]')

    def verifica_segmento(self):
        self.navigateTo("Segmenti")
        self.wait_loader()

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input')))
        self.send_keys_and_wait(search_input, "Segmento di Prova", wait_modal=False)
        modificato = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//tbody//tr[1]//td[2]'))).text
        self.assertEqual("Segmento di Prova", modificato)
        self.wait_for_element_and_click('//i[@class="deleteicon fa fa-times"]')

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input')))
        self.send_keys_and_wait(search_input, "Segmento di Prova da Eliminare", wait_modal=False)
        eliminato = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//tbody//tr[1]//td[@class="dataTables_empty"]'))).text
        self.assertEqual("La ricerca non ha portato alcun risultato.", eliminato)