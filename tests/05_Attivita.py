from common.Test import Test, get_html
from common.RowManager import RowManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Attivita(Test):
    def setUp(self):
        super().setUp()
        self.wait_driver = self.wait

    def test_attivita(self):
        # Crea un nuovo intervento. *Required*
        importi = RowManager.list()
        self.attivita("Cliente", "1", "2", importi[0])

        # Duplica attività
        self.duplica_attività()

        # Modifica intervento
        self.modifica_attività("4")

        # Cancellazione intervento
        self.elimina_attività()

        # Controllo righe
        self.controllo_righe()

        # Verifica attività
        self.verifica_attività()

        # Controllo storico attività plugin in Anagrafica
        self.storico_attivita()

        # Cambia stato (Azioni di gruppo)
        self.cambio_stato()

        # Duplica attività (Azioni di gruppo)
        self.duplica()

        # Elimina selezionati (Azioni di gruppo)
        self.elimina_selezionati()

        # Firma interventi (Azioni di gruppo)
        self.firma_interventi()

        # Fattura attività (Azioni di gruppo)
        self.fattura_attivita()

        # Stampa riepilogo (Azioni di gruppo)
        self.stampa_riepilogo()


    def attivita(self, cliente: str, tipo: str, stato: str, file_importi: str):
        self.navigateTo("Attività")

        # Crea attività
        self.wait_for_element_and_click('//i[@class="fa fa-plus"]')
        modal = self.wait_modal()

        self.input(modal, 'Cliente').setByText(cliente)
        self.input(modal, 'Tipo').setByIndex(tipo)

        self.wait_for_element_and_click('(//iframe[@class="cke_wysiwyg_frame cke_reset"])[1]')
        self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '(//iframe[@class="cke_wysiwyg_frame cke_reset"])[1]'))).send_keys("Test")
        self.wait_for_element_and_click('//div[@class="col-md-12 text-right"]//button[@type="button"]')

        row_manager = RowManager(self)
        self.valori = row_manager.compile(file_importi)

    def duplica_attività(self):
        self.navigateTo("Attività")

        self.wait_for_element_and_click('//tbody//tr//td[2]')

        self.wait_for_element_and_click('//div[@id="pulsanti"]//button[1]')
        self.wait_for_element_and_click('//span[@id="select2-id_stato-container"]')
        self.wait_for_element_and_click('//span[@class="select2-results"]//li[2]')
        self.wait_for_element_and_click('//div[@class="modal-content"]//button[@type="submit"]')

    def modifica_attività(self, modifica:str):
        self.navigateTo("Attività")

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input')))
        self.send_keys_and_wait(search_input, '1')

        self.wait_for_element_and_click('//tbody//tr//td[2]')

        self.input(None, 'Stato').setValue(modifica)
        self.wait_for_element_and_click('//div[@id="tab_0"]//button[@id="save"]')

        self.navigateTo("Attività")

        self.wait_for_element_and_click('//th[@id="th_Numero"]/i[@class="deleteicon fa fa-times"]')

    def elimina_attività(self):
        self.navigateTo("Attività")

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input')))
        self.send_keys_and_wait(search_input, '2')

        self.wait_for_element_and_click('//tbody//tr//td[2]')

        self.wait_for_element_and_click('//div[@id="tab_0"]//a[@class="btn btn-danger ask"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')

        self.navigateTo("Attività")

        self.wait_for_element_and_click('//th[@id="th_Numero"]/i[@class="deleteicon fa fa-times"]')

    def controllo_righe(self):
        self.navigateTo("Attività")

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input')))
        self.send_keys_and_wait(search_input, '1')

        self.wait_for_element_and_click('//tbody//tr//td[2]')

        imponibile = self.find(By.XPATH, '//div[@id="righe"]//tbody[2]//tr[1]//td[2]').text
        sconto = self.find(By.XPATH, '//div[@id="righe"]//tbody[2]//tr[2]//td[2]').text
        totale = self.find(By.XPATH, '//div[@id="righe"]//tbody[2]//tr[3]//td[2]').text

        self.assertEqual(imponibile, (self.valori["Imponibile"] + ' €'))
        self.assertEqual(sconto, (self.valori["Sconto/maggiorazione"] + ' €'))
        self.assertEqual(totale, (self.valori["Totale imponibile"] + ' €'))

        imponibilefinale = self.find(By.XPATH, '//div[@id="costi"]//tbody[2]//tr[1]//td[2]').text
        scontofinale = self.find(By.XPATH, '//div[@id="costi"]//tbody[2]//tr[2]//td[2]').text
        totaleimpfinale = self.find(By.XPATH, '//div[@id="costi"]//tbody[2]//tr[3]//td[2]').text
        IVA = self.find(By.XPATH, '//div[@id="costi"]//tbody[2]//tr[4]//td[2]').text
        totalefinale = self.find(By.XPATH, '//div[@id="costi"]//tbody[2]//tr[5]//td[2]').text

        self.assertEqual(imponibilefinale, imponibile)
        self.assertEqual(scontofinale, sconto)
        self.assertEqual(totaleimpfinale, totale)
        self.assertEqual(IVA, (self.valori["IVA"] + ' €'))
        self.assertEqual(totalefinale, (self.valori["Totale documento"] + ' €'))

        self.navigateTo("Attività")

        self.wait_for_element_and_click('//th[@id="th_Numero"]/i[@class="deleteicon fa fa-times"]')

    def verifica_attività(self):
        self.navigateTo("Attività")

        # Verifica elemento modificato
        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input')))
        self.send_keys_and_wait(search_input, '1')

        modificato = self.driver.find_element(By.XPATH, '//tbody//tr[1]//td[7]').text
        self.assertEqual("Completato", modificato)
        self.wait_for_element_and_click('//i[@class="deleteicon fa fa-times"]')

        # Verifica elemento eliminato
        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input')))
        self.send_keys_and_wait(search_input, '2')

        eliminato = self.driver.find_element(By.XPATH, '//tbody//tr[1]//td[@class="dataTables_empty"]').text
        self.assertEqual("La ricerca non ha portato alcun risultato.", eliminato)
        self.wait_for_element_and_click('//i[@class="deleteicon fa fa-times"]')

    def storico_attivita(self):
        self.navigateTo("Anagrafiche")

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Ragione-sociale"]/input')))
        self.send_keys_and_wait(search_input, 'Cliente')

        self.wait_for_element_and_click('//tbody//tr//td[2]')

        self.wait_for_element_and_click('//a[@id="link-tab_28"]')

        # Verifica attività
        self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_28"]//tbody//tr//td[1]')))

    def cambio_stato(self):
        self.navigateTo("Attività")

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input')))
        self.send_keys_and_wait(search_input, '1')

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_element_and_click('//button[@data-toggle="dropdown"]')
        self.wait_for_element_and_click('//a[@data-op="cambia_stato"]')

        self.wait_for_element_and_click('//span[@id="select2-id_stato-container"]')
        search_field = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]')))
        search_field.send_keys("Da programmare")

        self.wait_for_element_and_click('//li[@class="select2-results__option select2-results__option--highlighted"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-warning"]')

        stato = self.find(By.XPATH, '//tbody//tr//td[7]').text
        self.assertEqual(stato, "Da programmare")

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_element_and_click('//i[@class="deleteicon fa fa-times"]')

    def duplica(self):
        self.navigateTo("Attività")

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input')))
        self.send_keys_and_wait(search_input, '1')

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_element_and_click('//button[@data-toggle="dropdown"]')
        self.wait_for_element_and_click('//a[@data-op="copy-bulk"]')

        self.wait_for_element_and_click('//span[@id="select2-idstatointervento-container"]')
        search_field = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]')))
        search_field.send_keys("Da programmare")

        self.wait_for_element_and_click('//li[@class="select2-results__option select2-results__option--highlighted"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-warning"]')

        self.wait_for_element_and_click('//i[@class="deleteicon fa fa-times"]')

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input')))
        self.send_keys_and_wait(search_input, '2')

        numero = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//tbody//tr//td[2]'))).text
        self.assertEqual(numero, "2")

        self.wait_for_element_and_click('//i[@class="deleteicon fa fa-times"]')

    def elimina_selezionati(self):
        self.navigateTo("Attività")

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input')))
        self.send_keys_and_wait(search_input, '2')

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_element_and_click('//button[@data-toggle="dropdown"]')
        self.wait_for_element_and_click('//a[@data-op="delete-bulk"]')

        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')

        scritta = self.find(By.XPATH, '//tbody//tr//td').text
        self.assertEqual(scritta, "La ricerca non ha portato alcun risultato.")
        self.wait_for_element_and_click('//i[@class="deleteicon fa fa-times"]')

    def firma_interventi(self):
        self.navigateTo("Attività")

        # Aggiunta attività
        self.wait_for_element_and_click('//i[@class="fa fa-plus"]')

        self.wait_for_element_and_click('//span[@id="select2-idanagrafica-container"]')
        cliente_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-dropdown select2-dropdown--below"]//input')))
        cliente_input.send_keys("Cliente", Keys.ENTER)

        self.wait_for_element_and_click('//span[@id="select2-idtipointervento-container"]')
        tipo_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input')))
        tipo_input.send_keys("Generico")

        self.wait_for_element_and_click('//li[@class="select2-results__option select2-results__option--highlighted"]')

        iframe = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '(//iframe[@class="cke_wysiwyg_frame cke_reset"])[1]')))
        iframe.click()
        iframe.send_keys("Test")

        self.wait_for_element_and_click('//button[@class="btn btn-primary"]')

        # Firma attività
        self.navigateTo("Attività")

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_element_and_click('//button[@data-toggle="dropdown"]')
        self.wait_for_element_and_click('//a[@data-op="firma-intervento"]')

        self.wait_for_element_and_click('//button[@id="firma"]')
        firma_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="firma_nome"]')))
        firma_input.send_keys("firma")

        self.wait_for_element_and_click('//button[@class="btn btn-success pull-right"]')

        self.wait_for_element_and_click('//tbody//tr//td[2]')

        # Verifica firma
        self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '(//div[@class="text-center row"]//div)[3]')))

    def fattura_attivita(self):
        self.navigateTo("Attività")

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input')))
        self.send_keys_and_wait(search_input, '2')

        self.wait_for_element_and_click('//tbody//tr//td[2]')

        self.wait_for_element_and_click('//span[@id="select2-idstatointervento-container"]')

        stato_input = self.find(By.XPATH, '(//input[@class="select2-search__field"])[3]')
        stato_input.send_keys("Completato", Keys.ENTER)

        self.wait_for_element_and_click('//button[@id="save"]')

        self.wait_for_element_and_click('//a[@id="back"]')

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_element_and_click('//button[@data-toggle="dropdown"]')
        self.wait_for_element_and_click('//a[@data-op="crea_fattura"]')

        self.wait_for_element_and_click('//span[@id="select2-raggruppamento-container"]')
        cliente_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]')))
        cliente_input.send_keys("Cliente")

        self.wait_for_element_and_click('//ul[@id="select2-raggruppamento-results"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-warning"]')

        stato = self.find(By.XPATH, '//tbody//tr//td[7]').text
        self.assertEqual(stato, "Fatturato")

        self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")

        self.wait_for_element_and_click('//tbody//tr//td[2]')

        self.wait_for_element_and_click('//div[@id="tab_0"]//a[@class="btn btn-danger ask "]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')

        self.navigateTo("Attività")

        self.wait_for_element_and_click('//i[@class="deleteicon fa fa-times"]')

    def stampa_riepilogo(self):
        self.navigateTo("Attività")

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input')))
        self.send_keys_and_wait(search_input, '2')

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_element_and_click('//button[@data-toggle="dropdown"]')
        self.wait_for_element_and_click('//a[@data-op="stampa-riepilogo"]')

        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-warning"]')

        # Switch to the new window
        self.driver.switch_to.window(self.driver.window_handles[1])
        prezzo = self.find(By.XPATH, '(//div[@id="viewer"]//span)[59]').text
        self.assertEqual(prezzo, "0,00 €")
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

        self.wait_for_element_and_click('//tbody//tr//td[2]')

        self.wait_for_element_and_click('//a[@class="btn btn-danger ask"]')

        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')
