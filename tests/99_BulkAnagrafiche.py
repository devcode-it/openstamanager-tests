from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from common.Test import Test

class Anagrafiche(Test):
    def setUp(self):
        super().setUp()
        self.wait_driver = self.wait_driver
        self.navigateTo("Anagrafiche")

    def test_bulk_anagrafica(self):
        self.cambia_relazione()
        self.elimina_selezionati()
        #TODO: Esporta
        #self.esporta_selezionati()
        #TODO: Imposta listino
        #self.imposta_listino()
        self.ricerca_coordinate()
        self.wait_for_element_and_click('//i[@class="fa fa-power-off nav-icon"]')
        
    def cambia_relazione(self):
        self.navigateTo("Anagrafiche")
        self.wait_loader()
        self.search_entity("Cliente")

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_element_and_click('//button[@data-toggle="dropdown"]')
        self.wait_for_element_and_click('//a[@data-op="change_relation"]')

        self.wait_for_dropdown_and_select(
            '//span[@id="select2-idrelazione-container"]',
            option_text="Attivo"
        )
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-warning"]')

        relation = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//tbody//tr//td[7]'))
        ).text
        self.assertEqual(relation, "Attivo")

        self.wait_for_element_and_click('//tbody//tr//td[7]')
        self.wait_for_element_and_click('//span[@id="select2-idrelazione-container"]//span[@class="select2-selection__clear"]')

        search_field = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//input[@class="select2-search__field"])[2]'))
        )
        self.send_keys_and_wait(search_field, "Da contattare", wait_modal=False)
        self.wait_for_element_and_click('//button[@id="save"]')

        self.navigateTo("Anagrafiche")
        self.wait_loader()

        new_relation = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//tbody//tr//td[7]'))
        ).text
        self.assertNotEqual(new_relation, "Attivo")

        self.clear_filters()

    def elimina_selezionati(self):
        self.navigateTo("Anagrafiche")
        self.wait_loader()

        search_input = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Ragione-sociale"]/input'))
        )
        self.send_keys_and_wait(search_input, "Vettore", wait_modal=False)
        self.wait_for_search_results()

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_element_and_click('//button[@data-toggle="dropdown"]')
        self.wait_for_element_and_click('//a[@data-op="delete_bulk"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')

        no_results_message = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//tbody//tr[1]'))
        ).text
        self.assertEqual(no_results_message, "Nessun dato presente nella tabella")

        self.clear_filters()


    def ricerca_coordinate(self):
        self.navigateTo("Anagrafiche")
        self.wait_loader()

        search_input = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Ragione-sociale"]/input'))
        )
        self.send_keys_and_wait(search_input, "Admin spa", wait_modal=False)
        self.wait_for_search_results()

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_element_and_click('//button[@data-toggle="dropdown"]')
        self.wait_for_element_and_click('//a[@data-op="search_coordinates"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-warning"]')

        self.wait_for_element_and_click('//tbody//tr//td[2]')
        self.wait_for_element_and_click('//a[@onclick="modificaPosizione()"]')
        self.wait_for_element_and_click('//ul//li[2]//div')

        latitude = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//input[@id="lat"]'))
        ).text
        self.assertNotEqual(latitude, "0")
        longitude = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//input[@id="lng"]'))
        ).text
        self.assertNotEqual(longitude, "0")

        self.wait_for_element_and_click('//button[@class="close"]')

        self.navigateTo("Anagrafiche")
        self.wait_loader()
        self.clear_filters()