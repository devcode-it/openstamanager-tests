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

    def test_impostazioni_fatturazione(self):
        # Iva predefinita (1)
        self.iva_predefinita()

        # Tipo di pagamento predefinito (2)
        self.tipo_pagamento_predefinito()

        # Ritenuta d'acconto predefinita (3)
        self.ritenuta_acconto_predefinita()

        # Cassa previdenziale predefinita (4)
        self.cassa_previdenziale_predefinita()

        # Importo marca da bollo (5)
        self.importo_marca_bollo()

        # Soglia minima per l'applicazione della marca da bollo (6)
        self.soglia_minima_marca_bollo()

        # Conto predefinito fatture di vendita (8)
        self.conto_predefinito_vendita()

        # Conto predefinito fatture di acquisto (9)
        self.conto_predefinito_acquisto()

        # Dicitura fissa fattura (10)
        self.dicitura_fissa_fattura()   #da finire

        # Ritenuta previdenziale predefinita (12)
        self.ritenuta_previdenziale_predefinita()

        # Addebita marca da bollo al cliente (13)
        self.addebita_marca_bollo() #da finire

        # Descrizione addebito bollo (14)
        self.descrizione_marca_bollo()  

        # Conto predefinito per la marca da bollo (15)
        self.conto_marca_bollo()

        # Iva per lettere d'intento (16)
        self.iva_lettere_intento()

        # Utilizza prezzi di vendita comprensivi di IVA (17)
        self.prezzi_vendita_comprensivi_iva()

        # Liquidazione iva (18)
        self.liquidazione_iva()

        # Descrizione fattura pianificata (21)
        self.descrizione_fattura_pianificata()

        #  Bloccare i prezzi inferiori al minimo di vendita (28)
        self.bloccare_prezzi_inferiori_minimo_vendita() #da finire

        # Permetti fatturazione delle attività collegate a contratti (29)
        self.fattura_attivita_collegate_contratti()

        # Permetti fatturazione delle attività collegate a ordini (31)
        self.fattura_attivita_collegate_ordini()

        # Permetti fatturazione delle attività collegate a preventivi (32)
        self.fattura_attivita_collegate_preventivi()

    def iva_predefinita(self):
        wait = WebDriverWait(self.driver, 20)
        self.expandSidebar("Strumenti")
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

    def importo_marca_bollo(self):
        wait = WebDriverWait(self.driver, 20)
        self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.find(By.XPATH, '//button[@class="btn btn-primary bound clickable"]').click()   #click su +
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-idanagrafica_add-container"]').click() #seleziono Cliente come anagrafica
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente", Keys.ENTER)
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click() #click su aggiungi
        self.wait_loader()

        self.find(By.XPATH, '//a[@class="btn btn-primary"]').click()    #aggiungi riga
        sleep(2)

        #descrizione
        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("test")
        #prezzo unitario
        prezzo_unitario=self.find(By.XPATH, '//input[@id="prezzo_unitario"]')
        prezzo_unitario.clear()
        prezzo_unitario.send_keys("80")
        #iva
        self.find(By.XPATH, '//span[@id="select2-idiva-container"]').click()
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-idiva-results"]//li[20]').click()    #seleziono iva come non soggetta
        self.find(By.XPATH, '//button[@class="btn btn-primary pull-right"]').click()    #click su aggiungi
        self.wait_loader()
        sleep(1)

        totale=self.find(By.XPATH, '//tbody//tr[2]//td[9]').text
        self.assertEqual(totale, "2,00 €")     #check se la marca da bollo è di 2 euro
        #elimino fattura
        self.find(By.XPATH, '//a[@id="elimina"]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()   #click di conferma
        self.wait_loader()

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-9"]').click() #apro Fatturazione
        sleep(1)

        impostazione=self.find(By.XPATH, '//input[@id="setting10"]')
        impostazione.clear()
        impostazione.send_keys("3,00")  #cambio la marca da bollo da 2,00 a 3,00
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

        self.find(By.XPATH, '//a[@class="btn btn-primary"]').click()    #aggiungi riga
        sleep(2)

        #descrizione
        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("test")
        #prezzo unitario
        prezzo_unitario=self.find(By.XPATH, '//input[@id="prezzo_unitario"]')
        prezzo_unitario.clear()
        prezzo_unitario.send_keys("80")
        #iva
        self.find(By.XPATH, '//span[@id="select2-idiva-container"]').click()
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-idiva-results"]//li[20]').click()    #seleziono iva come non soggetta
        self.find(By.XPATH, '//button[@class="btn btn-primary pull-right"]').click()    #click su aggiungi
        self.wait_loader()
        sleep(1)

        totale=self.find(By.XPATH, '//tbody//tr[2]//td[9]').text
        self.assertEqual(totale, "3,00 €")     #check se la marca da bollo è di 3 euro
        #elimino fattura
        self.find(By.XPATH, '//a[@id="elimina"]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()   #click di conferma
        self.wait_loader()

        self.navigateTo("Impianti")
        self.wait_loader()

        #torno alle impostazioni di prima
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-9"]').click() #apro Fatturazione
        sleep(1)

        impostazione=self.find(By.XPATH, '//input[@id="setting10"]')
        impostazione.clear()
        impostazione.send_keys("2,00")  #cambio la marca da bollo da 3,00 a 2,00
        sleep(2)

    def soglia_minima_marca_bollo(self):
        wait = WebDriverWait(self.driver, 20)
        self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.find(By.XPATH, '//button[@class="btn btn-primary bound clickable"]').click()   #click su +
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-idanagrafica_add-container"]').click() #seleziono Cliente come anagrafica
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente", Keys.ENTER)
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click() #click su aggiungi
        self.wait_loader()

        self.find(By.XPATH, '//a[@class="btn btn-primary"]').click()    #aggiungi riga
        sleep(2)

        #descrizione
        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("test")
        #prezzo unitario
        prezzo_unitario=self.find(By.XPATH, '//input[@id="prezzo_unitario"]')
        prezzo_unitario.clear()
        prezzo_unitario.send_keys("80")
        #iva
        self.find(By.XPATH, '//span[@id="select2-idiva-container"]').click()
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-idiva-results"]//li[20]').click()    #seleziono iva come non soggetta
        self.find(By.XPATH, '//button[@class="btn btn-primary pull-right"]').click()    #click su aggiungi
        self.wait_loader()
        sleep(1)

        totale=self.find(By.XPATH, '//tbody//tr[2]//td[9]').text
        self.assertEqual(totale, "2,00 €")     #check se è presente la marca da bollo
        #elimino fattura
        self.find(By.XPATH, '//a[@id="elimina"]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()   #click di conferma
        self.wait_loader()

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-9"]').click() #apro Fatturazione
        sleep(1)

        impostazione=self.find(By.XPATH, '//input[@id="setting11"]')
        impostazione.clear()
        impostazione.send_keys("40")   #imposto la soglia minima a 40 euro
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

        self.find(By.XPATH, '//a[@class="btn btn-primary"]').click()    #aggiungi riga
        sleep(2)

        #descrizione
        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("test")
        #prezzo unitario
        prezzo_unitario=self.find(By.XPATH, '//input[@id="prezzo_unitario"]')
        prezzo_unitario.clear()
        prezzo_unitario.send_keys("45")    #prezzo più alto della soglia minima
        #iva
        self.find(By.XPATH, '//span[@id="select2-idiva-container"]').click()
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-idiva-results"]//li[20]').click()    #seleziono iva come non soggetta
        self.find(By.XPATH, '//button[@class="btn btn-primary pull-right"]').click()    #click su aggiungi
        self.wait_loader()
        sleep(1)

        totale=self.find(By.XPATH, '//tbody//tr[2]//td[9]').text
        self.assertEqual(totale, "2,00 €")     #check se è presente la marca da bollo
        #elimino fattura
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

        impostazione=self.find(By.XPATH, '//input[@id="setting11"]')
        impostazione.clear()
        impostazione.send_keys("77,47")   #imposto la soglia minima a 77,47 euro
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

    def dicitura_fissa_fattura(self):
        wait = WebDriverWait(self.driver, 20)
        self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr[1]//td[2]').click()    #apro prima fattura
        self.wait_loader()

        self.find(By.XPATH, '//a[@id="print-button_p"]').click()    #stampa fattura
        sleep(2)

        self.driver.switch_to.window(self.driver.window_handles[1]) #cambia scheda
        sleep(2)
        #prima riga
        prima_riga=self.find(By.XPATH, '(//div[@id="viewer"]//span)[73]').text
        self.assertEqual(prima_riga, "Ai sensi del D.Lgs. 196/2003 Vi informiamo che i Vs. dati saranno utilizzati esclusivamente per i ﬁni connessi ai rapporti commerciali tra di noi in essere. Contributo CONAI assolto ove dovuto - Vi")
        #seconda riga
        seconda_riga=self.find(By.XPATH, '(//div[@id="viewer"]//span)[74]').text
        self.assertEqual(seconda_riga, "preghiamo di controllare i Vs. dati anagraﬁci, la P. IVA e il Cod. Fiscale. Non ci riteniamo responsabili di eventuali errori.Copia della fattura elettronica disponibile nella Sua area riservata")
        #terza riga
        terza_riga=self.find(By.XPATH, '(//div[@id="viewer"]//span)[75]').text
        self.assertEqual(terza_riga, "dell’Agenzia delle Entrate")

        self.driver.close() #chiude scheda
        self.driver.switch_to.window(self.driver.window_handles[0]) #torna alla prima
        sleep(2)

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-9"]').click() #apro Fatturazione
        sleep(1)

        dicitura=self.find(By.XPATH, '//iframe[@class="cke_wysiwyg_frame cke_reset"]')
        dicitura.click()
        dicitura.send_keys("test")

        #crea fattura
        self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.find(By.XPATH, '//button[@class="btn btn-primary bound clickable"]').click()   #click su +
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-idanagrafica_add-container"]').click() #seleziono Cliente come anagrafica
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente")
        sleep(2)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(Keys.ENTER)
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click() #click su aggiungi
        self.wait_loader()

        #aggiungi riga
        self.find(By.XPATH, '//a[@class="btn btn-primary"]').click() #click su aggiungi riga
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("Test")    #scrivo "Test" come descrizione della riga
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("1") #scrivo 1 come prezzo unitario
        self.find(By.XPATH, '//button[@class="btn btn-primary pull-right"]').click() #click su aggiungi
        sleep(1)

        #cambio stato
        self.find(By.XPATH, '//span[@id="select2-idstatodocumento-container"]').click()
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-idstatodocumento-results"]//li[2]').click() #imposto stato "Emessa"
        self.find(By.XPATH, '//button[@id="save"]').click() #click su salva
        self.wait_loader()

        self.find(By.XPATH, '//a[@id="print-button_p"]').click()    #stampa fattura
        sleep(2)

        self.driver.switch_to.window(self.driver.window_handles[1]) #cambia scheda
        sleep(2)

        seconda_riga=self.find(By.XPATH, '(//div[@id="viewer"]//span)[84]').text
        self.assertEqual(seconda_riga, "preghiamo di controllare i Vs. dati anagraﬁci, ltesta P. IVA e il Cod. Fiscale. Non ci riteniamo responsabili di eventuali errori.")
        self.driver.close() #chiude scheda
        self.driver.switch_to.window(self.driver.window_handles[0]) #torna alla prima
        sleep(2)

        #elimina fattura
        self.find(By.XPATH, '//a[@id="elimina"]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()   #click di conferma
        self.wait_loader()
        #torna alle impostazioni di prima
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-9"]').click() #apro Fatturazione
        sleep(3)

        dicitura=self.find(By.XPATH, '//iframe[@class="cke_wysiwyg_frame cke_reset"]')
        dicitura.click()
        dicitura.clear()    #clear non funziona
        sleep(2)

        dicitura.send_keys("Ai sensi del D.Lgs. 196/2003 Vi informiamo che i Vs. dati saranno utilizzati esclusivamente per i fini connessi ai rapporti commerciali tra di noi in essere. Contributo CONAI assolto ove dovuto - Vi preghiamo di controllare i Vs. dati anagrafici, la P. IVA e il Cod. Fiscale. Non ci riteniamo responsabili di eventuali errori.")
        sleep(2)


    def ritenuta_previdenziale_predefinita(self):
        wait = WebDriverWait(self.driver, 20)
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-9"]').click() #apro Fatturazione
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-setting82-container"]').click()
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-setting82-results"]//li[1]').click() #seleziono ritenuta previdenziale
        sleep(2)

        self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.find(By.XPATH, '//button[@class="btn btn-primary bound clickable"]').click()   #click su +
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-idanagrafica_add-container"]').click() #seleziono Cliente come anagrafica
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente")
        sleep(2)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(Keys.ENTER)
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click() #click su aggiungi
        self.wait_loader()

        ritenuta_element=self.find(By.XPATH, '//span[@id="select2-id_ritenuta_contributi-container"]')  #check se è stata aggiunta la ritenuta
        ritenuta = ritenuta_element.get_attribute("title")
        self.assertEqual(ritenuta, "Ritenuta Previdenziale di Prova - 80.00% sul 60.00% imponibile")
        #elimino fattura
        self.find(By.XPATH, '//a[@id="elimina"]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click() #click di conferma
        self.wait_loader()
        #torno alle impostazioni di prima
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-9"]').click() #apro Fatturazione
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-setting82-container"]//span').click()
        sleep(2)

        self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.find(By.XPATH, '//button[@class="btn btn-primary bound clickable"]').click()   #click su +
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-idanagrafica_add-container"]').click() #seleziono Cliente come anagrafica
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente")
        sleep(2)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(Keys.ENTER)
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click() #click su aggiungi
        self.wait_loader()

        self.find(By.XPATH, '//span[@id="select2-id_ritenuta_contributi-container"]').click()
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-id_ritenuta_contributi-results"]//li[1]')))   #check se la ritenuta non è stata selezionata
        #elimino fattura
        self.find(By.XPATH, '//a[@id="elimina"]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click() #click di conferma
        self.wait_loader()


    def addebita_marca_bollo(self):
        wait = WebDriverWait(self.driver, 20)
        self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.find(By.XPATH, '//button[@class="btn btn-primary bound clickable"]').click()   #click su +
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-idanagrafica_add-container"]').click() #seleziono Cliente come anagrafica
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente", Keys.ENTER)
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click() #click su aggiungi
        self.wait_loader()

        self.find(By.XPATH, '(//label[@class="btn btn-default active"])[3]').click()    #disattiva bollo automatico
        sleep(1)

        self.find(By.XPATH, '//a[@class="btn btn-primary"]').click()    #aggiungi riga
        sleep(2)

        #descrizione
        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("test")
        #prezzo unitario
        prezzo_unitario=self.find(By.XPATH, '//input[@id="prezzo_unitario"]')
        prezzo_unitario.clear()
        prezzo_unitario.send_keys("80")
        #iva
        self.find(By.XPATH, '//span[@id="select2-idiva-container"]').click()
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-idiva-results"]//li[20]').click()    #seleziono iva come non soggetta
        self.find(By.XPATH, '//button[@class="btn btn-primary pull-right"]').click()    #click su aggiungi
        self.wait_loader()
        


    def descrizione_marca_bollo(self):
        wait = WebDriverWait(self.driver, 20)
        self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.find(By.XPATH, '//button[@class="btn btn-primary bound clickable"]').click()   #click su +
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-idanagrafica_add-container"]').click() #seleziono Cliente come anagrafica
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente", Keys.ENTER)
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click() #click su aggiungi
        self.wait_loader()

        self.find(By.XPATH, '//a[@class="btn btn-primary"]').click()    #aggiungi riga
        sleep(2)

        #descrizione
        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("test")
        #prezzo unitario
        prezzo_unitario=self.find(By.XPATH, '//input[@id="prezzo_unitario"]')
        prezzo_unitario.clear()
        prezzo_unitario.send_keys("80")
        #iva
        self.find(By.XPATH, '//span[@id="select2-idiva-container"]').click()
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-idiva-results"]//li[20]').click()    #seleziono iva come non soggetta
        self.find(By.XPATH, '//button[@class="btn btn-primary pull-right"]').click()    #click su aggiungi
        self.wait_loader()
        sleep(1)

        descrizione=self.find(By.XPATH, '(//tbody//tr[2]//td[3])[1]').text
        self.assertEqual(descrizione[0:30], "Rimborso spese marche da bollo")
        #elimino fattura
        self.find(By.XPATH, '//a[@id="elimina"]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()   #click di conferma
        self.wait_loader()

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-9"]').click() #apro Fatturazione
        sleep(1)

        descrizione=self.find(By.XPATH, '(//tbody//tr[2]//td[3])[1]').text
        self.assertEqual(descrizione[0:3], "Test")
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

        self.find(By.XPATH, '//a[@class="btn btn-primary"]').click()    #aggiungi riga
        sleep(2)

        #descrizione
        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("test")
        #prezzo unitario
        prezzo_unitario=self.find(By.XPATH, '//input[@id="prezzo_unitario"]')
        prezzo_unitario.clear()
        prezzo_unitario.send_keys("80")
        #iva
        self.find(By.XPATH, '//span[@id="select2-idiva-container"]').click()
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-idiva-results"]//li[20]').click()    #seleziono iva come non soggetta
        self.find(By.XPATH, '//button[@class="btn btn-primary pull-right"]').click()    #click su aggiungi
        self.wait_loader()
        sleep(1)

        descrizione_element = self.find(By.XPATH, '(//tbody//tr[2]//td[3])[1]')
        descrizione = descrizione_element.get_attribute("text")
        self.assertEqual(descrizione, "Test")   #controllo se la descrizione è cambiata
        #elimino fattura
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

        impostazione=self.find(By.XPATH, '//input[@id="setting89"]')    #scrivo "Rimborso spese marche da bollo" come descrizione
        impostazione.clear()
        impostazione.send_keys("Rimborso spese marche da bollo")
        sleep(2)


    def conto_marca_bollo(self):
        wait = WebDriverWait(self.driver, 20)
        self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.find(By.XPATH, '//button[@class="btn btn-primary bound clickable"]').click()   #click su +
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-idanagrafica_add-container"]').click() #seleziono Cliente come anagrafica
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente", Keys.ENTER)
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click() #click su aggiungi
        self.wait_loader()

        self.find(By.XPATH, '//a[@class="btn btn-primary"]').click()    #aggiungi riga
        sleep(2)

        #descrizione
        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("test")
        #prezzo unitario
        prezzo_unitario=self.find(By.XPATH, '//input[@id="prezzo_unitario"]')
        prezzo_unitario.clear()
        prezzo_unitario.send_keys("80")
        #iva
        self.find(By.XPATH, '//span[@id="select2-idiva-container"]').click()
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-idiva-results"]//li[20]').click()    #seleziono iva come non soggetta
        self.find(By.XPATH, '//button[@class="btn btn-primary pull-right"]').click()    #click su aggiungi
        self.wait_loader()
        
        conto=self.find(By.XPATH, '//tbody//tr[2]//td[3]//small').text  #check conto
        self.assertEqual(conto, "Rimborso spese marche da bollo")
        #elimino fattura
        self.find(By.XPATH, '//a[@id="elimina"]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()   #click di conferma
        self.wait_loader()

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-9"]').click() #apro Fatturazione
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-setting90-container"]').click()    #cambia conto
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-setting90-results"]//li[1]').click()
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

        self.find(By.XPATH, '//a[@class="btn btn-primary"]').click()    #aggiungi riga
        sleep(2)

        #descrizione
        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("test")
        #prezzo unitario
        prezzo_unitario=self.find(By.XPATH, '//input[@id="prezzo_unitario"]')
        prezzo_unitario.clear()
        prezzo_unitario.send_keys("80")
        #iva
        self.find(By.XPATH, '//span[@id="select2-idiva-container"]').click()
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-idiva-results"]//li[20]').click()    #seleziono iva come non soggetta
        self.find(By.XPATH, '//button[@class="btn btn-primary pull-right"]').click()    #click su aggiungi
        self.wait_loader()
        
        conto=self.find(By.XPATH, '//tbody//tr[2]//td[3]//small').text  #check conto
        self.assertEqual(conto, "Ricavi merci c/to vendite")
        #elimino fattura
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

        self.find(By.XPATH, '//span[@id="select2-setting90-container"]').click()    #cambia conto
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-setting90-results"]//li[6]').click()
        sleep(2)


    def iva_lettere_intento(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Anagrafiche")
        self.wait_loader() 

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Ragione-sociale"]/input'))).send_keys("Cliente", Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//tbody//tr[1]//td[2]').click()
        self.wait_loader() 

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="control-sidebar-button"]'))).click()
        self.find(By.XPATH, '//a[@id="link-tab_25"]').click()
        self.find(By.XPATH, '//div[@id="tab_25"]//i[@class="fa fa-plus"]').click()
        sleep(1)

        # Aggiunta dichiarazione di intento
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="numero_protocollo"]'))).send_keys("012345678901234567890123")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="data_protocollo"]'))).send_keys("06/08/2024")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="numero_progressivo"]'))).send_keys("001")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="data_inizio"]'))).send_keys("06/08/2024")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="data_fine"]'))).send_keys("06/10/2024")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="massimale"]'))).send_keys("50000")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="data_emissione"]'))).send_keys("06/08/2024", Keys.ENTER)
        self.find(By.XPATH, '(//button[@class="btn btn-primary"])[2]').click()
        self.wait_loader()

        self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.find(By.XPATH, '//i[@class="fa fa-plus"]').click() #crea fattura
        self.wait_modal()

        self.find(By.XPATH, '//span[@id="select2-idanagrafica_add-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente", Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click()
        self.wait_loader()

        self.find(By.XPATH, '//a[@class="btn btn-primary"]').click()    #aggiungi riga
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("prova per dichiarazione")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="qta"]'))).send_keys("100")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("1")
        self.find(By.XPATH, '//button[@class="btn btn-primary pull-right"]').click()
        sleep(1)

        iva=self.find(By.XPATH, '//tbody[@id="righe"]//tr[1]//td[8]//small').text
        self.assertEqual(iva, "Non imp. art. 8 c.1 lett. c DPR 633/1972 (I)  (N3.5)")
        #elimina fattura
        self.find(By.XPATH, '//a[@id="elimina"]').click()
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()
        #elimina dichiarazione
        self.navigateTo("Anagrafiche")
        self.wait_loader() 

        self.find(By.XPATH, '//tbody//tr[1]//td[2]').click()
        self.wait_loader() 

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="control-sidebar-button"]'))).click()
        self.find(By.XPATH, '//a[@id="link-tab_25"]').click()
        sleep(2)

        self.find(By.XPATH, '(//div[@id="tab_25"]//tr[1]//td[2])[2]').click()
        sleep(1)

        self.find(By.XPATH, '//a[@class="btn btn-danger ask "]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-9"]').click() #apro Fatturazione
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-setting94-container"]').click()    #cambio iva
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-setting94-results"]//li[1]').click() #iva 311
        sleep(2)

        self.navigateTo("Anagrafiche")
        self.wait_loader() 

        self.find(By.XPATH, '//tbody//tr[1]//td[2]').click()
        self.wait_loader() 

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="control-sidebar-button"]'))).click()
        self.find(By.XPATH, '//a[@id="link-tab_25"]').click()
        self.find(By.XPATH, '//div[@id="tab_25"]//i[@class="fa fa-plus"]').click()
        sleep(1)

        # Aggiunta dichiarazione di intento
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="numero_protocollo"]'))).send_keys("012345678901234567890123")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="data_protocollo"]'))).send_keys("06/08/2024")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="numero_progressivo"]'))).send_keys("001")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="data_inizio"]'))).send_keys("06/08/2024")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="data_fine"]'))).send_keys("06/10/2024")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="massimale"]'))).send_keys("50000")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="data_emissione"]'))).send_keys("06/08/2024", Keys.ENTER)
        self.find(By.XPATH, '(//button[@class="btn btn-primary"])[2]').click()
        self.wait_loader()

        self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.find(By.XPATH, '//i[@class="fa fa-plus"]').click() #crea fattura
        self.wait_modal()

        self.find(By.XPATH, '//span[@id="select2-idanagrafica_add-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente", Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click()
        self.wait_loader()

        self.find(By.XPATH, '//a[@class="btn btn-primary"]').click()    #aggiungi riga
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("prova per dichiarazione")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="qta"]'))).send_keys("100")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("1")
        self.find(By.XPATH, '//button[@class="btn btn-primary pull-right"]').click()
        sleep(1)

        iva=self.find(By.XPATH, '//tbody[@id="righe"]//tr[1]//td[8]//small').text
        self.assertEqual(iva, "Art. 2 c. 2, n. 4 DPR 633/1972 (I)  (N3.6)")
        #elimina fattura
        self.find(By.XPATH, '//a[@id="elimina"]').click()
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()
        #elimina dichiarazione
        self.navigateTo("Anagrafiche")
        self.wait_loader() 

        self.find(By.XPATH, '//tbody//tr[1]//td[2]').click()
        self.wait_loader() 

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="control-sidebar-button"]'))).click()
        self.find(By.XPATH, '//a[@id="link-tab_25"]').click()
        sleep(2)

        self.find(By.XPATH, '(//div[@id="tab_25"]//tr[1]//td[2])[2]').click()
        sleep(1)

        self.find(By.XPATH, '//a[@class="btn btn-danger ask "]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()

        self.navigateTo("Anagrafiche")
        self.wait_loader() 

        self.find(By.XPATH, '//th[@id="th_Ragione-sociale"]//i').click()    #elimina ricerca
        #torna alle impostazioni di prima
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-9"]').click() #apro Fatturazione
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-setting94-container"]').click()    #cambio iva
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-setting94-results"]//li[9]').click() #iva 307
        sleep(2)


    def prezzi_vendita_comprensivi_iva(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-9"]').click() #apro Fatturazione
        sleep(1)

        self.find(By.XPATH, '(//label[@class="btn btn-default active"])[2]').click()    #attivo impostazione
        sleep(2)

        self.expandSidebar("Magazzino")
        self.navigateTo("Articoli")
        self.wait_loader()

        self.find(By.XPATH, '//button[@class="btn btn-primary bound clickable"]').click() #click su +
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione"]'))).send_keys("Prova") #descrizione
        self.find(By.XPATH, '//button[@class="btn btn-tool"]').click()
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_vendita"]'))).send_keys("12") #prezzo di vendita
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="qta"]'))).send_keys("1")   #quantità    
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click()   #click su aggiungi
        self.wait_loader()

        self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.find(By.XPATH, '//button[@class="btn btn-primary bound clickable"]').click()   #click su +
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-idanagrafica_add-container"]').click() #seleziono Cliente come anagrafica
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente", Keys.ENTER)
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click() #click su aggiungi
        self.wait_loader()

        self.find(By.XPATH, '//span[@id="select2-id_articolo-container"]').click()  #aggiungo articolo
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Prova")
        sleep(2)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//button[@class="btn btn-primary tip tooltipstered"]').click() #click su aggiungi
        sleep(2)

        prezzo_element = self.find(By.XPATH, '//tbody//tr[1]//td[6]//input')    #check valore del prezzo
        prezzo = prezzo_element.get_attribute("value")
        self.assertEqual(prezzo, "12,00")
        self.find(By.XPATH, '//a[@id="print-button_p"]').click()    #stampa fattura
        sleep(1)

        self.driver.switch_to.window(self.driver.window_handles[1]) #cambia scheda
        sleep(2)

        prezzo=self.find(By.XPATH, '(//div[@id="viewer"]//span)[44]').text  #check prezzo in stampa
        self.assertEqual(prezzo, "12,00 €")
        self.driver.close() #chiude scheda
        self.driver.switch_to.window(self.driver.window_handles[0]) #torna alla prima
        sleep(2)

        #torno alle impostazioni di prima
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-9"]').click() #apro Fatturazione
        sleep(1)

        self.find(By.XPATH, '(//label[@class="btn btn-default active"])[2]').click()    #disattivo impostazione
        sleep(2)

        self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr//td[2]').click() #apro prima fattura
        self.wait_loader()

        prezzo_element = self.find(By.XPATH, '//tbody//tr[1]//td[6]//input')    #check valore del prezzo
        prezzo = prezzo_element.get_attribute("value")
        self.assertEqual(prezzo, "9,84")
        self.find(By.XPATH, '//a[@id="print-button_p"]').click()    #stampa fattura
        sleep(1)

        self.driver.switch_to.window(self.driver.window_handles[1]) #cambia scheda
        sleep(2)

        prezzo=self.find(By.XPATH, '(//div[@id="viewer"]//span)[44]').text  #check prezzo in stampa
        self.assertEqual(prezzo, "9,84 €")
        self.driver.close() #chiude scheda
        self.driver.switch_to.window(self.driver.window_handles[0]) #torna alla prima
        sleep(2)

        self.find(By.XPATH, '//a[@id="elimina"]').click()   #elimina fattura
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()   #click di conferma
        self.wait_loader()

        self.expandSidebar("Magazzino")
        self.navigateTo("Articoli")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input'))).send_keys('Prova', Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//tbody//tr[2]//td[2]').click()
        self.wait_loader()

        #elimino articolo
        self.find(By.XPATH, '//a[@class="btn btn-danger ask"]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()

        self.find(By.XPATH, '//th[@id="th_Descrizione"]/i[@class="deleteicon fa fa-times"]').click()    #cancella ricerca
        sleep(1)

        self.navigateTo("Impianti")
        self.wait_loader()

    def liquidazione_iva(self):
        wait = WebDriverWait(self.driver, 20)
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-9"]').click() #apro Fatturazione
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-setting128-container"]').click()   #cambio a trimestrale
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-setting128-results"]//li[2]').click()
        sleep(2)

        self.navigateTo("Contabilità")
        self.navigateTo("Stampe contabili")
        self.wait_loader()

        self.find(By.XPATH, '(//div[@class="row"]//div[3]//button)[1]').click()
        sleep(2)

        self.find(By.XPATH, '//span[@id="select2-periodo-container"]').click()  #click su periodo
        sleep(1)

        periodo=self.find(By.XPATH, '//ul[@id="select2-periodo-results"]//li[2]').text
        self.assertEqual(periodo, "1° Trimestre 2024")
        self.find(By.XPATH, '//button[@class="close"]').click() #click su chiudi
        sleep(1)

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-9"]').click() #apro Fatturazione
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-setting128-container"]').click()   #cambio a mensile
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-setting128-results"]//li[1]').click()
        sleep(2)

        self.navigateTo("Contabilità")
        self.navigateTo("Stampe contabili")
        self.wait_loader()

        self.find(By.XPATH, '(//div[@class="row"]//div[3]//button)[1]').click()
        sleep(2)

        self.find(By.XPATH, '//span[@id="select2-periodo-container"]').click()  #click su periodo
        sleep(1)

        periodo=self.find(By.XPATH, '//ul[@id="select2-periodo-results"]//li[2]').text
        self.assertEqual(periodo, "gennaio 2024")
        self.find(By.XPATH, '//button[@class="close"]').click() #click su chiudi
        sleep(1)


    def descrizione_fattura_pianificata(self):
        wait = WebDriverWait(self.driver, 20)
        self.expandSidebar("Vendite")
        self.navigateTo("Contratti")
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr[2]//td[2]').click()    #apri contratto
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="control-sidebar-button"]'))).click()  #apro barra dei plugin
        sleep(1)

        self.find(By.XPATH, '//a[@id="link-tab_26"]').click()   #plugin pianificazione fatturazione
        sleep(2)

        self.find(By.XPATH, '//button[@id="pianifica"]').click()    #click su pianifica
        sleep(2)

        self.find(By.XPATH, '(//div[@class="nav-tabs-custom"]//a)[2]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@id="btn_procedi"]').click()  #click su procedi
        self.wait_loader()

        self.find(By.XPATH, '//button[@class="btn btn-primary btn-sm "]').click()
        sleep(2)

        descrizione=self.find(By.XPATH, '//textarea[@id="note"]').text  #check descrizione
        self.assertEqual(descrizione, "Canone 1 del contratto numero 2")
        self.find(By.XPATH, '//button[@class="close"]').click() #click su chiudi
        sleep(1)
        #elimina fattura pianificata
        self.find(By.XPATH, '//button[@class="ask btn btn-danger pull-right tip tooltipstered"]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-9"]').click() #apro Fatturazione
        sleep(1)

        descrizione=self.find(By.XPATH, '//input[@id="setting138"]')
        descrizione.clear() 
        descrizione.send_keys("prova")
        sleep(2)

        self.expandSidebar("Vendite")
        self.navigateTo("Contratti")
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr[2]//td[2]').click()    #apri contratto
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="control-sidebar-button"]'))).click()  #apro barra dei plugin
        sleep(1)

        self.find(By.XPATH, '//a[@id="link-tab_26"]').click()   #plugin pianificazione fatturazione
        sleep(2)

        self.find(By.XPATH, '//button[@id="pianifica"]').click()    #click su pianifica
        sleep(2)

        self.find(By.XPATH, '(//div[@class="nav-tabs-custom"]//a)[2]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@id="btn_procedi"]').click()  #click su procedi
        self.wait_loader()

        self.find(By.XPATH, '//button[@class="btn btn-primary btn-sm "]').click()
        sleep(2)

        descrizione=self.find(By.XPATH, '//textarea[@id="note"]').text  #check descrizione
        self.assertEqual(descrizione, "prova")
        self.find(By.XPATH, '//button[@class="close"]').click() #click su chiudi
        sleep(1)
        #elimina fattura pianificata
        self.find(By.XPATH, '//button[@class="ask btn btn-danger pull-right tip tooltipstered"]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()
        #torno alle impostazioni di prima
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-9"]').click() #apro Fatturazione
        sleep(1)

        descrizione=self.find(By.XPATH, '//input[@id="setting138"]')
        descrizione.clear() 
        descrizione.send_keys("Canone {rata} del contratto numero {numero}")
        sleep(2)

    def bloccare_prezzi_inferiori_minimo_vendita(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-9"]').click() #apro Fatturazione
        sleep(1)

        self.find(By.XPATH, '(//label[@class="btn btn-default active"])[3]').click()    #attivo impostazione
        sleep(2)

        self.expandSidebar("Magazzino")
        self.navigateTo("Articoli")
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr[1]//td[2]').click()    #apri primo articolo
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="minimo_vendita"]'))).send_keys("5")    #5 come prezzo minimo
        self.find(By.XPATH, '//button[@id="save"]').click() #salva modifica
        self.wait_loader()

        self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.find(By.XPATH, '//i[@class="fa fa-plus"]').click() #crea fattura
        self.wait_modal()

        self.find(By.XPATH, '//span[@id="select2-idanagrafica_add-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente", Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click()
        self.wait_loader()

        #aggiungi articolo
        self.find(By.XPATH, '//span[@id="select2-id_articolo-container"]').click()
        sleep(1)

        self.find(By.XPATH, '//ul[@class="select2-results__options select2-results__options--nested"]//li[1]').click()
        self.find(By.XPATH, '//button[@class="btn btn-primary tip tooltipstered"]').click() #click su aggiungi
        sleep(2)




    def fattura_attivita_collegate_contratti(self):
        wait = WebDriverWait(self.driver, 20)
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-9"]').click() #apro Fatturazione
        sleep(1)

        self.find(By.XPATH, '(//label[@class="btn btn-default active"])[4]').click()    #attivo impostazione
        sleep(2)

        #crea contratto
        self.expandSidebar("Vendite")
        self.navigateTo("Contratti")
        self.wait_loader()

        self.find(By.XPATH, '//button[@class="btn btn-primary bound clickable"]').click()
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="nome"]'))).send_keys("Prova")
        self.find(By.XPATH, '//span[@id="select2-idanagrafica-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente")
        sleep(2)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(Keys.ENTER)
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="data_accettazione"]'))).send_keys("01/01/2024")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="data_conclusione"]'))).send_keys("31/12/2024")
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click()
        self.wait_loader()
        #aggiungi riga
        self.find(By.XPATH, '//a[@class="btn btn-primary"]').click() #click su aggiungi riga
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("Test")    #scrivo "Test" come descrizione della riga
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("1") #scrivo 1 come prezzo unitario
        self.find(By.XPATH, '//button[@class="btn btn-primary pull-right"]').click() #click su aggiungi
        sleep(1)

        #cambio stato
        self.find(By.XPATH, '//span[@id="select2-idstato-container"]').click()
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-idstato-results"]//li[6]').click() #imposto stato "In lavorazione"
        self.find(By.XPATH, '//button[@id="save"]').click() #click su salva
        self.wait_loader()

        #crea attività
        self.navigateTo("Attività")
        self.wait_loader()

        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click()  #click su +
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-idanagrafica-container"]').click() #seleziono Cliente come anagrafica
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-dropdown select2-dropdown--below"]//input'))).send_keys("Cliente")
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-dropdown select2-dropdown--below"]//input'))).send_keys(Keys.ENTER)
        self.find(By.XPATH, '//span[@id="select2-idtipointervento-container"]').click() #seleziono Generico come tipo di intervento
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys("Generico")
        sleep(1)

        self.find(By.XPATH, '//li[@class="select2-results__option select2-results__option--highlighted"]').click()  #click su primo risultato
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//iframe[@class="cke_wysiwyg_frame cke_reset"])[1]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//iframe[@class="cke_wysiwyg_frame cke_reset"])[1]'))).send_keys("Test")   #scrivo "Test" come richiesta
        self.find(By.XPATH, '//span[@id="select2-idcontratto-container"]').click()  #aggiungi contratto
        sleep(2)

        self.find(By.XPATH, '//ul[@id="select2-idcontratto-results"]//li[2]').click()
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click()   #click su Aggiungi
        self.wait_loader()

        self.find(By.XPATH, '//span[@id="select2-nuovo_tecnico-container"]').click()    #aggiungi sessione
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-nuovo_tecnico-results"]//li[2]').click()
        self.find(By.XPATH, '//button[@class="btn btn-primary btn-block"]').click()
        sleep(2)

        self.find(By.XPATH, '//span[@id="select2-idstatointervento-container"]').click()    #click su stato
        sleep(1)

        self.find(By.XPATH, '(//input[@class="select2-search__field"])[3]').send_keys("Completato", Keys.ENTER) #seleziono Completato come nuovo stato
        sleep(1)

        self.find(By.XPATH, '//button[@id="save"]').click() #click su salva
        self.wait_loader()

        self.navigateTo("Attività")
        self.wait_loader()
        
        self.find(By.XPATH, '//tbody//tr[1]//td[1]').click()
        self.find(By.XPATH, '//button[@class="btn btn-primary btn-lg dropdown-toggle dropdown-toggle-split"]').click() #apro azioni di gruppo
        wait.until(EC.visibility_of_element_located((By.XPATH, '//a[@data-op="crea_fattura"]'))).click()    #click su crea fattura
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-raggruppamento-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente")    #seleziono cliente
        self.find(By.XPATH, '//ul[@id="select2-raggruppamento-results"]').click()
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-warning"]').click()  #click di conferma
        self.wait_loader()

        stato=self.find(By.XPATH, '//tbody//tr[1]//td[7]//div').text    #controllo se l'attività è stata fatturata
        self.assertEqual(stato, "Fatturato")
        self.find(By.XPATH, '//tbody//tr[1]//td[2]').click()    #apro attività
        self.wait_loader()
        #elimino attività
        self.find(By.XPATH, '//a[@class="btn btn-danger ask"]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()
        #elimino fattura
        self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr[1]//td[2]').click() #apro prima fattura
        self.wait_loader()

        self.find(By.XPATH, '//a[@id="elimina"]').click() #elimina fattura
        self.wait_loader()

        #torno alle impostazioni di prima
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-9"]').click() #apro Fatturazione
        sleep(1)

        self.find(By.XPATH, '(//label[@class="btn btn-default active"])[4]').click()    #disattivo impostazione
        sleep(2)

        #crea attività
        self.navigateTo("Attività")
        self.wait_loader()

        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click()  #click su +
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-idanagrafica-container"]').click() #seleziono Cliente come anagrafica
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-dropdown select2-dropdown--below"]//input'))).send_keys("Cliente")
        sleep(2)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-dropdown select2-dropdown--below"]//input'))).send_keys(Keys.ENTER)
        self.find(By.XPATH, '//span[@id="select2-idtipointervento-container"]').click() #seleziono Generico come tipo di intervento
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys("Generico")
        sleep(1)

        self.find(By.XPATH, '//li[@class="select2-results__option select2-results__option--highlighted"]').click()  #click su primo risultato
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//iframe[@class="cke_wysiwyg_frame cke_reset"])[1]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//iframe[@class="cke_wysiwyg_frame cke_reset"])[1]'))).send_keys("Test")   #scrivo "Test" come richiesta
        self.find(By.XPATH, '//span[@id="select2-idcontratto-container"]').click()  #aggiungi contratto
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-idcontratto-results"]//li[2]').click()
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click()   #click su Aggiungi
        self.wait_loader()

        self.find(By.XPATH, '//span[@id="select2-nuovo_tecnico-container"]').click()    #aggiungi sessione
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-nuovo_tecnico-results"]//li[2]').click()
        self.find(By.XPATH, '//button[@class="btn btn-primary btn-block"]').click()
        sleep(2)

        self.find(By.XPATH, '//span[@id="select2-idstatointervento-container"]').click()    #click su stato
        sleep(1)

        self.find(By.XPATH, '(//input[@class="select2-search__field"])[3]').send_keys("Completato", Keys.ENTER) #seleziono Completato come nuovo stato
        sleep(1)

        self.find(By.XPATH, '//button[@id="save"]').click() #click su salva
        self.wait_loader()

        self.navigateTo("Attività")
        self.wait_loader()
        
        self.find(By.XPATH, '//tbody//tr[1]//td[1]').click()
        self.find(By.XPATH, '//button[@class="btn btn-primary btn-lg dropdown-toggle dropdown-toggle-split"]').click() #apro azioni di gruppo
        wait.until(EC.visibility_of_element_located((By.XPATH, '//a[@data-op="crea_fattura"]'))).click()    #click su crea fattura
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-raggruppamento-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente")    #seleziono cliente
        self.find(By.XPATH, '//ul[@id="select2-raggruppamento-results"]').click()
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-warning"]').click()  #click di conferma
        self.wait_loader()

        stato=self.find(By.XPATH, '//tbody//tr[1]//td[7]//div').text    #controllo se l'attività non è stata fatturata
        self.assertEqual(stato, "Completato")
        self.find(By.XPATH, '//tbody//tr[1]//td[2]').click()    #apro attività
        self.wait_loader()
        #elimino attività
        self.find(By.XPATH, '//a[@class="btn btn-danger ask"]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()
        #elimino contratto
        self.expandSidebar("Vendite")
        self.navigateTo("Contratti")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]//input'))).send_keys("Prova", Keys.ENTER)
        sleep(2)

        self.find(By.XPATH, '//tbody//tr[2]//td[2]').click()    #apro contratto
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_0"]//a[@class="btn btn-danger ask"]'))).click()  #elimina contratto 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))).click()
        self.wait_loader()

        self.find(By.XPATH, '//th[@id="th_Nome"]//i').click()   #cancella ricerca
        sleep(1)

    def fattura_attivita_collegate_ordini(self):
        wait = WebDriverWait(self.driver, 20)
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-9"]').click() #apro Fatturazione
        sleep(1)

        self.find(By.XPATH, '(//label[@class="btn btn-default active"])[6]').click()    #attivo impostazione
        sleep(2)

        #crea ordine
        self.expandSidebar("Vendite")
        self.navigateTo("Ordini cliente")
        self.wait_loader()

        self.find(By.XPATH, '//button[@class="btn btn-primary bound clickable"]').click()   #click su tasto +
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-idanagrafica-container"]').click()     #scelta di "Cliente" come anagrafica per l'ordine
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys('Cliente')
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(Keys.ENTER)
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click()   #click su tasto aggiungi
        self.wait_loader()
        #aggiungi articolo
        self.find(By.XPATH, '//span[@id="select2-id_articolo-container"]').click()
        sleep(1)

        self.find(By.XPATH, '//ul[@class="select2-results__options select2-results__options--nested"]//li[1]').click()
        self.find(By.XPATH, '//button[@class="btn btn-primary tip tooltipstered"]').click() #click su aggiungi
        sleep(2)
        #cambio stato
        self.find(By.XPATH, '//span[@id="select2-idstatoordine-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Accettato", Keys.ENTER)
        self.find(By.XPATH, '//button[@id="save"]').click()
        self.wait_loader()
        #crea attività
        self.navigateTo("Attività")
        self.wait_loader()

        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click()  #click su +
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-idanagrafica-container"]').click() #seleziono Cliente come anagrafica
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-dropdown select2-dropdown--below"]//input'))).send_keys("Cliente")
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-dropdown select2-dropdown--below"]//input'))).send_keys(Keys.ENTER)
        self.find(By.XPATH, '//span[@id="select2-idtipointervento-container"]').click() #seleziono Generico come tipo di intervento
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys("Generico")
        sleep(1)

        self.find(By.XPATH, '//li[@class="select2-results__option select2-results__option--highlighted"]').click()  #click su primo risultato
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//iframe[@class="cke_wysiwyg_frame cke_reset"])[1]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//iframe[@class="cke_wysiwyg_frame cke_reset"])[1]'))).send_keys("Test")   #scrivo "Test" come richiesta
        self.find(By.XPATH, '//span[@id="select2-idordine-container"]').click() #aggiungo ordine
        sleep(2)

        self.find(By.XPATH, '//ul[@id="select2-idordine-results"]//li[2]').click()
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click()   #click su Aggiungi
        self.wait_loader()

        self.find(By.XPATH, '//span[@id="select2-nuovo_tecnico-container"]').click()    #aggiungi sessione
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-nuovo_tecnico-results"]//li[2]').click()
        self.find(By.XPATH, '//button[@class="btn btn-primary btn-block"]').click()
        sleep(2)
    
        self.find(By.XPATH, '//span[@id="select2-idstatointervento-container"]').click()    #click su stato
        sleep(1)

        self.find(By.XPATH, '(//input[@class="select2-search__field"])[3]').send_keys("Completato", Keys.ENTER) #seleziono Completato come nuovo stato
        self.find(By.XPATH, '//button[@id="save"]').click()
        self.wait_loader()

        self.navigateTo("Attività")
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr[1]//td[1]').click() #seleziono attività 
        self.find(By.XPATH, '//button[@class="btn btn-primary btn-lg dropdown-toggle dropdown-toggle-split"]').click() #apro azioni di gruppo
        wait.until(EC.visibility_of_element_located((By.XPATH, '//a[@data-op="crea_fattura"]'))).click()    #click su crea fattura
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-raggruppamento-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente")    #seleziono cliente
        self.find(By.XPATH, '//ul[@id="select2-raggruppamento-results"]').click()
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-warning"]').click()  #click di conferma
        self.wait_loader()

        stato=self.find(By.XPATH, '//tbody//tr[1]//td[7]').text #controllo se lo stato è passato a "Fatturato"
        self.assertEqual(stato, "Fatturato")
        #elimina fattura
        self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr[1]//td[2]').click()
        self.wait_loader()

        self.find(By.XPATH, '//a[@id="elimina"]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()   #click di conferma
        self.wait_loader()
        #elimina ordine
        self.navigateTo("Ordini cliente")
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr[1]//td[2]').click() 
        self.wait_loader()

        self.find(By.XPATH, '//a[@class="btn btn-danger ask"]').click()
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()
        
        #torno alle impostazioni di prima
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-9"]').click() #apro Fatturazione
        sleep(1)

        self.find(By.XPATH, '(//label[@class="btn btn-default active"])[6]').click()    #disattivo impostazione
        sleep(2)

        #crea ordine
        self.expandSidebar("Vendite")
        self.navigateTo("Ordini cliente")
        self.wait_loader()

        self.find(By.XPATH, '//button[@class="btn btn-primary bound clickable"]').click()   #click su tasto +
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-idanagrafica-container"]').click()     #scelta di "Cliente" come anagrafica per l'ordine
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys('Cliente')
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(Keys.ENTER)
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click()   #click su tasto aggiungi
        self.wait_loader()
        #aggiungi articolo
        self.find(By.XPATH, '//span[@id="select2-id_articolo-container"]').click()
        sleep(1)

        self.find(By.XPATH, '//ul[@class="select2-results__options select2-results__options--nested"]//li[1]').click()
        self.find(By.XPATH, '//button[@class="btn btn-primary tip tooltipstered"]').click() #click su aggiungi
        sleep(2)
        #cambio stato
        self.find(By.XPATH, '//span[@id="select2-idstatoordine-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Accettato", Keys.ENTER)
        self.find(By.XPATH, '//button[@id="save"]').click()
        self.wait_loader()
        #crea attività
        self.navigateTo("Attività")
        self.wait_loader()

        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click()  #click su +
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-idanagrafica-container"]').click() #seleziono Cliente come anagrafica
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-dropdown select2-dropdown--below"]//input'))).send_keys("Cliente")
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-dropdown select2-dropdown--below"]//input'))).send_keys(Keys.ENTER)
        self.find(By.XPATH, '//span[@id="select2-idtipointervento-container"]').click() #seleziono Generico come tipo di intervento
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys("Generico")
        sleep(1)

        self.find(By.XPATH, '//li[@class="select2-results__option select2-results__option--highlighted"]').click()  #click su primo risultato
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//iframe[@class="cke_wysiwyg_frame cke_reset"])[1]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//iframe[@class="cke_wysiwyg_frame cke_reset"])[1]'))).send_keys("Test")   #scrivo "Test" come richiesta
        self.find(By.XPATH, '//span[@id="select2-idordine-container"]').click() #aggiungo ordine
        sleep(2)

        self.find(By.XPATH, '//ul[@id="select2-idordine-results"]//li[2]').click()
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click()   #click su Aggiungi
        self.wait_loader()

        self.find(By.XPATH, '//span[@id="select2-nuovo_tecnico-container"]').click()    #aggiungi sessione
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-nuovo_tecnico-results"]//li[2]').click()
        self.find(By.XPATH, '//button[@class="btn btn-primary btn-block"]').click()
        sleep(2)

        self.find(By.XPATH, '//span[@id="select2-idstatointervento-container"]').click()    #click su stato
        sleep(1)

        self.find(By.XPATH, '(//input[@class="select2-search__field"])[3]').send_keys("Completato", Keys.ENTER) #seleziono Completato come nuovo stato
        self.find(By.XPATH, '//button[@id="save"]').click()
        self.wait_loader()

        #fattura attività
        self.navigateTo("Attività")
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr[1]//td[1]').click()
        self.find(By.XPATH, '//button[@class="btn btn-primary btn-lg dropdown-toggle dropdown-toggle-split"]').click() #apro azioni di gruppo
        wait.until(EC.visibility_of_element_located((By.XPATH, '//a[@data-op="crea_fattura"]'))).click()    #click su crea fattura
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-raggruppamento-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente")    #seleziono cliente
        self.find(By.XPATH, '//ul[@id="select2-raggruppamento-results"]').click()
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-warning"]').click()  #click di conferma
        self.wait_loader()

        stato=self.find(By.XPATH, '//tbody//tr[1]//td[7]').text #controllo se lo stato è passato a "Fatturato"
        self.assertEqual(stato, "Fatturato")
        #elimina ordine
        self.expandSidebar("Vendite")
        self.navigateTo("Ordini cliente")
        self.wait_loader() 

        self.find(By.XPATH, '//tbody//tr[1//td[2]').click() 
        self.wait_loader()

        self.find(By.XPATH, '//a[@class="btn btn-danger ask"]').click()
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()
        #elimina fattura
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr[1]//td[2]').click()
        self.wait_loader()

        self.find(By.XPATH, '//a[@id="elimina"]').click() #elimina fattura
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()   #click di conferma
        self.wait_loader()
        #elimina attività
        self.navigateTo("Attività")
        self.wait_loader()
        
        self.find(By.XPATH, '//tbody//tr[1]//td[2]').click()
        self.wait_loader()

        self.find(By.XPATH, '//a[@class="btn btn-danger ask"]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()

    def fattura_attivita_collegate_preventivi(self):
        wait = WebDriverWait(self.driver, 20)
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-9"]').click() #apro Fatturazione
        sleep(1)

        self.find(By.XPATH, '(//label[@class="btn btn-default active"])[7]').click()    #attivo impostazione
        sleep(2)
        #creo preventivo
        self.expandSidebar("Vendite")
        self.navigateTo("Preventivi")
        self.wait_loader()

        self.find(By.XPATH, '//button[@class="btn btn-primary bound clickable"]').click()   #crea preventivo
        sleep(1)
        #nome
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="nome"]'))).send_keys('Prova')
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
        sleep(2)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(Keys.ENTER)
        self.find(By.XPATH, '//button[@class="btn btn-primary tip tooltipstered"]').click() #click su aggiungi
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-idstato-container"]').click()  #cambia stato
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-idstato-results"]//li[1]').click()   #stato accettato
        sleep(1)

        self.find(By.XPATH, '//button[@id="save"]').click()
        self.wait_loader()
        #creo attività
        self.navigateTo("Attività")
        self.wait_loader()

        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click()  #click su +
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-idanagrafica-container"]').click() #seleziono Cliente come anagrafica
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-dropdown select2-dropdown--below"]//input'))).send_keys("Cliente")
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-dropdown select2-dropdown--below"]//input'))).send_keys(Keys.ENTER)
        self.find(By.XPATH, '//span[@id="select2-idtipointervento-container"]').click() #seleziono Generico come tipo di intervento
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys("Generico")
        sleep(1)

        self.find(By.XPATH, '//li[@class="select2-results__option select2-results__option--highlighted"]').click()  #click su primo risultato
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//iframe[@class="cke_wysiwyg_frame cke_reset"])[1]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//iframe[@class="cke_wysiwyg_frame cke_reset"])[1]'))).send_keys("Test")   #scrivo "Test" come richiesta
        self.find(By.XPATH, '//span[@id="select2-idpreventivo-container"]').click() #aggiungo preventivo
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-idpreventivo-results"]//li[1]').click()
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click()   #click su Aggiungi
        self.wait_loader()

        self.find(By.XPATH, '//span[@id="select2-nuovo_tecnico-container"]').click()    #aggiungi sessione
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-nuovo_tecnico-results"]//li[2]').click()
        self.find(By.XPATH, '//button[@class="btn btn-primary btn-block"]').click()
        sleep(2)

        self.find(By.XPATH, '//span[@id="select2-idstatointervento-container"]').click()    #click su stato
        sleep(1)

        self.find(By.XPATH, '(//input[@class="select2-search__field"])[3]').send_keys("Completato", Keys.ENTER) #seleziono Completato come nuovo stato
        self.find(By.XPATH, '//button[@id="save"]').click()
        self.wait_loader()

        #fattura attività
        self.navigateTo("Attività")
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr[1]//td[1]').click()
        self.find(By.XPATH, '//button[@class="btn btn-primary btn-lg dropdown-toggle dropdown-toggle-split"]').click() #apro azioni di gruppo
        wait.until(EC.visibility_of_element_located((By.XPATH, '//a[@data-op="crea_fattura"]'))).click()    #click su crea fattura
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-raggruppamento-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente")    #seleziono cliente
        self.find(By.XPATH, '//ul[@id="select2-raggruppamento-results"]').click()
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-warning"]').click()  #click di conferma
        self.wait_loader()

        stato=self.find(By.XPATH, '//tbody//tr[1]//td[7]').text #controllo se lo stato è passato a "Fatturato"
        self.assertEqual(stato, "Fatturato")
        #elimina attività
        self.find(By.XPATH, '//tbody//tr[1]//td[2]').click()
        self.wait_loader()

        self.find(By.XPATH, '//a[@class="btn btn-danger ask"]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()
        #elimina preventivo
        self.expandSidebar("Vendite")
        self.navigateTo("Preventivi")
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr[1]//td[2]').click()
        self.wait_loader()

        self.find(By.XPATH, '//a[@class="btn btn-danger ask"]').click()
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()
        #elimina fattura
        self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr[1]//td[2]').click()
        self.wait_loader()

        self.find(By.XPATH, '//a[@id="elimina"]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()   #click di conferma
        self.wait_loader()
        #torna alle impostazioni di prima
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-9"]').click() #apro Fatturazione
        sleep(1)

        self.find(By.XPATH, '(//label[@class="btn btn-default active"])[7]').click()    #disattivo impostazione
        sleep(2)
        #creo preventivo
        self.expandSidebar("Vendite")
        self.navigateTo("Preventivi")
        self.wait_loader()

        self.find(By.XPATH, '//button[@class="btn btn-primary bound clickable"]').click()   #crea preventivo
        sleep(1)
        #nome
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="nome"]'))).send_keys('Prova')
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
        sleep(2)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(Keys.ENTER)
        self.find(By.XPATH, '//button[@class="btn btn-primary tip tooltipstered"]').click() #click su aggiungi
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-idstato-container"]').click()  #cambia stato
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-idstato-results"]//li[1]').click()   #stato accettato
        sleep(1)

        self.find(By.XPATH, '//button[@id="save"]').click()
        self.wait_loader()
        #creo attività
        self.navigateTo("Attività")
        self.wait_loader()

        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click()  #click su +
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-idanagrafica-container"]').click() #seleziono Cliente come anagrafica
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-dropdown select2-dropdown--below"]//input'))).send_keys("Cliente")
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-dropdown select2-dropdown--below"]//input'))).send_keys(Keys.ENTER)
        self.find(By.XPATH, '//span[@id="select2-idtipointervento-container"]').click() #seleziono Generico come tipo di intervento
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys("Generico")
        sleep(1)

        self.find(By.XPATH, '//li[@class="select2-results__option select2-results__option--highlighted"]').click()  #click su primo risultato
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//iframe[@class="cke_wysiwyg_frame cke_reset"])[1]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//iframe[@class="cke_wysiwyg_frame cke_reset"])[1]'))).send_keys("Test")   #scrivo "Test" come richiesta
        self.find(By.XPATH, '//span[@id="select2-idpreventivo-container"]').click() #aggiungo preventivo
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-idpreventivo-results"]//li[1]').click()
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click()   #click su Aggiungi
        self.wait_loader()

        self.find(By.XPATH, '//span[@id="select2-nuovo_tecnico-container"]').click()    #aggiungi sessione
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-nuovo_tecnico-results"]//li[2]').click()
        self.find(By.XPATH, '//button[@class="btn btn-primary btn-block"]').click()
        sleep(2)

        self.find(By.XPATH, '//span[@id="select2-idstatointervento-container"]').click()    #click su stato
        sleep(1)

        self.find(By.XPATH, '(//input[@class="select2-search__field"])[3]').send_keys("Completato", Keys.ENTER) #seleziono Completato come nuovo stato
        self.find(By.XPATH, '//button[@id="save"]').click()
        self.wait_loader()

        #fattura attività
        self.navigateTo("Attività")
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr[1]//td[1]').click()
        self.find(By.XPATH, '//button[@class="btn btn-primary btn-lg dropdown-toggle dropdown-toggle-split"]').click() #apro azioni di gruppo
        wait.until(EC.visibility_of_element_located((By.XPATH, '//a[@data-op="crea_fattura"]'))).click()    #click su crea fattura
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-raggruppamento-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente")    #seleziono cliente
        self.find(By.XPATH, '//ul[@id="select2-raggruppamento-results"]').click()
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-warning"]').click()  #click di conferma
        self.wait_loader()

        stato=self.find(By.XPATH, '//tbody//tr[1]//td[7]').text #controllo se lo stato è passato a "Fatturato"
        self.assertNotEqual(stato, "Fatturato")
        #elimina attività
        self.find(By.XPATH, '//tbody//tr[1]//td[2]').click()
        self.wait_loader()

        self.find(By.XPATH, '//a[@class="btn btn-danger ask"]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()
        #elimina preventivo
        self.expandSidebar("Vendite")
        self.navigateTo("Preventivi")
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr[1]//td[2]').click()
        self.wait_loader()

        self.find(By.XPATH, '//a[@class="btn btn-danger ask"]').click()
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()


