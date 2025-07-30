from common.Test import Test, get_html
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class MarcheImpianti(Test):
    def setUp(self):
        super().setUp()

        self.expandSidebar("Impianti")

    def test_creazione_marche_impianti(self):
        # Creazione marche impianto *Required*
        self.creazione_marche_impianti(nome= "Marca Impianti di Prova da Modificare")
        self.creazione_marche_impianti(nome= "Marca Impianti di Prova da Eliminare")

        # Modifica Marca impianto
        self.modifica_marche_impianti("Marca Impianti di Prova")
        
        # Cancellazione Marca impianto
        self.elimina_marche_impianti()
        
        # Verifica Marca impianto
        self.verifica_marche_impianti()

    def creazione_marche_impianti(self, nome = str):
        self.navigateTo("Marche impianti")
        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click()
        modal = self.wait_modal()

        self.input(modal, 'Nome').setValue(nome)
        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        self.wait_loader()

    def modifica_marche_impianti(self, modifica = str):
                self.navigateTo("Marche impianti")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))).send_keys('Marca Impianti di Prova da Modificare', Keys.ENTER)

        self.wait_for_element_and_click('//tbody//tr//td[2]')          

        self.driver.execute_script('window.scrollTo(0,0)')
        self.input(None,'Nome').setValue(modifica)
        self.find(By.XPATH, '//div[@id="tab_0"]//button[@id="save"]').click()
        self.wait_loader()

        self.navigateTo("Marche impianti")
        self.wait_loader()    

        self.find(By.XPATH, '//th[@id="th_Nome"]/i[@class="deleteicon fa fa-times"]').click()

    def elimina_marche_impianti(self):
                self.navigateTo("Marche impianti")
        self.wait_loader()    

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))).send_keys('Marca Impianti di Prova da Eliminare', Keys.ENTER)
        
        self.wait_for_element_and_click('//tbody//tr//td[2]')          

        self.driver.execute_script('window.scrollTo(0,0)')
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_0"]//a[@class="btn btn-danger ask"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))).click()
        self.wait_loader()

        self.find(By.XPATH, '//th[@id="th_Nome"]/i[@class="deleteicon fa fa-times"]').click()
        
    def verifica_marche_impianti(self):
                self.navigateTo("Marche impianti")
        self.wait_loader()    

        # Verifica elemento modificato
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))).send_keys("Marca Impianti di Prova", Keys.ENTER)

        modificato = self.driver.find_element(By.XPATH,'//tbody//tr[1]//td[3]').text
        self.assertEqual("Marca Impianti di Prova", modificato)
        self.find(By.XPATH, '//i[@class="deleteicon fa fa-times"]').click()

        # Verifica elemento eliminato
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))).send_keys("Marca Impianti di Prova da Eliminare", Keys.ENTER)
        
        eliminato = self.driver.find_element(By.XPATH,'//tbody//tr[1]//td[@class="dataTables_empty"]').text
        self.assertEqual("La ricerca non ha portato alcun risultato.", eliminato)