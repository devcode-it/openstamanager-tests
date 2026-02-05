from common.Test import Test
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class ModelliPrimaNota(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Strumenti")
        self.expandSidebar("Tabelle")

    def test_creazione_modelli_prima_nota(self):
        self.creazione_modelli_prima_nota(nome="Modello Prima Nota di Prova da Modificare", causale="Prova anticipo fattura num. {numero} del {data}")
        self.creazione_modelli_prima_nota(nome="Modello Prima Nota di Prova da Eliminare", causale="Prova anticipo fattura num. {numero} del {data}")
        self.modifica_modello_prima_nota("Modello Prima Nota di Prova")
        self.elimina_modello_prima_nota()
        self.verifica_modello_prima_nota()
        self.wait_for_element_and_click('//i[@class="fa fa-power-off nav-icon"]')
        
    def creazione_modelli_prima_nota(self, nome = str, causale = str):
        self.navigateTo("Modelli prima nota")
        self.wait_loader()

        self.wait_for_element_and_click('//i[@class="fa fa-plus"]')
        modal = self.wait_modal()

        self.input(modal, 'Nome').setValue(nome)
        self.input(modal, 'Causale').setValue(causale)

        self.wait_for_element_and_click('//span[@id="select2-conto0-container"]')
        self.wait_for_element_and_click('//li[@class="select2-results__option select2-results__option--highlighted"]')

        self.wait_for_element_and_click('//span[@id="select2-conto1-container"]')
        self.wait_for_element_and_click('//input[@class="select2-search__field"]')
        self.wait_for_element_and_click('//li[@class="select2-results__option select2-results__option--highlighted"]')
        self.wait_loader()

        self.wait_for_element_and_click('button[type="submit"]', By.CSS_SELECTOR)

    def modifica_modello_prima_nota(self, modifica = str):
        self.navigateTo("Modelli prima nota")
        self.wait_loader()

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input')))
        self.send_keys_and_wait(search_input, 'Modello Prima Nota di Prova da Modificare', wait_modal=False)
        self.wait_for_element_and_click('//tbody//tr//td[2]')

        self.input(None,'Nome').setValue(modifica)
        self.wait_for_element_and_click('//div[@id="tab_0"]//button[@id="save"]')

        self.navigateTo("Modelli prima nota")
        self.wait_loader()
        self.wait_for_element_and_click('//th[@id="th_Nome"]/i[@class="deleteicon fa fa-times"]')

    def elimina_modello_prima_nota(self):
        self.navigateTo("Modelli prima nota")
        self.wait_loader()

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input')))
        self.send_keys_and_wait(search_input, 'Modello Prima Nota di Prova da Eliminare', wait_modal=False)
        self.wait_for_element_and_click('//tbody//tr//td[2]')

        self.wait_for_element_and_click('//div[@id="tab_0"]//a[@class="btn btn-danger ask"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')
        self.wait_for_element_and_click('//th[@id="th_Nome"]/i[@class="deleteicon fa fa-times"]')

    def verifica_modello_prima_nota(self):
        self.navigateTo("Modelli prima nota")
        self.wait_loader()

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input')))
        self.send_keys_and_wait(search_input, "Modello Prima Nota di Prova", wait_modal=False)
        modificato = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//tbody//tr[1]//td[2]'))).text
        self.assertEqual("Modello Prima Nota di Prova", modificato)
        self.wait_for_element_and_click('//i[@class="deleteicon fa fa-times"]')

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input')))
        self.send_keys_and_wait(search_input, "Modello Prima Nota di Prova da Eliminare", wait_modal=False)
        eliminato = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//tbody//tr[1]//td[@class="dataTables_empty"]'))).text
        self.assertEqual("Nessun dato presente nella tabella", eliminato)