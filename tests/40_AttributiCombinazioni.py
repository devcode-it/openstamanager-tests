from common.Test import Test
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class AttributiCombinazioni(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Magazzino")

    def test_creazione_attributi(self):
        self.creazione_attributi("Attributo di Prova da Modificare")
        self.creazione_attributi("Attributo di Prova da Eliminare")
        self.modifica_attributi("Taglie")
        self.elimina_attributi()
        self.verifica_attributi()

    def creazione_attributi(self, titolo=str):
        self.navigateTo("Attributi Combinazioni")
        self.wait_loader()

        self.wait_for_element_and_click('//i[@class="fa fa-plus"]')
        modal = self.wait_modal()

        self.input(modal, 'Titolo').setValue(titolo)
        self.wait_for_element_and_click('button[type="submit"]', By.CSS_SELECTOR)

        self.wait_for_element_and_click('//button[@onclick="aggiungiValore(this)"]')
        modal = self.wait_modal()
        nome_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="nome"]')))
        self.send_keys_and_wait(nome_input, 'S')

        self.wait_for_element_and_click('//button[@onclick="aggiungiValore(this)"]')
        self.wait_modal()
        nome_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="nome"]')))
        self.send_keys_and_wait(nome_input, 'M')

        self.wait_for_element_and_click('//button[@onclick="aggiungiValore(this)"]')
        self.wait_modal()
        nome_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="nome"]')))
        self.send_keys_and_wait(nome_input, 'L')

    def modifica_attributi(self, modifica=str):
        self.navigateTo("Attributi Combinazioni")
        self.wait_loader()

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input')))
        self.send_keys_and_wait(search_input, 'Attributo di Prova da Modificare', wait_modal=False)

        self.wait_for_element_and_click('//tbody//tr//td[2]')

        self.input(None, 'Titolo').setValue(modifica)
        self.wait_for_element_and_click('//div[@id="tab_0"]//button[@id="save"]')

        self.navigateTo("Attributi Combinazioni")
        self.wait_loader()
        self.wait_for_element_and_click('//th[@id="th_Nome"]/i[@class="deleteicon fa fa-times"]')

    def elimina_attributi(self):
        self.navigateTo("Attributi Combinazioni")
        self.wait_loader()

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input')))
        self.send_keys_and_wait(search_input, 'Attributo di Prova da Eliminare', wait_modal=False)

        self.wait_for_element_and_click('//tbody//tr//td[2]')
        self.wait_for_element_and_click('//div[@id="tab_0"]//a[@class="btn btn-danger ask"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')

        self.wait_for_element_and_click('//th[@id="th_Nome"]/i[@class="deleteicon fa fa-times"]')

    def verifica_attributi(self):
        self.navigateTo("Attributi Combinazioni")
        self.wait_loader()

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input')))
        self.send_keys_and_wait(search_input, "Taglie", wait_modal=False)

        modificato = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//tbody//tr[1]//td[2]'))).text
        self.assertEqual("Taglie", modificato)

        self.wait_for_element_and_click('//i[@class="deleteicon fa fa-times"]')

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input')))
        self.send_keys_and_wait(search_input, "Attributo di Prova da Eliminare", wait_modal=False)

        eliminato = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//tbody//tr[1]//td[@class="dataTables_empty"]'))).text
        self.assertEqual("La ricerca non ha portato alcun risultato.", eliminato)
