from common.Test import Test, get_html
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Listini(Test):
    def setUp(self):
        super().setUp()
        self.navigateTo("Magazzino")

    def test_creazione_listino_cliente(self):
        # Crea un nuovo listino cliente. *Required*
        self.creazione_listino_cliente("Listino cliente di Prova da Modificare","01/12/2025", "01/01/2025")
        self.creazione_listino_cliente("Listino cliente di Prova da Eliminare", "01/12/2025", "01/01/2025")
        
        # Modifica listino cliente
        self.modifica_listino_cliente("Listino cliente di Prova")
        
        # Cancellazione listino cliente
        self.elimina_listino_cliente()
        
        # Verifica listino cliente
        self.verifica_listino_cliente()

        # Aggiorna listino cliente (Azione di gruppo) da anagrafiche
        self.aggiorna_listino_cliente()

        # Aggiungi a listino cliente (Azioni di gruppo) da Articoli
        self.aggiungi_a_listino_cliente()

    def creazione_listino_cliente(self, nome:str, dataatt: str, datascad: str):
        self.navigateTo("Listini cliente")
        self.wait_loader()

        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click()
        modal = self.wait_modal()

        self.input(modal, 'Data attivazione').setValue(dataatt)
        self.input(modal, 'Data scadenza default').setValue(datascad)
        self.input(modal, 'Nome').setValue(nome)

        # Submit
        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        self.wait_loader()

    def modifica_listino_cliente(self, modifica:str):
                self.navigateTo("Listini cliente")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))).send_keys('Listino cliente di Prova da Modificare', Keys.ENTER)

        self.wait_for_element_and_click('//tbody//tr//td[2]')  

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-selection select2-selection--single"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input[@type="search"]'))).send_keys("001")

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input[@type="search"]'))).send_keys(Keys.ENTER)
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="btn-group btn-group-flex"]//button[@class="btn btn-primary"]'))).click()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("10,00")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="sconto_percentuale"]'))).send_keys("10")
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//button[@class="btn btn-success"])[2]'))).click()

        self.input(None,'Nome').setValue(modifica)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@id="save"]'))).click()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//a[@id="back"]'))).click()

        self.find(By.XPATH, '//th[@id="th_Nome"]/i[@class="deleteicon fa fa-times"]').click()

    def elimina_listino_cliente(self):
                self.navigateTo("Listini cliente")
        self.wait_loader() 

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))).send_keys('Listino cliente di Prova da Eliminare', Keys.ENTER)

        self.wait_for_element_and_click('//tbody//tr//td[2]')

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_0"]//a[@class="btn btn-danger ask"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))).click()

        self.find(By.XPATH, '//th[@id="th_Nome"]/i[@class="deleteicon fa fa-times"]').click()

    def verifica_listino_cliente(self):
                self.navigateTo("Listini cliente")
        self.wait_loader()    

        # Verifica elemento modificato
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))).send_keys("Listino cliente di Prova", Keys.ENTER)

        modificato = self.driver.find_element(By.XPATH,'//tbody//tr[1]//td[2]').text
        self.assertEqual("Listino cliente di Prova", modificato)
        self.find(By.XPATH, '//i[@class="deleteicon fa fa-times"]').click()

        # Verifica elemento eliminato
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))).send_keys("Listino cliente di Prova da Eliminare", Keys.ENTER)

        eliminato = self.driver.find_element(By.XPATH,'//tbody//tr[1]//td[1]').text
        self.assertEqual("La ricerca non ha portato alcun risultato.", eliminato)

        self.find(By.XPATH, '//th[@id="th_Nome"]/i[@class="deleteicon fa fa-times"]').click()

    def aggiorna_listino_cliente(self):
                self.navigateTo("Anagrafiche")
        self.wait_loader() 

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Ragione-sociale"]/input'))).send_keys("Cliente", Keys.ENTER)

        self.wait_for_element_and_click('//tbody//tr//td') 
        self.find(By.XPATH, '//button[@data-toggle="dropdown"]').click() 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//a[@data-op="aggiorna-listino"]'))).click()    
        self.find(By.XPATH, '//span[@id="select2-id_listino-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Listino cliente di Prova", Keys.ENTER)  
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-warning"]').click()  
        self.wait_loader()

        self.wait_for_element_and_click('//tbody//tr//td[2]')  
        self.wait_loader()

        self.find(By.XPATH, '(//span[@class="select2-selection__clear"])[4]').click()  
        self.find(By.XPATH, '//button[@id="save"]').click() 
        self.wait_loader()

        self.navigateTo("Anagrafiche")
        self.wait_loader()

        self.find(By.XPATH, '//th[@id="th_Ragione-sociale"]/i[@class="deleteicon fa fa-times"]').click()

        self.navigateTo("Magazzino")

    def aggiungi_a_listino_cliente(self):
                self.navigateTo("Articoli")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Codice"]/input'))).send_keys("001", Keys.ENTER)

        self.wait_for_element_and_click('//tbody//tr//td') 
        self.find(By.XPATH, '//button[@data-toggle="dropdown"]').click() 
        self.find(By.XPATH, '//a[@data-op="add-listino"]').click()

        self.find(By.XPATH, '//span[@id="select2-id_listino-container"]').click()

        self.find(By.XPATH, '//li[@class="select2-results__option select2-results__option--highlighted"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="sconto_percentuale"]'))).send_keys("10")   
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-warning"]').click() 
        self.wait_loader()

        self.navigateTo("Listini cliente")
        self.wait_loader()

        self.wait_for_element_and_click('//tbody//tr//td[2]') 
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//tr[1]//td[8]'))) 
        self.wait_for_element_and_click('//tr[1]//td[9]//a[2]')
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-primary"]').click() 
        self.wait_loader()
        