from common.Test import Test, get_html
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

class Impostazioni(Test):
    def setUp(self):
        super().setUp()

    def test_impostazioni_fatturazione_elettronica(self):
        # Allega stampa per fattura verso Privati (1)
        self.allega_stampa_privati()

        # Allega stampa per fattura verso Aziende (2)
        self.allega_stampa_aziende()

        # Allega stampa per fattura verso PA (3)
        self.allega_stampa_PA()

        # Regime fiscale (4)
        self.regime_fiscale()

        # Tipo cassa previdenziale (5)
        self.tipo_cassa_previdenziale()

        # Causale ritenuta d'acconto (6)
        self.causale_ritenuta_acconto()

        ## TODO: Authorization ID indice PA

        ## TODO: OSMCloud services API token

        ## TODO: terzo intermediario

        # Riferimento dei documenti in fattura elettronica (10)
        self.riferimento_documenti_fattura_elettronica()

        ## TODO: OSMCloud Services API URL 

        ## TODO: OSMCloud Services API Version

        ## TODO: data inizio controlli su stati FE

        ## TODO: Movimenta magazzino da fatture di acquisto

        ## TODO: Rimuovi avviso fatture estere

        ## TODO: Creazione seriali in Import FE

        ## TODO: giorni validità fattura scartata

    def allega_stampa_privati(self):
        wait = self.wait_driver
        self.expandSidebar("Strumenti")
        self.navigate_to_and_wait("Impostazioni")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Fatturazione Elettronica"]'))
        ).click()


        self.wait_for_element_and_click('//div[@class="form-group" and contains(., "Allega stampa per fattura verso Privati")]//div//label')
        self.wait_ajax()

        self.expandSidebar("Vendite")
        self.navigate_to_and_wait("Fatture di vendita")

        self.crea_fattura_con_stato_emessa()

        allegato = self.wait_driver.until(
            EC.presence_of_element_located((By.XPATH, '//div[@class="card-body"]//tbody//tr[1]//a'))
        ).text
        self.assertIn("Stampa allegata", allegato)

        self.wait_for_element_and_click('//a[@id="elimina"]')
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()
        self.wait_loader()


        self.expandSidebar("Strumenti")
        self.navigate_to_and_wait("Impostazioni")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Fatturazione Elettronica"]'))
        ).click()

        self.wait_for_element_and_click('//div[@class="form-group" and contains(., "Allega stampa per fattura verso Privati")]//div//label')
        self.wait_ajax()

        self.expandSidebar("Vendite")
        self.navigate_to_and_wait("Fatture di vendita")

        self.crea_fattura_con_stato_emessa()

        allegato = self.wait_driver.until(
            EC.presence_of_element_located((By.XPATH, '//div[@class="card-body"]//tbody//tr[1]//a'))
        ).text
        self.assertNotIn("Stampa allegata", allegato)

        self.wait_for_element_and_click('//a[@id="elimina"]')
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()
        self.wait_loader()

    def crea_fattura_con_stato_emessa(self, cliente='Cliente', codice='00000004', rivalsa=None, ritenuta_acconto=False):
        wait = self.wait_driver

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//i[@class="fa fa-plus"]'))
        ).click()

        self.wait_for_element_and_click('//span[@id="select2-id_anagrafica_add-container"]')
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(cliente)
        if codice:
            wait.until(EC.visibility_of_element_located((By.XPATH, '//li[contains(normalize-space(.), "' + codice + '")]'))).click()
        else:
            wait.until(EC.visibility_of_element_located((By.XPATH, '//li[contains(@class, "select2-results__option--highlighted")]'))).click()
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[contains(@class,"modal") and contains(@class,"show")]//button[@type="submit"]'))
        ).click()
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@data-title="Aggiungi riga"]'))
        ).click()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="modals"]//textarea[@id="descrizione_riga"]'))).send_keys("Test")
        prezzo = wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="modals"]//input[@id="prezzo_unitario"]')))
        prezzo.send_keys('1')

        if rivalsa:
            self.wait_for_dropdown_and_select(
                '//div[@id="modals"]//span[@id="select2-id_rivalsa_inps-container"]',
                option_text=rivalsa
            )

        if ritenuta_acconto:
            self.wait_for_dropdown_and_select(
                '//div[@id="modals"]//span[@id="select2-id_ritenuta_acconto-container"]',
                option_text="Ritenuta d'acconto 20%"
            )
            self.wait_for_element_and_click('//div[@id="modals"]//span[@id="select2-calcolo_ritenuta_acconto-container"]')
            # i risultati select2 vengono appesi al body, non al modal
            self.wait_for_element_and_click('//ul[@id="select2-calcolo_ritenuta_acconto-results"]//li[1]')

        self.wait_loader()
        self.wait_for_element_and_click('//div[@id="modals"]//button[@onclick="submitForm()"]')
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-id_stato-container"]'))
        ).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Emessa")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//li[contains(@class, "select2-results__option--highlighted")]'))).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@id="save"]'))
        ).click()
        self.wait_loader()


    def allega_stampa_aziende(self):
        wait = self.wait_driver
        self.expandSidebar("Strumenti")
        self.navigate_to_and_wait("Impostazioni")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Fatturazione Elettronica"]'))
        ).click()


        self.wait_for_element_and_click('//div[@class="form-group" and contains(., "Allega stampa per fattura verso Aziende")]//div//label')
        self.wait_ajax()

        self.expandSidebar("Vendite")
        self.navigate_to_and_wait("Fatture di vendita")

        self.crea_fattura_con_stato_emessa(cliente='Cliente Estero', codice='00000003')

        allegato = self.wait_driver.until(
            EC.presence_of_element_located((By.XPATH, '//div[@class="card-body"]//tbody//tr[1]//a'))
        ).text
        self.assertIn("Stampa allegata", allegato)

        self.wait_for_element_and_click('//a[@id="elimina"]')
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()
        self.wait_loader()


        self.expandSidebar("Strumenti")
        self.navigate_to_and_wait("Impostazioni")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Fatturazione Elettronica"]'))
        ).click()

        self.wait_for_element_and_click('//div[@class="form-group" and contains(., "Allega stampa per fattura verso Aziende")]//div//label')
        self.wait_ajax()

        self.expandSidebar("Vendite")
        self.navigate_to_and_wait("Fatture di vendita")

        self.crea_fattura_con_stato_emessa(cliente='Cliente Estero', codice='00000003')

        allegato = self.wait_driver.until(
            EC.presence_of_element_located((By.XPATH, '//div[@class="card-body"]//tbody//tr[1]//a'))
        ).text
        self.assertNotIn("Stampa allegata", allegato)

        self.wait_for_element_and_click('//a[@id="elimina"]')
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()
        self.wait_loader()


    def allega_stampa_PA(self):
        wait = self.wait_driver
        self.navigate_to_and_wait("Anagrafiche")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//i[@class="fa fa-plus"]'))
        ).click()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="ragione_sociale_add"]'))).send_keys('Test')
        self.wait_for_element_and_click('//select[@id="id_tipo_anagrafica_add"]/following-sibling::span[1]//span[contains(@class, "select2-selection--multiple")]')
        wait.until(EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-id_tipo_anagrafica_add-results"]//li[contains(normalize-space(.), "Cliente")]'))).click()
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[contains(@class,"modal") and contains(@class,"show")]//button[@type="submit"]'))
        ).click()
        self.wait_loader()

        # tipologia Ente pubblico
        self.wait_for_dropdown_and_select('//span[@id="select2-tipo-container"]', option_text='Ente pubblico')

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="citta"]'))).send_keys("Prova")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="indirizzo"]'))).send_keys("via test 1")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="cap"]'))).send_keys("43190")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="codice_fiscale"]'))).send_keys("78954654")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="codice_destinatario"]'))).send_keys("CI7YID")
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@id="save"]'))
        ).click()
        self.wait_loader()

        self.expandSidebar("Strumenti")
        self.navigate_to_and_wait("Impostazioni")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Fatturazione Elettronica"]'))
        ).click()


        self.wait_for_element_and_click('//div[@class="form-group" and contains(., "Allega stampa per fattura verso PA")]//div//label')
        self.wait_ajax()

        self.expandSidebar("Vendite")
        self.navigate_to_and_wait("Fatture di vendita")

        self.crea_fattura_con_stato_emessa(cliente='Test', codice=None)

        allegato = self.wait_driver.until(
            EC.presence_of_element_located((By.XPATH, '//div[@class="card-body"]//tbody//tr[1]//a'))
        ).text
        self.assertIn("Stampa allegata", allegato)

        self.wait_for_element_and_click('//a[@id="elimina"]')
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()
        self.wait_loader()


        self.expandSidebar("Strumenti")
        self.navigate_to_and_wait("Impostazioni")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Fatturazione Elettronica"]'))
        ).click()

        self.wait_for_element_and_click('//div[@class="form-group" and contains(., "Allega stampa per fattura verso PA")]//div//label')
        self.wait_ajax()

        self.expandSidebar("Vendite")
        self.navigate_to_and_wait("Fatture di vendita")

        self.crea_fattura_con_stato_emessa(cliente='Test', codice=None)

        allegato = self.wait_driver.until(
            EC.presence_of_element_located((By.XPATH, '//div[@class="card-body"]//tbody//tr[1]//a'))
        ).text
        self.assertNotIn("Stampa allegata", allegato)

        self.wait_for_element_and_click('//a[@id="elimina"]')
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()
        self.wait_loader()

        # elimino l'anagrafica di prova
        self.navigate_to_and_wait("Anagrafiche")

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Ragione-sociale"]/input'))).send_keys("Test", Keys.ENTER)
        self.wait_loader()

        self.wait_and_click_table_row(1, 2)
        self.wait_loader()

        self.wait_for_element_and_click('//a[@class="btn btn-danger ask"]')
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Ragione-sociale"]//i'))
        ).click()


    def regime_fiscale(self):
        wait = self.wait_driver

        # Fase 1: regime RF01 (impostazione corrente)
        self.expandSidebar("Vendite")
        self.navigate_to_and_wait("Fatture di vendita")
        # la cassa previdenziale compare nell'XML solo con una riga con rivalsa INPS
        self.crea_fattura_con_stato_emessa(rivalsa='Cassa Previdenziale di Prova')

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//button[@class="btn btn-info dropdown-toggle dropdown-toggle-split"])[1]'))
        ).click()

        try:
            self.wait_driver.until(
                EC.visibility_of_element_located((By.XPATH, '//a[@id="print-button_1"]'))
            )
        except Exception:
            self.wait_driver.until(
                EC.visibility_of_element_located((By.XPATH, '(//button[@class="btn btn-info dropdown-toggle dropdown-toggle-split"])[2]'))
            ).click()
            self.wait_driver.until(
                EC.visibility_of_element_located((By.XPATH, '//a[@id="print-button_1"]'))
            )

        self.wait_for_element_and_click('//a[@id="print-button_1"]')

        wait.until(lambda d: len(d.window_handles) > 1)
        self.driver.switch_to.window(self.driver.window_handles[1])
        wait.until(lambda d: 'RF01' in d.page_source)

        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

        self.wait_for_element_and_click('//a[@id="elimina"]')
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()
        self.wait_loader()

        # cambio il regime a RF02
        self.expandSidebar("Strumenti")
        self.navigate_to_and_wait("Impostazioni")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Fatturazione Elettronica"]'))
        ).click()

        self.wait_for_dropdown_and_select(
            '//div[@class="form-group" and contains(., "Regime Fiscale")]//div//span',
            option_text='RF02'
        )

        # Fase 2: regime RF02
        self.expandSidebar("Vendite")
        self.navigate_to_and_wait("Fatture di vendita")
        self.crea_fattura_con_stato_emessa()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//button[@class="btn btn-info dropdown-toggle dropdown-toggle-split"])[1]'))
        ).click()

        try:
            self.wait_driver.until(
                EC.visibility_of_element_located((By.XPATH, '//a[@id="print-button_1"]'))
            )
        except Exception:
            self.wait_driver.until(
                EC.visibility_of_element_located((By.XPATH, '(//button[@class="btn btn-info dropdown-toggle dropdown-toggle-split"])[2]'))
            ).click()
            self.wait_driver.until(
                EC.visibility_of_element_located((By.XPATH, '//a[@id="print-button_1"]'))
            )

        self.wait_for_element_and_click('//a[@id="print-button_1"]')

        wait.until(lambda d: len(d.window_handles) > 1)
        self.driver.switch_to.window(self.driver.window_handles[1])
        wait.until(lambda d: 'RF02' in d.page_source)

        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

        self.wait_for_element_and_click('//a[@id="elimina"]')
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()
        self.wait_loader()

        # ripristino il regime a RF01
        self.expandSidebar("Strumenti")
        self.navigate_to_and_wait("Impostazioni")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Fatturazione Elettronica"]'))
        ).click()

        self.wait_for_dropdown_and_select(
            '//div[@class="form-group" and contains(., "Regime Fiscale")]//div//span',
            option_text='RF01'
        )


    def tipo_cassa_previdenziale(self):
        wait = self.wait_driver
        self.expandSidebar("Strumenti")
        self.navigate_to_and_wait("Impostazioni")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Fatturazione Elettronica"]'))
        ).click()

        self.wait_for_dropdown_and_select(
            '//div[@class="form-group" and contains(., "Tipo Cassa Previdenziale")]//div//span',
            option_text='TC01'
        )

        self.expandSidebar("Vendite")
        self.navigate_to_and_wait("Fatture di vendita")
        # la cassa previdenziale compare nell'XML solo con una riga con rivalsa INPS
        self.crea_fattura_con_stato_emessa(rivalsa='Cassa Previdenziale di Prova')

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//button[@class="btn btn-info dropdown-toggle dropdown-toggle-split"])[1]'))
        ).click()

        try:
            self.wait_driver.until(
                EC.visibility_of_element_located((By.XPATH, '//a[@id="print-button_1"]'))
            )
        except Exception:
            self.wait_driver.until(
                EC.visibility_of_element_located((By.XPATH, '(//button[@class="btn btn-info dropdown-toggle dropdown-toggle-split"])[2]'))
            ).click()
            self.wait_driver.until(
                EC.visibility_of_element_located((By.XPATH, '//a[@id="print-button_1"]'))
            )

        self.wait_for_element_and_click('//a[@id="print-button_1"]')

        wait.until(lambda d: len(d.window_handles) > 1)
        self.driver.switch_to.window(self.driver.window_handles[1])
        wait.until(lambda d: 'TC01' in d.page_source)

        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

        self.wait_for_element_and_click('//a[@id="elimina"]')
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()
        self.wait_loader()

        # ripristino: tolgo la cassa previdenziale (stato originale) via API select2
        self.expandSidebar("Strumenti")
        self.navigate_to_and_wait("Impostazioni")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Fatturazione Elettronica"]'))
        ).click()

        self.wait_driver.until(
            EC.presence_of_element_located((By.ID, 'setting74'))
        )
        self.driver.execute_script("$('#setting74').val(null).trigger('change');")
        self.wait_ajax()


    def causale_ritenuta_acconto(self):
        wait = self.wait_driver

        # Fase 1: causale A (impostazione corrente)
        self.expandSidebar("Vendite")
        self.navigate_to_and_wait("Fatture di vendita")
        self.crea_fattura_con_stato_emessa(ritenuta_acconto=True)

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//button[@class="btn btn-info dropdown-toggle dropdown-toggle-split"])[1]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@id="print-button_1"]'))
        ).click()

        wait.until(lambda d: len(d.window_handles) > 1)
        self.driver.switch_to.window(self.driver.window_handles[1])
        wait.until(lambda d: 'A (decodi' in d.page_source)

        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

        self.wait_for_element_and_click('//a[@id="elimina"]')
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()
        self.wait_loader()

        # cambio la causale a B
        self.expandSidebar("Strumenti")
        self.navigate_to_and_wait("Impostazioni")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Fatturazione Elettronica"]'))
        ).click()

        self.wait_for_dropdown_and_select(
            '//div[@class="form-group" and contains(., "Causale ritenuta d\'acconto")]//div//span',
            option_text='Utilizzazione economica'
        )

        # Fase 2: causale B
        self.expandSidebar("Vendite")
        self.navigate_to_and_wait("Fatture di vendita")
        self.crea_fattura_con_stato_emessa(ritenuta_acconto=True)

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//button[@class="btn btn-info dropdown-toggle dropdown-toggle-split"])[1]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@id="print-button_1"]'))
        ).click()

        wait.until(lambda d: len(d.window_handles) > 1)
        self.driver.switch_to.window(self.driver.window_handles[1])
        wait.until(lambda d: 'B (' in d.page_source)

        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

        self.wait_for_element_and_click('//a[@id="elimina"]')
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()
        self.wait_loader()

        # ripristino la causale A
        self.expandSidebar("Strumenti")
        self.navigate_to_and_wait("Impostazioni")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Fatturazione Elettronica"]'))
        ).click()

        self.wait_for_dropdown_and_select(
            '//div[@class="form-group" and contains(., "Causale ritenuta d\'acconto")]//div//span',
            option_text='Prestazioni di lavoro autonomo'
        )


    def riferimento_documenti_fattura_elettronica(self):
        wait = self.wait_driver

        # Fase 1: riferimento attivo (impostazione corrente)
        self.expandSidebar("Vendite")
        self.navigate_to_and_wait("Fatture di vendita")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//i[@class="fa fa-plus"]'))
        ).click()

        self.wait_for_element_and_click('//span[@id="select2-id_anagrafica_add-container"]')
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//li[contains(normalize-space(.), "00000004")]'))).click()
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[contains(@class,"modal") and contains(@class,"show")]//button[@type="submit"]'))
        ).click()
        self.wait_loader()

        self.wait_for_element_and_click('//button[@class="btn btn-primary dropdown-toggle" and contains(., "Altro")]')

        self.wait_for_element_and_click('//a[@data-title="Aggiungi Preventivo"]')

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="modals"]//span[@id="select2-id_documento-container"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-id_documento-results"]//li[contains(@class, "select2-results__option--highlighted")]'))
        ).click()
        self.wait_loader()

        # il change automatico non popola le righe (selectData non pronto):
        # caricamento manuale delle righe del preventivo
        id_record = self.driver.current_url.split('id_record=')[1].split('&')[0]
        self.driver.execute_script(
            "$('#righe_documento').load(globals.rootdir + '/modules/fatture/add_preventivo.php?id_module=14&id_record=" + id_record + "&id_documento=2');"
        )
        self.wait_loader()

        self.wait_driver.until(
            EC.presence_of_element_located((By.XPATH, '//input[@id="import_all"]'))
        ).click()

        self.wait_driver.until(
            EC.presence_of_element_located((By.XPATH, '//input[@id="checked_3"]'))
        ).click()
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@id="submit_btn"]'))
        ).click()
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-id_stato-container"]'))
        ).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Emessa")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//li[contains(@class, "select2-results__option--highlighted")]'))).click()
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@id="save"]'))
        ).click()
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//button[@class="btn btn-info dropdown-toggle dropdown-toggle-split"])[1]'))
        ).click()  # apro il menu stampe

        try:
            self.wait_driver.until(
                EC.visibility_of_element_located((By.XPATH, '//a[@id="print-button_1"]'))
            )
        except Exception:
            self.wait_driver.until(
                EC.visibility_of_element_located((By.XPATH, '(//button[@class="btn btn-info dropdown-toggle dropdown-toggle-split"])[2]'))
            ).click()
            self.wait_driver.until(
                EC.visibility_of_element_located((By.XPATH, '//a[@id="print-button_1"]'))
            )

        self.wait_for_element_and_click('//a[@id="print-button_1"]')

        wait.until(lambda d: len(d.window_handles) > 1)
        self.driver.switch_to.window(self.driver.window_handles[1])
        wait.until(lambda d: 'Rif. preventivo' in d.page_source)

        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

        self.wait_for_element_and_click('//a[@id="elimina"]')
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()
        self.wait_loader()

        # disattivo il riferimento dei documenti in fattura elettronica
        self.expandSidebar("Strumenti")
        self.navigate_to_and_wait("Impostazioni")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Fatturazione Elettronica"]'))
        ).click()

        self.wait_for_element_and_click('//div[@class="form-group" and contains(., "Riferimento dei documenti in Fattura Elettronica")]//div//label')
        self.wait_ajax()

        # Fase 2: riferimento disattivato
        self.expandSidebar("Vendite")
        self.navigate_to_and_wait("Fatture di vendita")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//i[@class="fa fa-plus"]'))
        ).click()

        self.wait_for_element_and_click('//span[@id="select2-id_anagrafica_add-container"]')
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//li[contains(normalize-space(.), "00000004")]'))).click()
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[contains(@class,"modal") and contains(@class,"show")]//button[@type="submit"]'))
        ).click()
        self.wait_loader()

        self.wait_for_element_and_click('//button[@class="btn btn-primary dropdown-toggle" and contains(., "Altro")]')

        self.wait_for_element_and_click('//a[@data-title="Aggiungi Preventivo"]')

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="modals"]//span[@id="select2-id_documento-container"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-id_documento-results"]//li[contains(@class, "select2-results__option--highlighted")]'))
        ).click()
        self.wait_loader()

        # il change automatico non popola le righe (selectData non pronto):
        # caricamento manuale delle righe del preventivo
        id_record = self.driver.current_url.split('id_record=')[1].split('&')[0]
        self.driver.execute_script(
            "$('#righe_documento').load(globals.rootdir + '/modules/fatture/add_preventivo.php?id_module=14&id_record=" + id_record + "&id_documento=2');"
        )
        self.wait_loader()

        self.wait_driver.until(
            EC.presence_of_element_located((By.XPATH, '//input[@id="import_all"]'))
        ).click()

        self.wait_driver.until(
            EC.presence_of_element_located((By.XPATH, '//input[@id="checked_3"]'))
        ).click()
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@id="submit_btn"]'))
        ).click()
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-id_stato-container"]'))
        ).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Emessa")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//li[contains(@class, "select2-results__option--highlighted")]'))).click()
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@id="save"]'))
        ).click()
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//button[@class="btn btn-info dropdown-toggle dropdown-toggle-split"])[1]'))
        ).click()  # apro il menu stampe

        try:
            self.wait_driver.until(
                EC.visibility_of_element_located((By.XPATH, '//a[@id="print-button_1"]'))
            )
        except Exception:
            self.wait_driver.until(
                EC.visibility_of_element_located((By.XPATH, '(//button[@class="btn btn-info dropdown-toggle dropdown-toggle-split"])[2]'))
            ).click()
            self.wait_driver.until(
                EC.visibility_of_element_located((By.XPATH, '//a[@id="print-button_1"]'))
            )

        self.wait_for_element_and_click('//a[@id="print-button_1"]')

        wait.until(lambda d: len(d.window_handles) > 1)
        self.driver.switch_to.window(self.driver.window_handles[1])
        wait.until(lambda d: 'Rif. preventivo' not in d.page_source)

        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

        self.wait_for_element_and_click('//a[@id="elimina"]')
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()
        self.wait_loader()

        # ripristino il riferimento dei documenti in fattura elettronica
        self.expandSidebar("Strumenti")
        self.navigate_to_and_wait("Impostazioni")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Fatturazione Elettronica"]'))
        ).click()

        self.wait_for_element_and_click('//div[@class="form-group" and contains(., "Riferimento dei documenti in Fattura Elettronica")]//div//label')
        self.wait_ajax()
