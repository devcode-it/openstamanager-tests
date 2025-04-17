#!/usr/bin/env python3
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from common.Test import Test
from common.functions import (
    wait_for_element_and_click,
    wait_loader,
    search_entity,
    click_first_result,
    clear_filters,
    wait_for_dropdown_and_select,
    wait_for_search_results
)
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
            wait_for_element_and_click(self.driver, self.wait_driver, '//button[@onclick="abilitaSottoModuli(this)"]')
            wait_for_element_and_click(self.driver, self.wait_driver, '//button[@class="swal2-confirm btn btn-lg btn-primary"]')
            wait_for_element_and_click(self.driver, self.wait_driver, '//div[@class="toast-message"]')
        self.logger.info("Tutti i moduli sono stati attivati con successo")

    def compila_azienda(self):
        self.logger.info("Compilazione delle informazioni aziendali")
        self.navigateTo("Anagrafiche")
        wait_for_element_and_click(self.driver, self.wait_driver, '//tbody//tr//td[2]')
        wait_loader(self.driver, self.wait_driver)
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

        wait_for_element_and_click(self.driver, self.wait_driver, '//button[@id="save"]')
        wait_loader(self.driver, self.wait_driver)
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
        self.logger.debug(f"Creazione nuova anagrafica: {nome} (Tipo: {tipo})")
        self.navigateTo("Anagrafiche")

        wait_for_element_and_click(self.driver, self.wait_driver, '//i[@class="fa fa-plus"]')
        modal = self.wait_modal()
        self.input(modal, 'Denominazione').setValue(nome)
        self.input(modal, 'Tipo di anagrafica').setByText(tipo)
        submit_button = modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        submit_button.click()
        wait_loader(self.driver, self.wait_driver)

    def _compila_anagrafica_estera(self, nome: str, piva: str, nazione: str, citta: str):
        self.logger.debug(f"Compilazione dettagli per anagrafica estera: {nome}")
        self.navigateTo("Anagrafiche")

        self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Ragione-sociale"]')))

        search_entity(self.driver, self.wait_driver, nome)

        click_first_result(self.driver, self.wait_driver)
        wait_loader(self.driver, self.wait_driver)

        wait_for_dropdown_and_select(
            self.driver, self.wait_driver,
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

        wait_for_element_and_click(self.driver, self.wait_driver, '//button[@id="save"]')
        wait_loader(self.driver, self.wait_driver)

        clear_filters(self.driver, self.wait_driver)
        self.navigateTo("Anagrafiche")
        wait_loader(self.driver, self.wait_driver)

    def _compila_campi_azienda(self, campi: dict):
        for campo, valore in campi.items():
            input_field = self.input(None, campo)
            if input_field:
                input_field.setValue(valore)
            else:
                self.logger.warning(f"Campo '{campo}' non trovato")
