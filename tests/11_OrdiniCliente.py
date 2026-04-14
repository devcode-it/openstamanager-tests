from common.Test import Test
from common.RowManager import RowManager
from selenium.webdriver.common.by import By

class OrdiniCliente(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Vendite")

    def test_creazione_ordine_cliente(self):
        importi = RowManager.list()
        self.creazione_ordine_cliente("Cliente", importi[0])
        self.creazione_ordine_cliente("Cliente", importi[0])
        self.modifica_ordine_cliente()
        self.elimina_ordine_cliente()
        self.verifica_ordine_cliente()
        self.wait_for_element_and_click('//i[@class="fa fa-power-off nav-icon"]')

    def creazione_ordine_cliente(self, cliente: str, file_importi: str):
        self.navigateTo("Ordini cliente")
        self.wait_loader()

        self.wait_for_element_and_click('//i[@class="fa fa-plus"]')
        modal = self.wait_modal()

        select = self.input(modal, 'Cliente')
        select.setByText(cliente)
        modal.find_element(By.XPATH, './/button[@type="submit"]').click()

        row_manager = RowManager(self)
        self.valori = row_manager.compile(file_importi)

    def modifica_ordine_cliente(self):
        self.navigateTo("Ordini cliente")
        self.wait_loader()

        self.send_keys_and_wait(self.find(By.XPATH, '//th[@id="th_Numero"]/input'), '01', wait_modal=False)

        self.wait_for_element_and_click('//tbody//tr//td[2]')
        self.driver.execute_script('window.scrollTo(0,0)')

        self.wait_for_dropdown_and_select('//span[@id="select2-idstatoordine-container"]', option_text='Accettato')
        self.wait_for_element_and_click('//div[@id="tab_0"]//button[@id="save"]')

        sconto = self.find(By.XPATH, '//div[@id="righe"]//tbody[2]//tr[2]//td[2]').text
        totale_imponibile = self.find(By.XPATH, '//div[@id="righe"]//tbody[2]//tr[3]//td[2]').text
        iva = self.find(By.XPATH, '//div[@id="righe"]//tbody[2]//tr[4]//td[2]').text
        totale = self.find(By.XPATH, '//div[@id="tab_0"]//div[@id="righe"]//tbody[2]//tr[5]//td[2]').text

        self.assertEqual(sconto, (self.valori["Sconto/maggiorazione"] + ' €'))
        self.assertEqual(totale_imponibile, (self.valori["Totale imponibile"] + ' €'))
        self.assertEqual(iva, (self.valori["IVA"] + ' €'))
        self.assertEqual(totale, (self.valori["Totale documento"] + ' €'))

        self.navigateTo("Ordini cliente")
        self.wait_loader()
        self.wait_for_element_and_click('//th[@id="th_Numero"]/i[@class="deleteicon fa fa-times"]')

    def elimina_ordine_cliente(self):
        self.navigateTo("Ordini cliente")
        self.wait_loader()

        self.send_keys_and_wait(self.find(By.XPATH, '//th[@id="th_Numero"]/input'), '2', wait_modal=False)

        self.wait_for_element_and_click('//tbody//tr//td[2]')
        self.wait_for_element_and_click('//div[@id="tab_0"]//a[@class="btn btn-danger ask"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')

        self.wait_for_element_and_click('//th[@id="th_Numero"]/i[@class="deleteicon fa fa-times"]')

    def verifica_ordine_cliente(self):
        self.navigateTo("Ordini cliente")
        self.wait_loader()

        self.send_keys_and_wait(self.find(By.XPATH, '//th[@id="th_icon_title_Stato"]/input'), "Accettato", wait_modal=False)

        modificato = self.find(By.XPATH, '//tbody//tr[1]//td[7]').text
        self.assertEqual("Accettato", modificato)
        self.wait_for_element_and_click('//i[@class="deleteicon fa fa-times"]')

        self.send_keys_and_wait(self.find(By.XPATH, '//th[@id="th_Numero"]/input'), "2", wait_modal=False)

        eliminato = self.find(By.XPATH, '//tbody//tr[1]//td[@class="dataTables_empty"]').text
        self.assertEqual("Nessun dato presente nella tabella", eliminato)
        self.wait_for_element_and_click('//th[@id="th_Numero"]/i[@class="deleteicon fa fa-times"]')
