from common.Test import Test, get_html
from common.RowManager import RowManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class Preventivi(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Vendite")

    def test_creazione_preventivo(self):
        importi = RowManager.list()
        self.creazione_preventivo("Preventivo di Prova","Cliente", "1", importi[0])
        self.duplica_preventivo()
        self.modifica_preventivo("Accettato")
        self.elimina_preventivo()

        self.creazione_contratto()
        self.creazione_ordine_cliente()
        self.creazione_ordine_fornitore()
        self.creazione_attività()
        self.creazione_ddt_uscita()
        self.creazione_fattura()
        self.verifica_preventivi()
        self.wait_for_element_and_click('//i[@class="fa fa-power-off nav-icon"]')

    def creazione_preventivo(self, nome:str, cliente:str, idtipo: str, file_importi: str):
        self.navigateTo("Preventivi")
        self.wait_loader()

        self.wait_for_element_and_click('//i[@class="fa fa-plus"]')
        modal = self.wait_modal()

        self.input(modal, 'Nome').setValue(nome)
        select = self.input(modal, 'Cliente')
        select.setByText(cliente)
        select = self.input(modal, 'Tipo di Attività')
        select.setByIndex(idtipo)
        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

        row_manager = RowManager(self)
        self.valori = row_manager.compile(file_importi)

    def duplica_preventivo(self):
        self.navigateTo("Preventivi")
        self.wait_loader()

        self.wait_for_element_and_click('//tbody//tr//td[2]')
        self.wait_for_element_and_click('//div[@id="pulsanti"]//button[@class="btn ask btn-primary"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-primary"]')

        self.driver.execute_script('window.scrollTo(0,0)')
        nome_field = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//input[@id="nome"]'))
        )
        nome_field.send_keys(" da Eliminare")

        self.wait_for_element_and_click('//button[@class="btn btn-success"]')

    def modifica_preventivo(self, stato:str):
        self.navigateTo("Preventivi")
        self.wait_loader()

        self.send_keys_and_wait(self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))), '=Preventivo di Prova', wait_modal=False)

        self.wait_for_element_and_click('//tbody//tr//td[2]')

        select = self.input(None, 'Stato')
        select.setByText(stato)
        self.wait_for_element_and_click('//div[@id="tab_0"]//button[@id="save"]')

        sconto = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="righe"]//tbody[2]//tr[2]//td[2]'))
        ).text
        totale_imponibile = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="righe"]//tbody[2]//tr[3]//td[2]'))
        ).text
        iva = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="righe"]//tbody[2]//tr[4]//td[2]'))
        ).text
        totale = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_0"]//div[@id="righe"]//tbody[2]//tr[5]//td[2]'))
        ).text

        self.assertEqual(sconto, (self.valori["Sconto/maggiorazione"] + ' €'))
        self.assertEqual(totale_imponibile, (self.valori["Totale imponibile"] + ' €'))
        self.assertEqual(iva, (self.valori["IVA"] + ' €'))
        self.assertEqual(totale, (self.valori["Totale documento"] + ' €'))

        self.navigateTo("Preventivi")
        self.wait_loader()
        self.wait_for_element_and_click('//th[@id="th_Nome"]/i[@class="deleteicon fa fa-times"]')

    def elimina_preventivo(self):
        self.navigateTo("Preventivi")
        self.wait_loader()

        self.send_keys_and_wait(self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))), '=Preventivo di Prova da Eliminare', wait_modal=False)

        self.wait_for_element_and_click('//tbody//tr//td[2]')
        self.wait_for_element_and_click('//div[@id="tab_0"]//a[@class="btn btn-danger ask"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')

        self.navigateTo("Preventivi")
        self.wait_loader()
        self.wait_for_element_and_click('//th[@id="th_Nome"]/i[@class="deleteicon fa fa-times"]')

    def creazione_contratto(self):
        self.navigateTo("Preventivi")
        self.wait_loader()

        self.send_keys_and_wait(self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))), 'Preventivo di Prova', wait_modal=False)

        self.wait_for_element_and_click('//tbody//tr//td[2]')
        totalepreventivo = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="righe"]//tbody[2]//tr[3]//td[2]'))
        ).text

        self.wait_for_element_and_click('//div[@id="pulsanti"]//button[@class="btn btn-info dropdown-toggle "]')
        self.wait_for_element_and_click('//a[@class="btn dropdown-item bound clickable"][@data-title="Crea contratto"]')
        self.wait_for_element_and_click('//span[@id="select2-id_segment-container"]')
        self.wait_for_element_and_click('//li[@class="select2-results__option select2-results__option--highlighted"]')
        self.wait_for_element_and_click('//button[@id="submit_btn"]')

        totalecontratto = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="righe"]//tbody[2]//tr[3]//td[2]'))
        ).text
        self.assertEqual(totalecontratto, totalepreventivo)

        self.wait_for_element_and_click('//div[@id="tab_0"]//a[@class="btn btn-danger ask"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')

        self.send_keys_and_wait(self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))), "Preventivo di Prova", wait_modal=False)

        eliminato = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//tbody//tr[1]//td[@class="dataTables_empty"]'))
        ).text
        self.assertEqual("Nessun dato presente nella tabella", eliminato)
        self.navigateTo("Preventivi")
        self.wait_loader()
        self.wait_for_element_and_click('//th[@id="th_Nome"]/i[@class="deleteicon fa fa-times"]')

    def creazione_ordine_cliente(self):
        self.navigateTo("Preventivi")
        self.wait_loader()

        self.send_keys_and_wait(self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))), 'Preventivo di Prova', wait_modal=False)

        self.wait_for_element_and_click('//tbody//tr//td[2]')
        totalepreventivo = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="righe"]//tbody[2]//tr[3]//td[2]'))
        ).text

        self.wait_for_element_and_click('//button[@class="btn btn-info dropdown-toggle "]')
        self.wait_for_element_and_click('//a[@class="btn dropdown-item bound clickable"][@data-title="Crea ordine cliente"]')
        self.wait_for_element_and_click('//span[@id="select2-id_segment-container"]')
        self.wait_for_element_and_click('//li[@class="select2-results__option select2-results__option--highlighted"]')
        self.wait_for_element_and_click('//button[@id="submit_btn"]')

        totaleordinecliente = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="righe"]//tbody[2]//tr[3]//td[2]'))
        ).text
        self.assertEqual(totaleordinecliente, totalepreventivo)

        self.wait_for_element_and_click('//div[@id="tab_0"]//a[@class="btn btn-danger ask"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')

        self.send_keys_and_wait(self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_icon_title_Stato"]/input'))), "Bozza", wait_modal=False)

        eliminato = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//tbody//tr[1]//td[@class="dataTables_empty"]'))
        ).text
        self.assertEqual("Nessun dato presente nella tabella", eliminato)
        self.navigateTo("Preventivi")
        self.wait_loader()
        self.wait_for_element_and_click('//th[@id="th_Nome"]/i[@class="deleteicon fa fa-times"]')

    def creazione_ordine_fornitore(self):
        self.navigateTo("Preventivi")
        self.wait_loader()

        self.send_keys_and_wait(self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))), 'Preventivo di Prova', wait_modal=False)

        self.wait_for_element_and_click('//tbody//tr//td[2]')

        self.wait_for_element_and_click('//button[@class="btn btn-info dropdown-toggle "]')
        self.wait_for_element_and_click('//a[@class="btn dropdown-item bound clickable"][@data-title="Crea ordine fornitore"]')
        self.wait_for_element_and_click('(//span [@id="select2-idanagrafica-container"])[2]')
        self.wait_for_element_and_click('//li[@class="select2-results__option select2-results__option--highlighted"]')
        self.wait_for_element_and_click('//span[@id="select2-id_segment-container"]')
        self.wait_for_element_and_click('//li[@class="select2-results__option select2-results__option--highlighted"]')
        self.wait_for_element_and_click('//button[@id="submit_btn"]')

        totaleordinefornitore = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="righe"]//tbody[2]//tr[3]//td[2]'))
        ).text
        self.assertEqual(totaleordinefornitore, '7,20 €')

        self.wait_for_element_and_click('//div[@id="tab_0"]//a[@class="btn btn-danger ask"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')

        self.send_keys_and_wait(self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_icon_title_Stato"]/input'))), "Bozza", wait_modal=False)

        eliminato = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//tbody//tr[1]//td[@class="dataTables_empty"]'))
        ).text
        self.assertEqual("Nessun dato presente nella tabella", eliminato)
        self.expandSidebar("Vendite")
        self.navigateTo("Preventivi")
        self.wait_loader()
        self.wait_for_element_and_click('//th[@id="th_Nome"]/i[@class="deleteicon fa fa-times"]')

    def creazione_attività(self):
        self.navigateTo("Preventivi")
        self.wait_loader()

        self.send_keys_and_wait(self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))), 'Preventivo di Prova', wait_modal=False)

        self.wait_for_element_and_click('//tbody//tr//td[2]')
        totalepreventivo = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="righe"]//tbody[2]//tr[3]//td[2]'))
        ).text

        self.wait_for_element_and_click('//button[@class="btn btn-info dropdown-toggle "]')
        self.wait_for_element_and_click('//a[@class="btn dropdown-item bound clickable"][@data-title="Crea attività"]')
        self.wait_for_element_and_click('//span[@id="select2-id_tipo_intervento-container"]')
        self.wait_for_element_and_click('//li[@class="select2-results__option select2-results__option--highlighted"]')
        self.wait_for_element_and_click('//span[@id="select2-id_stato_intervento-container"]')
        self.wait_for_element_and_click('//li[@class="select2-results__option"]')
        self.wait_for_element_and_click('//span[@id="select2-id_segment-container"]')
        self.wait_for_element_and_click('//li[@class="select2-results__option select2-results__option--highlighted"]')
        self.wait_for_element_and_click('//button[@id="submit_btn"]')

        totaleattività = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="righe"]//tbody[2]//tr[3]//td[2]'))
        ).text
        self.assertEqual(totaleattività, totalepreventivo)

        self.wait_for_element_and_click('//div[@id="tab_0"]//a[@class="btn btn-danger ask"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')

        self.send_keys_and_wait(self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input'))), "03", wait_modal=False)

        eliminato = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//tbody//tr[1]//td[@class="dataTables_empty"]'))
        ).text
        self.assertEqual("Nessun dato presente nella tabella", eliminato)
        self.expandSidebar("Vendite")
        self.navigateTo("Preventivi")
        self.wait_loader()
        self.wait_for_element_and_click('//th[@id="th_Nome"]/i[@class="deleteicon fa fa-times"]')

    def creazione_ddt_uscita(self):
        self.navigateTo("Preventivi")
        self.wait_loader()

        self.send_keys_and_wait(self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))), 'Preventivo di Prova', wait_modal=False)

        self.wait_for_element_and_click('//tbody//tr//td[2]')
        totalepreventivo = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="righe"]//tbody[2]//tr[3]//td[2]'))
        ).text

        self.wait_for_element_and_click('//button[@class="btn btn-info dropdown-toggle "]')
        self.wait_for_element_and_click('//a[@class="btn dropdown-item bound clickable"][@data-title="Crea DDT in uscita"]')
        self.wait_for_element_and_click('//span[@id="select2-id_causale_trasporto-container"]')
        self.wait_for_element_and_click('//li[@class="select2-results__option select2-results__option--highlighted"]')
        self.wait_for_element_and_click('//span[@id="select2-id_segment-container"]')
        self.wait_for_element_and_click('//li[@class="select2-results__option select2-results__option--highlighted"]')
        self.wait_for_element_and_click('//button[@id="submit_btn"]')

        totaleddtuscita = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="righe"]//tbody[2]//tr[3]//td[2]'))
        ).text
        self.assertEqual(totaleddtuscita, totalepreventivo)

        self.wait_for_element_and_click('//div[@id="tab_0"]//a[@class="btn btn-danger ask"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')

        self.send_keys_and_wait(self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input'))), "03", wait_modal=False)

        eliminato = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//tbody//tr[1]//td[@class="dataTables_empty"]'))
        ).text
        self.assertEqual("Nessun dato presente nella tabella", eliminato)
        self.expandSidebar("Vendite")
        self.navigateTo("Preventivi")
        self.wait_loader()
        self.wait_for_element_and_click('//th[@id="th_Nome"]/i[@class="deleteicon fa fa-times"]')

    def creazione_fattura(self):
        self.navigateTo("Preventivi")
        self.wait_loader()

        self.send_keys_and_wait(self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))), 'Preventivo di Prova', wait_modal=False)

        self.wait_for_element_and_click('//tbody//tr//td[2]')
        totalepreventivo = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="righe"]//tbody[2]//tr[3]//td[2]'))
        ).text

        self.wait_for_element_and_click('//button[@class="btn btn-info dropdown-toggle "]')
        self.wait_for_element_and_click('//a[@class="btn dropdown-item bound clickable"][@data-title="Crea fattura"]')
        self.wait_for_element_and_click('//button[@id="submit_btn"]')

        totalefattura = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="righe"]//tbody[2]//tr[3]//td[2]'))
        ).text
        self.assertEqual(totalefattura, totalepreventivo)

        self.wait_for_element_and_click('//div[@id="tab_0"]//a[@class="btn btn-danger ask "]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')

        self.send_keys_and_wait(self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input'))), "0003/2026", wait_modal=False)

        eliminato = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//tbody//tr[1]//td[@class="dataTables_empty"]'))
        ).text
        self.assertEqual("Nessun dato presente nella tabella", eliminato)
        self.navigateTo("Preventivi")
        self.wait_loader()
        self.wait_for_element_and_click('//th[@id="th_Nome"]/i[@class="deleteicon fa fa-times"]')

    def verifica_preventivi(self):
        self.navigateTo("Preventivi")
        self.wait_loader()

        self.send_keys_and_wait(self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))), "Preventivo di Prova", wait_modal=False)

        modificato = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//tbody//tr[1]//td[3]'))
        ).text
        self.assertEqual("Preventivo di Prova", modificato)
        self.wait_for_element_and_click('//i[@class="deleteicon fa fa-times"]')

        self.send_keys_and_wait(self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))), "Preventivo di Prova da Eliminare", wait_modal=False)

        eliminato = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//td[@class="dataTables_empty"]'))
        ).text
        self.assertEqual("Nessun dato presente nella tabella", eliminato)
        self.wait_for_element_and_click('//i[@class="deleteicon fa fa-times"]')

