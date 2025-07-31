from common.Test import Test, get_html
from selenium.webdriver.common.keys import Keys
from common.RowManager import RowManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class Contratti(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Vendite")

    def test_creazione_contratto(self):
        importi = RowManager.list()
        self.creazione_contratto("Contratto di Prova da Modificare", "Cliente", importi[0])
        self.duplica_contratto()
        self.modifica_contratto("Contratto di Prova")
        self.elimina_contratto()
        self.verifica_contratto()
        self.contratti_del_cliente()
        self.consuntivo()
        self.pianificazione_attivita()
        self.pianificazione_fatturazione()
        self.rinnovi()
        self.cambia_stato()
        self.fattura_contratti()
        self.rinnova_contratti()

    def creazione_contratto(self, nome:str, cliente: str, file_importi: str):
        self.navigateTo("Contratti")
        self.wait_loader()

        self.wait_for_element_and_click('//i[@class="fa fa-plus"]')
        modal = self.wait_modal()

        self.input(modal, 'Nome').setValue(nome)
        select = self.input(modal, 'Cliente')
        select.setByText(cliente)
        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

        row_manager = RowManager(self)
        self.valori = row_manager.compile(file_importi)

    def duplica_contratto(self):
        self.navigateTo("Contratti")
        self.wait_loader()

        self.wait_for_element_and_click('//tbody//tr//td[2]')
        self.wait_for_element_and_click('//div[@id="pulsanti"]//button[@class="btn btn-primary ask"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-primary"]')

        element = self.find(By.XPATH, '//input[@id="nome"]')
        element.clear()
        element.send_keys("Contratto di Prova da Eliminare")
        self.wait_for_element_and_click('//button[@id="save"]')

    def modifica_contratto(self, modifica=str):
        self.navigateTo("Contratti")
        self.wait_loader()

        self.send_keys_and_wait(self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))), '=Contratto di Prova da Modificare', False)

        self.wait_for_element_and_click('//tbody//tr//td[2]')

        element = self.find(By.XPATH, '//input[@id="nome"]')
        element.clear()
        element.send_keys(modifica)
        self.wait_for_element_and_click('//div[@id="tab_0"]//button[@id="save"]')

        sconto = self.find(By.XPATH, '//div[@id="righe"]//tbody[2]//tr[2]//td[2]').text
        totale_imponibile = self.find(By.XPATH, '//div[@id="righe"]//tbody[2]//tr[3]//td[2]').text
        iva = self.find(By.XPATH, '//div[@id="righe"]//tbody[2]//tr[4]//td[2]').text
        totale = self.find(By.XPATH, '//div[@id="tab_0"]//div[@id="righe"]//tbody[2]//tr[5]//td[2]').text

        self.assertEqual(sconto, (self.valori["Sconto/maggiorazione"] + ' €'))
        self.assertEqual(totale_imponibile, (self.valori["Totale imponibile"] + ' €'))
        self.assertEqual(iva, (self.valori["IVA"] + ' €'))
        self.assertEqual(totale, (self.valori["Totale documento"] + ' €'))

        self.navigateTo("Contratti")
        self.wait_loader()
        self.wait_for_element_and_click('//th[@id="th_Nome"]/i[@class="deleteicon fa fa-times"]')

    def elimina_contratto(self):
        self.navigateTo("Contratti")
        self.wait_loader()

        self.send_keys_and_wait(self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))), 'Contratto di Prova da Eliminare', False)

        self.wait_for_element_and_click('//tbody//tr//td[2]')
        self.wait_for_element_and_click('//div[@id="tab_0"]//a[@class="btn btn-danger ask"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')

        self.wait_for_element_and_click('//th[@id="th_Nome"]/i[@class="deleteicon fa fa-times"]')

    def verifica_contratto(self):
        self.navigateTo("Contratti")
        self.wait_loader()

        self.send_keys_and_wait(self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))), "Contratto di Prova", False)

        modificato = self.driver.find_element(By.XPATH, '//tbody//tr[1]//td[3]').text
        self.assertEqual("Contratto di Prova", modificato)
        self.wait_for_element_and_click('//i[@class="deleteicon fa fa-times"]')

        self.send_keys_and_wait(self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))), "Contratto di Prova da Eliminare", False)

        eliminato = self.driver.find_element(By.XPATH, '//tbody//tr[1]//td[@class="dataTables_empty"]').text
        self.assertEqual("La ricerca non ha portato alcun risultato.", eliminato)
        self.wait_for_element_and_click('//th[@id="th_Nome"]/i[@class="deleteicon fa fa-times"]')

    def contratti_del_cliente(self):
        self.navigateTo("Anagrafiche")
        self.wait_loader()

        self.send_keys_and_wait(self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Ragione-sociale"]/input'))), "Cliente", False)

        self.wait_for_element_and_click('//tbody//tr//td[2]')
        self.wait_for_element_and_click('//a[@id="link-tab_35"]')

        self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_35"]//tbody//tr/td[2]')))

    def consuntivo(self):
        self.expandSidebar("Vendite")
        self.navigateTo("Contratti")
        self.wait_loader()

        self.send_keys_and_wait(self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))), "Contratto di Prova", False)

        self.wait_for_element_and_click('//tbody//tr/td[2]')
        self.wait_for_element_and_click('//a[@id="link-tab_13"]')

        budget = self.find(By.XPATH, '//div[@id="tab_13"]//span[@class="text-success"]').text
        self.assertEqual(budget, "+ 250,80 €")

        self.navigateTo("Contratti")
        self.wait_loader()
        self.wait_for_element_and_click('//i[@class="deleteicon fa fa-times"]')

    def pianificazione_attivita(self):
        self.navigateTo("Contratti")
        self.wait_loader()

        self.wait_for_element_and_click('//i[@class="fa fa-plus"]')
        modal = self.wait_modal()

        self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="nome"]'))).send_keys("Manutenzione")
        self.wait_for_dropdown_and_select('//span[@id="select2-idanagrafica-container"]', option_text='Cliente')
        self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="data_accettazione"]'))).send_keys("01/01/2025")
        self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="data_conclusione"]'))).send_keys("31/12/2025")
        self.wait_for_element_and_click('//button[@class="btn btn-primary"]')

        self.wait_for_element_and_click('//a[@class="btn btn-primary"]')

        self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("Manutenzione")
        self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="qta"]'))).send_keys("12")
        self.wait_for_dropdown_and_select('//span[@id="select2-um-container"]', option_text='pz')
        self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("50")
        self.wait_for_element_and_click('//button[@class="btn btn-primary pull-right"]')

        self.driver.execute_script('window.scrollTo(0,0)')
        self.wait_for_dropdown_and_select('//span[@id="select2-idstato-container"]', option_text='In lavorazione')
        self.wait_for_element_and_click('//button[@id="save"]')

        self.wait_for_element_and_click('//a[@id="link-tab_14"]')

        self.wait_for_dropdown_and_select('//span[@id="select2-id_tipo_promemoria-container"]', option_text='Generico')
        self.wait_for_element_and_click('//button[@id="add_promemoria"]')

        description_field = self.wait_for_element_and_click('(//iframe[@class="cke_wysiwyg_frame cke_reset"])[3]')
        description_field = self.wait_driver.until(EC.visibility_of_element_located(
            (By.XPATH, '(//iframe[@class="cke_wysiwyg_frame cke_reset"])[3]')
        ))
        self.send_keys_and_wait(description_field, "Test")

        self.wait_for_dropdown_and_select('//span[@id="select2-id_segment-container"]', option_text='Standard attività')
        self.wait_for_element_and_click('//div[@class="modal-content"]//button[@class="btn btn-primary"]')

        self.wait_for_element_and_click('//button[@class="btn btn-primary btn-sm  "]')
        self.wait_for_element_and_click('//button[@class="btn btn-lg btn-success"]')

        self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//tbody//tr[1]//a')))

    def pianificazione_fatturazione(self):
        self.wait_loader()
        self.navigateTo("Contratti")
        self.wait_loader()

        self.send_keys_and_wait(self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))), "Manutenzione", False)

        self.wait_for_element_and_click('//tbody//tr//td[2]')
        self.wait_for_element_and_click('//a[@id="link-tab_26"]')
        self.wait_for_element_and_click('//button[@id="pianifica"]')

        self.wait_for_element_and_click('(//div[@class="nav-tabs-custom"]//a[@class="nav-link"])[2]')
        self.wait_for_element_and_click('//button[@id="btn_procedi"]')
        self.wait_for_element_and_click('(//button[@class="btn btn-primary btn-sm "])[1]')

        self.wait_for_dropdown_and_select('//span[@id="select2-idtipodocumento-container"]', option_text='Fattura immediata di vendita')
        self.wait_for_element_and_click('//button[@class="btn btn-primary pull-right"]')

        self.navigateTo("Dashboard")
        self.wait_loader()

        self.wait_for_element_and_click('(//div[@id="widget_11"]//div)[2]')
        self.wait_for_element_and_click('(//div[@class="month-button-wrapper mr-2 mb-2"])[2]')
        self.wait_for_element_and_click('//button[@class="btn btn-success btn-sm"]')

        self.wait_for_dropdown_and_select('//span[@id="select2-idtipodocumento-container"]', option_text='Fattura immediata di vendita')
        self.wait_for_element_and_click('//button[@class="btn btn-primary pull-right"]')

        self.navigateTo("Contratti")
        self.wait_loader()

        self.wait_for_element_and_click('//tbody//tr//td[2]')
        self.wait_for_element_and_click('//a[@id="link-tab_26"]')

        link = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_26"]//tbody//tr//td[2]'))).text
        self.assertEqual(link, "Fattura num. del 01/01/2025 ( Bozza)")

        self.navigateTo("Contratti")
        self.wait_loader()
        self.wait_for_element_and_click('//i[@class="deleteicon fa fa-times"]')

    def rinnovi(self):
        self.navigateTo("Contratti")
        self.wait_loader()

        self.wait_for_element_and_click('//tbody//tr//td[2]')

        self.wait_for_element_and_click('(//label[@for="rinnovabile"])[2]')
        self.wait_for_element_and_click('//button[@id="save"]')

    def cambia_stato(self):
        self.navigateTo("Contratti")
        self.wait_loader()

        self.send_keys_and_wait(self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input'))), "2", False)

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_element_and_click('//button[@data-toggle="dropdown"]')
        self.wait_for_element_and_click('//a[@data-op="change_status"]')

        self.wait_for_dropdown_and_select('//span[@id="select2-id_stato-container"]', option_text='In lavorazione')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-warning"]')

        stato = self.find(By.XPATH, '//tbody//tr//td[5]').text
        self.assertEqual(stato, "In lavorazione")

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_element_and_click('//i[@class="deleteicon fa fa-times"]')


    def fattura_contratti(self):
        self.navigateTo("Contratti")
        self.wait_loader()

        self.send_keys_and_wait(self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input'))), "2", False)

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_element_and_click('//button[@data-toggle="dropdown"]')
        self.wait_for_element_and_click('//a[@data-op="create_invoice"]')

        self.wait_for_dropdown_and_select('//span[@id="select2-raggruppamento-container"]', option_text='Cliente')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-warning"]')

        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        tipo = self.find(By.XPATH, '//tbody//tr[1]//td[5]').text
        self.assertEqual(tipo, "Fattura immediata di vendita")

        self.wait_for_element_and_click('//tbody//tr[2]//td[4]')
        self.wait_for_element_and_click('//div[@id="tab_0"]//a[@class="btn btn-danger ask "]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')

        self.navigateTo("Contratti")
        self.wait_loader()
        self.wait_for_element_and_click('//i[@class="deleteicon fa fa-times"]')

    def rinnova_contratti(self):
        self.navigateTo("Contratti")
        self.wait_loader()

        self.send_keys_and_wait(self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input'))), "1", False)

        self.wait_for_element_and_click('//tbody//tr//td[2]')

        self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="data_accettazione"]'))).send_keys("01/01/2025")
        self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="data_conclusione"]'))).send_keys("31/12/2025")
        self.wait_for_dropdown_and_select('//span[@id="select2-idstato-container"]', option_text='Accettato')
        self.wait_for_element_and_click('//button[@id="save"]')

        self.navigateTo("Contratti")
        self.wait_loader()

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_element_and_click('//button[@data-toggle="dropdown"]')
        self.wait_for_element_and_click('//a[@data-op="renew_contract"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-warning"]')

        self.wait_for_element_and_click('(//i[@class="deleteicon fa fa-times"])[1]')

        self.send_keys_and_wait(self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input'))), "3", False)

        self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//tbody//tr//td[2]')))
        self.wait_for_element_and_click('//tbody//tr//td[2]')
        self.wait_for_element_and_click('//div[@id="tab_0"]//a[@class="btn btn-danger ask"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')

        self.wait_for_element_and_click('(//i[@class="deleteicon fa fa-times"])[1]')
