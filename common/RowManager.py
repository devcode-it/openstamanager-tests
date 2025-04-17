from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebElement
from .Test import Test, get_text
from .Input import Input, Select
from .functions import get_cache_directory
import json
import os
import glob

class RowManager:
    def __init__(self, tester: Test):
        self.tester = tester
        self.wait = WebDriverWait(self.tester.driver, 10)

    def get_button(self, name):
        xpath = f'//button[contains(., "{name}")]'
        return self.tester.find(By.XPATH, xpath)

    def add_sconto(self, data: dict):
        self.tester.find(By.XPATH, '//button[@class="btn btn-primary dropdown-toggle"]').click()
        self.tester.find(By.XPATH, '//a[@data-title="Aggiungi sconto/maggiorazione"]').click()
        modal = self.tester.wait_modal()

        if 'descrizione' in data:
            self.input(modal, 'Descrizione').setValue(data['descrizione'])

        if 'sconto_percentuale' in data:
            self.input(
                modal, 'Sconto/maggiorazione percentuale').setValue(data['sconto_percentuale'])
        elif 'sconto_unitario' in data:
            self.input(
                modal, 'Sconto/maggiorazione unitario').setValue(data['sconto_unitario'])

        submit_button = modal.find_element(By.CSS_SELECTOR, 'button[onclick="submitForm()"]')
        submit_button.click()
        self.wait.until(EC.staleness_of(modal))

    def add_descrizione(self, data: dict):
        self.get_button('Descrizione').click()
        modal = self.tester.wait_modal()

        self.input(modal, 'Descrizione').setValue(data['descrizione'])

        submit_button = modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        submit_button.click()
        self.wait.until(EC.staleness_of(modal))

    def add_riga(self, data: dict):
        self.tester.find(By.XPATH, '//a[@class="btn btn-primary"]').click()
        modal = self.tester.wait_modal()

        self.fill(modal, data)

        submit_button = modal.find_element(By.CSS_SELECTOR, 'button[onclick="submitForm()"]')
        submit_button.click()
        self.wait.until(EC.staleness_of(modal))

    def add_articolo(self, data: dict):
        article_code = data.get('codice', '')

        self.tester.find(By.XPATH, '//span[@id="select2-id_articolo-container"]').click()
        search_input = self.tester.find(By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input[@type="search"]')
        search_input.send_keys(article_code, Keys.ENTER)

        self.wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@onclick="salvaArticolo()"]')))

        save_button = self.tester.find(By.XPATH, '//button[@onclick="salvaArticolo()"]')
        save_button.click()

        self.wait.until(EC.invisibility_of_element_located((By.XPATH, '//button[@onclick="salvaArticolo()"]')))

    def fill(self, modal, data: dict):
        self.input(modal, 'Descrizione').setValue(data['descrizione'])

        if 'qta' in data:
            self.input(modal, 'Q.tà').setValue(data['qta'])

        if (self.input(modal, 'Prezzo unitario di vendita')):
            self.input(modal, 'Prezzo unitario di vendita').setValue(
                data['prezzo_unitario'])
        else:
            self.input(modal, 'Prezzo unitario').setValue(
                data['prezzo_unitario'])

        sconto_xpath = Input.xpath(modal, None, 'input[@id="sconto"]')
        sconto_input = self.tester.find(By.XPATH, sconto_xpath)
        sconto = Input(self.tester.driver, sconto_input)
        if 'sconto_unitario' in data:
            sconto.setValue(data['sconto_unitario'])
            data['tipo_sconto'] = 'UNT'
        elif 'sconto_percentuale' in data:
            sconto.setValue(data['sconto_percentuale'])
            data['tipo_sconto'] = 'PRC'

        if 'tipo_sconto' in data:
            tipo_sconto_xpath = Input.xpath(
                modal, None, 'select[@name="tipo_sconto"]')
            tipo_sconto_input = self.tester.find(By.XPATH, tipo_sconto_xpath)
            tipo_sconto = Select(self.tester.driver, tipo_sconto_input)
            tipo_sconto.setValue(data['tipo_sconto'])

        if 'iva' in data:
            select = self.input(modal, 'IVA')
            select.setByText(data['iva'])

        if 'rivalsa_inps' in data:
            select = self.input(modal, 'Rivalsa INPS')
            select.setByText(data['rivalsa_inps'])

        if 'ritenuta_acconto' in data:
            select = self.input(modal, "Ritenuta d'acconto")
            select.setByText(data['ritenuta_acconto'])

    def input(self, element: WebElement, name=None, css_id=None):
        return self.tester.input(element, name, css_id)

    def compile(self, filename: str):
        importi = self.read(filename)

        if not importi or 'righe' not in importi:
            return {}

        for riga in importi.get('righe', []):
            if 'tipo' not in riga:
                continue

            if riga['tipo'] == 'riga':
                self.add_riga(riga)
            elif riga['tipo'] == 'articolo':
                self.add_articolo(riga)
            elif riga['tipo'] == 'descrizione':
                self.add_descrizione(riga)
            elif riga['tipo'] == 'sconto':
                self.add_sconto(riga)

        self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='card-header']/parent::*//table//tr")))

        table_pattern = "//div[@class='card-header']/parent::*//table//tr[contains(., '|name|')][1]//td[2]"
        valori = {}

        for key, value in importi.get('totali', {}).items():
            try:
                totale = self.tester.find(
                    By.XPATH, table_pattern.replace('|name|', key.upper() + ':'))
                valori[key] = get_text(totale).split()[0]
            except Exception:
                continue

        return valori

    def read(self, filename: str) -> dict:
        if not os.path.exists(filename):
            directory = os.path.dirname(get_cache_directory())
            path = os.path.join(directory, filename)
        else:
            path = filename

        if os.path.exists(path):
            try:
                with open(path, 'r') as json_file:
                    return json.load(json_file)
            except json.JSONDecodeError:
                print(f"Error: Invalid JSON format in file {path}")
                return {}
            except Exception as e:
                print(f"Error reading file {path}: {str(e)}")
                return {}
        else:
            print(f"Warning: File not found: {path}")
            return {}

    @staticmethod
    def list() -> list:
        directory = os.path.dirname(get_cache_directory())
        path = os.path.join(directory, 'importi')

        if not os.path.exists(path):
            print(f"Warning: Directory not found: {path}")
            return []

        return glob.glob(os.path.join(path, "*.json"))
