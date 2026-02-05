from common.Test import Test
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class TipiDocumento(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Strumenti")
        self.expandSidebar("Tabelle")

    def test_creazione_tipi_documento(self):
        self.creazione_tipi_documento(descrizione="Tipo di Documento di Prova da Modificare", direzione="Entrata", codice="TD01 - Fattura" )
        self.creazione_tipi_documento(descrizione="Tipo di Documento di Prova da Eliminare", direzione="Entrata", codice="TD01 - Fattura" )
        self.modifica_documento("Tipo di Documento di Prova")
        self.elimina_documento()
        self.verifica_tipo_documento()
        self.wait_for_element_and_click('//i[@class="fa fa-power-off nav-icon"]')
        
    def creazione_tipi_documento(self, descrizione = str, direzione = str, codice = str):
        self.navigateTo("Tipi documento")
        self.wait_for_element_and_click('//i[@class="fa fa-plus"]')
        modal = self.wait_modal()

        self.input(modal, 'Descrizione').setValue(descrizione)
        select = self.input(modal, 'Direzione')
        select.setByText(direzione)
        select = self.input(modal, 'Codice tipo documento FE')
        select.setByText(codice)
        self.wait_for_element_and_click('button[type="submit"]', By.CSS_SELECTOR)

    def modifica_documento(self, modifica):
        self.navigateTo("Tipi documento")
        self.wait_loader()

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input')))
        self.send_keys_and_wait(search_input, 'Tipo di Documento di Prova da Modificare', wait_modal=False)
        self.wait_for_element_and_click('//tbody//tr//td[2]')

        self.input(None,'Descrizione').setValue(modifica)
        self.input(None, 'Sezionale predefinito').setByText('Autofatture')
        self.wait_for_element_and_click('//div[@id="tab_0"]//button[@id="save"]')

        self.navigateTo("Tipi documento")
        self.wait_loader()
        self.wait_for_element_and_click('//th[@id="th_Descrizione"]/i[@class="deleteicon fa fa-times"]')

    def elimina_documento(self):
        self.navigateTo("Tipi documento")
        self.wait_loader()

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input')))
        self.send_keys_and_wait(search_input, 'Tipo di Documento di Prova da Eliminare', wait_modal=False)
        self.wait_for_element_and_click('//tbody//tr//td[2]')

        self.wait_for_element_and_click('//div[@id="tab_0"]//a[@class="btn btn-danger ask"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')
        self.wait_for_element_and_click('//th[@id="th_Descrizione"]/i[@class="deleteicon fa fa-times"]')

    def verifica_tipo_documento(self):
        self.navigateTo("Tipi documento")
        self.wait_loader()

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input')))
        self.send_keys_and_wait(search_input, "Tipo di Documento di Prova", wait_modal=False)
        modificato = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//tbody//tr[1]//td[2]'))).text
        self.assertEqual("Tipo di Documento di Prova", modificato)
        self.wait_for_element_and_click('//i[@class="deleteicon fa fa-times"]')

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input')))
        self.send_keys_and_wait(search_input, "Tipo di Documento di Prova da Eliminare", wait_modal=False)
        eliminato = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//tbody//tr[1]//td[@class="dataTables_empty"]'))).text
        self.assertEqual("Nessun dato presente nella tabella", eliminato)