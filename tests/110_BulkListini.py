from common.Test import Test
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Articoli(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Magazzino")
        self.wait_loader()

    def test_bulk_listini(self):
        self.aggiorna_prezzo_unitario()
        self.copia_listini()
        self.wait_for_element_and_click('//i[@class="fa fa-power-off nav-icon"]')
        
    def aggiorna_prezzo_unitario(self):
        self.navigateTo("Articoli")
        self.wait_loader()

        search_input = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Codice"]/input'))
        )
        self.send_keys_and_wait(search_input, '08', wait_modal=False)

        self.click_first_result()
        self.wait_for_element_and_click('//a[@id="link-tab_32"]')

        self.wait_for_dropdown_and_select('//span[@id="select2-id_fornitore_informazioni-container"]', option_text='Fornitore')

        self.wait_for_element_and_click('//button[@class="btn btn-info"]')
        modal = self.wait_modal()

        qta_minima = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//input[@id="qta_minima"]'))
        )
        qta_minima.send_keys("100")

        giorni_consegna = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//input[@id="giorni_consegna"]'))
        )
        giorni_consegna.send_keys("15")

        self.wait_for_element_and_click('//div[@class="modal-content"]//div[@class="btn-group checkbox-buttons"]')

        prezzo_unitario = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario_fisso"]'))
        )
        self.send_keys_and_wait(prezzo_unitario, '15')

        self.navigateTo("Listini")
        self.wait_loader()

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_element_and_click('//button[@data-toggle="dropdown"]')
        self.wait_for_element_and_click('//a[@data-op="change_prezzo"]')

        percentuale_input = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//input[@id="percentuale"]'))
        )
        percentuale_input.send_keys("20")

        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-warning"]')

        prezzo = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//tbody//tr[2]//td[8]'))
        ).text
        self.assertEqual(prezzo, "15,00")

        self.navigateTo("Listini")
        self.wait_loader()

        self.wait_for_element_and_click('//tbody//tr//td')

        self.navigateTo("Articoli")
        self.wait_loader()

        self.wait_for_element_and_click('//tbody//tr//td')
        self.clear_filters()

    def copia_listini(self):
        self.navigateTo("Listini")
        self.wait_loader()

        self.wait_for_dropdown_and_select('//span[@id="select2-id_segment_-container"]', option_text='Fornitori')
        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_element_and_click('//button[@data-toggle="dropdown"]')
        self.wait_for_element_and_click('//a[@data-op="copy_listino"]')

        self.wait_for_dropdown_and_select('//span[@class="select2-selection select2-selection--multiple"]', option_text='Estero')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-warning"]')

        self.wait_for_element_and_click('//tbody//tr//td')

        search_input = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Ragione-sociale"]/input'))
        )
        self.send_keys_and_wait(search_input, 'Fornitore Estero', wait_modal=False)

        articolo = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//tbody//tr//td[2]'))
        ).text
        self.assertEqual(articolo, "08 - Prova")

        self.navigateTo("Articoli")
        self.wait_loader()

        search_input = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Codice"]/input'))
        )
        self.send_keys_and_wait(search_input, '08', wait_modal=False)

        self.click_first_result()
        self.wait_for_element_and_click('//a[@id="link-tab_32"]')
        self.wait_for_element_and_click('//a[@class="btn btn-secondary btn-danger ask"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')
        self.wait_for_element_and_click('//button[@class="btn btn-warning"]')
        self.wait_for_element_and_click('(//label[@class="btn btn-default active"])[4]')
        self.wait_for_element_and_click('//button[@class="btn btn-primary pull-right"]')

        self.navigateTo("Articoli")
        self.wait_loader()
        self.clear_filters()

