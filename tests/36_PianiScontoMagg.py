from common.Test import Test
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class PianiScontoMagg(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Magazzino")

    def test_creazione_piano_sconto_magg(self):
        self.creazione_piano_sconto_magg("Piano di sconto di Prova da Modificare", "10")
        self.creazione_piano_sconto_magg("Piano di sconto di Prova da Eliminare", "5")
        self.modifica_piano_sconto("Piano di sconto di Prova")
        self.elimina_piano_sconto()
        self.verifica_piano_sconto()
        self.plugin_sconto_maggiorazione()
        self.wait_for_element_and_click('//i[@class="fa fa-power-off nav-icon"]')

    def creazione_piano_sconto_magg(self, nome: str, sconto: str):
        self.navigateTo("Piani di sconto/magg.")
        self.wait_for_element_and_click('//i[@class="fa fa-plus"]')
        modal = self.wait_modal()

        self.input(modal, 'Nome').setValue(nome)
        self.input(modal, 'Sconto/magg. combinato').setValue(sconto)
        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        self.wait_loader()

    def modifica_piano_sconto(self, modifica=str):
        self.navigateTo("Piani di sconto/magg.")
        self.wait_loader()

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input')))
        self.send_keys_and_wait(search_input, 'Piano di sconto di Prova da Modificare', wait_modal=False)
        self.wait_for_element_and_click('//tbody//tr//td[2]')

        self.input(None, 'Nome').setValue(modifica)
        self.wait_for_element_and_click('//div[@id="tab_0"]//button[@id="save"]')

        self.navigateTo("Piani di sconto/magg.")
        self.wait_loader()
        self.clear_filters()

    def elimina_piano_sconto(self):
        self.navigateTo("Piani di sconto/magg.")
        self.wait_loader()

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input')))
        self.send_keys_and_wait(search_input, 'Piano di sconto di Prova da Eliminare', wait_modal=False)
        self.wait_for_element_and_click('//tbody//tr//td[2]')

        self.wait_for_element_and_click('//div[@id="tab_0"]//a[@class="btn btn-danger ask"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')
        self.clear_filters()

    def verifica_piano_sconto(self):
        self.navigateTo("Piani di sconto/magg.")
        self.wait_loader()

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input')))
        self.send_keys_and_wait(search_input, "Piano di sconto di Prova", wait_modal=False)
        modificato = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//tbody//tr[1]//td[2]'))).text
        self.assertEqual("Piano di sconto di Prova", modificato)
        self.clear_filters()

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input')))
        self.send_keys_and_wait(search_input, "Piano di sconto di Prova da Eliminare", wait_modal=False)
        eliminato = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//tbody//tr[1]//td[@class="dataTables_empty"]'))).text
        self.assertEqual("Nessun dato presente nella tabella", eliminato)

    def plugin_sconto_maggiorazione(self):
        self.navigateTo("Articoli")
        self.wait_loader()

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input')))
        self.send_keys_and_wait(search_input, 'Articolo 1', wait_modal=False)
        self.wait_for_element_and_click('//tbody//td[2]//div[1]')
        self.wait_for_element_and_click('//a[@id="link-tab_33"]')

        prezzo_nuovo = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '(//div[@id="tab_33"]//tr[3]//td[2])[2]'))).text
        self.assertEqual(prezzo_nuovo, "18,00 €")

        self.navigateTo("Articoli")
        self.wait_loader()
        self.clear_filters()