from common.Test import Test, get_html
from common.RowManager import RowManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Attivita(Test):
    def setUp(self):
        super().setUp()

    def test_attivita(self):
        importi = RowManager.list()
        self.attivita('Cliente', '1', '2', importi[0])
        self.duplica_attività()
        self.modifica_attività('4')
        self.elimina_attività()
        self.controllo_righe()
        self.verifica_attività()
        self.storico_attivita()
        self.cambio_stato()
        self.duplica()
        self.elimina_selezionati()
        self.firma_interventi()
        self.fattura_attivita()
        self.stampa_riepilogo()

    def attivita(self, cliente: str, tipo: str, stato: str, file_importi: str):
        self.navigateTo('Attività')
        self.wait_for_element_and_click('//i[@class="fa fa-plus"]')
        modal = self.wait_modal()
        self.input(modal, 'Cliente').setByText(cliente)
        self.input(modal, 'Tipo').setByIndex(tipo)
        iframe = self.wait_for_element_and_click('(//iframe[@class="cke_wysiwyg_frame cke_reset"])[1]')
        iframe.send_keys('Test')
        self.wait_for_element_and_click('//div[@class="col-md-12 text-right"]//button[@type="button"]')
        self.wait_loader()

        row_manager = RowManager(self)
        self.valori = row_manager.compile(file_importi)

    def duplica_attività(self):
        self.navigateTo('Attività')
        self.click_first_result()
        self.wait_for_element_and_click('//div[@id="pulsanti"]//button[1]')
        self.wait_for_dropdown_and_select(
            '//span[@id="select2-id_stato-container"]',
            option_xpath='//span[@class="select2-results"]//li[2]'
        )
        self.wait_for_element_and_click('//div[@class="modal-content"]//button[@type="submit"]')

    def modifica_attività(self, modifica: str):
        self.navigateTo('Attività')
        search_input = self.wait_for_element_and_click('//th[@id="th_Numero"]/input')
        self.send_keys_and_wait(search_input, '1', wait_modal=False)
        self.click_first_result()
        self.input(None, 'Stato').setValue(modifica)
        self.wait_for_element_and_click('//div[@id="tab_0"]//button[@id="save"]')
        self.navigateTo('Attività')
        self.clear_filters()

    def elimina_attività(self):
        self.navigateTo('Attività')
        search_input = self.wait_for_element_and_click('//th[@id="th_Numero"]/input')
        self.send_keys_and_wait(search_input, '2', wait_modal=False)
        self.click_first_result()
        self.wait_for_element_and_click('//div[@id="tab_0"]//a[@class="btn btn-danger ask"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')
        self.navigateTo('Attività')
        self.clear_filters()

    def controllo_righe(self):
        self.navigateTo('Attività')
        search_input = self.wait_for_element_and_click('//th[@id="th_Numero"]/input')
        self.send_keys_and_wait(search_input, '1', wait_modal=False)
        self.click_first_result()

        imponibile = self.find(By.XPATH, '//div[@id="righe"]//tbody[2]//tr[1]//td[2]').text
        sconto = self.find(By.XPATH, '//div[@id="righe"]//tbody[2]//tr[2]//td[2]').text
        totale = self.find(By.XPATH, '//div[@id="righe"]//tbody[2]//tr[3]//td[2]').text

        self.assertEqual(imponibile, (self.valori['Imponibile'] + ' €'))
        self.assertEqual(sconto, (self.valori['Sconto/maggiorazione'] + ' €'))
        self.assertEqual(totale, (self.valori['Totale imponibile'] + ' €'))

        imponibilefinale = self.find(By.XPATH, '//div[@id="costi"]//tbody[2]//tr[1]//td[2]').text
        scontofinale = self.find(By.XPATH, '//div[@id="costi"]//tbody[2]//tr[2]//td[2]').text
        totaleimpfinale = self.find(By.XPATH, '//div[@id="costi"]//tbody[2]//tr[3]//td[2]').text
        IVA = self.find(By.XPATH, '//div[@id="costi"]//tbody[2]//tr[4]//td[2]').text
        totalefinale = self.find(By.XPATH, '//div[@id="costi"]//tbody[2]//tr[5]//td[2]').text

        self.assertEqual(imponibilefinale, imponibile)
        self.assertEqual(scontofinale, sconto)
        self.assertEqual(totaleimpfinale, totale)
        self.assertEqual(IVA, (self.valori['IVA'] + ' €'))
        self.assertEqual(totalefinale, (self.valori['Totale documento'] + ' €'))

        self.navigateTo('Attività')
        self.clear_filters()

    def verifica_attività(self):
        self.navigateTo('Attività')
        search_input = self.wait_for_element_and_click('//th[@id="th_Numero"]/input')
        self.send_keys_and_wait(search_input, '1', wait_modal=False)
        modificato = self.find(By.XPATH, '//tbody//tr[1]//td[7]').text
        self.assertEqual('Completato', modificato)
        self.clear_filters()

        search_input = self.wait_for_element_and_click('//th[@id="th_Numero"]/input')
        self.send_keys_and_wait(search_input, '2', wait_modal=False)
        eliminato = self.find(By.XPATH, '//tbody//tr[1]//td[@class="dataTables_empty"]').text
        self.assertEqual('La ricerca non ha portato alcun risultato.', eliminato)
        self.clear_filters()

    def storico_attivita(self):
        self.navigateTo('Anagrafiche')
        self.search_entity('Cliente')
        self.click_first_result()
        self.wait_for_element_and_click('//a[@id="link-tab_28"]')
        self.wait_for_element_and_click('//div[@id="tab_28"]//tbody//tr//td[1]')

    def cambio_stato(self):
        self.navigateTo('Attività')
        search_input = self.wait_for_element_and_click('//th[@id="th_Numero"]/input')
        self.send_keys_and_wait(search_input, '1', wait_modal=False)

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_dropdown_and_select(
            '//button[@data-toggle="dropdown"]',
            option_xpath='//a[@data-op="change_status"]'
        )

        self.wait_for_dropdown_and_select(
            '//span[@id="select2-id_stato-container"]',
            option_text='Da programmare'
        )
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-warning"]')

        stato = self.find(By.XPATH, '//tbody//tr//td[7]').text
        self.assertEqual(stato, 'Da programmare')
        self.wait_for_element_and_click('//tbody//tr//td')
        self.clear_filters()

    def duplica(self):
        self.navigateTo('Attività')
        search_input = self.wait_for_element_and_click('//th[@id="th_Numero"]/input')
        self.send_keys_and_wait(search_input, '1', wait_modal=False)

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_dropdown_and_select(
            '//button[@data-toggle="dropdown"]',
            option_xpath='//a[@data-op="copy_bulk"]'
        )

        self.wait_for_dropdown_and_select(
            '//span[@id="select2-idstatointervento-container"]',
            option_text='Da programmare'
        )
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-warning"]')
        self.clear_filters()

        search_input = self.wait_for_element_and_click('//th[@id="th_Numero"]/input')
        self.send_keys_and_wait(search_input, '2', wait_modal=False)
        numero = self.find(By.XPATH, '//tbody//tr//td[2]').text
        self.assertEqual(numero, '2')
        self.clear_filters()

    def elimina_selezionati(self):
        self.navigateTo('Attività')
        search_input = self.wait_for_element_and_click('//th[@id="th_Numero"]/input')
        self.send_keys_and_wait(search_input, '2', wait_modal=False)

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_dropdown_and_select(
            '//button[@data-toggle="dropdown"]',
            option_xpath='//a[@data-op="delete_bulk"]'
        )
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')

        scritta = self.find(By.XPATH, '//tbody//tr//td').text
        self.assertEqual(scritta, 'La ricerca non ha portato alcun risultato.')
        self.clear_filters()

    def firma_interventi(self):
        importi = RowManager.list()
        self.attivita('Cliente', '2', '1', importi[0])

        self.navigateTo('Attività')
        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_dropdown_and_select(
            '//button[@data-toggle="dropdown"]',
            option_xpath='//a[@data-op="firma-intervento"]'
        )

        self.wait_for_element_and_click('//button[@id="firma"]')
        firma_input = self.wait_for_element_and_click('//input[@id="firma_nome"]')
        firma_input.send_keys('firma')
        self.wait_for_element_and_click('//button[@class="btn btn-success pull-right"]')

        self.click_first_result()
        self.wait_for_element_and_click('(//div[@class="text-center row"]//div)[3]')

    def fattura_attivita(self):
        self.navigateTo('Attività')
        search_input = self.wait_for_element_and_click('//th[@id="th_Numero"]/input')
        self.send_keys_and_wait(search_input, '2', wait_modal=False)

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_dropdown_and_select(
            '//button[@data-toggle="dropdown"]',
            option_xpath='//a[@data-op="create_invoice"]'
        )

        self.wait_for_dropdown_and_select(
            '//span[@id="select2-raggruppamento-container"]',
            option_text='Cliente'
        )
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-warning"]')

        stato = self.find(By.XPATH, '//tbody//tr//td[7]').text
        self.assertEqual(stato, 'Fatturato')

        self.expandSidebar('Vendite')
        self.navigateTo('Fatture di vendita')
        self.click_first_result()
        self.wait_for_element_and_click('//div[@id="tab_0"]//a[@class="btn btn-danger ask "]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')

        self.navigateTo('Attività')
        self.clear_filters()

    def stampa_riepilogo(self):
        self.navigateTo('Attività')
        search_input = self.wait_for_element_and_click('//th[@id="th_Numero"]/input')
        self.send_keys_and_wait(search_input, '2', wait_modal=False)

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_dropdown_and_select(
            '//button[@data-toggle="dropdown"]',
            option_xpath='//a[@data-op="print_summary"]'
        )
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-warning"]')

        self.driver.switch_to.window(self.driver.window_handles[1])
        prezzo = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '(//div[@id="viewer"]//span)[40]'))).text
        self.assertEqual(prezzo, '0,00')

        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

        self.click_first_result()
        self.wait_for_element_and_click('//a[@class="btn btn-danger ask"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')
