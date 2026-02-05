from common.Test import Test
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class TipiScadenze(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Strumenti")
        self.expandSidebar("Tabelle")

    def test_creazione_categorie_contratti(self):
        self.creazione_categorie_contratti("Categoria di Contratto di Prova da Modificare")
        self.creazione_categorie_contratti("Categoria di Contratto di Prova da Eliminare")
        self.modifica_categorie_contratti("Categoria di Contratto di Prova")
        self.elimina_categorie_contratti()
        self.verifica_categorie_contratti()
        self.wait_for_element_and_click('//i[@class="fa fa-power-off nav-icon"]')
        
    def creazione_categorie_contratti(self, descrizione= str):
        self.navigateTo("Categorie contratti")
        self.wait_for_element_and_click('//i[@class="fa fa-plus"]')
        modal = self.wait_modal()

        self.input(modal, 'Nome').setValue(descrizione)
        self.wait_for_element_and_click('button[type="submit"]', By.CSS_SELECTOR)

    def modifica_categorie_contratti(self, modifica = str):
        self.navigateTo("Categorie contratti")
        self.wait_loader()

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))) 
        self.send_keys_and_wait(search_input, 'Categoria di Contratto di Prova da Modificare', wait_modal=False)
        self.wait_for_element_and_click('//tbody//tr//td[2]')

        self.input(None,'Nome').setValue(modifica)
        self.wait_for_element_and_click('//div[@id="tab_0"]//button[@id="save"]')

        self.navigateTo("Categorie contratti")
        self.wait_loader()
        self.clear_filters()

    def elimina_categorie_contratti(self):  
        self.navigateTo("Categorie contratti")  
        self.wait_loader()

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))) 
        self.send_keys_and_wait(search_input, 'Categoria di Contratto di Prova da Eliminare', wait_modal=False)
        self.wait_for_element_and_click('//tbody//tr//td[2]')

        self.wait_for_element_and_click('//div[@id="tab_0"]//a[@class="btn btn-danger ask"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')
        self.clear_filters()

    def verifica_categorie_contratti(self):
        self.navigateTo("Categorie contratti")
        self.wait_loader()

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))) 
        self.send_keys_and_wait(search_input, 'Categoria di Contratto di Prova', wait_modal=False)
        self.wait_for_element_and_click('//tbody//tr//td[2]')       