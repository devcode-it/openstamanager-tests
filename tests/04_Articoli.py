from common.Test import Test
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Articoli(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Magazzino")
        self.wait_loader()

    def test_creazione_articolo(self):
        self.creazione_articolo("001", "Articolo 1", "2")
        self.creazione_articolo("002", "Articolo di Prova da Eliminare", "2")
        self.modifica_articolo("20", "1")
        self.elimina_articolo()
        self.verifica_articolo()
    

    def creazione_articolo(self, codice: str, descrizione: str, qta: str):
        self.navigateTo("Articoli")
        self.wait_loader()

        self.wait_for_element_and_click('//i[@class="fa fa-plus"]')
        modal = self.wait_modal()

        self.input(modal, 'Codice').setValue(codice)
        self.input(modal, 'Descrizione').setValue(descrizione)

        self.wait_for_element_and_click('//button[@class="btn btn-tool"]')
        self.wait(EC.visibility_of_element_located((By.XPATH, '//label[contains(text(), "Quantità iniziale")]/following-sibling::div/input')))

        self.input(modal, 'Quantità iniziale').setValue(qta)
        self.wait_for_element_and_click('button[type="submit"]', By.CSS_SELECTOR)

    def modifica_articolo(self, acquisto: str, coefficiente: str):
        self.navigateTo("Articoli")
        self.wait_loader()

        search_input = self.find(By.XPATH, '//th[@id="th_Descrizione"]/input')
        self.send_keys_and_wait(search_input, 'Articolo 1', False)

        self.click_first_result()

        self.input(None, 'Prezzo di acquisto').setValue(acquisto)
        self.input(None, 'Coefficiente').setValue(coefficiente)

        self.wait_for_element_and_click('//div[@id="tab_0"]//button[@id="save"]')
        self.wait_for_element_and_click('//a[@id="back"]')

        verificaqta = self.find(By.XPATH, '//div[@id="tab_0"]//tbody//td[10]//div[1][1]').text
        self.assertEqual(verificaqta, "2,00")

        self.clear_filters()

    def elimina_articolo(self):
        self.navigateTo("Articoli")
        self.wait_loader()

        search_input = self.find(By.XPATH, '//th[@id="th_Descrizione"]/input')
        self.send_keys_and_wait(search_input, 'Articolo di Prova da Eliminare', False)

        self.click_first_result()

        self.wait_for_element_and_click('//div[@id="tab_0"]//a[@class="btn btn-danger ask"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')

        self.clear_filters()

    def verifica_articolo(self):
        self.navigateTo("Articoli")
        self.wait_loader()

        search_input = self.find(By.XPATH, '//th[@id="th_Codice"]/input')
        self.send_keys_and_wait(search_input, '001', False)

        modificato = self.find(By.XPATH, '//tbody//tr[1]//td[9]').text
        self.assertEqual("20,00", modificato)
        self.clear_filters()

        search_input = self.find(By.XPATH, '//th[@id="th_Descrizione"]/input')
        self.send_keys_and_wait(search_input, 'Articolo di prova da Eliminare', False)

        eliminato = self.find(By.XPATH, '//tbody//tr[1]//td[1]').text
        self.assertEqual("La ricerca non ha portato alcun risultato.", eliminato)
        self.clear_filters()
