from common.Test import Test
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Combinazioni(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Magazzino")

    def test_creazione_combinazioni(self):
        self.creazione_combinazioni(
            codice="0001",
            nome="Combinazione di Prova da Modificare",
            attributi="Taglie"
        )
        self.creazione_combinazioni(
            codice="0002",
            nome="Combinazione di Prova da Eliminare",
            attributi="Taglie"
        )
        self.modifica_combinazioni("Vestito")
        self.elimina_combinazioni()
        self.verifica_combinazioni()
        self.varianti_articoli()

    def creazione_combinazioni(self, codice: str, nome: str, attributi: str):
        self.navigate_to_and_wait("Combinazioni")

        self.click_add_button()
        modal = self.wait_modal()

        self.input(modal, 'Codice').setValue(codice)
        self.input(modal, 'Nome').setValue(nome)
        self.input(modal, 'Attributi').setByText(attributi)

        self.wait_for_element_and_click('button[type="submit"]', By.CSS_SELECTOR)

    def modifica_combinazioni(self, modifica):
        self.navigate_to_and_wait("Combinazioni")

        search_input = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))
        )
        self.send_keys_and_wait(search_input, 'Combinazione di Prova da Modificare', wait_modal=False)

        self.click_first_table_row()
        self.input(None,'Nome').setValue(modifica)
        self.click_save_button()
        self.wait_for_element_and_click('//button[@onclick="generaVarianti(this)"]')
        self.click_save_button()

        self.navigate_to_and_wait("Combinazioni")
        self.clear_filters()

    def elimina_combinazioni(self):
        self.navigate_to_and_wait("Combinazioni")

        search_input = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))
        )
        self.send_keys_and_wait(search_input, 'Combinazione di Prova da Eliminare', wait_modal=False)

        self.click_first_table_row()
        self.delete_current_and_clear()

    def verifica_combinazioni(self):
        self.navigate_to_and_wait("Combinazioni")

        search_input = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))
        )
        self.send_keys_and_wait(search_input, "Vestito", wait_modal=False)

        modificato = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//tbody//tr[1]//td[3]'))
        ).text
        self.assertEqual("Vestito", modificato)

        self.clear_filters()

        search_input = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))
        )
        self.send_keys_and_wait(search_input, "Attributo di Prova da Eliminare", wait_modal=False)

        eliminato = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//tbody//tr[1]//td[@class="dataTables_empty"]'))
        ).text
        self.assertEqual("Nessun dato presente nella tabella", eliminato)

    def varianti_articoli(self):
        self.navigate_to_and_wait("Articoli")

        search_input = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input'))
        )
        self.send_keys_and_wait(search_input, 'Vestito', wait_modal=False)

        self.click_first_table_row()
        self.wait_for_element_and_click('//a[@id="link-tab_34"]')

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_34"]//tr[3]'))
        )

        self.navigate_to_and_wait("Attributi Combinazioni")

        self.click_first_table_row()
        self.wait_for_element_and_click('(//button[@class="btn btn-warning btn-xs"])[1]')

        element = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//input[@id="nome"]'))
        )
        element.clear()
        self.send_keys_and_wait(element, "XS", wait_modal=False)

        self.navigate_to_and_wait("Articoli")

        self.click_first_table_row()
        self.wait_for_element_and_click('//a[@id="link-tab_34"]')

        taglia = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_34"]//div[@class="card card-primary"]//tbody//tr//td[2]'))
        ).text
        self.assertEqual(taglia, "Taglie: XS")

        self.navigate_to_and_wait("Combinazioni")

        self.clear_filters()
        self.click_first_table_row()
        self.delete_current_and_clear()