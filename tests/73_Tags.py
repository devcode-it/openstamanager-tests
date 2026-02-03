from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from common.Test import Test


class Tags(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Attività")
        self.wait_loader()
        
    def test_creazione_tags(self):
        self.expandSidebar("Strumenti")
        self.expandSidebar("Tabelle")
        self.creazione_tags("Tags di Prova da Modificare")
        self.creazione_tags("Tags di Prova da Eliminare")
        self.modifica_tags("Tags di Prova")
        self.elimina_tags()
        self.verifica_tags()

    def creazione_tags(self, descrizione: str):
        self.navigateTo("Tags")
        self.wait_loader()
        self.wait_for_element_and_click('//i[@class="fa fa-plus"]')
        modal = self.wait_modal()
        self.input(modal, 'Nome').setValue(descrizione)
        self.wait_for_element_and_click('button[type="submit"]', By.CSS_SELECTOR)

    def search_tag(self, nome: str):
        self.navigateTo("Tags")
        self.wait_loader()
        search_input = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))
        )
        search_input.clear()
        self.send_keys_and_wait(search_input, nome, wait_modal=False)

    def modifica_tags(self, modifica: str):
        self.search_tag('Tags di Prova da Modificare')
        self.click_first_result()
        self.input(None, 'Nome').setValue(modifica)
        self.wait_for_element_and_click('//div[@id="tab_0"]//button[@id="save"]')

        self.navigateTo("Tags")
        self.wait_loader()
        self.clear_filters()

    def elimina_tags(self):
        self.search_tag('Tags di Prova da Eliminare')
        self.click_first_result()
        self.wait_for_element_and_click('//div[@id="tab_0"]//a[@class="btn btn-danger ask"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')
        self.clear_filters()

    def verifica_tags(self):
        self.search_tag("Tags di Prova")
        modificato = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//tbody//tr[1]//td[3]'))
        ).text
        self.assertEqual("Tags di Prova", modificato)
        self.clear_filters()

        self.search_tag("Tags di Prova da Eliminare")
        eliminato = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//tbody//tr[1]//td[@class="dataTables_empty"]'))
        ).text
        self.assertEqual("Nessun dato presente nella tabella", eliminato)
        self.clear_filters()