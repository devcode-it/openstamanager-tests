from common.Test import Test
from common.RowManager import RowManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class DdtUscita(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Magazzino")

    def test_creazione_ddt_uscita(self):
        importi = RowManager.list()
        self.creazione_ddt_uscita("Cliente", "2", importi[0])
        self.duplica_ddt_uscita()
        self.modifica_ddt("Evaso")
        self.elimina_ddt()
        self.verifica_ddt()
        self.ddt_del_cliente()
        self.cambia_stato()
        self.fattura_ddt_uscita()

        self.duplica_ddt_uscita()
        self.elimina_selezionati()

    def creazione_ddt_uscita(self, cliente: str, causale: str, file_importi: str):
        self.navigateTo("Ddt in uscita")
        self.wait_for_element_and_click( '//i[@class="fa fa-plus"]')
        modal = self.wait_modal()

        select = self.input(modal, 'Destinatario')
        select.setByText(cliente)
        select = self.input(modal, 'Causale trasporto')
        select.setByIndex(causale)
        self.wait_for_element_and_click( 'button[type="submit"]', By.CSS_SELECTOR)

        row_manager = RowManager(self)
        self.valori = row_manager.compile(file_importi)

    def duplica_ddt_uscita(self):
        self.navigateTo("Ddt in uscita")
        self.click_first_result()

        self.wait_for_element_and_click( '//button[@class="btn btn-primary ask"]')
        self.wait_for_element_and_click( '//button[@class="swal2-confirm btn btn-lg btn-primary"]')

    def modifica_ddt(self, modifica):
        self.navigateTo("Ddt in uscita")
        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input')))
        self.send_keys_and_wait( search_input, '01', False)
        self.click_first_result()

        self.driver.execute_script('window.scrollTo(0,0)')
        self.wait_for_dropdown_and_select( '//span[@id="select2-idstatoddt-container"]', option_text='Evaso')
        self.wait_for_element_and_click( '//div[@id="tab_0"]//button[@id="save"]')

        sconto = self.find(By.XPATH, '//div[@id="righe"]//tbody[2]//tr[2]//td[2]').text
        totale_imponibile = self.find(By.XPATH, '//div[@id="righe"]//tbody[2]//tr[3]//td[2]').text
        iva = self.find(By.XPATH, '//div[@id="righe"]//tbody[2]//tr[4]//td[2]').text
        totale = self.find(By.XPATH, '//div[@id="tab_0"]//div[@id="righe"]//tbody[2]//tr[5]//td[2]').text

        self.assertEqual(sconto, (self.valori["Sconto/maggiorazione"] + ' €'))
        self.assertEqual(totale_imponibile, (self.valori["Totale imponibile"] + ' €'))
        self.assertEqual(iva, (self.valori["IVA"] + ' €'))
        self.assertEqual(totale, (self.valori["Totale documento"] + ' €'))

        self.navigateTo("Ddt in uscita")
        self.clear_filters()

    def elimina_ddt(self):
        self.navigateTo("Ddt in uscita")
        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input')))
        self.send_keys_and_wait( search_input, '02', False)

        self.click_first_result()
        self.wait_for_element_and_click( '//div[@id="tab_0"]//a[@class="btn btn-danger ask"]')
        self.wait_for_element_and_click( '//button[@class="swal2-confirm btn btn-lg btn-danger"]')
        self.clear_filters()

    def verifica_ddt(self):
        self.navigateTo("Ddt in uscita")
        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input')))
        self.send_keys_and_wait( search_input, "01", False)

        modificato = self.driver.find_element(By.XPATH, '//tbody//tr[1]//td[11]').text
        self.assertEqual("Evaso", modificato)
        self.wait_for_element_and_click( '//i[@class="deleteicon fa fa-times"]')

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input')))
        self.send_keys_and_wait( search_input, "02", False)

        eliminato = self.driver.find_element(By.XPATH, '//tbody//tr[1]//td[@class="dataTables_empty"]').text
        self.assertEqual("La ricerca non ha portato alcun risultato.", eliminato)
        self.wait_for_element_and_click( '//i[@class="deleteicon fa fa-times"]')

    def ddt_del_cliente(self):
        self.navigateTo("Anagrafiche")
        self.wait_loader()

        self.search_entity( "Cliente")
        self.click_first_result()

        self.wait_for_element_and_click( '//a[@id="link-tab_17"]')
        self.wait_for_element_and_click( '//tbody//tr[10]//td[2]')

    def cambia_stato(self):
        self.navigateTo("Ddt in uscita")
        self.wait_loader()

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input')))
        self.send_keys_and_wait( search_input, "01", False)

        self.wait_for_element_and_click( '//tbody//tr//td')
        self.wait_for_element_and_click( '//button[@data-toggle="dropdown"]')
        self.wait_for_element_and_click( '//a[@data-op="change_status"]')

        self.wait_for_dropdown_and_select( '//span[@id="select2-id_stato-container"]', option_text='Evaso')
        self.wait_for_element_and_click( '//button[@class="swal2-confirm btn btn-lg btn-warning"]')

        stato = self.find(By.XPATH, '(//tr[1]//td[11]//span)[2]').text
        self.assertEqual(stato, "Evaso")
        self.wait_for_element_and_click( '//i[@class="deleteicon fa fa-times"]')

    def fattura_ddt_uscita(self):
        self.navigateTo("Ddt in uscita")
        self.wait_loader()

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input')))
        self.send_keys_and_wait( search_input, "01", False)

        self.wait_for_element_and_click( '//tbody//tr//td')
        self.wait_for_element_and_click( '//button[@data-toggle="dropdown"]')
        self.wait_for_element_and_click( '//a[@data-op="create_invoice"]')

        self.wait_for_dropdown_and_select( '//span[@id="select2-raggruppamento-container"]', option_text='Cliente')
        self.wait_for_element_and_click( '//button[@class="swal2-confirm btn btn-lg btn-warning"]')

        self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        tipo = self.find(By.XPATH, '//tbody//tr[3]//td[4]').text
        self.assertEqual(tipo, "Cliente")

        self.wait_for_element_and_click( '//tbody//tr[3]//td[5]')
        self.wait_for_element_and_click( '//div[@id="tab_0"]//a[@class="btn btn-danger ask "]')
        self.wait_for_element_and_click( '//button[@class="swal2-confirm btn btn-lg btn-danger"]')

        self.expandSidebar("Magazzino")
        self.navigateTo("Ddt in uscita")
        self.wait_loader()

        self.wait_for_element_and_click( '//tbody//tr//td')
        self.wait_for_element_and_click( '//th[@id="th_Numero"]/i[@class="deleteicon fa fa-times"]')

    def elimina_selezionati(self):
        self.navigateTo("Ddt in uscita")
        self.wait_loader()

        self.wait_for_element_and_click( '//tbody//tr//td')
        self.wait_for_element_and_click( '//button[@data-toggle="dropdown"]')
        self.wait_for_element_and_click( '//a[@data-op="delete_bulk"]')
        self.wait_for_element_and_click( '//button[@class="swal2-confirm btn btn-lg btn-danger"]')

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input')))
        self.send_keys_and_wait( search_input, '2', False)

        scritta = self.find(By.XPATH, '//tbody//tr').text
        self.assertEqual(scritta, "La ricerca non ha portato alcun risultato.")
        self.wait_for_element_and_click( '//th[@id="th_Numero"]/i[@class="deleteicon fa fa-times"]')