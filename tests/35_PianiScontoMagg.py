from common.Test import Test, get_html
from common.RowManager import RowManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class PianiScontoMagg(Test):
    def setUp(self):
        super().setUp()

        self.expandSidebar("Magazzino")

    def test_creazione_piano_sconto_magg(self):
        # Crea un nuovo piano. *Required*
        self.creazione_piano_sconto_magg("Piano di sconto di Prova da Modificare", "10")
        self.creazione_piano_sconto_magg("Piano di sconto di Prova da Eliminare", "5")

        # Modifica piano di sconto
        self.modifica_piano_sconto("Piano di sconto di Prova")

        # Cancellazione piano di sconto
        self.elimina_piano_sconto()
        
        # Verifica piano di sconto
        self.verifica_piano_sconto()

        #plugin sconto e maggiorazione da articoli
        self.plugin_sconto_maggiorazione()

    def creazione_piano_sconto_magg(self, nome: str, sconto: str):
        self.navigateTo("Piani di sconto/magg.")

        # Crea un nuovo piano. 
        # Apre la schermata di nuovo elemento
        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click()
        modal = self.wait_modal()

        self.input(modal, 'Nome').setValue(nome)
        self.input(modal, 'Sconto/magg. combinato').setValue(sconto)

        # Submit
        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        self.wait_loader()
            
    def modifica_piano_sconto(self, modifica = str):
                self.navigateTo("Piani di sconto/magg.")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))).send_keys('Piano di sconto di Prova da Modificare', Keys.ENTER)

        self.wait_for_element_and_click('//tbody//tr//td[2]')
        
        self.input(None,'Nome').setValue(modifica)

        self.find(By.XPATH, '//div[@id="tab_0"]//button[@id="save"]').click()
        self.wait_loader()

        self.navigateTo("Piani di sconto/magg.")
        self.wait_loader()  

        self.find(By.XPATH, '//th[@id="th_Nome"]/i[@class="deleteicon fa fa-times"]').click()

    def elimina_piano_sconto(self):
                self.navigateTo("Piani di sconto/magg.")
        self.wait_loader()  

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))).send_keys('Piano di sconto di Prova da Eliminare', Keys.ENTER)

        self.wait_for_element_and_click('//tbody//tr//td[2]')

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_0"]//a[@class="btn btn-danger ask"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))).click()
        self.wait_loader()

        self.find(By.XPATH, '//th[@id="th_Nome"]/i[@class="deleteicon fa fa-times"]').click()
        
    def verifica_piano_sconto(self):
                self.navigateTo("Piani di sconto/magg.")
        self.wait_loader()    

        # Verifica elemento modificato
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))).send_keys("Piano di sconto di Prova", Keys.ENTER)

        modificato = self.driver.find_element(By.XPATH,'//tbody//tr[1]//td[2]').text
        self.assertEqual("Piano di sconto di Prova", modificato)
        self.find(By.XPATH, '//i[@class="deleteicon fa fa-times"]').click()

        # Verifica elemento eliminato
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))).send_keys("Piano di sconto di Prova da Eliminare", Keys.ENTER)
        
        eliminato = self.driver.find_element(By.XPATH,'//tbody//tr[1]//td[@class="dataTables_empty"]').text
        self.assertEqual("La ricerca non ha portato alcun risultato.", eliminato)

    def plugin_sconto_maggiorazione(self):
                self.navigateTo("Articoli")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input'))).send_keys('Articolo 1', Keys.ENTER)

        self.wait_for_element_and_click('//tbody//td[2]//div[1]')

        self.find(By.XPATH, '//a[@id="link-tab_33"]').click()

        prezzo_nuovo = self.find(By.XPATH, '(//div[@id="tab_33"]//tr[3]//td[2])[2]').text
        self.assertEqual(prezzo_nuovo, "18,00 €")
        
        self.navigateTo("Articoli")
        self.wait_loader()
        
        self.find(By.XPATH, '//th[@id="th_Descrizione"]//i[@class="deleteicon fa fa-times"]').click()