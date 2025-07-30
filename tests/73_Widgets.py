from common.Test import Test, get_html
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Dashboard(Test):
      
    def test_Dashboard(self):
        self.navigateTo("Dashboard")
        self.wait_loader()

        self.find(By.XPATH, '(//div[@class="info-box"])[1]').click()
        widget = self.find(By.XPATH, '//div[@class="modal-body"]//p').text
        self.assertEqual(widget, "Non ci sono promemoria da pianificare.")
        self.find(By.XPATH, '//div[@class="modal-content"]//button[@class="close"]').click()

        self.find(By.XPATH, '(//div[@class="info-box"])[2]').click()
        widget = self.find(By.XPATH, '//div[@id="modals"]//tbody//tr//td').text
        self.assertEqual(widget, "2")
        self.find(By.XPATH, '//div[@class="modal-content"]//button[@class="close"]').click()

        self.find(By.XPATH, '(//div[@class="info-box"])[3]').click()
        widget = self.find(By.XPATH, '//div[@class="modal-body"]//p').text
        self.assertEqual(widget, "Non ci sono note da notificare.")
        self.find(By.XPATH, '//div[@class="modal-content"]//button[@class="close"]').click()

        self.find(By.XPATH, '(//div[@class="info-box"])[4]').click()
        verifica = self.find(By.XPATH, '//tbody//tr[1]//td[2]').text
        self.assertEqual(verifica, "Fattura immediata di acquisto numero 01")

        self.navigateTo("Dashboard")
        self.wait_loader()

        self.find(By.XPATH, '(//div[@class="info-box"])[5]').click()
        widget = self.find(By.XPATH, '//div[@class="modal-body"]//div').text
        self.assertEqual(widget, "Non ci sono articoli in esaurimento.")
        self.find(By.XPATH, '//div[@class="modal-content"]//button[@class="close"]').click()

        self.find(By.XPATH, '(//div[@class="info-box"])[6]').click()
        widget = self.find(By.XPATH, '//div[@class="modal-body"]//tr//th').text
        self.assertEqual(widget, "Preventivo")
        self.find(By.XPATH, '//div[@class="modal-content"]//button[@class="close"]').click()
        
        self.find(By.XPATH, '(//div[@class="info-box"])[7]').click()
        widget = self.find(By.XPATH, '//div[@class="modal-content"]//p').text
        self.assertEqual(widget, "Non ci sono contratti in scadenza.")
        self.find(By.XPATH, '//div[@class="modal-content"]//button[@class="close"]').click()

        self.find(By.XPATH, '(//div[@class="info-box"])[8]').click()
        widget = self.find(By.XPATH, '(//table[@id="tbl-rate"]//tr//th)[2]').text
        self.assertEqual(widget, "Scadenza")
        self.find(By.XPATH, '//div[@class="modal-content"]//button[@class="close"]').click()

        self.find(By.XPATH, '(//div[@class="info-box"])[9]').click()
        widget = self.find(By.XPATH, '//div[@class="modal-body"]//label').text
        self.assertEqual(widget, "Mese e anno*")
        self.find(By.XPATH, '//div[@class="modal-content"]//button[@class="close"]').click()

        self.find(By.XPATH, '(//div[@class="info-box"])[10]').click()
        widget = self.find(By.XPATH, '//div[@class="modal-body"]//label').text
        self.assertEqual(widget, "Settimana*")
        self.find(By.XPATH, '//div[@class="modal-content"]//button[@class="close"]').click()

        self.find(By.XPATH, '(//div[@class="info-box"])[11]').click()
        widget = self.find(By.XPATH, '//div[@class="modal-body"]//tbody//tr//th').text
        self.assertEqual(widget, "Codice")
        self.find(By.XPATH, '//div[@class="modal-content"]//button[@class="close"]').click()

        self.find(By.XPATH, '(//div[@class="info-box"])[12]').click()
        widget = self.find(By.XPATH, '//div[@class="modal-body"]//tbody//tr//th').text
        self.assertEqual(widget, "Attività")
        self.find(By.XPATH, '//div[@class="modal-content"]//button[@class="close"]').click()