from common.Test import Test, get_html
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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
        ## TODO: ritardo apertura tooltip dashboard

    def visualizzare_domenica_calendario(self):
        wait = self.wait_driver
        self.expandSidebar("Strumenti")
        self.navigate_to_and_wait("Impostazioni")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Dashboard"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="form-group" and contains(., "Visualizzare la domenica sul calendario")]//div//label'))
        ).click()

        self.navigate_to_and_wait("Dashboard")

        wait.until(EC.invisibility_of_element_located((By.XPATH, '//tr[1]//th[8]')))

        self.expandSidebar("Strumenti")
        self.navigate_to_and_wait("Impostazioni")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Dashboard"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="form-group" and contains(., "Visualizzare la domenica sul calendario")]//div//label'))
        ).click()

    def vista_dashboard(self):
        wait = self.wait_driver
        self.expandSidebar("Strumenti")
        self.navigate_to_and_wait("Impostazioni")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Dashboard"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="form-group" and contains(., "Vista dashboard")]//div//span'))
        ).click()

        search = wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input')))
        search.send_keys("mese")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//li[contains(@class, "select2-results__option--highlighted")]'))).click()
        self.wait_ajax()

        self.navigate_to_and_wait("Dashboard")

        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[contains(@class, "fc-dayGridMonth-button") and contains(@class, "fc-button-active")]')))

        self.expandSidebar("Strumenti")
        self.navigate_to_and_wait("Impostazioni")
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Dashboard"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="form-group" and contains(., "Vista dashboard")]//div//span'))
        ).click()

        search = wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input')))
        search.send_keys("settimana")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//li[contains(@class, "select2-results__option--highlighted")]'))).click()
        self.wait_ajax()

    def ora_inizio_calendario(self):
        wait = self.wait_driver
        self.expandSidebar("Strumenti")
        self.navigate_to_and_wait("Impostazioni")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Dashboard"]'))
        ).click()

        element = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="form-group" and contains(., "Ora inizio sul calendario")]//input'))
        )
        element.send_keys(Keys.CONTROL, 'a')
        element.send_keys('01:00')
        # il salvataggio dei setting di tipo time è legato all'evento blur
        self.driver.execute_script("arguments[0].blur();", element)
        self.wait_ajax()

        self.navigate_to_and_wait("Dashboard")

        ora = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//td[@role="presentation"]//tbody//tr//td'))
        ).text
        self.assertEqual(ora, "1:00")

        self.expandSidebar("Strumenti")
        self.navigate_to_and_wait("Impostazioni")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Dashboard"]'))
        ).click()

        element = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="form-group" and contains(., "Ora inizio sul calendario")]//input'))
        )
        element.send_keys(Keys.CONTROL, 'a')
        element.send_keys('00:00')
        self.driver.execute_script("arguments[0].blur();", element)
        self.wait_ajax()

    def ora_fine_calendario(self):
        wait = self.wait_driver
        self.expandSidebar("Strumenti")
        self.navigate_to_and_wait("Impostazioni")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Dashboard"]'))
        ).click()

        element = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="form-group" and contains(., "Ora fine sul calendario")]//input'))
        )
        element.send_keys(Keys.CONTROL, 'a')
        element.send_keys('13:30')
        # il salvataggio dei setting di tipo time è legato all'evento blur
        self.driver.execute_script("arguments[0].blur();", element)
        self.wait_ajax()

        self.navigate_to_and_wait("Dashboard")

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[contains(@class, "fc-timegrid-slot-label")][.="13:00"]')))
        wait.until(EC.invisibility_of_element_located((By.XPATH, '//div[contains(@class, "fc-timegrid-slot-label")][.="14:00"]')))

        self.expandSidebar("Strumenti")
        self.navigate_to_and_wait("Impostazioni")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Dashboard"]'))
        ).click()

        element = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="form-group" and contains(., "Ora fine sul calendario")]//input'))
        )
        element.send_keys(Keys.CONTROL, 'a')
        element.send_keys('23:59')
        self.driver.execute_script("arguments[0].blur();", element)
        self.wait_ajax()

    def visualizza_informazioni_aggiuntive(self):
        wait = self.wait_driver
        self.expandSidebar("Strumenti")
        self.navigate_to_and_wait("Impostazioni")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Dashboard"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="form-group" and contains(., "Visualizza informazioni aggiuntive sul calendario")]//div//label'))
        ).click()
        self.wait_ajax()

        self.navigate_to_and_wait("Dashboard")

        scritta = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//td[@class="fc-timegrid-axis fc-scrollgrid-shrink"]'))
        ).text
        self.assertEqual(scritta, "Tutto il giorno")

        self.expandSidebar("Strumenti")
        self.navigate_to_and_wait("Impostazioni")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Dashboard"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="form-group" and contains(., "Visualizza informazioni aggiuntive sul calendario")]//div//label'))
        ).click()
        self.wait_ajax()

    def visualizza_colori_sessioni(self):
        wait = self.wait_driver
        self.expandSidebar("Strumenti")
        self.navigate_to_and_wait("Impostazioni")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Dashboard"]'))
        ).click()

        contenitore = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="form-group" and contains(., "Visualizzazione colori sessioni")]//div//span'))
        )
        if 'sfondo colore tecnico - bordo colore stato' not in contenitore.text.lower():
            contenitore.click()
            search = wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input')))
            search.send_keys("sfondo colore tecnico")
            wait.until(EC.visibility_of_element_located((By.XPATH, '//li[contains(@class, "select2-results__option--highlighted")]'))).click()
            self.wait_ajax()

        self.navigate_to_and_wait("Attività")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//i[@class="fa fa-plus"]'))
        ).click()

        self.wait_for_dropdown_and_select('//span[@id="select2-id_anagrafica-container"]', option_text='Cliente')

        self.wait_for_dropdown_and_select('//span[@id="select2-id_tipo_intervento-container"]', option_text='Generico')

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="cke_1_contents"]//iframe'))
        ).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="cke_1_contents"]//iframe'))).send_keys('Test')
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[contains(@class,"modal") and contains(@class,"show")]//button[contains(@class, "btn-success") and contains(., "Aggiungi attività")]'))
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

        self.navigate_to_and_wait("Dashboard")

        # Filtro tecnici: assicura che il tecnico della sessione sia selezionato
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="dashboard_tecnici"]//button[contains(@class, "counter_object")]'))
        ).click()
        checkbox = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//input[@class="dashboard_tecnico"]'))
        )
        if not checkbox.is_selected():
            checkbox.click()
            self.wait_ajax()
        self.driver.switch_to.active_element.send_keys(Keys.ESCAPE)

        colori_element = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[contains(@class, "fc-timegrid-event-harness")]//a'))
        )
        colori = colori_element.get_attribute("style")
        self.assertEqual(colori, "border-color: rgb(255, 239, 153); background-color: rgb(255, 255, 255);")

        self.expandSidebar("Strumenti")
        self.navigate_to_and_wait("Impostazioni")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Dashboard"]'))
        ).click()

        contenitore = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="form-group" and contains(., "Visualizzazione colori sessioni")]//div//span'))
        )
        if 'sfondo colore stato - bordo colore tecnico' not in contenitore.text.lower():
            contenitore.click()
            search = wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input')))
            search.send_keys("sfondo colore stato")
            wait.until(EC.visibility_of_element_located((By.XPATH, '//li[contains(@class, "select2-results__option--highlighted")]'))).click()
            self.wait_ajax()

        self.navigate_to_and_wait("Dashboard")

        colori_element = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[contains(@class, "fc-timegrid-event-harness")]//a'))
        )
        colori = colori_element.get_attribute("style")
        self.assertEqual(colori, "border-color: rgb(255, 255, 255); background-color: rgb(255, 239, 153);")

        self.navigate_to_and_wait("Attività")

        self.wait_and_click_table_row(1, 2)

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="btn btn-danger ask"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()
        self.wait_loader()

        