from common.Test import Test, get_html
from selenium.webdriver.common.keys import Keys
from common.RowManager import RowManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep

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
        self.consuntivo()
        self.revisioni()
        self.cambia_stato()
        self.fattura_preventivi()

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
        nome_field = self.find(By.XPATH, '//input[@id="nome"]')
        nome_field.send_keys(" da Eliminare")

        self.wait_for_element_and_click('//button[@class="btn btn-success"]')

    def modifica_preventivo(self, stato:str):
        self.navigateTo("Preventivi")
        self.wait_loader()

        self.send_keys_and_wait(self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))), '=Preventivo di Prova', False)

        self.wait_for_element_and_click('//tbody//tr//td[2]')

        select = self.input(None, 'Stato')
        select.setByText(stato)
        self.wait_for_element_and_click('//div[@id="tab_0"]//button[@id="save"]')

        sconto = self.find(By.XPATH, '//div[@id="righe"]//tbody[2]//tr[2]//td[2]').text
        totale_imponibile = self.find(By.XPATH, '//div[@id="righe"]//tbody[2]//tr[3]//td[2]').text
        iva = self.find(By.XPATH, '//div[@id="righe"]//tbody[2]//tr[4]//td[2]').text
        totale = self.find(By.XPATH, '//div[@id="tab_0"]//div[@id="righe"]//tbody[2]//tr[5]//td[2]').text

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

        self.send_keys_and_wait(self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))), '=Preventivo di Prova da Eliminare', False)

        self.wait_for_element_and_click('//tbody//tr//td[2]')
        self.wait_for_element_and_click('//div[@id="tab_0"]//a[@class="btn btn-danger ask"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')

        self.navigateTo("Preventivi")
        self.wait_loader()
        self.wait_for_element_and_click('//th[@id="th_Nome"]/i[@class="deleteicon fa fa-times"]')

    def creazione_contratto(self):
        self.navigateTo("Preventivi")
        self.wait_loader()

        self.send_keys_and_wait(self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))), 'Preventivo di Prova', False)

        self.wait_for_element_and_click('//tbody//tr//td[2]')
        totalepreventivo = self.find(By.XPATH, '//div[@id="righe"]//tbody[2]//tr[3]//td[2]').text

        self.wait_for_element_and_click('//div[@id="pulsanti"]//button[@class="btn btn-info dropdown-toggle "]')
        self.wait_for_element_and_click('//a[@class="btn dropdown-item bound clickable"][@data-title="Crea contratto"]')
        self.wait_for_element_and_click('//span[@id="select2-id_segment-container"]')
        self.wait_for_element_and_click('//li[@class="select2-results__option select2-results__option--highlighted"]')
        self.wait_for_element_and_click('//button[@id="submit_btn"]')

        totalecontratto = self.find(By.XPATH, '//div[@id="righe"]//tbody[2]//tr[3]//td[2]').text
        self.assertEqual(totalecontratto, totalepreventivo)

        self.wait_for_element_and_click('//div[@id="tab_0"]//a[@class="btn btn-danger ask"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')

        self.send_keys_and_wait(self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))), "Preventivo di Prova", False)

        eliminato = self.find(By.XPATH, '//tbody//tr[1]//td[@class="dataTables_empty"]').text
        self.assertEqual("La ricerca non ha portato alcun risultato.", eliminato)
        self.navigateTo("Preventivi")
        self.wait_loader()
        self.wait_for_element_and_click('//th[@id="th_Nome"]/i[@class="deleteicon fa fa-times"]')

    def creazione_ordine_cliente(self):
        self.navigateTo("Preventivi")
        self.wait_loader()

        self.send_keys_and_wait(self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))), 'Preventivo di Prova', False)

        self.wait_for_element_and_click('//tbody//tr//td[2]')
        totalepreventivo = self.find(By.XPATH, '//div[@id="righe"]//tbody[2]//tr[3]//td[2]').text

        self.wait_for_element_and_click('//button[@class="btn btn-info dropdown-toggle "]')
        self.wait_for_element_and_click('//a[@class="btn dropdown-item bound clickable"][@data-title="Crea ordine cliente"]')
        self.wait_for_element_and_click('//span[@id="select2-id_segment-container"]')
        self.wait_for_element_and_click('//li[@class="select2-results__option select2-results__option--highlighted"]')
        self.wait_for_element_and_click('//button[@id="submit_btn"]')

        totaleordinecliente = self.find(By.XPATH, '//div[@id="righe"]//tbody[2]//tr[3]//td[2]').text
        self.assertEqual(totaleordinecliente, totalepreventivo)

        self.wait_for_element_and_click('//div[@id="tab_0"]//a[@class="btn btn-danger ask"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')

        self.send_keys_and_wait(self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_icon_title_Stato"]/input'))), "Bozza", False)

        eliminato = self.find(By.XPATH, '//tbody//tr[1]//td[@class="dataTables_empty"]').text
        self.assertEqual("La ricerca non ha portato alcun risultato.", eliminato)
        self.navigateTo("Preventivi")
        self.wait_loader()
        self.wait_for_element_and_click('//th[@id="th_Nome"]/i[@class="deleteicon fa fa-times"]')

    def creazione_ordine_fornitore(self):
        self.navigateTo("Preventivi")
        self.wait_loader()

        self.send_keys_and_wait(self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))), 'Preventivo di Prova', False)

        self.wait_for_element_and_click('//tbody//tr//td[2]')

        self.wait_for_element_and_click('//button[@class="btn btn-info dropdown-toggle "]')
        self.wait_for_element_and_click('//a[@class="btn dropdown-item bound clickable"][@data-title="Crea ordine fornitore"]')
        self.wait_for_element_and_click('(//span [@id="select2-idanagrafica-container"])[2]')
        self.wait_for_element_and_click('//li[@class="select2-results__option select2-results__option--highlighted"]')
        self.wait_for_element_and_click('//span[@id="select2-id_segment-container"]')
        self.wait_for_element_and_click('//li[@class="select2-results__option select2-results__option--highlighted"]')
        self.wait_for_element_and_click('//button[@id="submit_btn"]')

        totaleordinefornitore = self.find(By.XPATH, '//div[@id="righe"]//tbody[2]//tr[3]//td[2]').text
        self.assertEqual(totaleordinefornitore, self.valori["Totale imponibile"] + ' €')

        self.wait_for_element_and_click('//div[@id="tab_0"]//a[@class="btn btn-danger ask"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')

        self.send_keys_and_wait(self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_icon_title_Stato"]/input'))), "Bozza", False)

        eliminato = self.find(By.XPATH, '//tbody//tr[1]//td[@class="dataTables_empty"]').text
        self.assertEqual("La ricerca non ha portato alcun risultato.", eliminato)
        self.expandSidebar("Vendite")
        self.navigateTo("Preventivi")
        self.wait_loader()
        self.wait_for_element_and_click('//th[@id="th_Nome"]/i[@class="deleteicon fa fa-times"]')

    def creazione_attività(self):
        self.navigateTo("Preventivi")
        self.wait_loader()

        self.send_keys_and_wait(self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))), 'Preventivo di Prova', False)

        self.wait_for_element_and_click('//tbody//tr//td[2]')
        totalepreventivo = self.find(By.XPATH, '//div[@id="righe"]//tbody[2]//tr[3]//td[2]').text

        self.wait_for_element_and_click('//button[@class="btn btn-info dropdown-toggle "]')
        self.wait_for_element_and_click('//a[@class="btn dropdown-item bound clickable"][@data-title="Crea attività"]')
        self.wait_for_element_and_click('//span[@id="select2-id_tipo_intervento-container"]')
        self.wait_for_element_and_click('//li[@class="select2-results__option select2-results__option--highlighted"]')
        self.wait_for_element_and_click('//span[@id="select2-id_stato_intervento-container"]')
        self.wait_for_element_and_click('//li[@class="select2-results__option"]')
        self.wait_for_element_and_click('//span[@id="select2-id_segment-container"]')
        self.wait_for_element_and_click('//li[@class="select2-results__option select2-results__option--highlighted"]')
        self.wait_for_element_and_click('//button[@id="submit_btn"]')

        totaleattività = self.find(By.XPATH, '//div[@id="righe"]//tbody[2]//tr[3]//td[2]').text
        self.assertEqual(totaleattività, totalepreventivo)

        self.wait_for_element_and_click('//div[@id="tab_0"]//a[@class="btn btn-danger ask"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')

        self.send_keys_and_wait(self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input'))), "03", False)

        eliminato = self.find(By.XPATH, '//tbody//tr[1]//td[@class="dataTables_empty"]').text
        self.assertEqual("La ricerca non ha portato alcun risultato.", eliminato)
        self.expandSidebar("Vendite")
        self.navigateTo("Preventivi")
        self.wait_loader()
        self.wait_for_element_and_click('//th[@id="th_Nome"]/i[@class="deleteicon fa fa-times"]')

    def creazione_ddt_uscita(self):
        self.navigateTo("Preventivi")
        self.wait_loader()

        self.send_keys_and_wait(self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))), 'Preventivo di Prova', False)

        self.wait_for_element_and_click('//tbody//tr//td[2]')
        totalepreventivo = self.find(By.XPATH, '//div[@id="righe"]//tbody[2]//tr[3]//td[2]').text

        self.wait_for_element_and_click('//button[@class="btn btn-info dropdown-toggle "]')
        self.wait_for_element_and_click('//a[@class="btn dropdown-item bound clickable"][@data-title="Crea ordine cliente"]//i[@class="fa fa-truck"]')
        self.wait_for_element_and_click('//span[@id="select2-id_causale_trasporto-container"]')
        self.wait_for_element_and_click('//li[@class="select2-results__option select2-results__option--highlighted"]')
        self.wait_for_element_and_click('//span[@id="select2-id_segment-container"]')
        self.wait_for_element_and_click('//li[@class="select2-results__option select2-results__option--highlighted"]')
        self.wait_for_element_and_click('//button[@id="submit_btn"]')

        totaleddtuscita = self.find(By.XPATH, '//div[@id="righe"]//tbody[2]//tr[3]//td[2]').text
        self.assertEqual(totaleddtuscita, totalepreventivo)

        self.wait_for_element_and_click('//div[@id="tab_0"]//a[@class="btn btn-danger ask"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')

        self.send_keys_and_wait(self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input'))), "03", False)

        eliminato = self.find(By.XPATH, '//tbody//tr[1]//td[@class="dataTables_empty"]').text
        self.assertEqual("La ricerca non ha portato alcun risultato.", eliminato)
        self.expandSidebar("Vendite")
        self.navigateTo("Preventivi")
        self.wait_loader()
        self.wait_for_element_and_click('//th[@id="th_Nome"]/i[@class="deleteicon fa fa-times"]')

    def creazione_fattura(self):
        self.navigateTo("Preventivi")
        self.wait_loader()

        self.send_keys_and_wait(self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))), 'Preventivo di Prova', False)

        self.wait_for_element_and_click('//tbody//tr//td[2]')
        totalepreventivo = self.find(By.XPATH, '//div[@id="righe"]//tbody[2]//tr[3]//td[2]').text

        self.wait_for_element_and_click('//button[@class="btn btn-info dropdown-toggle "]')
        self.wait_for_element_and_click('//a[@class="btn dropdown-item bound clickable"][@data-title="Crea fattura"]')
        self.wait_for_element_and_click('//button[@id="submit_btn"]')

        totalefattura = self.find(By.XPATH, '//div[@id="righe"]//tbody[2]//tr[3]//td[2]').text
        self.assertEqual(totalefattura, totalepreventivo)

        self.wait_for_element_and_click('//div[@id="tab_0"]//a[@class="btn btn-danger ask "]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')

        self.send_keys_and_wait(self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input'))), "0003/2025", False)

        eliminato = self.find(By.XPATH, '//tbody//tr[1]//td[@class="dataTables_empty"]').text
        self.assertEqual("La ricerca non ha portato alcun risultato.", eliminato)
        self.navigateTo("Preventivi")
        self.wait_loader()
        self.wait_for_element_and_click('//th[@id="th_Nome"]/i[@class="deleteicon fa fa-times"]')

    def verifica_preventivi(self):
        self.navigateTo("Preventivi")
        self.wait_loader()

        self.send_keys_and_wait(self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))), "Preventivo di Prova", False)

        modificato = self.find(By.XPATH, '//tbody//tr[1]//td[3]').text
        self.assertEqual("Preventivo di Prova", modificato)
        self.wait_for_element_and_click('//i[@class="deleteicon fa fa-times"]')

        self.send_keys_and_wait(self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))), "Preventivo di Prova da Eliminare", False)

        eliminato = self.find(By.XPATH, '//td[@class="dataTables_empty"]').text
        self.assertEqual("La ricerca non ha portato alcun risultato.", eliminato)
        self.wait_for_element_and_click('//i[@class="deleteicon fa fa-times"]')

    def consuntivo(self):
        self.navigateTo("Preventivi")
        self.wait_loader()

        self.wait_for_element_and_click('//tbody//tr//td[2]')
        self.wait_for_element_and_click('//a[@id="link-tab_12"]')
        budget = self.find(By.XPATH, '//span[@class="text-success"]').text
        self.assertEqual(budget, "+ 264,80 €")

    def revisioni(self):
        self.navigateTo("Preventivi")
        self.wait_loader()

        self.wait_for_element_and_click('//tbody//tr//td[3]')
        self.wait_for_element_and_click('//a[@id="link-tab_20"]')
        self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_20"]//td[@class="text-center"][1]')))

    def cambia_stato(self):
        self.navigateTo("Preventivi")
        self.wait_loader()

        self.send_keys_and_wait(self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input'))), "1", False)

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_element_and_click('//button[@data-toggle="dropdown"]')
        self.wait_for_element_and_click('//a[@data-op="change_status"]')

        self.wait_for_dropdown_and_select('//span[@id="select2-id_stato-container"]', option_text='Bozza')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-warning"]')

        stato = self.find(By.XPATH, '//tbody//tr//td[6]').text
        self.assertEqual(stato, "Bozza")

        self.wait_for_element_and_click('//button[@data-toggle="dropdown"]')
        self.wait_for_element_and_click('//a[@data-op="change_status"]')

        self.wait_for_dropdown_and_select('//span[@id="select2-id_stato-container"]', option_text='Accettato')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-warning"]')

        self.wait_for_element_and_click('//i[@class="deleteicon fa fa-times"]')

    def fattura_preventivi(self):
        self.navigateTo("Preventivi")
        self.wait_loader()

        self.send_keys_and_wait(self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input'))), "1", False)

        self.wait_for_element_and_click('//tbody//tr//td[1]')
        self.wait_for_element_and_click('//button[@data-toggle="dropdown"]')
        self.wait_for_element_and_click('//a[@data-op="crea_fattura"]')

        self.wait_for_dropdown_and_select('//span[@id="select2-raggruppamento-container"]', option_text='Cliente')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-warning"]')

        self.wait_for_element_and_click('//tbody//tr//td[2]')

        self.wait_for_dropdown_and_select('//span[@id="select2-idstato-container"]', option_text='In lavorazione')
        self.wait_for_element_and_click('//button[@id="save"]')
