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

    def test_impostazioni_contratti(self):
        # Condizioni generali di fornitura contratti (1)
        self.condizioni_generali_contratti()

        # Crea contratto rinnocabile di default (2)
        self.crea_contratto_rinnovabile()

        # Giorni di preavviso di default (3)
        self.giorni_preavviso()

    def condizioni_generali_contratti(self):
        wait = WebDriverWait(self.driver, 20)
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-6"]').click() #apro Contratti
        sleep(1)
        #scrivo Prova come scritta per condizioni generali 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//iframe[@class="cke_wysiwyg_frame cke_reset"]'))).click()  
        wait.until(EC.visibility_of_element_located((By.XPATH, '//iframe[@class="cke_wysiwyg_frame cke_reset"]'))).send_keys("Prova")
        sleep(1)

        self.expandSidebar("Vendite")
        self.navigateTo("Contratti")
        self.wait_loader()

        self.find(By.XPATH, '//button[@class="btn btn-primary bound clickable"]').click()
        sleep(1)
        #creo contratto
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="nome"]'))).send_keys("Manutenzione")
        self.find(By.XPATH, '//span[@id="select2-idanagrafica-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente", Keys.ENTER)
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="data_accettazione"]'))).send_keys("01/01/2024")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="data_conclusione"]'))).send_keys("31/12/2024")
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click()
        self.wait_loader()
        
        self.find(By.XPATH, '//a[@id="print-button_p"]').click()    #click su stampa contratto
        sleep(2)

        self.driver.switch_to.window(self.driver.window_handles[1]) #cambia scheda
        scritta=self.find(By.XPATH, '//span[@style="left: 5.71%; top: 13.88%; font-size: calc(var(--scale-factor)*8.50px); font-family: sans-serif; transform: scaleX(0.913535);"]').text
        self.assertEqual(scritta, "Prova")
        self.driver.close() #chiude scheda
        self.driver.switch_to.window(self.driver.window_handles[0]) #torna alla prima

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_0"]//a[@class="btn btn-danger ask"]'))).click()  #elimino contratto 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))).click()
        self.wait_loader()

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()
        #torno alle impostazioni di prima
        self.find(By.XPATH, '//div[@id="impostazioni-6"]').click() #apro Contratti
        sleep(1)

        self.find(By.XPATH, '//iframe[@class="cke_wysiwyg_frame cke_reset"]').click()   #cancello la descrizione "Prova"
        wait.until(EC.visibility_of_element_located((By.XPATH, '//iframe[@class="cke_wysiwyg_frame cke_reset"]'))).send_keys(Keys.BACKSPACE, Keys.BACKSPACE, Keys.BACKSPACE, Keys.BACKSPACE, Keys.BACKSPACE, Keys.BACKSPACE)
        sleep(2)
        
    def crea_contratto_rinnovabile(self):
        wait = WebDriverWait(self.driver, 20)  
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-6"]').click() #apro Contratti
        sleep(1)

        self.find(By.XPATH, '//label[@class="btn btn-default active"]').click() #attivo impostazione
        sleep(1)

        self.expandSidebar("Vendite")
        self.navigateTo("Contratti")
        self.wait_loader()

        self.find(By.XPATH, '//button[@class="btn btn-primary bound clickable"]').click()   #click su +
        sleep(1)

        self.find(By.XPATH, '//button[@class="btn btn-tool"]').click()  #click su informazioni per rinnovo
        sleep(1)

        stato=self.find(By.XPATH, '//label[@class="btn btn-default active"]//span[1]').text #check per vedere se il rinnovo è attivato
        self.assertEqual(stato, "Attivato")

        self.find(By.XPATH, '//button[@class="close"]').click() #chiudi
        sleep(1)

        #torno alle impostazioni di prima
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-6"]').click() #apro Contratti
        sleep(1)

        self.find(By.XPATH, '//label[@class="btn btn-default active"]').click() #disattivo impostazione
        sleep(1)

    def giorni_preavviso(self):
        wait = WebDriverWait(self.driver, 20)  
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-6"]').click() #apro Contratti
        sleep(1)
  
        giorni=self.find(By.XPATH, '//input[@id="setting192"]') #imposto i giorni di preavviso a 3
        giorni.clear()
        giorni.send_keys("3", Keys.ENTER)
        sleep(1)

        self.expandSidebar("Vendite")
        self.navigateTo("Contratti")
        self.wait_loader()

        self.find(By.XPATH, '//button[@class="btn btn-primary bound clickable"]').click()   #click su +
        sleep(1)

        self.find(By.XPATH, '//button[@class="btn btn-tool"]').click()  #click su informazioni per rinnovo
        sleep(1)

        giorni_element = self.find(By.XPATH, '//input[@id="giorni_preavviso_rinnovo_add"]')   #controllo se i giorni di preavviso sono 3
        giorni = giorni_element.get_attribute("value")
        self.assertEqual(giorni, "3,00")
        self.find(By.XPATH, '//button[@class="close"]').click() #chiudi
        sleep(1)

        #torno alle impostazioni di prima
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-6"]').click() #apro Contratti
        sleep(1)
  
        giorni=self.find(By.XPATH, '//input[@id="setting192"]') #imposto i giorni di preavviso a 2
        giorni.clear()
        giorni.send_keys("2", Keys.ENTER)
        sleep(1)