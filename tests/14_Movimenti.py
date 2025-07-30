from common.Test import Test, get_html
from common.RowManager import RowManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Movimenti(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Magazzino")
        self.navigateTo("Movimenti")
        self.wait_loader()
        self.wait_for_element_and_click('//i[@class="fa fa-plus"]')

    def test_creazione_movimento(self, modifica="Movimento di Prova"):
        self.creazione_movimento("10", "Articolo di Prova", "Movimento di Prova")
        self.creazione_movimento("5", "Articolo di Prova", "Movimento di Prova da Eliminare")
        self.elimina_movimento()
        self.verifica_movimento()
        self.verifica_movimenti_documenti()

    def creazione_movimento(self, qta: str, articolo: str, descrizione:str):
        modal = self.wait_modal()

        self.wait_for_dropdown_and_select('//span[@id="select2-idarticolo-container"]', option_text=articolo)

        self.input(modal, 'Quantità').setValue(qta)
        element = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="movimento"]')))
        element.clear()
        element.send_keys(descrizione)

    def elimina_movimento(self):
        self.wait_for_element_and_click('//button[@class="close"]')

        self.send_keys_and_wait(self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input'))), 'Movimento di Prova da Eliminare', False)

        self.wait_for_element_and_click('//tbody//tr//td[2]')
        self.wait_for_element_and_click('//a[@class="btn btn-danger btn-xs ask"]/i[@class="fa fa-trash"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')

        self.navigateTo("Movimenti")
        self.wait_loader()
        self.wait_for_element_and_click('//th[@id="th_Descrizione"]/i[@class="deleteicon fa fa-times"]')

    def verifica_movimento(self):
        self.navigateTo("Movimenti")
        self.wait_loader()

        self.send_keys_and_wait(self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input'))), "Movimento di prova da Eliminare", False)

        eliminato = self.driver.find_element(By.XPATH, '//tbody//tr[1]//td[@class="dataTables_empty"]').text
        self.assertEqual("La ricerca non ha portato alcun risultato.", eliminato)

    def verifica_movimenti_documenti(self):
        self.navigateTo("Articoli")
        self.wait_loader()

        self.send_keys_and_wait(self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Codice"]/input'))), "001", False)

        self.wait_for_element_and_click('//tbody//tr//td[2]')
        self.wait_for_element_and_click('//a[@id="link-tab_10"]')

        movimento = self.find(By.XPATH, '//div[@id="tab_10"]//div[@class="card"]//div[@class="card-body"]//tbody//tr[2]//td[2]').text
        fattura_vendita = self.find(By.XPATH, '//div[@id="tab_10"]//div[@class="card"]//div[@class="card-body"]//tbody//tr[3]//td[2]').text
        ddt_uscita = self.find(By.XPATH, '//div[@id="tab_10"]//div[@class="card"]//div[@class="card-body"]//tbody//tr[4]//td[2]').text
        ddt_entrata = self.find(By.XPATH, '//div[@id="tab_10"]//div[@class="card"]//div[@class="card-body"]//tbody//tr[5]//td[2]').text
        fattura_acquisto2 = self.find(By.XPATH, '//div[@id="tab_10"]//div[@class="card"]//div[@class="card-body"]//tbody//tr[6]//td[2]').text
        fattura_vendita2 = self.find(By.XPATH, '//div[@id="tab_10"]//div[@class="card"]//div[@class="card-body"]//tbody//tr[7]//td[2]').text
        fattura_acquisto = self.find(By.XPATH, '//div[@id="tab_10"]//div[@class="card"]//div[@class="card-body"]//tbody//tr[8]//td[2]').text
        attività = self.find(By.XPATH, '//div[@id="tab_10"]//div[@class="card"]//div[@class="card-body"]//tbody//tr[9]//td[2]').text
        eliminazioneserial = self.find(By.XPATH, '//div[@id="tab_10"]//div[@class="card"]//div[@class="card-body"]//tbody//tr[10]//td[2]').text
        serial = self.find(By.XPATH, '//div[@id="tab_10"]//div[@class="card"]//div[@class="card-body"]//tbody//tr[11]//td[2]').text
        carico = self.find(By.XPATH, '//div[@id="tab_10"]//div[@class="card"]//div[@class="card-body"]//tbody//tr[12]//td[2]').text

        self.assertEqual(movimento, "10,00")
        self.assertEqual(fattura_vendita, "-1,00")
        self.assertEqual(ddt_uscita, "-1,00")
        self.assertEqual(ddt_entrata, "1,00")
        self.assertEqual(fattura_acquisto2, "1,00")
        self.assertEqual(fattura_vendita2, "-1,00")
        self.assertEqual(fattura_acquisto, "1,00")
        self.assertEqual(attività, "-1,00")
        self.assertEqual(eliminazioneserial, "-1,00")
        self.assertEqual(serial, "2,00")
        self.assertEqual(carico, "2,00")
