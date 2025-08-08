from common.Test import Test
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Listini(Test):
    def setUp(self):
        super().setUp()
        self.navigateTo("Magazzino")

    def test_creazione_listino_cliente(self):
        self.navigateTo("Listini cliente")
        self.wait_loader()

        self.creazione_listino_cliente("Listino cliente di Prova da Modificare","01/12/2025", "01/01/2025")
        self.creazione_listino_cliente("Listino cliente di Prova da Eliminare", "01/12/2025", "01/01/2025")
        self.modifica_listino_cliente("Listino cliente di Prova")
        self.elimina_listino_cliente()
        self.verifica_listino_cliente()
        self.aggiorna_listino_cliente()
        self.aggiungi_a_listino_cliente()

    def creazione_listino_cliente(self, nome:str, dataatt: str, datascad: str):
        self.wait_for_element_and_click('//i[@class="fa fa-plus"]')
        modal = self.wait_modal()

        self.input(modal, 'Data attivazione').setValue(dataatt)
        self.input(modal, 'Data scadenza default').setValue(datascad)
        self.input(modal, 'Nome').setValue(nome)
        self.wait_for_element_and_click('//div[@class="modal-footer"]//button[@type="submit"]')

    def modifica_listino_cliente(self, modifica:str):
        self.navigateTo("Listini cliente")
        self.wait_loader()

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input')))
        self.send_keys_and_wait(search_input, 'Listino cliente di Prova da Modificare', wait_modal=False)
        self.wait_for_element_and_click('//tbody//tr//td[2]')

        self.wait_for_dropdown_and_select('//span[@class="select2-selection select2-selection--single"]', option_text='001')

        self.wait_for_element_and_click('//button[@class="btn btn-success btn-block"]')

        prezzo_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]')))
        prezzo_input.send_keys("10,00")
        sconto_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="sconto_percentuale"]')))
        sconto_input.send_keys("10")
        self.wait_for_element_and_click('(//button[@class="btn btn-success"])[2]')

        self.input(None,'Nome').setValue(modifica)
        self.wait_for_element_and_click('//button[@id="save"]')
        self.wait_for_element_and_click('//a[@id="back"]')
        self.wait_for_element_and_click('//th[@id="th_Nome"]/i[@class="deleteicon fa fa-times"]')

    def elimina_listino_cliente(self):
        self.navigateTo("Listini cliente")
        self.wait_loader()

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input')))
        self.send_keys_and_wait(search_input, 'Listino cliente di Prova da Eliminare', wait_modal=False)
        self.wait_for_element_and_click('//tbody//tr//td[2]')

        self.wait_for_element_and_click('//div[@id="tab_0"]//a[@class="btn btn-danger ask"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')
        self.wait_for_element_and_click('//th[@id="th_Nome"]/i[@class="deleteicon fa fa-times"]')

    def verifica_listino_cliente(self):
        self.navigateTo("Listini cliente")
        self.wait_loader()

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input')))
        self.send_keys_and_wait(search_input, "Listino cliente di Prova", wait_modal=False)
        modificato = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//tbody//tr[1]//td[2]'))).text
        self.assertEqual("Listino cliente di Prova", modificato)
        self.wait_for_element_and_click('//i[@class="deleteicon fa fa-times"]')

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input')))
        self.send_keys_and_wait(search_input, "Listino cliente di Prova da Eliminare", wait_modal=False)
        eliminato = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//tbody//tr[1]//td[1]'))).text
        self.assertEqual("La ricerca non ha portato alcun risultato.", eliminato)
        self.wait_for_element_and_click('//th[@id="th_Nome"]/i[@class="deleteicon fa fa-times"]')

    def aggiorna_listino_cliente(self):
        self.navigateTo("Anagrafiche")
        self.wait_loader()

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Ragione-sociale"]/input')))
        self.send_keys_and_wait(search_input, "Cliente", wait_modal=False)

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_element_and_click('//button[@data-toggle="dropdown"]')
        self.wait_for_element_and_click('//a[@data-op="update_price_list"]')

        self.wait_for_dropdown_and_select('//span[@id="select2-id_listino-container"]', option_text='Listino cliente di Prova')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-warning"]')

        self.wait_for_element_and_click('//tbody//tr//td[2]')
        self.wait_loader()

        self.wait_for_element_and_click('(//span[@class="select2-selection__clear"])[4]')
        self.wait_for_element_and_click('//button[@id="save"]')
        self.wait_loader()

        self.navigateTo("Anagrafiche")
        self.wait_loader()
        self.wait_for_element_and_click('//th[@id="th_Ragione-sociale"]/i[@class="deleteicon fa fa-times"]')
        self.navigateTo("Magazzino")

    def aggiungi_a_listino_cliente(self):
        self.navigateTo("Articoli")
        self.wait_loader()

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Codice"]/input')))
        self.send_keys_and_wait(search_input, "001", wait_modal=False)

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_element_and_click('//button[@data-toggle="dropdown"]')
        self.wait_for_element_and_click('//a[@data-op="add_price_list"]')

        self.wait_for_element_and_click('//span[@id="select2-id_listino-container"]')
        self.wait_for_element_and_click('//li[@class="select2-results__option select2-results__option--highlighted"]')

        sconto_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="sconto_percentuale"]')))
        sconto_input.send_keys("10")
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-warning"]')

        self.navigateTo("Listini cliente")
        self.wait_loader()

        self.wait_for_element_and_click('//tbody//tr//td[2]')
        self.wait_loader()

        self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//tr[1]//td[8]')))
        self.wait_for_element_and_click('//tr[1]//td[9]//a[2]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-primary"]')
