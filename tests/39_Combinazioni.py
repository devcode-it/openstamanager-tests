from common.Test import Test, get_html
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Combinazioni(Test):
    def setUp(self):
        super().setUp()

        self.expandSidebar("Magazzino")

    def test_creazione_combinazioni(self):
        # Creazione combinazioni *Required*
        self.creazione_combinazioni(codice="0001", nome="Combinazione di Prova da Modificare", attributi="Taglie")
        self.creazione_combinazioni(codice="0002", nome="Combinazione di Prova da Eliminare", attributi="Taglie")

        # Modifica Combinazioni
        self.modifica_combinazioni("Vestito")

        # Cancellazione Combinazioni
        self.elimina_combinazioni()
        
        # Verifica Combinazioni
        self.verifica_combinazioni()

        # Plugin varianti articoli da Articoli
        self.varianti_articoli()

    def creazione_combinazioni(self, codice: str, nome: str, attributi: str):
        self.navigateTo("Combinazioni")
        self.wait_loader()

        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click()
        modal = self.wait_modal()

        self.input(modal, 'Codice').setValue(codice)
        self.input(modal, 'Nome').setValue(nome)
        select = self.input(modal, 'Attributi')
        select.setByText(attributi)
        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        self.wait_loader()
       
    def modifica_combinazioni(self, modifica):
                self.navigateTo("Combinazioni")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))).send_keys('Combinazione di Prova da Modificare', Keys.ENTER)

        self.wait_for_element_and_click('//tbody//tr//td[2]')
        
        self.input(None,'Nome').setValue(modifica)
        self.find(By.XPATH, '//div[@id="tab_0"]//button[@id="save"]').click()
        self.wait_loader()

        self.find(By.XPATH, '//button[@onclick="generaVarianti(this)"]').click()
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="tab_0"]//button[@id="save"]').click()
        self.wait_loader()

        self.navigateTo("Combinazioni")
        self.wait_loader()

        self.find(By.XPATH, '//th[@id="th_Nome"]/i[@class="deleteicon fa fa-times"]').click()

    def elimina_combinazioni(self):
                self.navigateTo("Combinazioni")
        self.wait_loader()    

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))).send_keys('Combinazione di Prova da Eliminare', Keys.ENTER)

        self.wait_for_element_and_click('//tbody//tr//td[2]')

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_0"]//a[@class="btn btn-danger ask"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))).click()
        
        self.find(By.XPATH, '//th[@id="th_Nome"]/i[@class="deleteicon fa fa-times"]').click()
        
    def verifica_combinazioni(self):
                self.navigateTo("Combinazioni")
        self.wait_loader()    

        # Verifica elemento modificato
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))).send_keys("Vestito", Keys.ENTER)

        modificato = self.driver.find_element(By.XPATH,'//tbody//tr[1]//td[3]').text
        self.assertEqual("Vestito", modificato)
        self.find(By.XPATH, '//i[@class="deleteicon fa fa-times"]').click()

        # Verifica elemento eliminato
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))).send_keys("Attributo di Prova da Eliminare", Keys.ENTER)

        eliminato = self.driver.find_element(By.XPATH,'//tbody//tr[1]//td[@class="dataTables_empty"]').text
        self.assertEqual("La ricerca non ha portato alcun risultato.", eliminato)

    def varianti_articoli(self):
                self.navigateTo("Articoli")
        self.wait_loader()

        # Verifica combinazioni
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input'))).send_keys('Vestito', Keys.ENTER)

        self.wait_for_element_and_click('//tbody//tr//td[2]')

        self.find(By.XPATH, '//a[@id="link-tab_34"]').click() 
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_34"]//tr[3]')))

        # Modifica combinazioni
        self.navigateTo("Attributi Combinazioni")
        self.wait_loader()

        self.wait_for_element_and_click('//tbody//tr//td[2]')

        self.find(By.XPATH, '(//button[@class="btn btn-warning btn-xs"])[1]').click()

        element = self.find(By.XPATH, '//input[@id="nome"]')
        element.clear()
        element.send_keys("XS",Keys.ENTER)

        self.navigateTo("Articoli")
        self.wait_loader()

        self.wait_for_element_and_click('//tbody//tr//td[2]')

        self.find(By.XPATH, '//a[@id="link-tab_34"]').click() 
        self.wait_loader()

        taglia = self.find(By.XPATH, '//div[@id="tab_34"]//div[@class="card card-primary"]//tbody//tr//td[2]').text
        self.assertEqual(taglia, "Taglie: XS")

        # Elimina combinazioni
        self.navigateTo("Combinazioni")
        self.wait_loader()

        self.find(By.XPATH, '//th[@id="th_Nome"]/i[@class="deleteicon fa fa-times"]').click()

        self.wait_for_element_and_click('//tbody//tr//td[2]')

        self.find(By.XPATH, '//a[@class="btn btn-danger ask"]').click()
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()