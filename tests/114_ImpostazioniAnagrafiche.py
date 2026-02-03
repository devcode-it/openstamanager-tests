from common.Test import Test
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Impostazioni(Test):
    def setUp(self):
        super().setUp()
        self.navigateTo("Anagrafiche")
        self.wait_loader()

    def test_impostazioni_anagrafiche(self):
        self.cambio_formato_codice()

    def cambio_formato_codice(self):
        self._crea_anagrafica_test("00000010")
        self._elimina_anagrafica()
        self._cambia_formato_codice("####")
        self._crea_anagrafica_test("0010")
        self._elimina_anagrafica()
        self._cambia_formato_codice("########")

    def _crea_anagrafica_test(self, codice_atteso):
        self.wait_for_element_and_click('//i[@class="fa fa-plus"]')

        ragione_sociale_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="ragione_sociale_add"]')))
        ragione_sociale_input.send_keys('Test')

        self.wait_for_element_and_click('//span[@class="select2-selection select2-selection--multiple"]')
        self.wait_for_element_and_click('//ul[@id="select2-idtipoanagrafica_add-results"]//li[5]')
        self.wait_for_element_and_click('//button[@class="btn btn-primary"]')

        codice_element = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="codice"]')))
        codice = codice_element.get_attribute("value")
        self.assertEqual(codice, codice_atteso)

    def _elimina_anagrafica(self):
        self.wait_for_element_and_click('//a[@class="btn btn-danger ask"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')

    def _cambia_formato_codice(self, formato):
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.wait_for_element_and_click('//div[@data-title="Anagrafiche"]')

        formato_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="form-group" and contains(., "Formato codice anagrafica")]//input')))
        formato_input.clear()
        formato_input.send_keys(formato, Keys.ENTER)

        self.navigateTo("Anagrafiche")
        self.wait_loader()

