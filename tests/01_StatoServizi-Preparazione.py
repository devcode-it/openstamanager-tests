#!/usr/bin/env python3
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from common.Test import Test
# Helper functions are now available as methods through TestHelperMixin
import logging

class StatoServizi(Test):
    def setUp(self):
        super().setUp()
        self.wait_driver = WebDriverWait(self.driver, 10)
        self.logger = logging.getLogger(self.__class__.__name__)

    def test_stato_servizi(self):
        self.logger.info("Avvio del test di preparazione dello stato dei servizi")
        self.attiva_moduli()
        self.compila_azienda()
        self.creazione_fornitore_estero()
        self.creazione_cliente_estero()
        self.logger.info("Preparazione dello stato dei servizi completata con successo")

    def attiva_moduli(self):
        self.logger.info("Attivazione dei moduli nascosti")
        self.expandSidebar("Strumenti")
        self.navigateTo("Stato dei servizi")
        for i in range(3):
            self.wait_for_element_and_click('//button[@onclick="abilitaSottoModuli(this)"]')
            self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-primary"]')
            self.wait_for_element_and_click('//div[@class="toast-message"]')
        self.logger.info("Tutti i moduli sono stati attivati con successo")

    def compila_azienda(self):
        self.logger.info("Compilazione delle informazioni aziendali")
        self.navigateTo("Anagrafiche")
        self.wait_for_element_and_click('//tbody//tr//td[2]')
        self.wait_loader()
        self._compila_campi_azienda({
            'Partita IVA': '05024030289',
            'Codice fiscale': '05024030289',
            'Tipologia': 'Azienda',
            'C.A.P.': '35042',
            'Città': 'Este'
        })

        indirizzo = self.wait_driver.until(
            EC.presence_of_element_located((By.XPATH, '//input[@id="indirizzo"]'))
        )
        indirizzo.clear()
        indirizzo.send_keys("Via Rovigo, 51")

        self.wait_for_element_and_click('//button[@id="save"]')
        self.wait_loader()
        self.logger.info("Informazioni aziendali salvate con successo")

    def creazione_fornitore_estero(self):
        self.logger.info("Creazione del fornitore estero")
        self._crea_anagrafica("Fornitore Estero", "Fornitore")
        self._compila_anagrafica_estera("Fornitore Estero", "05024030286", "Germania", "Berlino")
        self.logger.info("Fornitore estero creato con successo")

    def creazione_cliente_estero(self):
        self.logger.info("Creazione del cliente estero")
        self._crea_anagrafica("Cliente Estero", "Cliente")
        self._compila_anagrafica_estera("Cliente Estero", "05024030288", "Germania", "Piacenza d'Adige")
        self.logger.info("Cliente estero creato con successo")

    def _crea_anagrafica(self, nome: str, tipo: str):
        self.navigateTo("Anagrafiche")

        self.wait_for_element_and_click('//i[@class="fa fa-plus"]')
        modal = self.wait_modal()
        self.input(modal, 'Denominazione').setValue(nome)
        self.input(modal, 'Tipo di anagrafica').setByText(tipo)
        submit_button = modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        submit_button.click()
        self.wait_loader()

    def _compila_anagrafica_estera(self, nome: str, piva: str, nazione: str, citta: str):
        self.navigateTo("Anagrafiche")

        self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Ragione-sociale"]')))

        self.search_entity(nome)

        self.click_first_result()
        self.wait_loader()

        self.wait_for_dropdown_and_select(
            '//span[@id="select2-id_nazione-container"]',
            option_text=nazione
        )

        self._compila_campi_azienda({
            'Partita IVA': piva,
            'Codice fiscale': piva,
            'Tipologia': 'Azienda',
            'C.A.P.': '35042',
            'Città': citta
        })

        indirizzo = self.wait_driver.until(
            EC.presence_of_element_located((By.XPATH, '//input[@id="indirizzo"]'))
        )
        indirizzo.clear()
        indirizzo.send_keys('Via controllo caratteri speciali: &"<>èéàòùì?\'\'`')

        self.wait_for_element_and_click('//button[@id="save"]')
        self.wait_loader()

        self.clear_filters()
        self.navigateTo("Anagrafiche")
        self.wait_loader()

    def _compila_campi_azienda(self, campi: dict):
        for campo, valore in campi.items():
            input_field = self.input(None, campo)
            if input_field:
                input_field.setValue(valore)
            else:
                self.logger.warning(f"Campo '{campo}' non trovato")
