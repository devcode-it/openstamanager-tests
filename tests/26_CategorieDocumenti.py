from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from common.Test import Test


class CategorieDocumenti(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Gestione documentale")
        self.wait_loader()

    def test_creazione_categorie_documenti(self):
        self.add_categorie_documenti('Categoria di Prova da Modificare')
        self.add_categorie_documenti('Categoria di Prova da Eliminare')
        self.modifica_categoria_documenti("Categoria Documenti di Prova")
        self.elimina_categoria_documenti()
        self.verifica_categoria_documento()
        self.wait_for_element_and_click('//i[@class="fa fa-power-off nav-icon"]')

    def add_categorie_documenti(self, descrizione: str):
        self.navigateTo("Categorie documenti")
        self.wait_loader()

        self.wait_for_element_and_click('//i[@class="fa fa-plus"]')
        modal = self.wait_modal()
        self.input(modal, 'Descrizione').setValue(descrizione)
        self.wait_for_element_and_click('button[type="submit"]', By.CSS_SELECTOR)

    def search_categoria(self, nome: str):
        self.navigateTo("Categorie documenti")
        self.wait_loader()

        search_input = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input'))
        )
        search_input.clear()
        self.send_keys_and_wait(search_input, nome, wait_modal=False)

    def modifica_categoria_documenti(self, modifica: str):
        self.search_categoria('Categoria di Prova da Modificare')
        self.click_first_result()
        self.input(None, 'Descrizione').setValue(modifica)
        self.wait_for_element_and_click('//div[@id="tab_0"]//button[@id="save"]')

        self.navigateTo("Categorie documenti")
        self.wait_loader()

        self.clear_filters()

    def elimina_categoria_documenti(self):
        self.search_categoria('Categoria di Prova da Eliminare')
        self.click_first_result()
        self.wait_for_element_and_click('//div[@id="tab_0"]//a[@class="btn btn-danger ask"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')
        self.clear_filters()

    def verifica_categoria_documento(self):
        self.search_categoria("Categoria Documenti di Prova")
        modificato = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//tbody//tr[1]//td[2]'))
        ).text
        self.assertEqual("Categoria Documenti di Prova", modificato)
        self.clear_filters()

        self.search_categoria("Categoria Documenti di Prova da Eliminare")
        eliminato = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//tbody//tr[1]//td[@class="dataTables_empty"]'))
        ).text
        self.assertEqual("Nessun dato presente nella tabella", eliminato)
        self.clear_filters()