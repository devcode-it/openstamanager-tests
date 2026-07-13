from common.Test import Test
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

class Impostazioni(Test):
    def setUp(self):
        super().setUp()
        self.navigate_to_and_wait("Anagrafiche")

    def test_impostazioni_anagrafiche(self):
        self.cambio_formato_codice()
        self.geolocalizzazione()
        
    def cambio_formato_codice(self):
        self._crea_anagrafica_test("00000010")
        self._elimina_anagrafica()
        self._cambia_formato_codice("####")
        self._crea_anagrafica_test("0010")
        self._elimina_anagrafica()
        self._cambia_formato_codice("########")

    def geolocalizzazione(self):
        self._crea_anagrafica_geolocalizzazione("Via Roma 1, Milano")
        self._elimina_anagrafica()
        self._crea_anagrafica_geolocalizzazione("Piazza Duomo, Milano")
        self._elimina_anagrafica()

    def _crea_anagrafica_test(self, codice_atteso):
        self.click_add_button()

        modal = self.wait_modal()
        ragione_sociale_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="ragione_sociale_add"]')))
        ragione_sociale_input.send_keys('Test')

        self.wait_for_dropdown_and_select('//span[@class="select2-selection select2-selection--multiple"]')
        self.wait_for_element_and_click('//ul[@id="select2-id_tipo_anagrafica_add-results"]//li[5]')
        self.wait_for_element_and_click('//button[@class="btn btn-primary"]')

        codice_element = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="codice"]')))
        codice = codice_element.get_attribute("value")
        self.assertEqual(codice, codice_atteso)

    def _crea_anagrafica_geolocalizzazione(self, indirizzo):
        self.click_add_button()

        modal = self.wait_modal()
        ragione_sociale_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="ragione_sociale_add"]')))
        ragione_sociale_input.send_keys('Test Geolocalizzazione')

        self.wait_for_dropdown_and_select('//span[@class="select2-selection select2-selection--multiple"]')
        self.wait_for_element_and_click('//ul[@id="select2-id_tipo_anagrafica_add-results"]//li[5]')
        self.wait_for_element_and_click('//button[@class="btn btn-primary"]')

        indirizzo_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="indirizzo"]')))
        indirizzo_input.send_keys(indirizzo)

    def _elimina_anagrafica(self):
        self.delete_current_and_clear()

    def _cambia_formato_codice(self, formato):
        self.expandSidebar("Strumenti")
        self.navigate_to_and_wait("Impostazioni")

        self.wait_for_element_and_click('//div[@data-title="Anagrafiche"]')

        formato_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="form-group" and contains(., "Formato codice anagrafica")]//input')))
        formato_input.clear()
        self.send_keys_and_wait(formato_input, formato, wait_modal=False)

        self.navigate_to_and_wait("Anagrafiche")

