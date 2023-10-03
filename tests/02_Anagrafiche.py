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
        # Creazione anagrafiche *Required*
        self.add_anagrafica('Cliente', 'Cliente')  
        self.add_anagrafica('Tecnico', 'Tecnico') 
        self.add_anagrafica('Fornitore', 'Fornitore')
        self.add_anagrafica('Vettore', 'Vettore') 
        self.add_anagrafica('Agente', 'Agente')
        self.add_anagrafica('Anagrafica di Prova da Eliminare', 'Cliente')

        # Modifica anagrafica
        self.modifica_anagrafica('Privato')

        # Aggiunta referente
        self.aggiunta_referente()

        # Aggiunta sede
        self.aggiunta_sede()

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

        # Crea registrazione contabile
        self.crea_registrazione_contabile()


    def add_anagrafica(self, nome=str, tipo=str):
        # Crea una nuova anagrafica del tipo indicato.
        self.find(By.CSS_SELECTOR, '#tabs > li:first-child .btn-primary > .fa-plus').click()
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
 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Ragione-sociale"]/input'))).send_keys("Cliente", Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//div[@id="tab_0"]//tbody//td[2]//div[1]').click()    
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="select2-tipo-container"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//input[@class="select2-search__field"])[3]'))).send_keys(tipologia, Keys.ENTER)
        self.wait_loader()

        self.input(None, 'Partita IVA').setValue("05024030287")
        self.input(None, 'Codice fiscale').setValue("05024030287")
        self.driver.find_element(By.XPATH,'//input[@id="indirizzo"]').send_keys("Via controllo caratteri speciali: &\"<>èéàòùì?'`")
        self.input(None, 'C.A.P.').setValue("35042")
        self.input(None, 'Città').setValue("Este")

        self.find(By.XPATH, '//a[@id="save"]').click()

        self.navigateTo("Anagrafiche")
        self.wait_loader()    

        self.find(By.XPATH, '//i[@class="deleteicon fa fa-times fa-2x"]').click()

    def aggiunta_referente(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Anagrafiche")
 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Ragione-sociale"]/input'))).send_keys("Cliente", Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//div[@id="tab_0"]//tbody//td[2]//div[1]').click()    
        #Aggiunta referente
        wait.until(EC.visibility_of_element_located((By.XPATH, '//a[@id="link-tab_3"]'))).click()
        sleep(1)

        self.find(By.XPATH, '//h4//i[@class="fa fa-plus"]').click()
        sleep(1)

        self.input(None,'Nominativo').setValue("Referente di prova")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="modal-dialog modal-lg"]//i[@class="fa fa-plus"]'))).click()
        modal=self.wait_modal()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="modal-content"]//div[@id="form_82-"]//input[@id="nome"]'))).send_keys("Segretario", Keys.ENTER)
        sleep(1)
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//div[@id="form_2-3"]//i[@class="fa fa-plus"])[3]'))).click()
        
        #Verifica referente
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Mansione"]/input'))).send_keys("Segretario", Keys.ENTER)
        sleep(1)

        modificato=self.driver.find_element(By.XPATH,'//tbody//tr[1]//td[3]').text
        self.assertEqual("Segretario", modificato)
        self.navigateTo("Anagrafiche")
        self.wait_loader()    

        self.find(By.XPATH, '//i[@class="deleteicon fa fa-times fa-2x"]').click()

    def aggiunta_sede(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Anagrafiche")
 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Ragione-sociale"]/input'))).send_keys("Cliente", Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//div[@id="tab_0"]//tbody//td[2]//div[1]').click()
        sleep(1) 
        #Aggiunta sede
        wait.until(EC.visibility_of_element_located((By.XPATH, '//a[@id="link-tab_4"]'))).click()
        sleep(1)

        self.find(By.XPATH, '//div[@id="tab_4"]//i[@class="fa fa-plus"]').click()
        sleep(1)

        self.input(None, 'Nome sede').setValue("Filiale XY")
        self.find(By.XPATH, '(//input[@id="citta"])[2]').click()
        self.find(By.XPATH, '(//input[@id="citta"])[2]').send_keys("Padova")
        sleep(1)
        
        self.find(By.XPATH, '(//span[@id="select2-id_nazione-container"])[2]').click()
        self.find(By.XPATH, '//li[@class="select2-results__option select2-results__option--highlighted"]').click()

        self.find(By.XPATH, '(//div[@id="form_2-4"]//i[@class="fa fa-plus"])[2]').click()
        sleep(1)

        #Verifica sede
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))).send_keys("Filiale XY", Keys.ENTER)
        sleep(1)

        modificato=self.driver.find_element(By.XPATH,'//tbody//tr[1]//td[2]').text
        self.assertEqual("Filiale XY", modificato)
        self.navigateTo("Anagrafiche")
        self.wait_loader()    

        self.find(By.XPATH, '//i[@class="deleteicon fa fa-times fa-2x"]').click()

    def elimina_anagrafica(self):
        wait = WebDriverWait(self.driver, 20)     
        self.navigateTo("Anagrafiche")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Ragione-sociale"]/input'))).send_keys('Anagrafica di Prova da Eliminare', Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//div[@id="tab_0"]//tbody//td[2]//div[1]').click()
        sleep(1)
             
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_0"]//a[@class="btn btn-danger ask"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))).click()
        self.wait_loader()

        self.find(By.XPATH, '//i[@class="deleteicon fa fa-times fa-2x"]').click()

    def verifica_anagrafica(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Anagrafiche")
        self.wait_loader()    

        #verifica elemento modificato
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Tipologia"]/input'))).send_keys("Privato", Keys.ENTER)
        sleep(1)

        modificato=self.driver.find_element(By.XPATH,'//tbody//tr[1]//td[2]').text
        self.assertEqual("Cliente",modificato)
        self.find(By.XPATH, '//i[@class="deleteicon fa fa-times fa-2x"]').click()

        #verifica elemento eliminato
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Ragione-sociale"]/input'))).send_keys("Anagrafica di Prova da Eliminare", Keys.ENTER)
        sleep(1)

        eliminato=self.driver.find_element(By.XPATH,'//tbody//tr[1]//td[1]').text
        self.assertEqual("La ricerca non ha portato alcun risultato.",eliminato)
        self.find(By.XPATH, '//i[@class="deleteicon fa fa-times fa-2x"]').click()

    def crea_attivita(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Anagrafiche")
 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Ragione-sociale"]/input'))).send_keys("Cliente", Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//div[@id="tab_0"]//tbody//td[2]//div[1]').click()    
        sleep(1)
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//button[@type="button"])[3]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//a[@class="bound clickable"])[1]'))).click()
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

        self.find(By.XPATH, '//div[@id="tab_0"]//tbody//td[2]//div[1]').click()   
        sleep(2)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//a[@id="link-tab_28"]'))).click()
        sleep(2)

        modificato=self.driver.find_element(By.XPATH,'//div[@id="tab_28"]//tbody//tr[1]//td[2]').text
        self.assertEqual("1",modificato)

        self.find(By.XPATH, '//div[@id="tab_28"]//tbody//td[2]').click()
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_0"]//a[@class="btn btn-danger ask"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))).click()
        self.wait_loader()

        self.navigateTo("Anagrafiche")
        self.find(By.XPATH, '//i[@class="deleteicon fa fa-times fa-2x"]').click()

    def crea_preventivo(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Anagrafiche")
 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Ragione-sociale"]/input'))).send_keys("Cliente", Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//div[@id="tab_0"]//tbody//td[2]//div[1]').click()   
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '(//button[@type="button"])[3]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//a[@class="bound clickable"])[2]'))).click()
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

        self.find(By.XPATH, '//div[@id="tab_0"]//tbody//td[2]//div[1]').click()   
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-box-tool"]'))).click()
        sleep(1)

        modificato=self.driver.find_element(By.XPATH,'(//div[@class="box-body"]//li)[1]').text
        self.assertEqual("Preventivo 1",modificato[0:12])
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="box-body"]//li//a'))).click()
        sleep(2)

        self.driver.switch_to.window(self.driver.window_handles[1])

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_0"]//a[@class="btn btn-danger ask"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))).click()
        self.wait_loader() 

        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

        self.navigateTo("Anagrafiche")
        self.find(By.XPATH, '//i[@class="deleteicon fa fa-times fa-2x"]').click()

    def crea_contratto(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Anagrafiche")
 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Ragione-sociale"]/input'))).send_keys("Cliente", Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//div[@id="tab_0"]//tbody//td[2]//div[1]').click()  
        sleep(1)  
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//button[@type="button"])[3]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//a[@class="bound clickable"])[3]'))).click()
        modal = self.wait_modal()

        self.input(modal, 'Nome').setValue("Contratto di prova anagrafica")
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//form[@id="add-form"]//span[@class="select2-selection select2-selection--single"])[2]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//li[@class="select2-results__option"])'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//div[@id="form_31-"]//button[@class="btn btn-primary"])'))).click()
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_0"]//a[@class="btn btn-danger ask"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))).click()
        self.wait_loader() 

        self.navigateTo("Anagrafiche")
        self.find(By.XPATH, '//i[@class="deleteicon fa fa-times fa-2x"]').click()

    def crea_ordine_cliente(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Anagrafiche")
 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Ragione-sociale"]/input'))).send_keys("Cliente", Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//div[@id="tab_0"]//tbody//td[2]//div[1]').click()
        self.wait_loader()
           
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//button[@type="button"])[3]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//a[@class="bound clickable"])[4]'))).click()
        modal = self.wait_modal()

        wait.until(EC.visibility_of_element_located((By.XPATH, '(//div[@id="form_24-"]//button[@class="btn btn-primary"])'))).click()
        sleep(1)

        self.navigateTo("Anagrafiche")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="tab_0"]//tbody//td[2]//div[1]').click()   
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-box-tool"]'))).click()
        sleep(1)

        modificato=self.driver.find_element(By.XPATH,'(//div[@class="box-body"]//li)[1]').text
        self.assertEqual("Ordine cliente 01",modificato[0:17])
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="box-body"]//li//a'))).click()
        sleep(2)

        self.driver.switch_to.window(self.driver.window_handles[1])

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_0"]//a[@class="btn btn-danger ask"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))).click()
        self.wait_loader() 

        self.navigateTo("Anagrafiche")
        self.find(By.XPATH, '//i[@class="deleteicon fa fa-times fa-2x"]').click()

        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
  
    def crea_DDT_uscita(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Anagrafiche")
 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Ragione-sociale"]/input'))).send_keys("Cliente", Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//div[@id="tab_0"]//tbody//td[2]//div[1]').click()
        sleep(1)    

        wait.until(EC.visibility_of_element_located((By.XPATH, '(//button[@type="button"])[3]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//a[@class="bound clickable"])[5]'))).click()
        modal = self.wait_modal()

        wait.until(EC.visibility_of_element_located((By.XPATH, '(//form[@id="add-form"]//span[@class="select2-selection select2-selection--single"])[3]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//li[@class="select2-results__option"])'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//div[@id="form_26-"]//button[@class="btn btn-primary"])'))).click()
        sleep(1)

        self.navigateTo("Anagrafiche")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="tab_0"]//tbody//td[2]//div[1]').click()   
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//a[@id="link-tab_17"]'))).click()
        sleep(2)

        modificato=self.driver.find_element(By.XPATH,'//div[@id="tab_17"]//tbody//td[2]').text
        self.assertEqual("01",modificato)
        sleep(1)

        self.find(By.XPATH, '//div[@id="tab_17"]//tbody//td[2]').click()
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_0"]//a[@class="btn btn-danger ask"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))).click()
        self.wait_loader() 

        self.navigateTo("Anagrafiche")
        self.find(By.XPATH, '//i[@class="deleteicon fa fa-times fa-2x"]').click()

    def crea_fattura_vendita(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Anagrafiche")
 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Ragione-sociale"]/input'))).send_keys("Cliente", Keys.ENTER)
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_0"]//tbody//td[2]//div[1]'))).click()
        sleep(1)
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//button[@type="button"])[3]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//a[@class="bound clickable"])[6]'))).click()
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '(//div[@id="form_14-"]//button[@class="btn btn-primary"])'))).click()
        sleep(1)

        self.navigateTo("Anagrafiche")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="tab_0"]//tbody//td[2]//div[1]').click()   
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-box-tool"]'))).click()
        sleep(1)

        modificato=self.driver.find_element(By.XPATH,'(//div[@class="box-body"]//li)[1]').text
        self.assertEqual("Fattura immediata di vendita",modificato[0:28])
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="box-body"]//li//a'))).click()
        sleep(1)

        self.driver.close() 
        sleep(1)

        self.driver.switch_to.window(self.driver.window_handles[0])

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_0"]//a[@class="btn btn-danger ask "]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))).click()
        self.wait_loader() 

        self.navigateTo("Anagrafiche")
        self.find(By.XPATH, '//i[@class="deleteicon fa fa-times fa-2x"]').click()

    def crea_registrazione_contabile(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Anagrafiche")
 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Ragione-sociale"]/input'))).send_keys("Cliente", Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//div[@id="tab_0"]//tbody//td[2]//div[1]').click()    
        sleep(1)
        
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//button[@type="button"])[3]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//a[@class="bound clickable"])[7]'))).click()
        modal = self.wait_modal()

        self.input(modal, 'Causale').setValue("Causale movimento in prima nota di prova anagrafica")
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//form[@id="add-form"]//span[@class="select2-selection select2-selection--single"])[2]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//li[@class="select2-results__option"])'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//form[@id="add-form"]//span[@class="select2-selection select2-selection--single"])[3]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//li[@class="select2-results__option"])'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//div[@id="form_16-"]//button[@class="btn btn-primary"])'))).click()
        sleep(1)

        self.navigateTo("Anagrafiche")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="tab_0"]//tbody//td[2]//div[1]').click()   
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//a[@id="link-tab_38"]'))).click()
        sleep(1)

        modificato=self.driver.find_element(By.XPATH,'//div[@id="tab_38"]//tbody//td[2]').text
        self.assertEqual("100",modificato[0:3])
        sleep(1)

        self.find(By.XPATH, '//div[@id="tab_38"]//tbody//td[2]//a').click()
        sleep(2)

        self.driver.switch_to.window(self.driver.window_handles[1])

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_0"]//a[@class="btn btn-danger ask"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))).click()
        self.wait_loader() 

        self.navigateTo("Anagrafiche")
        self.find(By.XPATH, '//i[@class="deleteicon fa fa-times fa-2x"]').click()