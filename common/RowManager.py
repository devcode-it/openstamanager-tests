from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebElement
from selenium.webdriver.support.ui import Select
from .Test import Test, get_text
from .Input import Input, Select
from .functions import get_cache_directory
import json
import os
import sys
import glob
import time


class RowManager:
    def __init__(self, tester: Test):
        self.tester = tester

    def get_button(self, name):
        xpath = ''.join(['//button[contains(., "', name, '")]'])
        return self.tester.find(By.XPATH, xpath)

    def add_sconto(self, data: dict):
        # Aggiunge un nuovo sconto. 
        self.tester.find(By.XPATH, '//button[@class="btn btn-primary dropdown-toggle"]').click()
        self.tester.find(By.XPATH, '//a[@data-title="Aggiungi sconto/maggiorazione"]').click()
        modal = self.tester.wait_modal()

        if 'descrizione' in data:
            self.input(modal, 'Descrizione').setValue(data['descrizione'])

        if 'sconto_percentuale' in data:
            self.input(
                modal, 'Sconto/maggiorazione percentuale').setValue(data['sconto_percentuale'])
        else:
            self.input(
                modal, 'Sconto/maggiorazione unitario').setValue(data['sconto_unitario'])

        # Submit
        modal.find_element(By.CSS_SELECTOR, 'button[onclick="submitForm()"]').click()
        sleep(1)

    def add_descrizione(self, data: dict):
        # Aggiunge una nuova descrizione. 
        self.get_button('Descrizione').click()
        modal = self.tester.wait_modal()

        self.input(modal, 'Descrizione').setValue(data['descrizione'])

        # Submit
        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        sleep(1)

    def add_riga(self, data: dict):
        # Aggiunge una nuova riga. 
        self.tester.find(By.XPATH, '//a[@class="btn btn-primary"]').click()
        modal = self.tester.wait_modal()

        # Completamento informazioni
        self.fill(modal, data)

        # Submit
        modal.find_element(By.CSS_SELECTOR, 'button[onclick="submitForm()"]').click()
        sleep(1)

    def add_articolo(self, data: dict):

        # Selezione articolo
        self.tester.find(By.XPATH, '//span[@id="select2-id_articolo-container"]').click()
        self.tester.find(By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input[@type="search"]').send_keys("002", Keys.ENTER)
        sleep(1)
        self.tester.find(By.XPATH, '//button[@onclick="salvaArticolo()"]').click()
        sleep(1)

       

    def fill(self, modal, data: dict):
        # Completa le informazioni per la creazione di un nuovo elemento. 
        self.input(modal, 'Descrizione').setValue(data['descrizione'])

        if 'qta' in data:
            self.input(modal, 'Q.tà').setValue(data['qta'])

        if (self.input(modal, 'Prezzo unitario di vendita')):
            self.input(modal, 'Prezzo unitario di vendita').setValue(
                data['prezzo_unitario'])
        else:
            self.input(modal, 'Prezzo unitario').setValue(
                data['prezzo_unitario'])

        # Impostazione valore sconto
        sconto_xpath = Input.xpath(modal, None, 'input[@id="sconto"]')
        sconto_input = self.tester.find(By.XPATH, sconto_xpath)
        sconto = Input(self.tester.driver, sconto_input)
        if 'sconto_unitario' in data:
            sconto.setValue(data['sconto_unitario'])
            data['tipo_sconto'] = 'UNT'
        elif 'sconto_percentuale' in data:
            sconto.setValue(data['sconto_percentuale'])
            data['tipo_sconto'] = 'PRC'

        # Impostazione del tipo sconto
        if 'tipo_sconto' in data:
            tipo_sconto_xpath = Input.xpath(
                modal, None, 'select[@name="tipo_sconto"]')
            tipo_sconto_input = self.tester.find(By.XPATH, tipo_sconto_xpath)
            tipo_sconto = Select(self.tester.driver, tipo_sconto_input)
            tipo_sconto.setValue(data['tipo_sconto'])

        # Selezione IVA
        if 'iva' in data:
            select = self.input(modal, 'IVA')
            select.setByText(data['iva'])
            # select.send_keys(Keys.ENTER)

        # Selezione Rivalsa INPS
        if 'rivalsa_inps' in data:
            select = self.input(modal, 'Rivalsa INPS')
            select.setByText(data['rivalsa_inps'])
            # select.send_keys(Keys.ENTER)

        # Selezione Ritenuta d'acconto
        if 'ritenuta_acconto' in data:
            select = self.input(modal, "Ritenuta d'acconto")
            select.setByText(data['ritenuta_acconto'])
            # select.send_keys(Keys.ENTER)

    def input(self, element: WebElement, name=None, css_id=None):
        return self.tester.input(element, name, css_id)

    def compile(self, filename: str):
        # Compila il documento secondo la configurazione del file indicato.
        importi = self.read(filename)

        for riga in importi['righe']:
            if riga['tipo'] == 'riga':
                self.add_riga(riga)
            elif riga['tipo'] == 'articolo':
                self.add_articolo(riga)
            elif riga['tipo'] == 'descrizione':
                self.add_descrizione(riga)
            elif riga['tipo'] == 'sconto':
                self.add_sconto(riga)

        time.sleep(4)

        tablePattern = "//div[@class='card-header']/parent::*//table//tr[contains(., '|name|')][1]//td[2]"
        valori = {}

        for key, value in importi['totali'].items():
            totale = self.tester.find(
                By.XPATH, tablePattern.replace('|name|', key.upper() + ':'))
            valori[key] = get_text(totale).split()[0]

        return valori




    def read(self, filename: str) -> dict:
        # Restituisce la configurazione delle righe contenuta dal file indicato.
        if not os.path.exists(filename):
            directory = get_cache_directory()
            directory = os.path.dirname(directory)

            path = directory + '/' + filename
        else:
            path = filename

        if os.path.exists(path):
            with open(path, 'r') as json_file:
                data = json.load(json_file)

                return data
        else:
            return dict()

    @staticmethod
    def list() -> dict:
        # Restituisce un elenco di configurazioni di importi disponibili.
        directory = get_cache_directory()
        directory = os.path.dirname(directory)

        path = directory + '/importi'

        return glob.glob(path + "/*.json")
