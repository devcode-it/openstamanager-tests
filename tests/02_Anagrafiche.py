from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from common.Test import Test, get_html



class Anagrafiche(Test):
    def setUp(self):
        super().setUp()
        self.navigateTo("Anagrafiche")
        

    def test_creazione_anagrafica(self):
        #Creazione anagrafiche *Required*
        self.add_anagrafica('Cliente', 'Cliente')  
        self.add_anagrafica('Tecnico', 'Tecnico') 
        self.add_anagrafica('Fornitore', 'Fornitore')
        self.add_anagrafica('Vettore', 'Vettore') 
        self.add_anagrafica('Agente', 'Agente')
        self.add_anagrafica('Anagrafica di Prova da Eliminare', 'Cliente')

        # Modifica anagrafica
        self.modifica_anagrafica('Privato')

        # Cancellazione anagrafica
        self.elimina_anagrafica()       
      
        # Verifica test
        self.verifica_anagrafica()         

        # Crea attività
        self.crea_attivita()             

        # Crea preventivo
        self.crea_preventivo()         

        # Crea contratto
        self.crea_contratto()

        # Crea ordine cliente
        self.crea_ordine_cliente()       

        # Crea DDT in uscita
        self.crea_DDT_uscita()              

        # Crea fattura di vendita
        self.crea_fattura_vendita()

        # Aggiunta referente
        self.aggiunta_referente()

        # Aggiunta sede
        self.aggiunta_sede()

        # Plugin statistiche
        self.plugin_statistiche()

        # Plugin dichiarazione d'intento
        self.dichiarazione_di_intento()

        # Plugin assicurazione crediti
        self.assicurazione_crediti()

        # Ricerca coordinate (Azioni di gruppo)
        self.ricerca_coordinate()

        # Elimina selezionati (Azioni di gruppo)
        self.elimina_selezionati()

        # Cambia relazione (Azioni di gruppo)
        self.cambia_relazione()
    
    def add_anagrafica(self, nome=str, tipo=str):
        # Crea una nuova anagrafica del tipo indicato.
        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click()
        modal = self.wait_modal()

        self.input(modal, 'Denominazione').setValue(nome)

        select = self.input(modal, 'Tipo di anagrafica')
        select.setByText(tipo)

        # Submit
        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        self.wait_loader()

    def modifica_anagrafica(self, tipologia:str): 
        wait = WebDriverWait(self.driver, 20)  
        self.navigateTo("Anagrafiche")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Ragione-sociale"]/input'))).send_keys("Cliente", Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//tbody//tr//td[2]').click()    
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="select2-tipo-container"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//input[@class="select2-search__field"])[2]'))).send_keys(tipologia, Keys.ENTER)
        self.wait_loader()

        self.input(None, 'Partita IVA').setValue("05024030287")
        self.input(None, 'Codice fiscale').setValue("05024030287")
        self.driver.find_element(By.XPATH,'//input[@id="indirizzo"]').send_keys("Via controllo caratteri speciali: &\"<>èéàòùì?'`")
        self.input(None, 'C.A.P.').setValue("35042")
        self.input(None, 'Città').setValue("Este")
        self.find(By.XPATH, '//button[@id="save"]').click()
        self.wait_loader()   
        
        self.navigateTo("Anagrafiche")
        self.wait_loader() 

        self.find(By.XPATH, '//i[@class="deleteicon fa fa-times"]').click()
        sleep(1)

    def elimina_anagrafica(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Anagrafiche")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Ragione-sociale"]/input'))).send_keys('Anagrafica di Prova da Eliminare', Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//tbody//tr//td[2]').click()
        self.wait_loader()
             
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_0"]//a[@class="btn btn-danger ask"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))).click()
        self.wait_loader()

        self.find(By.XPATH, '//i[@class="deleteicon fa fa-times"]').click()
        sleep(1)

    def verifica_anagrafica(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Anagrafiche")
        self.wait_loader()  

        # Verifica elemento modificato
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Tipologia"]/input'))).send_keys("Privato", Keys.ENTER)
        sleep(1)

        modificato=self.driver.find_element(By.XPATH,'//tbody//tr//td[2]').text
        self.assertEqual("Cliente",modificato)
        self.find(By.XPATH, '//i[@class="deleteicon fa fa-times"]').click()
        sleep(1)

        # Verifica elemento eliminato
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Ragione-sociale"]/input'))).send_keys("Anagrafica di Prova da Eliminare", Keys.ENTER)
        sleep(1)

        eliminato=self.driver.find_element(By.XPATH,'//tbody//tr//td[1]').text
        self.assertEqual("La ricerca non ha portato alcun risultato.",eliminato)
        self.find(By.XPATH, '//i[@class="deleteicon fa fa-times"]').click()
        sleep(1)

    def crea_attivita(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Anagrafiche")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Ragione-sociale"]/input'))).send_keys("Cliente", Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//tbody//tr//td[2]').click()    
        sleep(1)

        # Crea attività
        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-info dropdown-toggle"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//a[@class="dropdown-item bound clickable"])[1]'))).click()
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '(//form[@id="add-form"]//span[@class="select2-selection select2-selection--single"])[8]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//li[@class="select2-results__option"])'))).click()
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '(//iframe[@class="cke_wysiwyg_frame cke_reset"])[2]'))).click()  
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//iframe[@class="cke_wysiwyg_frame cke_reset"])[2]'))).send_keys("Test")
        self.find(By.XPATH, '//div[@class="col-md-12 text-right"]//button[@type="button"]').click()
        sleep(1) 

        self.navigateTo("Anagrafiche")
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr//td[2]').click()   
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="control-sidebar-button"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//a[@id="link-tab_28"]'))).click()
        modificato=self.driver.find_element(By.XPATH,'//div[@id="tab_28"]//tbody//tr//td[2]').text
        self.assertEqual("1",modificato)

        self.find(By.XPATH, '//div[@id="tab_28"]//tbody//td[2]').click()
        sleep(1)

        # Elimina attività creata
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_0"]//a[@class="btn btn-danger ask"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))).click()
        self.wait_loader()
  
        self.navigateTo("Anagrafiche")
        self.find(By.XPATH, '//i[@class="deleteicon fa fa-times"]').click()
        sleep(1)

    def crea_preventivo(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Anagrafiche")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Ragione-sociale"]/input'))).send_keys("Cliente", Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//tbody//tr//td[2]').click()   
        self.wait_loader()

        # Crea preventivo
        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-info dropdown-toggle"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//a[@class="dropdown-item bound clickable"])[2]'))).click()
        modal = self.wait_modal()

        wait.until(EC.visibility_of_element_located((By.XPATH, '(//form[@id="add-form"]//span[@class="select2-selection select2-selection--single"])[4]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//li[@class="select2-results__option"])'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//form[@id="add-form"]//span[@class="select2-selection select2-selection--single"])[5]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//li[@class="select2-results__option"])'))).click()
        self.input(modal, 'Nome').setValue("Preventivo di prova anagrafica")
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//div[@id="form_13-"]//button[@class="btn btn-primary"])'))).click()
        sleep(1)   

        self.navigateTo("Anagrafiche")
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr//td[2]').click()   
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-tool"]'))).click()
        sleep(1)

        modificato=self.driver.find_element(By.XPATH,'(//div[@class="card-body"]//li)[7]').text
        self.assertEqual("Preventivo 1",modificato[0:12])
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//div[@class="card-body"]//li//a)[5]'))).click()
        sleep(1)

        self.driver.switch_to.window(self.driver.window_handles[1])
        sleep(1)

        # Elimina preventivo
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_0"]//a[@class="btn btn-danger ask"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))).click()
        self.wait_loader()

        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
  
        self.navigateTo("Anagrafiche")
        self.find(By.XPATH, '//i[@class="deleteicon fa fa-times"]').click()
        sleep(1)

    def crea_contratto(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Anagrafiche")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Ragione-sociale"]/input'))).send_keys("Cliente", Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//tbody//tr//td[2]').click()  
        sleep(1)  

        # Crea contratto
        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-info dropdown-toggle"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//a[@class="dropdown-item bound clickable"])[3]'))).click()
        modal = self.wait_modal()

        self.input(modal, 'Nome').setValue("Contratto di prova anagrafica")
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//form[@id="add-form"]//span[@class="select2-selection select2-selection--single"])[2]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//li[@class="select2-results__option"])'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//div[@id="form_31-"]//button[@class="btn btn-primary"])'))).click()
        sleep(1)

        # Elimina contratto
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_0"]//a[@class="btn btn-danger ask"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))).click()
        self.wait_loader()
 
        self.navigateTo("Anagrafiche")
        self.wait_loader()

        self.find(By.XPATH, '//i[@class="deleteicon fa fa-times"]').click()
        sleep(1)

    def crea_ordine_cliente(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Anagrafiche")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Ragione-sociale"]/input'))).send_keys("Cliente", Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//tbody//tr//td[2]').click()
        self.wait_loader()
           
        # Crea ordine
        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-info dropdown-toggle"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//a[@class="dropdown-item bound clickable"])[4]'))).click()
        self.wait_modal()

        wait.until(EC.visibility_of_element_located((By.XPATH, '(//div[@id="form_24-"]//button[@class="btn btn-primary"])'))).click()
        self.wait_loader()

        self.navigateTo("Anagrafiche")
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr//td[2]').click()   
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-tool"]'))).click()
        sleep(1)

        modificato=self.driver.find_element(By.XPATH,'(//div[@class="card-body"]//li)[7]').text
        self.assertEqual("Ordine cliente 01",modificato[0:17])
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//div[@class="card-body"]//li//a)[5]'))).click()
        sleep(1)

        self.driver.switch_to.window(self.driver.window_handles[1])

        # Elimina ordine
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_0"]//a[@class="btn btn-danger ask"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))).click()
        self.wait_loader()

        self.navigateTo("Anagrafiche")
        self.find(By.XPATH, '//i[@class="deleteicon fa fa-times"]').click()
        sleep(1)

        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        sleep(1)

    def crea_DDT_uscita(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Anagrafiche")
        self.wait_loader()  

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Ragione-sociale"]/input'))).send_keys("Cliente", Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//tbody//tr//td[2]').click()
        self.wait_loader()   

        # Crea DDT
        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-info dropdown-toggle"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//a[@class="dropdown-item bound clickable"])[5]'))).click()
        modal = self.wait_modal()

        wait.until(EC.visibility_of_element_located((By.XPATH, '(//form[@id="add-form"]//span[@class="select2-selection select2-selection--single"])[3]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//li[@class="select2-results__option"])'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//div[@id="form_26-"]//button[@class="btn btn-primary"])'))).click()
        sleep(1)   

        self.navigateTo("Anagrafiche")
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr//td[2]').click()   
        self.wait_loader()


        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="control-sidebar-button"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//a[@id="link-tab_17"]'))).click()
        modificato=self.driver.find_element(By.XPATH,'//div[@id="tab_17"]//tbody//td[2]').text
        self.assertEqual("01",modificato)
        sleep(1)

        self.find(By.XPATH, '//div[@id="tab_17"]//tbody//td[2]').click()
        self.wait_loader()

        # Elimina DDT
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_0"]//a[@class="btn btn-danger ask"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))).click()
        self.wait_loader()
 
        self.navigateTo("Anagrafiche")
        self.find(By.XPATH, '//i[@class="deleteicon fa fa-times"]').click()
        sleep(1)

    def crea_fattura_vendita(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Anagrafiche")
        self.wait_loader() 

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Ragione-sociale"]/input'))).send_keys("Cliente", Keys.ENTER)
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//tbody//tr//td[2]'))).click()
        self.wait_loader()

        # Crea fattura
        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-info dropdown-toggle"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//a[@class="dropdown-item bound clickable"])[6]'))).click()
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '(//div[@id="form_14-"]//button[@class="btn btn-primary"])'))).click()
        sleep(1) 

        self.navigateTo("Anagrafiche")
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr//td[2]').click()   
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-tool"]'))).click()
        sleep(1)

        modificato=self.driver.find_element(By.XPATH,'(//div[@class="card-body"]//li)[7]').text
        self.assertEqual("Fattura immediata di vendita",modificato[0:28])
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//div[@class="card-body"]//li//a)[5]'))).click()
        sleep(1)

        self.driver.close() 
        self.driver.switch_to.window(self.driver.window_handles[0])

        # Elimina fattura
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_0"]//a[@class="btn btn-danger ask "]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))).click()
        self.wait_loader()
  
        self.navigateTo("Anagrafiche")
        self.wait_loader()

        self.find(By.XPATH, '//i[@class="deleteicon fa fa-times"]').click()
        sleep(1)

    def aggiunta_referente(self):
        wait = WebDriverWait(self.driver, 20)   
        self.navigateTo("Anagrafiche")
        self.wait_loader() 
 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Ragione-sociale"]/input'))).send_keys("Cliente", Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//tbody//tr//td[2]').click()    
        self.wait_loader()

        # Aggiunta referente
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="control-sidebar-button"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//a[@id="link-tab_3"]'))).click()
        self.find(By.XPATH, '//h4//i[@class="fa fa-plus"]').click()
        modal = self.wait_modal()

        wait.until(EC.visibility_of_element_located((By.XPATH, '(//input[@id="nome"])[2]'))).send_keys("Referente di prova")
        self.find(By.XPATH, '//span[@id="select2-idmansione-container"]').click()
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-idmansione-results"]//li[1]').click()
        sleep(1)

        self.find(By.XPATH, '(//button[@type="submit"])[3]').click()   
        self.wait_loader()

        # Modifica referente
        self.find(By.XPATH, '(//div[@id="tab_3"]//tr[1]//td[2])[2]').click()
        sleep(2)

        nome=self.find(By.XPATH, '(//input[@id="nome"])[2]')
        nome.clear()
        nome.send_keys("Prova")
        self.find(By.XPATH, '//button[@class="btn btn-success pull-right"]').click()
        self.wait_loader()

        modifica=self.find(By.XPATH, '(//div[@id="tab_3"]//tr[1]//td[2]//div)[2]').text
        self.assertEqual(modifica, "Prova")

        # Elimina referente
        self.find(By.XPATH, '(//div[@id="tab_3"]//tr[1]//td[2])[2]').click()
        sleep(1)
        
        self.find(By.XPATH, '(//a[@class="btn btn-danger ask"])[2]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()

        eliminato=self.find(By.XPATH, '//div[@id="tab_3"]//tbody//tr[1]').text
        self.assertEqual(eliminato, "Nessun dato presente nella tabella")

        # Aggiunta referente
        self.find(By.XPATH, '//h4//i[@class="fa fa-plus"]').click()
        modal = self.wait_modal()

        wait.until(EC.visibility_of_element_located((By.XPATH, '(//input[@id="nome"])[2]'))).send_keys("Referente di prova")
        self.find(By.XPATH, '//span[@id="select2-idmansione-container"]').click()
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-idmansione-results"]//li[1]').click()
        sleep(1)

        self.find(By.XPATH, '(//button[@type="submit"])[3]').click()   
        self.wait_loader()

        # Verifica referente
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Mansione"]/input'))).send_keys("Segretario", Keys.ENTER)
        sleep(1)

        modificato=self.driver.find_element(By.XPATH,'(//div[@id="tab_3"]//tr[1]//td[3]//div)[2]').text
        self.assertEqual("Segretario", modificato)

        self.navigateTo("Anagrafiche")
        self.wait_loader() 

        self.find(By.XPATH, '//i[@class="deleteicon fa fa-times"]').click()
        sleep(1)

    def aggiunta_sede(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Anagrafiche")
        self.wait_loader() 
 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Ragione-sociale"]/input'))).send_keys("Cliente", Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//tbody//tr[1]//td[2]').click()
        self.wait_loader()
        
        # Aggiunta sede
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="control-sidebar-button"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//a[@id="link-tab_4"]'))).click()
        sleep(1)

        self.find(By.XPATH, '//div[@id="tab_4"]//i[@class="fa fa-plus"]').click()
        sleep(1)

        self.input(None, 'Nome sede').setValue("Filiale XY")
        self.find(By.XPATH, '(//input[@id="cap"])[2]').send_keys("35042")
        self.find(By.XPATH, '(//input[@id="citta"])[2]').click()
        self.find(By.XPATH, '(//input[@id="citta"])[2]').send_keys("Padova")
        sleep(1)
        
        self.find(By.XPATH, '(//span[@id="select2-id_nazione-container"])[2]').click()
        self.find(By.XPATH, '//li[@class="select2-results__option select2-results__option--highlighted"]').click()
        self.find(By.XPATH, '(//button[@type="submit"])[3]').click()
        sleep(1)

        # Modifica sede
        self.find(By.XPATH, '(//div[@id="tab_4"]//tr[1]//td[2])[2]').click()
        sleep(1)

        nome=self.find(By.XPATH, '//input[@id="nomesede"]')
        nome.clear()
        nome.send_keys("Prova")
        self.find(By.XPATH, '//button[@class="btn btn-primary pull-right"]').click()
        self.wait_loader()

        modificato=self.find(By.XPATH, '(//div[@id="tab_4"]//tr[1]//td[2]//div)[2]')
        self.assertEqual(modificato, "Prova")
        # Elimina sede
        self.find(By.XPATH, '(//div[@id="tab_4"]//tr[1]//td[2])[2]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@class="btn btn-danger "]').click()
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()

        eliminato=self.find(By.XPATH, '//div[@id="tab_4"]//tbody//tr[1]').text
        self.assertEqual(eliminato, "Nessun dato presente nella tabella")

        # Aggiunta sede
        self.find(By.XPATH, '//div[@id="tab_4"]//i[@class="fa fa-plus"]').click()
        sleep(1)

        self.input(None, 'Nome sede').setValue("Filiale XY")
        self.find(By.XPATH, '(//input[@id="cap"])[2]').send_keys("35042")
        self.find(By.XPATH, '(//input[@id="citta"])[2]').click()
        self.find(By.XPATH, '(//input[@id="citta"])[2]').send_keys("Padova")
        sleep(1)
        
        self.find(By.XPATH, '(//span[@id="select2-id_nazione-container"])[2]').click()
        self.find(By.XPATH, '//li[@class="select2-results__option select2-results__option--highlighted"]').click()
        self.find(By.XPATH, '(//button[@type="submit"])[3]').click()
        sleep(1)

        # Verifica sede
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//th[@id="th_Nome"]/input)[2]'))).send_keys("Filiale XY", Keys.ENTER)
        sleep(1)

        modificato=self.driver.find_element(By.XPATH,'//div[@id="tab_4"]//tbody//td[2]').text
        self.assertEqual("Filiale XY", modificato)
        self.navigateTo("Anagrafiche")
        self.wait_loader()  

        self.find(By.XPATH, '//i[@class="deleteicon fa fa-times"]').click()
        sleep(1)

    def plugin_statistiche(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Anagrafiche")
        self.wait_loader() 
 
        # Verifica statistiche
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Ragione-sociale"]/input'))).send_keys("Cliente", Keys.ENTER)
        sleep(1) 

        self.find(By.XPATH, '//tbody//tr//td[2]').click()
        self.wait_loader() 
        
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="control-sidebar-button"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//a[@id="link-tab_7"]'))).click()

        preventivi=wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="info-box-text pull-left"]'))).text
        self.assertEqual(preventivi, "Preventivi")
        contratti=wait.until(EC.visibility_of_element_located((By.XPATH, '(//span[@class="info-box-text pull-left"])[2]'))).text
        self.assertEqual(contratti, "Contratti")
        ordini_cliente=wait.until(EC.visibility_of_element_located((By.XPATH, '(//span[@class="info-box-text pull-left"])[3]'))).text
        self.assertEqual(ordini_cliente, "Ordini cliente")
        attivita=wait.until(EC.visibility_of_element_located((By.XPATH, '(//span[@class="info-box-text pull-left"])[4]'))).text
        self.assertEqual(attivita, "Attività")
        ddt_in_uscita=wait.until(EC.visibility_of_element_located((By.XPATH, '(//span[@class="info-box-text pull-left"])[5]'))).text
        self.assertEqual(ddt_in_uscita, "Ddt in uscita")
        fatture=wait.until(EC.visibility_of_element_located((By.XPATH, '(//span[@class="info-box-text pull-left"])[6]'))).text
        self.assertEqual(fatture, "Fatture")
        ore_lavorate=wait.until(EC.visibility_of_element_located((By.XPATH, '(//span[@class="info-box-text pull-left"])[7]'))).text
        self.assertEqual(ore_lavorate, "Ore lavorate")

        self.navigateTo("Anagrafiche")
        self.wait_loader() 
        self.find(By.XPATH, '//i[@class="deleteicon fa fa-times"]').click()
        sleep(1)
    
    def dichiarazione_di_intento(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Anagrafiche")
        self.wait_loader() 

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Ragione-sociale"]/input'))).send_keys("Cliente", Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//tbody//tr//td[2]').click()
        self.wait_loader() 

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="control-sidebar-button"]'))).click()
        self.find(By.XPATH, '//a[@id="link-tab_25"]').click()
        self.find(By.XPATH, '//div[@id="tab_25"]//i[@class="fa fa-plus"]').click()
        sleep(1)

        # Aggiunta dichiarazione di intento
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="numero_protocollo"]'))).send_keys("012345678901234567890123")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="data_protocollo"]'))).send_keys("08/07/2024")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="numero_progressivo"]'))).send_keys("001")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="data_inizio"]'))).send_keys("08/07/2024")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="data_fine"]'))).send_keys("08/09/2024")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="massimale"]'))).send_keys("50000")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="data_emissione"]'))).send_keys("08/07/2024", Keys.ENTER)
        self.find(By.XPATH, '(//button[@class="btn btn-primary"])[2]').click()
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_25"]//tbody//tr//td[1]')))
        self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.find(By.XPATH, '//i[@class="fa fa-plus"]').click()
        self.wait_modal()

        self.find(By.XPATH, '//span[@id="select2-idanagrafica_add-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente", Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click()
        self.wait_loader()
        
        # Verifica dichiarazione di intento
        elemento = self.find(By.XPATH, '(//div[@class="alert alert-info"])[1]').text
        self.assertEqual("La fattura è collegata ad una dichiarazione d'intento", elemento[0:53])
        self.find(By.XPATH, '//a[@class="btn btn-primary"]').click()
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("prova per dichiarazione")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="qta"]'))).send_keys("100")
        self.find(By.XPATH, '//span[@id="select2-um-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("pz", Keys.ENTER)
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("1")
        self.find(By.XPATH, '//button[@class="btn btn-primary pull-right"]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@id="save"]').click()
        self.wait_loader()

        self.navigateTo("Anagrafiche")
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr//td[2]').click()
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="control-sidebar-button"]'))).click()
        self.find(By.XPATH, '//a[@id="link-tab_25"]').click()
        sleep(1)

        totale=self.find(By.XPATH, '//div[@id="tab_25"]//tbody//tr//td[5]').text
        self.assertEqual(totale, "102.00")

        # Modifica della dichiarazione
        self.find(By.XPATH, '//div[@id="tab_25"]//tbody//tr//td[5]').click()
        modal = self.wait_modal()

        self.input(modal, 'Progressivo int.').setValue("01")
        self.find(By.XPATH, '//div[@id="modals"]//button[@type="submit"]').click()
        self.wait_loader()

        num_progressivo=self.find(By.XPATH, '//div[@id="tab_25"]//tbody//td[3]').text
        self.assertEqual(num_progressivo, "01")

        # Elimina dichiarazione
        self.find(By.XPATH, '//div[@id="tab_25"]//tbody//td[3]').click()
        sleep(1)

        self.find(By.XPATH, '//a[@class="btn btn-danger ask "]').click()
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))).click()
        self.wait_loader()

        messaggio=self.find(By.XPATH, '//div[@id="tab_25"]//td[@class="dataTables_empty"]').text
        self.assertEqual(messaggio, "Nessun dato presente nella tabella")

        # Eliminazione fattura creata per la dichiarazione
        self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr//td[2]').click()
        self.wait_loader()

        self.find(By.XPATH, '//a[@id="elimina"]').click()
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))).click()
        self.wait_loader()
        
        self.navigateTo("Anagrafiche")
        self.find(By.XPATH, '//i[@class="deleteicon fa fa-times"]').click()
        sleep(1)

    def assicurazione_crediti(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Anagrafiche")
        self.wait_loader() 

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Ragione-sociale"]/input'))).send_keys("Cliente", Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//tbody//tr//td[2]').click()
        self.wait_loader() 

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="control-sidebar-button"]'))).click()
        self.find(By.XPATH, '//a[@id="link-tab_45"]').click()
        self.find(By.XPATH,'//div[@id="tab_45"]//i[@class="fa fa-plus"]').click()
        self.wait_loader() 

        # Aggiunta assicurazione crediti
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="data_inizio"]'))).send_keys("01/01/2024")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="data_fine"]'))).send_keys("31/12/2024")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="fido_assicurato"]'))).send_keys("50000", Keys.ENTER)
        self.wait_loader()

        self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click()
        modal = self.wait_modal()

        # Verifica assicurazione crediti
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="data"]'))).send_keys( "01/01/2024")
        self.find(By.XPATH, '//span[@id="select2-idanagrafica_add-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente", Keys.ENTER)
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click()
        self.wait_loader()

        self.find(By.XPATH, '//a[@class="btn btn-primary"]').click()
        sleep(1)
        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("prova")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("51000")
        self.find(By.XPATH, '//button[@class="btn btn-primary pull-right"]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@id="save"]').click()
        self.wait_loader()

        elemento = self.find(By.XPATH, '//div[@class="alert alert-warning text-center"]').text
        self.assertEqual("Attenzione!", elemento[0:11])

        self.find(By.XPATH, '//a[@id="elimina"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))).click()
        self.wait_loader()

        # Modifica assicurazione crediti    
        self.navigateTo("Anagrafiche")
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr//td[2]').click()
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="control-sidebar-button"]'))).click()
        self.find(By.XPATH, '//a[@id="link-tab_45"]').click()
        self.find(By.XPATH, '//div[@id="tab_45"]//tbody//tr//td[2]').click()
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="fido_assicurato"]'))).send_keys(Keys.BACK_SPACE, "49000")
        self.find(By.XPATH, '//button[@class="btn btn-primary pull-right"]').click()
        sleep(1)

        modifica=self.find(By.XPATH, '//div[@id="tab_45"]//tbody//tr//td[2]').text
        self.assertEqual(modifica, "49000.00")
        sleep(1)

        # Elimina assicurazione crediti
        self.find(By.XPATH, '//div[@id="tab_45"]//tbody//tr//td[2]').click()
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="modals"]//a[@class="btn btn-danger ask"]').click()
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))).click()
        self.wait_loader()

        self.navigateTo("Anagrafiche")
        self.find(By.XPATH, '//i[@class="deleteicon fa fa-times"]').click()
        sleep(1)

    def ricerca_coordinate(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Anagrafiche")
        self.wait_loader() 

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Ragione-sociale"]/input'))).send_keys("Admin spa", Keys.ENTER) 
        sleep(1)

        self.find(By.XPATH, '//tbody//tr//td').click() 
        self.find(By.XPATH, '//button[@class="btn btn-primary btn-lg dropdown-toggle dropdown-toggle-split"]').click()  
        wait.until(EC.visibility_of_element_located((By.XPATH, '//a[@data-op="ricerca-coordinate"]'))).click()  
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-warning"]').click()  
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr//td[2]').click() 
        self.wait_loader()

        self.find(By.XPATH, '//a[@onclick="modificaPosizione()"]').click()
        sleep(1)

        self.find(By.XPATH, '//ul//li[2]//div').click()
        latitudine=self.find(By.XPATH, '//input[@id="lat"]').text  
        self.assertNotEqual(latitudine, "0")
        longitudine=self.find(By.XPATH, '//input[@id="lng"]').text
        self.assertNotEqual(longitudine, "0")   
        self.find(By.XPATH, '//button[@class="close"]').click() 
        self.wait_loader()
        
        self.navigateTo("Anagrafiche")
        self.wait_loader()
        self.find(By.XPATH, '//i[@class="deleteicon fa fa-times"]').click()
        sleep(1)

    def elimina_selezionati(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Anagrafiche")
        self.wait_loader() 

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Ragione-sociale"]/input'))).send_keys("Vettore", Keys.ENTER)  
        sleep(1)

        self.find(By.XPATH, '//tbody//tr//td').click()
        self.find(By.XPATH, '//button[@class="btn btn-primary btn-lg dropdown-toggle dropdown-toggle-split"]').click() 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//a[@data-op="delete-bulk"]'))).click() 
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()

        scritta=self.find(By.XPATH, '//tbody//tr[1]').text  
        self.assertEqual(scritta, "La ricerca non ha portato alcun risultato.")
        self.find(By.XPATH, '//i[@class="deleteicon fa fa-times"]').click() 
        sleep(1)

    def cambia_relazione(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Anagrafiche")
        self.wait_loader() 

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Ragione-sociale"]/input'))).send_keys("Cliente", Keys.ENTER)  
        sleep(1)

        self.find(By.XPATH, '//tbody//tr//td').click() 
        self.find(By.XPATH, '//button[@class="btn btn-primary btn-lg dropdown-toggle dropdown-toggle-split"]').click()  
        wait.until(EC.visibility_of_element_located((By.XPATH, '//a[@data-op="cambia-relazione"]'))).click()   
        self.find(By.XPATH, '//span[@id="select2-idrelazione-container"]').click() 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Attivo")
        sleep(1)

        self.find(By.XPATH, '//li[@class="select2-results__option select2-results__option--highlighted"]').click()
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-warning"]').click()
        self.wait_loader()

        relazione=self.find(By.XPATH, '//tbody//tr//td[7]').text 
        self.assertEqual(relazione, "Attivo")
        self.find(By.XPATH, '//tbody//tr//td[7]').click() 
        self.wait_loader()

        self.find(By.XPATH, '//span[@id="select2-idrelazione-container"]//span[@class="select2-selection__clear"]').click()   
        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@id="save"]'))).click()
        sleep(1)

        self.navigateTo("Anagrafiche")
        self.wait_loader()

        nuova_relazione=self.find(By.XPATH, '//tbody//tr//td[7]').text 
        self.assertNotEqual(nuova_relazione, "Attivo")
        self.find(By.XPATH, '//i[@class="deleteicon fa fa-times"]').click() 
        


