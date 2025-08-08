from common.Test import Test
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

class Dashboard(Test):

    def test_Dashboard(self):
        self.navigateTo("Dashboard")
        self.wait_loader()

        self.wait_for_element_and_click('(//div[@class="info-box"])[1]')
        widget = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="modal-body"]//p'))).text
        self.assertEqual(widget, "Non ci sono promemoria da pianificare.")
        self.wait_for_element_and_click('//div[@class="modal-content"]//button[@class="close"]')
        self.wait_driver.until(EC.invisibility_of_element_located((By.XPATH, '//div[@class="modal-dialog modal-lg"]')))

        self.wait_for_element_and_click('(//div[@class="info-box"])[2]')
        widget = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="modals"]//tbody//tr//td'))).text
        self.assertEqual(widget, "3")
        self.wait_for_element_and_click('//div[@class="modal-content"]//button[@class="close"]')
        self.wait_driver.until(EC.invisibility_of_element_located((By.XPATH, '//div[@class="modal-dialog modal-lg"]')))

        self.wait_for_element_and_click('(//div[@class="info-box"])[3]')
        widget = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="modal-body"]//p'))).text
        self.assertEqual(widget, "Non ci sono note da notificare.")
        self.wait_for_element_and_click('//div[@class="modal-content"]//button[@class="close"]')
        self.wait_driver.until(EC.invisibility_of_element_located((By.XPATH, '//div[@class="modal-dialog modal-lg"]')))

        self.wait_for_element_and_click('(//div[@class="info-box"])[4]')
        verifica = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//tbody//tr[1]//td[2]'))).text
        self.assertEqual(verifica, "Integrazione/autofattura per acquisto servizi dall'estero numero 0001")

        self.navigateTo("Dashboard")
        self.wait_loader()

        self.wait_for_element_and_click('(//div[@class="info-box"])[5]')
        widget = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="modal-body"]//div'))).text
        self.assertEqual(widget, "Non ci sono articoli in esaurimento.")
        self.wait_for_element_and_click('//div[@class="modal-content"]//button[@class="close"]')
        self.wait_driver.until(EC.invisibility_of_element_located((By.XPATH, '//div[@class="modal-dialog modal-lg"]')))

        self.wait_for_element_and_click('(//div[@class="info-box"])[6]')
        widget = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="modal-body"]//tr//th'))).text
        self.assertEqual(widget, "Preventivo")
        self.wait_for_element_and_click('//div[@class="modal-content"]//button[@class="close"]')
        self.wait_driver.until(EC.invisibility_of_element_located((By.XPATH, '//div[@class="modal-dialog modal-lg"]')))

        self.wait_for_element_and_click('(//div[@class="info-box"])[7]')
        widget = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="modal-content"]//p'))).text
        self.assertEqual(widget, "Non ci sono contratti in scadenza.")
        self.wait_for_element_and_click('//div[@class="modal-content"]//button[@class="close"]')
        self.wait_driver.until(EC.invisibility_of_element_located((By.XPATH, '//div[@class="modal-dialog modal-lg"]')))

        self.wait_for_element_and_click('(//div[@class="info-box"])[8]')
        widget = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '(//table[@id="tbl-rate"]//tr//th)[2]'))).text
        self.assertEqual(widget, "Scadenza")
        self.wait_for_element_and_click('//div[@class="modal-content"]//button[@class="close"]')
        self.wait_driver.until(EC.invisibility_of_element_located((By.XPATH, '//div[@class="modal-dialog modal-lg"]')))

        self.wait_for_element_and_click('(//div[@class="info-box"])[9]')
        widget = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="modal-body"]//label'))).text
        self.assertEqual(widget, "Mese e anno*")
        self.wait_for_element_and_click('//div[@class="modal-content"]//button[@class="close"]')
        self.wait_driver.until(EC.invisibility_of_element_located((By.XPATH, '//div[@class="modal-dialog modal-lg"]')))

        self.wait_for_element_and_click('(//div[@class="info-box"])[10]')
        widget = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="modal-body"]//label'))).text
        self.assertEqual(widget, "Settimana*")
        self.wait_for_element_and_click('//div[@class="modal-content"]//button[@class="close"]')
        self.wait_driver.until(EC.invisibility_of_element_located((By.XPATH, '//div[@class="modal-dialog modal-lg"]')))

        self.wait_for_element_and_click('(//div[@class="info-box"])[11]')
        widget = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="modal-body"]//tbody//tr//th'))).text
        self.assertEqual(widget, "Codice")
        self.wait_for_element_and_click('//div[@class="modal-content"]//button[@class="close"]')
        self.wait_driver.until(EC.invisibility_of_element_located((By.XPATH, '//div[@class="modal-dialog modal-lg"]')))

        self.wait_for_element_and_click('(//div[@class="info-box"])[12]')
        widget = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="modal-body"]//tbody//tr//th'))).text
        self.assertEqual(widget, "Attività")
        self.wait_for_element_and_click('//div[@class="modal-content"]//button[@class="close"]')
        self.wait_driver.until(EC.invisibility_of_element_located((By.XPATH, '//div[@class="modal-dialog modal-lg"]')))
