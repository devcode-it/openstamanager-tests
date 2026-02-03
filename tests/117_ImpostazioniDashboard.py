from common.Test import Test, get_html
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Impostazioni(Test):
    def setUp(self):
        super().setUp()

    def test_impostazioni_dashboard(self):
        ## TODO: utilizzare i tooltip sul calendario

        # Test Visualizzare domenica sul calendario 
        self.visualizzare_domenica_calendario()

        # Test Vista Dashboard
        self.vista_dashboard()

        # Test Ora inizio sul calendario 
        self.ora_inizio_calendario()

        # Test Ora fine sul calendario 
        self.ora_fine_calendario()

        # Test Visualizza informazioni aggiuntive sul calendario 
        self.visualizza_informazioni_aggiuntive()

        # Test Visualizzazione colori sessioni 
        self.visualizza_colori_sessioni()

        ## TODO: tempo predefinito di snap attività sul calendario

    def visualizzare_domenica_calendario(self):
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Dashboard"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="form-group" and contains(., "Visualizzare la domenica sul calendario"))
        )]//div//label').click()

        self.navigateTo("Dashboard")
        self.wait_loader()

        wait.until(EC.invisibility_of_element_located((By.XPATH, '//tr[1]//th[8]')))   

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Dashboard"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="form-group" and contains(., "Visualizzare la domenica sul calendario"))
        )]//div//label').click()

    def vista_dashboard(self):
        wait = self.wait_driver  
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Dashboard"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="form-group" and contains(., "Vista dashboard"))
        )]//div//span').click()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys("mese")

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)

        self.navigateTo("Dashboard")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@class="fc-dayGridMonth-button fc-button fc-button-primary fc-button-active"]')))

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Dashboard"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="form-group" and contains(., "Vista dashboard"))
        )]//div//span').click()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys("settimana")

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)

    def ora_inizio_calendario(self):
        wait = self.wait_driver  
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Dashboard"]'))
        ).click()

        element = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="form-group" and contains(., "Ora inizio sul calendario"))
        )]//input')
        element.clear()
        element.send_keys('01:00')

        self.navigateTo("Dashboard")
        self.wait_loader()

        ora = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//td[@role="presentation"]//tbody//tr//td'))
        ).text 
        self.assertEqual(ora, "1:00", Keys.ENTER)

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Dashboard"]'))
        ).click()

        element = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="form-group" and contains(., "Ora inizio sul calendario"))
        )]//input')
        element.clear()
        element.send_keys('6:00', Keys.ENTER)

    def ora_fine_calendario(self):
        wait = self.wait_driver  
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Dashboard"]'))
        ).click()

        element = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="form-group" and contains(., "Ora fine sul calendario"))
        )]//input')
        element.clear()
        element.send_keys('13:30', Keys.ENTER)

        self.navigateTo("Dashboard")
        self.wait_loader()

        wait.until(EC.invisibility_of_element_located((By.XPATH, '//tbody//tr[55]//td')))

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Dashboard"]'))
        ).click()

        element = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="form-group" and contains(., "Ora fine sul calendario"))
        )]//input')
        element.clear()
        element.send_keys('18:59', Keys.ENTER)

    def visualizza_informazioni_aggiuntive(self):
        wait = self.wait_driver  
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Dashboard"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="form-group" and contains(., "Visualizza informazioni aggiuntive sul calendario"))
        )]//span').click()

        self.navigateTo("Dashboard")
        self.wait_loader()

        scritta = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//tr[1]//td[@class="fc-timegrid-axis fc-scrollgrid-shrink"]'))
        ).text
        self.assertEqual(scritta, "Tutto il giorno")

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Dashboard"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="form-group" and contains(., "Visualizza informazioni aggiuntive sul calendario"))
        )]//span').click()

    def visualizza_colori_sessioni(self):
        wait = self.wait_driver  
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Dashboard"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="form-group" and contains(., "Visualizzazione colori sessioni"))
        )]//div//span').click()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys("sfondo colore tecnico - bordo colore stato")

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)

        self.navigateTo("Attività")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//i[@class="fa fa-plus"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idanagrafica-container"]'))
        ).click() 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-dropdown select2-dropdown--below"]//input'))).send_keys("Cliente")

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-dropdown select2-dropdown--below"]//input'))).send_keys(Keys.ENTER)
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idtipointervento-container"]'))
        ).click() 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys("Generico")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//li[@class="select2-results__option select2-results__option--highlighted"]'))
        ).click() 
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//iframe[@class="cke_wysiwyg_frame cke_reset"])[1]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//iframe[@class="cke_wysiwyg_frame cke_reset"])[1]'))).send_keys("Test")   
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary"]'))
        ).click()  
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-nuovo_tecnico-container"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-nuovo_tecnico-results"]//li[2]'))
        ).click()
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary btn-block"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@id="save"]'))
        ).click() 
        self.wait_loader()

        self.navigateTo("Dashboard")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-block counter_object btn-danger"]'))
        ).click()
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//input[@class="dashboard_tecnico"]'))
        ).click()

        colori_element = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//td[@role="presentation"]//tbody//tr//td//a'))
        )
        colori = colori_element.get_attribute("style")
        self.assertEqual(colori, "border-color: rgb(255, 239, 153); background-color: rgb(255, 255, 255);")

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Dashboard"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="form-group" and contains(., "Visualizzazione colori sessioni"))
        )]//div//span').click()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys("sfondo colore stato - bordo colore tecnico")

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)

        self.navigateTo("Dashboard")
        self.wait_loader()

        colori_element = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="fc-timegrid-event-harness fc-timegrid-event-harness-inset"]//a'))
        )
        colori = colori_element.get_attribute("style")  
        self.assertEqual(colori, "border-color: rgb(255, 255, 255); background-color: rgb(255, 239, 153);")

        self.navigateTo("Attività")
        self.wait_loader()

        self.wait_for_element_and_click('//tbody//tr[1]//td[2]')

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="btn btn-danger ask"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()
        self.wait_loader()

        