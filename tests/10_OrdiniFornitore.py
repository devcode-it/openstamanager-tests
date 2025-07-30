from common.Test import Test, get_html
from selenium.webdriver.common.keys import Keys
from common.RowManager import RowManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class OrdiniFornitore(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Acquisti")

    def test_creazione_ordine_fornitore(self):
        importi = RowManager.list()
        self.creazione_ordine_fornitore("Fornitore", importi[0])
        self.creazione_ordine_fornitore("Fornitore", importi[0])
        self.modifica_ordine_fornitore("Modifica di Prova")
        self.elimina_ordine_fornitore()
        self.verifica_ordine_fornitore()
        self.cambia_stato()

    def creazione_ordine_fornitore(self, fornitore: str, file_importi: str):
        self.navigateTo("Ordini fornitore")

        self.wait_for_element_and_click('//i[@class="fa fa-plus"]')
        modal = self.wait_modal()

        select = self.input(modal, 'Fornitore')
        select.setByText(fornitore)
        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        self.wait_loader()

        row_manager = RowManager(self)
        self.valori = row_manager.compile(file_importi)

    def modifica_ordine_fornitore(self, modifica):
        self.navigateTo("Ordini fornitore")
        self.wait_loader()

        self.send_keys_and_wait(self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input'))), '1', False)

        self.wait_for_element_and_click('//tbody//tr//td[2]')
        self.driver.execute_script('window.scrollTo(0,0)')

        self.wait_for_dropdown_and_select('//span[@aria-labelledby="select2-idstatoordine-container"]', option_text='Accettato')
        self.wait_for_element_and_click('//div[@id="tab_0"]//button[@id="save"]')

        sconto = self.find(By.XPATH, '//div[@id="righe"]//tbody[2]//tr[2]//td[2]').text
        totale_imponibile = self.find(By.XPATH, '//div[@id="righe"]//tbody[2]//tr[3]//td[2]').text
        iva = self.find(By.XPATH, '//div[@id="righe"]//tbody[2]//tr[4]//td[2]').text
        totale = self.find(By.XPATH, '//div[@id="tab_0"]//div[@id="righe"]//tbody[2]//tr[5]//td[2]').text

        self.assertEqual(sconto, (self.valori["Sconto/maggiorazione"] + ' €'))
        self.assertEqual(totale_imponibile, (self.valori["Totale imponibile"] + ' €'))
        self.assertEqual(iva, (self.valori["IVA"] + ' €'))
        self.assertEqual(totale, (self.valori["Totale documento"] + ' €'))

        self.navigateTo("Ordini fornitore")
        self.wait_loader()
        self.wait_for_element_and_click('//th[@id="th_Numero"]/i[@class="deleteicon fa fa-times"]')

    def elimina_ordine_fornitore(self):
        self.navigateTo("Ordini fornitore")
        self.wait_loader()

        self.send_keys_and_wait(self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input'))), '2', False)

        self.wait_for_element_and_click('//tbody//tr//td[2]')
        self.wait_for_element_and_click('//div[@id="tab_0"]//a[@class="btn btn-danger ask"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')

        self.wait_for_element_and_click('//th[@id="th_Numero"]/i[@class="deleteicon fa fa-times"]')

    def verifica_ordine_fornitore(self):
        self.navigateTo("Ordini fornitore")
        self.wait_loader()

        self.send_keys_and_wait(self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_icon_title_Stato"]/input'))), "Accettato", False)

        modificato = self.driver.find_element(By.XPATH, '//tbody//tr[1]//td[6]').text
        self.assertEqual("Accettato", modificato)
        self.wait_for_element_and_click('//i[@class="deleteicon fa fa-times"]')

        self.send_keys_and_wait(self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input'))), "2", False)

        eliminato = self.driver.find_element(By.XPATH, '//tbody//tr[1]//td[@class="dataTables_empty"]').text
        self.assertEqual("La ricerca non ha portato alcun risultato.", eliminato)
        self.wait_for_element_and_click('//th[@id="th_Numero"]/i[@class="deleteicon fa fa-times"]')

    def cambia_stato(self):
        self.navigateTo("Ordini fornitore")
        self.wait_loader()

        self.send_keys_and_wait(self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input'))), "1", False)

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_element_and_click('//button[@data-toggle="dropdown"]')
        self.wait_for_element_and_click('//a[@data-op="change_status"]')

        self.wait_for_dropdown_and_select('//span[@id="select2-id_stato-container"]', option_text='Evaso')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-warning"]')

        stato = self.find(By.XPATH, '//tbody//tr//td[6]').text
        self.assertEqual(stato, "Evaso")

        self.wait_for_element_and_click('//th[@id="th_Numero"]/i[@class="deleteicon fa fa-times"]')
