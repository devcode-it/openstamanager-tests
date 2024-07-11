from common.Test import Test, get_html
from selenium.webdriver.common.keys import Keys
from common.RowManager import RowManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Articoli(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Magazzino")
        self.wait_loader()

    def test_creazione_articolo(self):
        # Crea un nuovo articolo. *Required*
        self.creazione_articolo("002", "Articolo di Prova")
        self.creazione_articolo("003", "Articolo di Prova da Eliminare")
        
        # Modifica articolo
        self.modifica_articolo("20", "1", "2", "carico di test")
        
        # Cancellazione articolo
        self.elimina_articolo()
        
        # Verifica articolo
        self.verifica_articolo()

        #plugin seriali
        self.serial()

        #plugin provvigioni
        self.provvigioni()

        #plugin listino fornitori
        self.listino_fornitori()

        #plugin giacenze
        self.giacenze()

        #plugin movimenti
        self.plugin_movimenti()

        #plugin statistiche
        self.statistiche()

        #plugin netto clienti
        self.netto_clienti()

        #plugin statistiche vendite
        self.statistiche_vendita()

        #plugin varianti articoli
        self.varianti_articoli()

    def creazione_articolo(self, codice: str, descrizione: str):
        self.navigateTo("Articoli")
        self.wait_loader()
        # #
        # 1/2 Crea un nuovo articolo. 
        # #
        # Apre la schermata di nuovo elemento
        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click()
        modal = self.wait_modal()

        self.input(modal, 'Codice').setValue(codice)
        self.input(modal, 'Descrizione').setValue(descrizione)

        # Submit
        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        self.wait_loader()
       
    def modifica_articolo(self, acquisto:str, coefficiente:str, qta: str, descrizione: str):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Articoli")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input'))).send_keys('Articolo 1', Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//div[@id="tab_0"]//tbody//td[2]//div[1]').click()
        self.wait_loader()

        self.input(None, 'Prezzo di acquisto').setValue(acquisto)
        self.input(None, 'Coefficiente').setValue(coefficiente)

        self.find(By.XPATH, '//div[@class="btn-group checkbox-buttons"]//label[@for="qta_manuale"]').click()
        self.input(None, 'Quantità').setValue(qta)
        self.input(None, 'Descrizione').setValue(descrizione)

        self.find(By.XPATH, '//div[@id="tab_0"]//button[@id="save"]').click()
        sleep(1)

        # Controllo quantità 
        self.find(By.XPATH, '//a[@id="back"]').click()
        sleep(1)
        
        verificaqta = self.find(By.XPATH, '//div[@id="tab_0"]//tbody//td[10]//div[1][1]').text
        self.assertEqual(verificaqta, "2,00")

        self.find(By.XPATH, '//th[@id="th_Descrizione"]/i[@class="deleteicon fa fa-times"]').click()
        sleep(2)  

    def elimina_articolo(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Articoli")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input'))).send_keys('Articolo di Prova da Eliminare', Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//div[@id="tab_0"]//tbody//td[2]//div[1]').click()
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_0"]//a[@class="btn btn-danger ask"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))).click()
        sleep(1)

        self.find(By.XPATH, '//th[@id="th_Descrizione"]/i[@class="deleteicon fa fa-times"]').click()
        sleep(1)

    def verifica_articolo(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Articoli")
        self.wait_loader()    

        #verifica elemento modificato
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Codice"]/input'))).send_keys("001", Keys.ENTER)
        sleep(1)

        modificato=self.driver.find_element(By.XPATH,'//tbody//tr[1]//td[9]').text
        self.assertEqual("20,00",modificato)
        self.find(By.XPATH, '//i[@class="deleteicon fa fa-times"]').click()
        self.wait_loader()

        #verifica elemento eliminato
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input'))).send_keys("Articolo di prova da Eliminare", Keys.ENTER)
        sleep(1)

        eliminato=self.driver.find_element(By.XPATH,'//tbody//tr[1]//td[1]').text
        self.assertEqual("La ricerca non ha portato alcun risultato.",eliminato)
        self.find(By.XPATH, '//th[@id="th_Descrizione"]/i[@class="deleteicon fa fa-times"]').click()
        sleep(1)

    def serial(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Articoli")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input'))).send_keys('Articolo 1', Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//tbody//td[2]//div[1]').click()
        self.wait_loader()
        
        self.find(By.XPATH, '(//label[@class="btn btn-default"])[1]').click()
        self.find(By.XPATH, '//button[@id="save"]').click()
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="control-sidebar-button"]'))).click()
        self.find(By.XPATH, '//a[@id="link-tab_11"]').click()
        sleep(1)
        self.find(By.XPATH, '//input[@id="serial_start"]').send_keys("1")
        sleep(1)
        self.find(By.XPATH, '//input[@id="serial_end"]').send_keys(Keys.BACK_SPACE, "2")
        sleep(1)
        self.find(By.XPATH, '(//button[@class="btn btn-primary"])[3]').click()
        sleep(1)
        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-primary"]'))).click()
        sleep(1)
        serial = self.find(By.XPATH, '//div[@id="tab_11"]//tbody//tr[2]//td[1]').text
        self.assertEqual(serial, "1")
        self.wait_loader()

        #elimina seriale e verifica eliminazione 
        self.find(By.XPATH, '(//a[@class="btn btn-danger btn-sm ask"])[2]').click()
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()  
        wait.until(EC.invisibility_of_element_located((By.XPATH, '//div[@id="tab_11"]//tbody//tr[2]//td[1]'))) 
        self.navigateTo("Articoli")
        self.wait_loader()
        self.find(By.XPATH, '//th[@id="th_Descrizione"]/i[@class="deleteicon fa fa-times"]').click()
        sleep(1)

    def provvigioni(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Articoli")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input'))).send_keys('Articolo 1', Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//tbody//td[2]//div[1]').click()
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="control-sidebar-button"]'))).click()
        sleep(1)

        self.find(By.XPATH, '//a[@id="link-tab_43"]').click()
        sleep(1)

        self.find(By.XPATH, '//div[@id="tab_43"]//i[@class="fa fa-plus"]').click()
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-idagente-container"]').click()
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '(//input[@class="select2-search__field"])[2]'))).send_keys("Agente", Keys.ENTER)
        sleep(1)
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="provvigione"]'))).send_keys("1.00", Keys.ENTER)
        sleep(2)
        self.wait_loader()
        
        self.find(By.XPATH, '//td[@class="  select-checkbox"]') #se trova il checkbox test superato
        #modifica provvigione
        self.find(By.XPATH, '(//div[@id="tab_43"]//tr[1]//td[2])[2]').click()
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="provvigione"]'))).send_keys("2", Keys.ENTER)
        self.wait_loader()

        provvigione=self.find(By.XPATH, '(//div[@id="tab_43"]//tr[1]//td[3]/div)[2]').text
        self.assertEqual(provvigione, "2.00 €")
        
        #eliminazione provvigione
        self.find(By.XPATH, '//td[@class="bound clickable"][1]').click()
        sleep(2)

        self.find(By.XPATH, '(//a[@class="btn btn-danger ask"])[2]').click()
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()

        self.navigateTo("Articoli")
        self.wait_loader()
        
        self.find(By.XPATH, '//th[@id="th_Descrizione"]//i[@class="deleteicon fa fa-times"]').click()
        sleep(1)

    def listino_fornitori(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Articoli")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input'))).send_keys('Articolo 1', Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//tbody//td[2]//div[1]').click()
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="control-sidebar-button"]'))).click()
        sleep(1)

        self.find(By.XPATH, '//a[@id="link-tab_32"]').click()
        self.wait_loader()

        self.find(By.XPATH, '//span[@id="select2-id_fornitore_informazioni-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//input[@class="select2-search__field"])[2]'))).send_keys("Fornitore", Keys.ENTER)
        self.find(By.XPATH, '//button[@class="btn btn-info"]').click()
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="qta_minima"]'))).send_keys("100")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="giorni_consegna"]'))).send_keys("15")
        self.find(By.XPATH, '(//label[@class="btn btn-default active"])[4]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario_fisso"]'))).send_keys("15", Keys.ENTER)
        self.wait_loader()

        self.navigateTo("Articoli")
        self.wait_loader()

        self.find(By.XPATH, '//th[@id="th_Descrizione"]//i[@class="deleteicon fa fa-times"]').click()
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input'))).send_keys('Articolo 1', Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//tbody//td[2]//div[1]').click()
        self.wait_loader()

        self.find(By.XPATH, '//span[@id="select2-id_fornitore-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//input[@class="select2-search__field"])[2]'))).send_keys("Fornitore", Keys.ENTER) 

        self.navigateTo("Articoli")
        self.wait_loader()

        self.find(By.XPATH, '//th[@id="th_Descrizione"]//i[@class="deleteicon fa fa-times"]').click()
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input'))).send_keys('Articolo 1', Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//tbody//td[2]//div[1]').click()
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="control-sidebar-button"]'))).click()
        sleep(1)

        self.find(By.XPATH, '//a[@id="link-tab_32"]').click()
        self.wait_loader()

        nome=self.find(By.XPATH, '//div[@id="tab_32"]//tr//td[2]').text
        self.assertEqual(nome, "Articolo 1")
        #modifica
        self.find(By.XPATH, '//a[@class="btn btn-secondary btn-warning"]').click()
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="codice_fornitore"]'))).send_keys(Keys.BACKSPACE,Keys.BACK_SPACE,"1", Keys.ENTER)
        self.wait_loader()

        codice=self.find(By.XPATH, '(//div[@id="tab_32"]//td[3])[1]').text
        self.assertEqual(codice,"01")

        #elimina
        self.find(By.XPATH, '//a[@class="btn btn-secondary btn-danger ask"]').click()
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))).click()
        self.wait_loader()

        messaggio=self.find(By.XPATH, '(//div[@class="alert alert-info"])[5]').text
        self.assertEqual(messaggio, "Nessuna informazione disponibile...")
        self.wait_loader()

        self.navigateTo("Articoli")
        self.wait_loader()

        self.find(By.XPATH, '//th[@id="th_Descrizione"]/i[@class="deleteicon fa fa-times"]').click()
        sleep(1)

    def giacenze(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Articoli")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input'))).send_keys('Articolo 1', Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//tbody//td[2]//div[1]').click()
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="control-sidebar-button"]'))).click()
        sleep(1)

        self.find(By.XPATH, '//a[@id="link-tab_22"]').click()
        sleep(1)

        totale=self.find(By.XPATH, '//div[@id="tab_22"]//tbody//tr//td[2]').text
        self.assertEqual(totale, "3,00")
        self.find(By.XPATH, '//a[@class="btn btn-xs btn-info"]').click()
        sleep(1)

        totale_2=self.find(By.XPATH, '(//div[@id="tab_22"]//div[@class="col-md-12 text-center"])[2]').text
        self.assertEqual(totale_2, "3,00")
        sleep(1)

        self.find(By.XPATH, '//button[@class="close"]').click()
        sleep(1)

        self.navigateTo("Articoli")
        self.wait_loader()

        self.find(By.XPATH, '//th[@id="th_Descrizione"]/i[@class="deleteicon fa fa-times"]').click()
        sleep(1)

    def plugin_movimenti(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Articoli")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input'))).send_keys('Articolo 1', Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//tbody//td[2]//div[1]').click()
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="control-sidebar-button"]'))).click()
        sleep(1)

        self.find(By.XPATH, '//a[@id="link-tab_10"]').click()
        sleep(2)

        quantita=self.find(By.XPATH, '(//div[@id="tab_10"]//div[2]//b)[4]').text
        self.assertEqual(quantita, "3,00")

        self.navigateTo("Articoli")
        self.wait_loader()

        self.find(By.XPATH, '//th[@id="th_Descrizione"]/i[@class="deleteicon fa fa-times"]').click()
        sleep(1)

    def statistiche(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Articoli")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input'))).send_keys('Articolo 1', Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//tbody//td[2]//div[1]').click()
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="control-sidebar-button"]'))).click()
        sleep(1)

        self.find(By.XPATH, '//a[@id="link-tab_24"]').click()
        self.wait_loader()

        numero_1=self.find(By.XPATH, '(//div[@id="tab_24"]//td[@class="text-center"])[1]').text
        self.assertEqual(numero_1, "1")

        numero_2=self.find(By.XPATH, '(//div[@id="tab_24"]//td[@class="text-center"])[2]').text
        self.assertEqual(numero_2, "1")
        sleep(2)

        self.navigateTo("Articoli")
        self.wait_loader()

        self.find(By.XPATH, '//th[@id="th_Descrizione"]/i[@class="deleteicon fa fa-times"]').click()
        sleep(1)

    def netto_clienti(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Articoli")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input'))).send_keys('Articolo 1', Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//tbody//td[2]//div[1]').click()
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="control-sidebar-button"]'))).click()
        sleep(1)

        self.find(By.XPATH, '//a[@id="link-tab_27"]').click()
        self.wait_loader()

        self.find(By.XPATH, '//span[@id="select2-id_cliente_informazioni-container"]').click()
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '(//input[@class="select2-search__field"])[2]'))).send_keys('Cliente', Keys.ENTER)
        self.find(By.XPATH, '//button[@class="btn btn-info btn-block"]').click()
        sleep(1)

        self.find(By.XPATH, '(//label[@class="btn btn-default"])[4]').click()
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario_fisso"]'))).send_keys('5', Keys.ENTER)
        sleep(2)
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_27"]//tr[3]//td[1]')))
        #modifica
        self.find(By.XPATH, '//button[@class="btn btn-xs btn-warning"]').click()
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario_fisso"]'))).send_keys(Keys.BACK_SPACE,'2', Keys.ENTER)
        sleep(2)
        self.wait_loader()

        prezzo=self.find(By.XPATH, '//div[@id="tab_27"]//tr[3]//td[4]').text
        self.assertEqual(prezzo[0:6], "2,00 €")
        #eliminazione
        self.find(By.XPATH, '//button[@class="btn btn-xs btn-warning"]').click()
        sleep(1)

        self.find(By.XPATH, '(//label[@class="btn btn-default"])[4]').click()
        self.find(By.XPATH, '//button[@class="btn btn-primary pull-right"]').click()
        self.wait_loader()

        messaggio=self.find(By.XPATH, '//div[@id="tab_27"]//div[@class="alert alert-info"]').text
        self.assertEqual(messaggio,"Nessuna informazione disponibile...")
        self.navigateTo("Articoli")
        self.wait_loader()

        self.find(By.XPATH, '//th[@id="th_Descrizione"]/i[@class="deleteicon fa fa-times"]').click()
        sleep(1)

    def statistiche_vendita(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Articoli")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="control-sidebar-button"]'))).click()
        sleep(1)

        self.find(By.XPATH, '//a[@id="link-tab_44"]').click()
        self.wait_loader()

        self.find(By.XPATH, '(//div[@id="tab_44"]//tr[1]//td[1])[2]')   #checkbox
        self.navigateTo("Articoli")
        self.wait_loader()      

    def varianti_articoli(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Attributi Combinazioni")
        self.wait_loader()

        self.find(By.XPATH, '//button[@class="btn btn-primary bound clickable"]').click()
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="titolo"]'))).send_keys('Taglie', Keys.ENTER)
        self.wait_loader()

        self.find(By.XPATH, '//button[@class="btn btn-primary pull-right"]').click()
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="nome"]'))).send_keys('S', Keys.ENTER)
        self.wait_loader()

        self.find(By.XPATH, '//button[@class="btn btn-primary pull-right"]').click()
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="nome"]'))).send_keys('M', Keys.ENTER)
        self.wait_loader()

        self.find(By.XPATH, '//button[@class="btn btn-primary pull-right"]').click()
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="nome"]'))).send_keys('L', Keys.ENTER)
        self.wait_loader()

        self.navigateTo("Combinazioni")
        self.wait_loader()

        self.find(By.XPATH, '//button[@class="btn btn-primary bound clickable"]').click()
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="codice"]'))).send_keys('001')
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="nome"]'))).send_keys('Vestito')
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-selection select2-selection--multiple"]'))).send_keys('Taglie', Keys.ENTER)
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click()
        self.wait_loader()

        self.find(By.XPATH, '//button[@class="btn btn-warning "]').click()
        self.wait_loader()

        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Articoli")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input'))).send_keys('Vestito', Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//tbody//td[2]//div[1]').click()
        self.wait_loader()

        self.find(By.XPATH, '//button[@id="save"]').click()
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="control-sidebar-button"]'))).click()
        sleep(1)

        self.find(By.XPATH, '//a[@id="link-tab_34"]').click() 
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_34"]//tr[3]')))
        #modifica
        self.navigateTo("Attributi Combinazioni")
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr[1]//td[2]').click()
        self.wait_loader()

        self.find(By.XPATH, '(//button[@class="btn btn-warning btn-xs"])[1]').click()
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="nome"]'))).send_keys(Keys.BACKSPACE,"XS",Keys.ENTER)
        self.wait_loader()

        self.navigateTo("Articoli")
        self.wait_loader()

        self.find(By.XPATH, '//th[@id="th_Descrizione"]/i[@class="deleteicon fa fa-times"]').click()
        sleep(2) 

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input'))).send_keys('Vestito', Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//tbody//td[2]//div[1]').click()
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="control-sidebar-button"]'))).click()
        sleep(1)

        self.find(By.XPATH, '//a[@id="link-tab_34"]').click() 
        self.wait_loader()

        taglia=self.find(By.XPATH, '//div[@id="tab_34"]//tr[1]//td[2]').text
        self.assertEqual(taglia, "Taglie: XS")
        #elimina
        self.navigateTo("Attributi Combinazioni")
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr[1]//td[2]').click()
        self.wait_loader()

        self.find(By.XPATH, '//a[@class="btn btn-danger ask"]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()

        scritta=self.find(By.XPATH, '//tbody//tr[1]').text
        self.assertEqual(scritta, "Nessun dato presente nella tabella")

        self.navigateTo("Articoli")
        self.wait_loader()

        self.find(By.XPATH, '//th[@id="th_Descrizione"]/i[@class="deleteicon fa fa-times"]').click()
        sleep(1)