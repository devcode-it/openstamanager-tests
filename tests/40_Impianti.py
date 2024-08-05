from common.Test import Test, get_html
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Impianti(Test):
    def setUp(self):
        super().setUp()

        
    def test_creazione_impianto(self):
        # Crea un nuovo impianto.   *Required*
        self.add_impianto('01', 'Impianto di Prova da Modificare', 'Cliente')
        self.add_impianto('02', 'Impianto di Prova da Eliminare', 'Cliente')

        # Modifica Impianto
        self.modifica_impianto("Impianto di Prova")

        # Cancellazione Impianto
        self.elimina_impianto()

        # Verifica Impianto
        self.verifica_impianto()

        # Plugin impianti del cliente da anagrafiche 
        self.apri_impianti()

        # Plugin impianti da attività
        self.plugin_impianti()

        # Plugin interventi svolti
        self.plugin_interventi_svolti()

        # Plugin componenti
        self.componenti()

        # Elimina selezionati (Azioni di gruppo)
        self.elimina_selezionati()
        
    def add_impianto(self, matricola: str, nome:str, cliente: str):
        self.navigateTo("Impianti")
        # Crea un nuovo impianto
        # Apre la schermata di nuovo elemento
        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click()
        modal = self.wait_modal()

        # Completamento dei campi per il nuovo elemento
        self.input(modal, 'Matricola').setValue(matricola)
        self.input(modal, 'Nome').setValue(nome)
        select = self.input(modal, 'Cliente')
        select.setByText(cliente)

        # Submit
        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        self.wait_loader()

    def modifica_impianto(self, modifica=str):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Impianti")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))).send_keys('Impianto di Prova da Modificare', Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//tbody//tr//td[2]').click()
        self.wait_loader()
        
        self.input(None,'Nome').setValue(modifica)
        self.find(By.XPATH, '//div[@id="tab_0"]//button[@id="save"]').click()
        self.wait_loader()

        self.navigateTo("Impianti")
        self.wait_loader()    

        self.find(By.XPATH, '//th[@id="th_Nome"]/i[@class="deleteicon fa fa-times"]').click()
        sleep(2)

    def elimina_impianto(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Impianti")
        self.wait_loader()    

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))).send_keys('Impianto di Prova da Eliminare', Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//tbody//tr//td[2]').click()
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_0"]//a[@class="btn btn-danger ask "]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))).click()
        sleep(1)

        self.find(By.XPATH, '//th[@id="th_Nome"]/i[@class="deleteicon fa fa-times"]').click()
        sleep(2)
        
    def verifica_impianto(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Impianti")
        self.wait_loader()    

        #verifica elemento modificato
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))).send_keys("Impianto di Prova", Keys.ENTER)
        sleep(1)

        modificato=self.driver.find_element(By.XPATH,'//tbody//tr[1]//td[3]').text
        self.assertEqual("Impianto di Prova",modificato)
        self.find(By.XPATH, '//i[@class="deleteicon fa fa-times"]').click()
        sleep(2)

        #verifica elemento eliminato
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))).send_keys("Impianto di Prova da Eliminare", Keys.ENTER)
        sleep(1)
        
        eliminato=self.driver.find_element(By.XPATH,'//tbody//tr[1]//td[@class="dataTables_empty"]').text
        self.assertEqual("La ricerca non ha portato alcun risultato.",eliminato)
        self.navigateTo("Impianti")
        self.find(By.XPATH, '//i[@class="deleteicon fa fa-times"]').click()
        sleep(1)

    def apri_impianti(self): 
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Anagrafiche")
        self.wait_loader() 

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Ragione-sociale"]/input'))).send_keys("Cliente", Keys.ENTER)
        sleep(1)
        self.find(By.XPATH, '//tbody//tr//td[2]').click()
        sleep(1) 

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="control-sidebar-button"]'))).click()
        self.find(By.XPATH, '//a[@id="link-tab_1"]').click()
        self.find(By.XPATH, '//div[@class="text-right"]').click
        impianto=self.find(By.XPATH, '//div [@class="text-right"]').text
        self.assertEqual(impianto,"01")

        self.navigateTo("Anagrafiche")
        self.find(By.XPATH, '//i[@class="deleteicon fa fa-times"]').click()
        sleep(1)

    def plugin_impianti(self):     
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Attività")
        self.wait_loader()    

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Ragione-sociale"]//input'))).send_keys("Cliente", Keys.ENTER)
        sleep(1) 

        wait.until(EC.visibility_of_element_located((By.XPATH, '(//td[@class="bound clickable"])[1]'))).click()
        sleep(1)

        self.find(By.XPATH , '//span[@id="select2-idstatointervento-container"]').click()
        sleep(1)
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//input[@class="select2-search__field"])[3]'))).send_keys("Programmato",Keys.ENTER)
        sleep(1)
        self.find(By.XPATH, '//button[@id="save"]').click()
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="control-sidebar-button"]'))).click()
        sleep(1)

        self.find(By.XPATH, '//a[@id="link-tab_2"]').click()
        self.wait_loader()

        self.find(By.XPATH, '//span[@id="select2-id_impianto_add-container"]').click()
        self.find(By.XPATH, '//li[@class="select2-results__option select2-results__option--highlighted"]').click()
        self.find(By.XPATH, '//button[@class="btn btn-default tip tooltipstered"]').click()
        sleep(1)

        matricola=self.find(By.XPATH, '(//tbody//tr[2]//td[2])[5]').text
        self.assertEqual(matricola,"01")
        self.find(By.XPATH, '//button[@class="btn btn-sm btn-danger "]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-primary"]').click()
        sleep(2)

        self.find(By.XPATH, '//span[@id="select2-id_impianto_add-container"]').click()
        self.find(By.XPATH, '//li[@class="select2-results__option select2-results__option--highlighted"]').click()
        self.find(By.XPATH, '//button[@class="btn btn-default tip tooltipstered"]').click()
        sleep(1)

        self.navigateTo("Attività")
        self.find(By.XPATH, '//i[@class="deleteicon fa fa-times"]').click()
        sleep(1)

    def plugin_interventi_svolti(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Impianti")
        self.wait_loader()    

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))).send_keys("Impianto di Prova", Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//tbody//tr//td[3]').click()
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="control-sidebar-button"]'))).click()
        sleep(1)

        self.find(By.XPATH, '//a[@id="link-tab_8"]').click()
        self.wait_loader()

        totale=self.find(By.XPATH, '//tbody//tr[3]//td[2]').text
        self.assertEqual(totale, "0,00 €")
        self.navigateTo("Impianti")
        self.wait_loader()

        self.find(By.XPATH, '//th[@id="th_Nome"]//i').click()
        sleep(1)

    def componenti(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Impianti")
        self.wait_loader()    

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))).send_keys("Impianto di Prova", Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//tbody//tr//td[3]').click()
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="control-sidebar-button"]'))).click()
        sleep(1)

        self.find(By.XPATH, '//a[@id="link-tab_31"]').click()
        self.wait_loader()

        self.find(By.XPATH, '(//button[@class="btn btn-primary bound clickable"])[2]').click()
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-id_articolo-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Articolo 1", Keys.ENTER)
        self.find(By.XPATH, '(//form//button[@class="btn btn-primary"])[2]').click()
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="tab_31"]//button[@class="btn btn-tool"]').click()
        sleep(1)
        #modifica
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="data_installazione_1"]'))).send_keys("01/01/2024")
        self.find(By.XPATH, '//button[@class="btn btn-success pull-right"]').click()
        self.wait_loader()

        data_installazione=self.find(By.XPATH, '//div[@id="tab_31"]//tr[1]//td[3]').text
        self.assertEqual(data_installazione, "01/01/2024")
        #elimina
        self.find(By.XPATH, '//div[@id="tab_31"]//button[@class="btn btn-tool"]').click()
        sleep(1)
        self.find(By.XPATH, '//button[@class="btn btn-warning pull-right"]').click()
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-primary"]').click()
        self.wait_loader()
        
        sostituito=self.find(By.XPATH, '(//div[@id="tab_31"]//tr[1]//td[1])[1]').text
        self.assertEqual(sostituito, "#2")
        self.navigateTo("Impianti")
        self.wait_loader()

        self.find(By.XPATH, '//th[@id="th_Nome"]//i').click()
        sleep(1)

    def elimina_selezionati(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Impianti")
        self.wait_loader()  

        self.find(By.XPATH, '//button[@class="btn btn-primary bound clickable"]').click() #click su +
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="matricola"]'))).send_keys("08")    #seleziono "08" come matricola
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="nome"]'))).send_keys("Prova")      #seleziono "Prova" come nome
        self.find(By.XPATH, '//span[@id="select2-idanagrafica_impianto-container"]').click()        #seleziono "Cliente" come cliente
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente", Keys.ENTER)
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click() #click su aggiungi
        self.wait_loader()

        self.navigateTo("Impianti") #torno indietro
        self.wait_loader() 
        
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Matricola"]/input'))).send_keys("08", Keys.ENTER)  #cerco impianto con matricola "08"
        sleep(1)

        self.find(By.XPATH, '//tbody//td[1]').click() #seleziono primo risultato
        self.find(By.XPATH, '//button[@class="btn btn-primary btn-lg dropdown-toggle dropdown-toggle-split"]').click()  #apro azioni di gruppo
        self.find(By.XPATH, '//a[@data-op="delete-bulk"]').click()   #click su elimina selezionati
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()   #click su procedi
        self.wait_loader()

        scritta=self.find(By.XPATH, '//tbody//tr').text
        self.assertEqual(scritta, "La ricerca non ha portato alcun risultato.") #controllo se l' impianto è stato eliminato
        self.find(By.XPATH, '//th[@id="th_Matricola"]//i').click()  #cancella ricerca
        sleep(2)
