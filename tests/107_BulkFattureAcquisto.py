from common.Test import Test
from common.RowManager import RowManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
class FattureAcquisto(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Acquisti")

    def test_bulk_fattura_acquisto(self):
        #TODO: Aggiorna banca
        #self.aggiorna_banca()
        self.cambia_sezionale()
        self.duplica_selezionati()
        self.elimina_selezionati()
        #TODO: Esporta
        #self.esporta_selezionati()
        #TODO: Esporta stampe FE
        #self.esporta_stampe_fe()
        #TODO: Esporta ricevute
        #self.esporta_ricevute()
        #TODO: Esporta XML
        #self.esporta_xml()
        #TODO: Invia fatture
        #self.invia_fatture()
        self.registrazione_contabile()



    def cambia_sezionale(self):
        self.navigateTo("Fatture di acquisto")
        self.wait_for_element_and_click('//i[@class="fa fa-plus"]')
        modal = self.wait_modal()

        numero_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="numero_esterno"]')))
        numero_input.send_keys("2")
        self.wait_for_dropdown_and_select('//span[@id="select2-idanagrafica_add-container"]', option_text='Fornitore')
        self.wait_for_element_and_click('//button[@class="btn btn-primary"]')

        self.navigateTo("Fatture di acquisto")
        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input')))
        self.send_keys_and_wait(search_input, "2", wait_modal=False)

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_dropdown_and_select('//button[@data-toggle="dropdown"]', option_xpath='//a[@data-op="change_segment"]')
        self.wait_for_dropdown_and_select('//span[@id="select2-id_segment-container"]', option_text='Autofatture')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-warning"]')
        self.wait_for_dropdown_and_select('//span[@id="select2-id_segment_-container"]', option_text='Autofatture')

        self.clear_filters()
        self.wait_for_element_and_click('//tbody//tr[1]//td[1]')
        self.wait_for_dropdown_and_select('//button[@data-toggle="dropdown"]', option_xpath='//a[@data-op="change_segment"]')
        self.wait_for_dropdown_and_select('//span[@id="select2-id_segment-container"]', option_text='Standard')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-warning"]')
        self.wait_for_dropdown_and_select('//span[@id="select2-id_segment_-container"]', option_text='Standard')

    def duplica_selezionati(self):
        self.navigateTo("Fatture di acquisto")
        self.wait_for_element_and_click('//tbody//tr//td[1]')
        self.wait_for_dropdown_and_select('//button[@data-toggle="dropdown"]', option_xpath='//a[@data-op="copy_bulk"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-warning"]')

        self.wait_for_element_and_click('//tbody//tr//td[2]')
        self.wait_for_element_and_click('//a[@id="elimina"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')

    def elimina_selezionati(self):
        self.navigateTo("Fatture di acquisto")
        self.wait_loader()

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]//input')))
        self.send_keys_and_wait(search_input, "2", wait_modal=False)

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_dropdown_and_select('//button[@data-toggle="dropdown"]', option_xpath='//a[@data-op="delete_bulk"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')

        scritta = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//tbody//tr//td'))
        ).text
        self.assertEqual(scritta, "Nessun dato presente nella tabella")
        self.clear_filters()

    def registrazione_contabile(self):
        self.navigateTo("Fatture di acquisto")
        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input')))
        self.send_keys_and_wait(search_input, "2", wait_modal=False)
        self.click_first_result()

        self.driver.execute_script('window.scrollTo(0,0)')
        numero_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="numero_esterno"]')))
        numero_input.send_keys("2")

        self.wait_for_element_and_click('//a[@class="btn btn-primary"]')

        descrizione_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]')))
        descrizione_input.send_keys("Prova")
        prezzo_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]')))
        prezzo_input.send_keys("1")
        self.wait_for_element_and_click('//button[@class="btn btn-primary pull-right"]')

        self.input(None,'Stato*').setByText('Emessa')
        self.wait_for_element_and_click('//button[@id="save"]')

        self.navigateTo("Fatture di acquisto")
        self.wait_for_element_and_click('//tbody//tr//td[1]')
        self.wait_for_element_and_click('//button[@data-toggle="dropdown"]')
        self.wait_for_element_and_click('//a[@data-op="registrazione_contabile"]')

        prezzo = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="totale_avere_add"]'))).text
        self.assertEqual(prezzo, "1,22 €")
        self.wait_for_dropdown_and_select('//span[@id="select2-conto_add_1-container"]', option_text='Banca C/C')

        self.wait_for_element_and_click('//button[@id="add-submit"]')

        self.expandSidebar("Acquisti")
        self.navigateTo("Fatture di acquisto")
        self.wait_loader()
        self.clear_filters()

