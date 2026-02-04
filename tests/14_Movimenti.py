from common.Test import Test
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Movimenti(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Magazzino")

    def test_creazione_movimento(self):
        self.navigateTo("Movimenti")
        self.wait_loader()

        self.wait_for_element_and_click('//i[@class="fa fa-plus"]')

        self.creazione_movimento("10", "Articolo 1", "Movimento di Prova")
        self.creazione_movimento("5", "Articolo 1", "Movimento di Prova da Eliminare")
        self.elimina_movimento()
        self.verifica_movimento()
        self.verifica_movimenti_documenti()
        self.wait_for_element_and_click('//i[@class="fa fa-power-off nav-icon"]')

    def creazione_movimento(self, qta: str, articolo: str, descrizione: str):
        modal = self.wait_modal()
        self.wait_for_dropdown_and_select('//span[@id="select2-idarticolo-container"]', option_text=articolo)
        self.input(modal, 'Quantità').setValue(qta)
        descrizione_field = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="movimento"]')))
        descrizione_field.clear()
        descrizione_field.send_keys(descrizione)
        self.wait_for_element_and_click('//div[@class="modal-body"]//button[@type="button"]')


    def elimina_movimento(self):
        self.wait_for_element_and_click('//button[@class="close"]')
        search_field = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input')))
        self.send_keys_and_wait(search_field, 'Movimento di Prova da Eliminare', wait_modal=False)
        self.wait_for_element_and_click('//tbody//tr//td[2]')
        self.wait_for_element_and_click('(//a[@class="btn btn-danger btn-xs ask"]//i[@class="fa fa-trash"])[2]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')

        self.navigateTo("Movimenti")
        self.wait_loader()
        self.wait_for_element_and_click('//th[@id="th_Descrizione"]/i[@class="deleteicon fa fa-times"]')

    def verifica_movimento(self):
        self.navigateTo("Movimenti")
        self.wait_loader()
        search_field = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input')))
        self.send_keys_and_wait(search_field, "Movimento di prova da Eliminare", wait_modal=False)
        eliminato = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//tbody//tr[1]//td[@class="dataTables_empty"]'))
        ).text
        self.assertEqual("Nessun dato presente nella tabella", eliminato)

    def verifica_movimenti_documenti(self):
        self.navigateTo("Articoli")
        self.wait_loader()
        search_field = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Codice"]/input')))
        self.send_keys_and_wait(search_field, "001", wait_modal=False)
        self.wait_for_element_and_click('//tbody//tr//td[2]')
        self.wait_for_element_and_click('//a[@id="link-tab_10"]')

        base_xpath = '//div[@id="tab_10"]//div[@class="card"]//div[@class="card-body"]//tbody'
        ddt_entrata = self.find(By.XPATH, f'{base_xpath}//tr[2]//td[2]').text
        ddt_uscita = self.find(By.XPATH, f'{base_xpath}//tr[3]//td[3]').text
        movimento = self.find(By.XPATH, f'{base_xpath}//tr[4]//td[2]').text
        attività = self.find(By.XPATH, f'{base_xpath}//tr[5]//td[3]').text
        fattura_acquisto = self.find(By.XPATH, f'{base_xpath}//tr[6]//td[2]').text
        fattura_vendita = self.find(By.XPATH, f'{base_xpath}//tr[7]//td[3]').text
        nota_credito = self.find(By.XPATH, f'{base_xpath}//tr[8]//td[2]').text
        fattura_acquisto2 = self.find(By.XPATH, f'{base_xpath}//tr[9]//td[2]').text

        self.assertEqual(ddt_entrata, "1,00")
        self.assertEqual(ddt_uscita, "1,00")
        self.assertEqual(movimento, "10,00")
        self.assertEqual(attività, "1,00")
        self.assertEqual(fattura_acquisto, "1,00")
        self.assertEqual(fattura_vendita, "1,00")
        self.assertEqual(nota_credito, "1,00")
        self.assertEqual(fattura_acquisto2, "1,00")




