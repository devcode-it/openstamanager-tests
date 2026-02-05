from common.Test import Test
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Categorie(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Strumenti")
        self.expandSidebar("Tabelle")
        self.wait_loader()

    def test_creazione_categorie(self):
        self.navigateTo("Categorie file")
        self.creazione_categorie(descrizione="Categoria di Prova da Modificare")
        self.creazione_categorie(descrizione="Categoria di Prova da Eliminare")
        self.modifica_categorie("Categoria di Prova")
        self.elimina_categorie()
        self.verifica_categorie()
        self.wait_for_element_and_click('//i[@class="fa fa-power-off nav-icon"]')
        
    def creazione_categorie(self, descrizione: str):
        self.wait_for_element_and_click('//i[@class="fa fa-plus"]')
        modal = self.wait_modal()

        descrizione_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//input[@name="name_add"]')))
        descrizione_input.send_keys(descrizione)

        self.wait_for_element_and_click('//div[@class="modal-footer"]//button[@type="submit"]')
        self.wait_loader()

    def modifica_categorie(self, modifica: str):
        self.navigateTo("Categorie file")
        self.wait_loader()

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input')))
        self.send_keys_and_wait(search_input, 'Categoria di Prova da Modificare', wait_modal=False)
        self.wait_for_element_and_click('//tbody//tr//td[2]')

        self.input(None, 'Descrizione').setValue(modifica)
        self.wait_for_element_and_click('//div[@id="tab_0"]//button[@id="save"]')

        self.navigateTo("Categorie file")
        self.wait_loader()
        self.clear_filters()

    def elimina_categorie(self):
        self.navigateTo("Categorie file")
        self.wait_loader()

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input')))
        self.send_keys_and_wait(search_input, "Categoria di Prova da Eliminare", wait_modal=False)
        self.click_first_result()
        self.wait_loader()

        self.wait_for_element_and_click('//div[@id="tab_0"]//a[@class="btn btn-danger ask"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')
        self.clear_filters()

    def verifica_categorie(self):
        self.navigateTo("Categorie file")
        self.wait_loader()

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input')))
        self.send_keys_and_wait(search_input, "Categoria di Prova", wait_modal=False)
        self.click_first_result()
        self.wait_loader()

        modificato = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//input[@name="name"]'))
        ).get_attribute('value')
        self.assertEqual('Categoria di Prova', modificato)

        self.navigateTo("Categorie file")
        self.wait_loader()
        self.clear_filters()

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input')))
        self.send_keys_and_wait(search_input, 'Categoria di Prova da Eliminare', wait_modal=False)
        eliminato = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//tbody//tr[1]//td[@class="dataTables_empty"]'))).text
        self.assertEqual('Nessun dato presente nella tabella', eliminato)
