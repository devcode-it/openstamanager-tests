from common.Test import Test
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Categoriearticoli(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Strumenti")
        self.expandSidebar("Tabelle")
        self.wait_loader()

    def test_creazione_categorie_articoli(self):
        self.navigateTo("Categorie")
        self.creazione_categorie_articoli(nome="Categoria articoli di Prova da Modificare", colore="#30db67")
        self.creazione_categorie_articoli(nome="Categoria articoli di Prova da Eliminare", colore="#ea2c2c")
        self.modifica_categorie_articoli("Categoria articoli di Prova")
        self.elimina_categorie_articoli()
        self.verifica_categorie_articoli()

    def creazione_categorie_articoli(self, nome: str, colore: str):
        self.wait_for_element_and_click('//i[@class="fa fa-plus"]')
        modal = self.wait_modal()

        colore_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//input[@name="colore_add"]')))
        colore_input.send_keys(colore)

        nome_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//input[@name="nome_add"]')))
        nome_input.send_keys(nome)

        self.wait_for_element_and_click('//div[@class="modal-footer"]//button[@type="submit"]')
        self.wait_loader()

    def modifica_categorie_articoli(self, modifica: str):
        self.navigateTo("Categorie")
        self.wait_loader()

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input')))
        self.send_keys_and_wait(search_input, 'Categoria articoli di Prova da Modificare', wait_modal=False)
        self.wait_for_element_and_click('//tbody//tr//td[2]')

        self.driver.execute_script('window.scrollTo(0,0)')
        self.input(None, 'Nome').setValue(modifica)
        self.wait_for_element_and_click('//div[@id="tab_0"]//button[@id="save"]')

        self.navigateTo("Categorie")
        self.wait_loader()
        self.clear_filters()

    def elimina_categorie_articoli(self):
        self.navigateTo("Categorie")
        self.wait_loader()

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input')))
        self.clear_filters()
        self.send_keys_and_wait(search_input, 'Categoria articoli di Prova da Eliminare')
        self.wait_for_element_and_click('//tbody//tr//td[2]')

        self.driver.execute_script('window.scrollTo(0,0)')
        self.wait_for_element_and_click('//div[@id="tab_0"]//a[@class="btn btn-danger ask"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')
        self.clear_filters()

    def verifica_categorie_articoli(self):
        self.navigateTo("Categorie")
        self.wait_loader()

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input')))
        self.send_keys_and_wait(search_input, 'Categoria articoli di Prova')
        self.wait_for_element_and_click('//tbody//tr//td[2]')
        modificato = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="nome"]'))).text
        self.assertEqual('Categoria articoli di Prova', modificato)

        self.navigateTo("Categorie")
        self.wait_loader()
        self.clear_filters()
        
        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input')))
        self.send_keys_and_wait(search_input, 'Categoria articoli di Prova da Eliminare', wait_modal=False)
        eliminato = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//tbody//tr[1]//td[@class="dataTables_empty"]'))).text
        self.assertEqual('La ricerca non ha portato alcun risultato.', eliminato)
