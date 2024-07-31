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

    def test_impostazioni_fatturazione(self):
        # Iva predefinita (1)
        self.iva_predefinita()

        # Tipo di pagamento predefinito (2)
        self.tipo_pagamento_predefinito()

        # Ritenuta d'acconto predefinita (3)
        self.ritenuta_acconto_predefinita()

        # Cassa previdenziale predefinita (4)
        self.cassa_previdenziale_predefinita()

        # Conto predefinito fatture di vendita (8)
        self.conto_predefinito_vendita()

        # Conto predefinito fatture di acquisto (9)
        self.conto_predefinito_acquisto()


    def iva_predefinita(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-9"]').click() #apro Fatturazione
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-setting6-container"]').click() #aggiungi iva al 10
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Aliq. Iva 10")
        sleep(2)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(Keys.ENTER)
        sleep(2)

        self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.find(By.XPATH, '//button[@class="btn btn-primary bound clickable"]').click()   #click su +
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-idanagrafica_add-container"]').click() #seleziono Cliente come anagrafica
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente", Keys.ENTER)
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click() #click su aggiungi
        self.wait_loader()

        self.find(By.XPATH, '//a[@class="btn btn-primary"]').click() #aggiungi riga
        sleep(1)

        iva=self.find(By.XPATH, '//span[@id="select2-idiva-container"]').text   #check iva
        self.assertEqual(iva[2:21], "10 - Aliq. Iva 10%")
        self.find(By.XPATH, '//button[@class="close"]').click()
        sleep(1)

        self.find(By.XPATH, '//a[@id="elimina"]').click() #elimina fattura
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()   #click di conferma
        self.wait_loader()
        #torno alle impostazioni di prima
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-9"]').click() #apro Fatturazione
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-setting6-container"]').click() #aggiungi iva al 22
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Aliq. Iva 22")
        sleep(2)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(Keys.ENTER)
        sleep(2)

    def tipo_pagamento_predefinito(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-9"]').click() #apro Fatturazione
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-setting7-container"]').click() #metto come tipo di pagamento "Rimessa diretta"
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Rimessa diretta")
        sleep(2)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(Keys.ENTER)
        sleep(2)

        self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.find(By.XPATH, '//button[@class="btn btn-primary bound clickable"]').click()   #click su +
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-idanagrafica_add-container"]').click() #seleziono Cliente come anagrafica
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente", Keys.ENTER)
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click() #click su aggiungi
        self.wait_loader()
        #check se è cambiato il tipo di pagamento
        tipo=self.find(By.XPATH, '//span[@id="select2-idpagamento-container"]').text
        self.assertEqual(tipo[2:24], "MP01 - Rimessa diretta")
        self.find(By.XPATH, '//a[@id="elimina"]').click() #elimina fattura
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()   #click di conferma
        self.wait_loader()
        #torno alle impostazioni di prima
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-9"]').click() #apro Fatturazione
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-setting7-container"]').click() #metto come tipo di pagamento "Bonifico 30gg d.f.f.m."
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Bonifico 30gg d.f.f.m.")
        sleep(2)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(Keys.ENTER)
        sleep(2)

    def ritenuta_acconto_predefinita(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-9"]').click() #apro Fatturazione
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-setting8-container"]').click() #seleziona ritenuta acconto
        sleep(1)

        self.find(By.XPATH, '(//ul[@id="select2-setting8-results"]//li)[1]').click()
        sleep(2)

        self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.find(By.XPATH, '//button[@class="btn btn-primary bound clickable"]').click()   #click su +
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-idanagrafica_add-container"]').click() #seleziono Cliente come anagrafica
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente", Keys.ENTER)
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click() #click su aggiungi
        self.wait_loader()

        self.find(By.XPATH, '//a[@class="btn btn-primary"]').click()
        sleep(2)

        ritenuta=self.find(By.XPATH, '//span[@id="select2-id_ritenuta_acconto-container"]').text    #check se è stata impostata la ritenuta
        self.assertEqual(ritenuta[2:25], "Ritenuta d'acconto 10%")
        self.find(By.XPATH, '//button[@class="close"]').click()
        sleep(1)
        #elimina fattura
        self.find(By.XPATH, '//a[@id="elimina"]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()   #click di conferma
        self.wait_loader()
        #torno alle impostazioni di prima
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-9"]').click() #apro Fatturazione
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-setting8-container"]//span').click()   #cancella ritenuta

    def cassa_previdenziale_predefinita(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-9"]').click() #apro Fatturazione
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-setting9-container"]').click() #imposta cassa previdenziale
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-setting9-results"]//li').click()
        sleep(2)

        self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.find(By.XPATH, '//button[@class="btn btn-primary bound clickable"]').click()   #click su +
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-idanagrafica_add-container"]').click() #seleziono Cliente come anagrafica
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente", Keys.ENTER)
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click() #click su aggiungi
        self.wait_loader()

        self.find(By.XPATH, '//a[@class="btn btn-primary"]').click()
        sleep(2)

        cassa_previdenziale=self.find(By.XPATH, '//span[@id="select2-id_rivalsa_inps-container"]').text #check se la cassa è stata impostata
        self.assertEqual(cassa_previdenziale[2:17], "Rivalsa INPS 4%")
        self.find(By.XPATH, '//button[@class="close"]').click() #chiudo
        sleep(1)
        #elimina fattura
        self.find(By.XPATH, '//a[@id="elimina"]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()   #click di conferma
        self.wait_loader()
        #torno alle impostazioni di prima
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-9"]').click() #apro Fatturazione
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-setting9-container"]//span').click()
        sleep(2)

    def conto_predefinito_vendita(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-9"]').click() #apro Fatturazione
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-setting36-container"]').click()    #cambio conto
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-setting36-results"]//li[2]').click()
        sleep(2)

        self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.find(By.XPATH, '//button[@class="btn btn-primary bound clickable"]').click()   #click su +
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-idanagrafica_add-container"]').click() #seleziono Cliente come anagrafica
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente", Keys.ENTER)
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click() #click su aggiungi
        self.wait_loader()

        self.find(By.XPATH, '//a[@class="btn btn-primary"]').click()
        sleep(2)

        conto=self.find(By.XPATH, '//span[@id="select2-idconto-container"]').text   #check se il conto è cambiato
        self.assertEqual(conto[2:47], "700.000020 Ricavi vendita prestazione servizi")
        self.find(By.XPATH, '//button[@class="close"]').click() #chiudo
        sleep(1)
        #elimina fattura
        self.find(By.XPATH, '//a[@id="elimina"]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()   #click di conferma
        self.wait_loader()
        #torno alle impostazioni di prima
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-9"]').click() #apro Fatturazione
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-setting36-container"]').click()    #cambio conto
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-setting36-results"]//li[1]').click()
        sleep(2)

    def conto_predefinito_acquisto(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-9"]').click() #apro Fatturazione
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-setting37-container"]').click() #cambio conto
        sleep(2)

        self.find(By.XPATH, '//ul[@id="select2-setting37-results"]//li[2]').click()
        sleep(2)

        self.expandSidebar("Acquisti")
        self.navigateTo("Fatture di acquisto")
        self.wait_loader()

        self.find(By.XPATH, '//button[@class="btn btn-primary bound clickable"]').click()   #click su +
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="numero_esterno"]'))).send_keys("05")   #scrivo 05 come numero esterno
        self.find(By.XPATH, '//span[@id="select2-idanagrafica_add-container"]').click() #seleziono "Fornitore" come fornitore
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Fornitore", Keys.ENTER)
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click()   #click su aggiungi
        self.wait_loader()

        self.find(By.XPATH, '//span[@id="select2-idpagamento-container"]').click()  #æggiungi pagamento
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-idpagamento-results"]//li[1]').click()
        sleep(1)

        self.find(By.XPATH, '//a[@class="btn btn-primary"]').click()    #aggiungi riga
        sleep(1)

        conto=self.find(By.XPATH, '//span[@id="select2-idconto-container"]').text
        self.assertEqual(conto[2:50], "600.000020 Costi merci c/acquisto di produzione")
        self.find(By.XPATH, '//button[@class="close"]').click()     #chiudi
        sleep(1)

        self.find(By.XPATH, '//a[@id="elimina"]').click()   #elimino fattura
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()
        #torno alle impostazioni di prima
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-9"]').click() #apro Fatturazione
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-setting37-container"]').click() #cambio conto
        sleep(2)

        self.find(By.XPATH, '//ul[@id="select2-setting37-results"]//li[1]').click()
        sleep(2)
