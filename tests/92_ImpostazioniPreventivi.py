from common.Test import Test, get_html
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Impostazioni(Test):
    def setUp(self):
        super().setUp()

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")

    def test_impostazioni_preventivi(self):
        # Condizioni generali di fornitura preventivi (1)
        self.condizioni_fornitura_preventivi()

        # Conferma automatica la quantità nei preventivi (2)
        self.conferma_quantita_preventivi()

        # Esclusioni default preventivi (3)
        self.esclusioni_preventivi()

    def condizioni_fornitura_preventivi(self):
        wait = WebDriverWait(self.driver, 20)
        self.expandSidebar("Vendite")
        self.navigateTo("Preventivi")
        self.wait_loader()

        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click()   #crea preventivo
        sleep(1)
        #nome
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="nome"]'))).send_keys('Test')
        #cliente
        self.find(By.XPATH, '//span[@id="select2-idanagrafica-container"]').click()
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-idanagrafica-results"]//li[2]').click()
        #tipo di attività
        self.find(By.XPATH, '//span[@id="select2-idtipointervento-container"]').click()
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-idtipointervento-results"]//li[1]').click()
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click()   #click su aggiungi
        self.wait_loader()

        self.find(By.XPATH, '//a[@id="print-button_p"]').click()    #stampa preventivo
        sleep(1)

        self.driver.switch_to.window(self.driver.window_handles[1]) #cambia scheda
        sleep(1)

        wait.until(EC.invisibility_of_element_located((By.XPATH, '(//div[@id="viewer"]//span)[65]')))  #controlla se non trova l'elemento collegato alla condizione
        self.driver.close() #chiude scheda
        self.driver.switch_to.window(self.driver.window_handles[0]) #torna alla prima
        sleep(1)
        #elimina preventivo
        self.find(By.XPATH, '//a[@class="btn btn-danger ask"]').click()
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-17"]').click() #apro preventivi
        sleep(1)
        
        #scrivo "Prova" come scritta per condizioni generali 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//iframe[@class="cke_wysiwyg_frame cke_reset"]'))).click()  
        wait.until(EC.visibility_of_element_located((By.XPATH, '//iframe[@class="cke_wysiwyg_frame cke_reset"]'))).send_keys("Prova")
        sleep(1)

        self.expandSidebar("Vendite")
        self.navigateTo("Preventivi")
        self.wait_loader()

        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click()   #crea preventivo
        sleep(1)
        #nome
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="nome"]'))).send_keys('Test')
        #cliente
        self.find(By.XPATH, '//span[@id="select2-idanagrafica-container"]').click()
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-idanagrafica-results"]//li[2]').click()
        #tipo di attività
        self.find(By.XPATH, '//span[@id="select2-idtipointervento-container"]').click()
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-idtipointervento-results"]//li[1]').click()
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click()   #click su aggiungi
        self.wait_loader()

        self.find(By.XPATH, '//a[@id="print-button_p"]').click()    #stampa preventivo
        sleep(1)

        self.driver.switch_to.window(self.driver.window_handles[1]) #cambia scheda
        sleep(1)

        testo=self.find(By.XPATH, '(//div[@id="viewer"]//span)[65]').text   #controlla se la condizione coincide con quella messa in impostazioni
        self.assertEqual(testo, "Prova")
        self.driver.close() #chiude scheda
        self.driver.switch_to.window(self.driver.window_handles[0]) #torna alla prima
        sleep(1)
        #elimina preventivo
        self.find(By.XPATH, '//a[@class="btn btn-danger ask"]').click()
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()

        #torno alle impostazioni di prima
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-17"]').click() #apro preventivi
        sleep(1)

        element = self.find(By.XPATH, '//iframe[@class="cke_wysiwyg_frame cke_reset"]')
        element.click()
        element.clear()
        sleep(1)

    def conferma_quantita_preventivi(self):
        wait = WebDriverWait(self.driver, 20)
        self.expandSidebar("Vendite")
        self.navigateTo("Preventivi")
        self.wait_loader()

        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click()   #crea preventivo
        sleep(1)
        #nome
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="nome"]'))).send_keys('Test')
        #cliente
        self.find(By.XPATH, '//span[@id="select2-idanagrafica-container"]').click()
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-idanagrafica-results"]//li[2]').click()
        #tipo di attività
        self.find(By.XPATH, '//span[@id="select2-idtipointervento-container"]').click()
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-idtipointervento-results"]//li[1]').click()
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click()   #click su aggiungi
        self.wait_loader()

        self.find(By.XPATH, '//span[@id="select2-id_articolo-container"]').click()  #aggiungo un articolo
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys('Articolo 1')
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(Keys.ENTER)
        self.find(By.XPATH, '//button[@class="btn btn-primary tip tooltipstered"]').click() #click su aggiungi
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//i[@class="fa fa-check text-success"]')))    #check se la quantità è stata confermata automaticamente
        #elimina preventivo
        self.find(By.XPATH, '//a[@class="btn btn-danger ask"]').click()
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-17"]').click() #apro preventivi
        sleep(1)

        self.find(By.XPATH, '//label[@class="btn btn-default active"]').click() #disattiva impostazione
        sleep(1)

        self.expandSidebar("Vendite")
        self.navigateTo("Preventivi")
        self.wait_loader()

        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click()   #crea preventivo
        sleep(1)
        #nome
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="nome"]'))).send_keys('Test')
        #cliente
        self.find(By.XPATH, '//span[@id="select2-idanagrafica-container"]').click()
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-idanagrafica-results"]//li[2]').click()
        #tipo di attività
        self.find(By.XPATH, '//span[@id="select2-idtipointervento-container"]').click()
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-idtipointervento-results"]//li[1]').click()
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click()   #click su aggiungi
        self.wait_loader()

        self.find(By.XPATH, '//span[@id="select2-id_articolo-container"]').click()  #aggiungo un articolo
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys('Articolo 1')
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(Keys.ENTER)
        self.find(By.XPATH, '//button[@class="btn btn-primary tip tooltipstered"]').click() #click su aggiungi
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//i[@class="fa fa-clock-o text-warning"]')))    #check se la quantità è stata confermata automaticamente
        #elimina preventivo
        self.find(By.XPATH, '//a[@class="btn btn-danger ask"]').click()
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()

        #torno alle impostazioni di prima
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-17"]').click() #apro preventivi
        sleep(1)

        self.find(By.XPATH, '//label[@class="btn btn-default active"]').click() #attiva impostazione
        sleep(1)

    def esclusioni_preventivi(self):
        wait = WebDriverWait(self.driver, 20)
        self.expandSidebar("Vendite")
        self.navigateTo("Preventivi")
        self.wait_loader()

        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click()   #crea preventivo
        sleep(1)
        #nome
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="nome"]'))).send_keys('Test')
        #cliente
        self.find(By.XPATH, '//span[@id="select2-idanagrafica-container"]').click()
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-idanagrafica-results"]//li[2]').click()
        #tipo di attività
        self.find(By.XPATH, '//span[@id="select2-idtipointervento-container"]').click()
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-idtipointervento-results"]//li[1]').click()
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click()   #click su aggiungi
        self.wait_loader()

        testo=self.find(By.XPATH, '//textarea[@id="esclusioni"]').text  #check se non è stato aggiunto nessun testo
        self.assertEqual(testo, "")
        #elimina preventivo
        self.find(By.XPATH, '//a[@class="btn btn-danger ask"]').click()
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-17"]').click() #apro preventivi
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="setting205"]'))).send_keys("test")  #scrivo esclusioni
        sleep(1)

        self.expandSidebar("Vendite")
        self.navigateTo("Preventivi")
        self.wait_loader()

        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click()   #crea preventivo
        sleep(1)
        #nome
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="nome"]'))).send_keys('Test')
        #cliente
        self.find(By.XPATH, '//span[@id="select2-idanagrafica-container"]').click()
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-idanagrafica-results"]//li[2]').click()
        #tipo di attività
        self.find(By.XPATH, '//span[@id="select2-idtipointervento-container"]').click()
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-idtipointervento-results"]//li[1]').click()
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click()   #click su aggiungi
        self.wait_loader()

        testo=self.find(By.XPATH, '//textarea[@id="esclusioni"]').text  #check se è stato aggiunto il testo
        self.assertEqual(testo, "test")
        #elimina preventivo
        self.find(By.XPATH, '//a[@class="btn btn-danger ask"]').click()
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-17"]').click() #apro preventivi
        sleep(1)

        testo=self.find(By.XPATH, '//textarea[@id="setting205"]')   #cancello testo
        testo.clear()
        sleep(1)
        



