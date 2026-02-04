from common.Test import Test
from common.RowManager import RowManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class FattureVendita(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Vendite")

    def test_bulk_fattura_vendita(self):
        #TODO: Aggiorna banca
        #self.aggiorna_banca()
        self.cambia_sezionale()
        self.controlla_fatture_elettroniche()
        self.duplica_selezionati()
        self.elimina_selezionati()
        self.emetti_fatture()
        #TODO: Esporta
        #self.esporta_selezionati()
        #TODO: Esporta stampe
        #self.esporta_stampe()
        #TODO: Esporta stampe FE
        #self.esporta_stampe_fe()
        #TODO: Esporta ricevute
        #self.esporta_ricevute()
        #TODO: Esporta XML
        #self.esporta_xml()
        self.genera_fatture_elettroniche()
        #TODO: Invia fatture
        #self.invia_fatture()
        self.registrazione_contabile()





    def cambia_sezionale(self):
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_element_and_click('//button[@data-toggle="dropdown"]')
        self.wait_for_element_and_click('//a[@data-op="change_segment"]')

        self.wait_for_dropdown_and_select(
            '//span[@id="select2-id_segment-container"]',
            option_text='Autofatture'
        )
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-warning"]')
        self.wait_for_dropdown_and_select(
            '//span[@id="select2-id_segment_-container"]',
            option_text='Autofatture'
        )

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_element_and_click('//button[@data-toggle="dropdown"]')
        self.wait_for_element_and_click('//a[@data-op="change_segment"]')

        self.wait_for_dropdown_and_select(
            '//span[@id="select2-id_segment-container"]',
            option_text='Standard vendite'
        )
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-warning"]')
        self.wait_for_dropdown_and_select(
            '//span[@id="select2-id_segment_-container"]',
            option_text='Standard vendite'
        )
    
    def controlla_fatture_elettroniche(self):
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_element_and_click('//button[@data-toggle="dropdown"]')
        self.wait_for_element_and_click('//a[@data-op="check_bulk"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-warning"]')

        self.driver.switch_to.window(self.driver.window_handles[1])
        self.wait_for_element_and_click('//div[@class="toast toast-success"]')
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

    def duplica_selezionati(self):
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_element_and_click('//button[@data-toggle="dropdown"]')
        self.wait_for_element_and_click('//a[@data-op="copy_bulk"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-warning"]')
        self.wait_for_element_and_click('//tbody//tr//td')

    def elimina_selezionati(self):
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_element_and_click('//button[@data-toggle="dropdown"]')
        self.wait_for_element_and_click('//a[@data-op="delete_bulk"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')

        test = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//tbody//tr//td[2]'))).text
        self.assertEqual(test, "0002/2026")

    def emetti_fatture(self):
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_element_and_click('//button[@data-toggle="dropdown"]')
        self.wait_for_element_and_click('//a[@data-op="change_status"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-warning"]')

        stato = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//tbody//tr//td[11]'))).text
        self.assertEqual(stato, "Emessa")
        self.wait_for_element_and_click('//tbody//tr//td')

    def genera_fatture_elettroniche(self):
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_element_and_click('//button[@data-toggle="dropdown"]')
        self.wait_for_element_and_click('//a[@data-op="generate_xml"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-warning"]')

        self.driver.switch_to.window(self.driver.window_handles[1])

        self.wait_for_element_and_click('//tbody//tr//td[2]')
        self.wait_for_element_and_click('//button[@class="btn btn-xs btn-info"]')
        self.wait_for_element_and_click('//button[@class="close"]')

        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

        self.navigateTo("Fatture di vendita")
        self.wait_loader()
        self.wait_for_element_and_click('//tbody//tr//td')

    def registrazione_contabile(self):
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input')))
        self.send_keys_and_wait(search_input, "0001", wait_modal=False)

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_element_and_click('//button[@data-toggle="dropdown"]')
        self.wait_for_element_and_click('//a[@data-op="registrazione_contabile"]')

        totale = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="totale_dare_add"]'))).text
        self.assertEqual(totale, "305,98 €")

        self.wait_for_element_and_click('//button[@type="submit"]')

        self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")
        self.wait_loader()
        self.wait_for_element_and_click('//i[@class="deleteicon fa fa-times"]')

