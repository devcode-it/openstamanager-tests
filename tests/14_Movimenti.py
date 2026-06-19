from common.Test import Test
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Movimenti(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Magazzino")

    def test_creazione_movimento(self):
        self.navigate_to_and_wait("Movimenti")

        self.click_add_button()

        self._creazione_movimento("10", "Articolo 1", "Movimento di Prova")
        self._creazione_movimento("5", "Articolo 1", "Movimento di Prova da Eliminare")
        self._elimina_movimento()
        self._verifica_movimento()
        self._verifica_movimenti_documenti()

    def _creazione_movimento(self, qta: str, articolo: str, descrizione: str):
        modal = self.wait_modal()
        self.wait_for_dropdown_and_select('//span[@id="select2-id_articolo-container"]', option_text=articolo)
        self.input(modal, 'Quantità').setValue(qta)
        descrizione_field = self.find(By.XPATH, '//textarea[@id="movimento"]')
        descrizione_field.clear()
        descrizione_field.send_keys(descrizione)
        self.wait_for_element_and_click('//button[@id="aggiungi"]')


    def _elimina_movimento(self):
        self.wait_for_element_and_click('//button[@class="close"]')
        search_field = self.find(By.XPATH, '//th[@id="th_Descrizione"]/input')
        self.send_keys_and_wait(search_field, 'Movimento di Prova da Eliminare', wait_modal=False)
        self.click_first_table_row()
        self.wait_for_element_and_click('(//a[@class="btn btn-danger btn-xs ask"]//i[@class="fa fa-trash"])[1]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-success"]')

        self.navigate_to_and_wait("Movimenti")
        self.wait_for_element_and_click('//th[@id="th_Descrizione"]/i[@class="deleteicon fa fa-times"]')

    def _verifica_movimento(self):
        self.navigate_to_and_wait("Movimenti")
        search_field = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input')))
        self.send_keys_and_wait(search_field, "Movimento di prova da Eliminare", wait_modal=False)
        eliminato = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//tbody//tr[1]//td[@class="dataTables_empty"]'))
        ).text
        self.assertEqual("Nessun dato presente nella tabella", eliminato)

    def _verifica_movimenti_documenti(self):
        self.navigate_to_and_wait("Articoli")
        search_field = self.find(By.XPATH, '//th[@id="th_Codice"]/input')
        self.send_keys_and_wait(search_field, "001", wait_modal=False)
        self.click_first_table_row()
        self.wait_for_element_and_click('//a[@id="link-tab_10"]')

        base_xpath = '//div[@id="tab_10"]//div[@class="card"]//div[@class="card-body"]//tbody'

        movimento = self.find(By.XPATH, f'{base_xpath}//tr[2]//td[2]').text
        ddt_uscita = self.find(By.XPATH, f'{base_xpath}//tr[3]//td[3]').text   
        ddt_entrata = self.find(By.XPATH, f'{base_xpath}//tr[4]//td[2]').text
        fattura_acquisto2 = self.find(By.XPATH, f'{base_xpath}//tr[5]//td[2]').text
        nota_credito = self.find(By.XPATH, f'{base_xpath}//tr[6]//td[2]').text
        fattura_vendita = self.find(By.XPATH, f'{base_xpath}//tr[7]//td[3]').text
        fattura_acquisto = self.find(By.XPATH, f'{base_xpath}//tr[8]//td[2]').text
        attività = self.find(By.XPATH, f'{base_xpath}//tr[9]//td[3]').text
        carico = self.find(By.XPATH, f'{base_xpath}//tr[10]//td[2]').text

        self.assertEqual(attività, "1,00")
        self.assertEqual(fattura_acquisto, "1,00")
        self.assertEqual(fattura_vendita, "1,00")
        self.assertEqual(nota_credito, "1,00")
        self.assertEqual(fattura_acquisto2, "1,00")
        self.assertEqual(carico, "2,00")
        self.assertEqual(ddt_entrata, "1,00")
        self.assertEqual(ddt_uscita, "1,00")
        self.assertEqual(movimento, "10,00")
