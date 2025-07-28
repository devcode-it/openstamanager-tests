from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebElement
from selenium.common.exceptions import NoSuchElementException
from .Test import Test, get_text
from .Input import Input, Select, Checkbox
from .functions import get_cache_directory, wait_for_element_and_click, send_keys_and_click, wait_loader, wait_for_dropdown_and_select
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
        wait_for_dropdown_and_select(
            self.tester.driver,
            self.wait,
            '//button[@class="btn btn-primary dropdown-toggle"]',
            option_xpath='//a[@data-title="Aggiungi sconto/maggiorazione"]'
        )
        modal = self.tester.wait_modal()

        if 'descrizione' in data:
            descrizione_input = self.input_exact(modal, 'Descrizione')
            if descrizione_input:
                descrizione_input.setValue(data['descrizione'])
            else:
                print(f"Errore: campo 'Descrizione' non trovato nel modal")

        if 'sconto_percentuale' in data:
            sconto_perc_input = self.input(modal, 'Sconto/maggiorazione percentuale')
            if sconto_perc_input:
                sconto_perc_input.setValue(data['sconto_percentuale'])
            else:
                print(f"Errore: campo 'Sconto/maggiorazione percentuale' non trovato nel modal")
        elif 'sconto_unitario' in data:
            sconto_unit_input = self.input(modal, 'Sconto/maggiorazione unitario')
            if sconto_unit_input:
                sconto_unit_input.setValue(data['sconto_unitario'])
            else:
                print(f"Errore: campo 'Sconto/maggiorazione unitario' non trovato nel modal")

        wait_for_element_and_click(self.tester.driver, self.wait, 'button[onclick="submitForm()"]', By.CSS_SELECTOR)
        self.wait.until(EC.staleness_of(modal))

    def add_descrizione(self, data: dict):
        button = self.get_button('Descrizione')
        button.click()
        wait_loader(self.tester.driver, self.wait)
        modal = self.tester.wait_modal()

        descrizione_input = self.input_exact(modal, 'Descrizione')
        if descrizione_input:
            descrizione_input.setValue(data['descrizione'])
        else:
            print(f"Errore: campo 'Descrizione' non trovato nel modal")

        wait_for_element_and_click(self.tester.driver, self.wait, 'button[type="submit"]', By.CSS_SELECTOR)
        self.wait.until(EC.staleness_of(modal))

    def add_riga(self, data: dict):
        wait_for_element_and_click(self.tester.driver, self.wait, '//a[@class="btn btn-primary"]')
        modal = self.tester.wait_modal()

        self.fill(modal, data)

        wait_for_element_and_click(self.tester.driver, self.wait, 'button[onclick="submitForm()"]', By.CSS_SELECTOR)
        self.wait.until(EC.staleness_of(modal))

    def add_articolo(self, data: dict):
        article_code = data.get('codice', '')

        wait_for_dropdown_and_select(
            self.tester.driver,
            self.wait,
            '//span[@id="select2-id_articolo-container"]',
            option_text=article_code
        )

        wait_for_element_and_click(self.tester.driver, self.wait, '//button[@onclick="salvaArticolo()"]')

    def fill(self, modal, data: dict):
        descrizione_input = self.input_exact(modal, 'Descrizione')
        if descrizione_input:
            descrizione_input.setValue(data['descrizione'])
        else:
            print(f"Errore: campo 'Descrizione' non trovato nel modal")

        if 'qta' in data:
            qta_input = self.input(modal, 'Q.tà')
            if qta_input:
                qta_input.setValue(data['qta'])
            else:
                print(f"Errore: campo 'Q.tà' non trovato nel modal")

        prezzo_vendita_input = self.input(modal, 'Prezzo unitario di vendita')
        if prezzo_vendita_input:
            prezzo_vendita_input.setValue(data['prezzo_unitario'])
        else:
            prezzo_unitario_input = self.input(modal, 'Prezzo unitario')
            if prezzo_unitario_input:
                prezzo_unitario_input.setValue(data['prezzo_unitario'])
            else:
                print(f"Errore: nessun campo prezzo trovato nel modal")

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
            iva_select = self.input(modal, 'IVA')
            if iva_select:
                iva_select.setByText(data['iva'])
            else:
                print(f"Errore: campo 'IVA' non trovato nel modal")

        if 'rivalsa_inps' in data:
            rivalsa_select = self.input(modal, 'Rivalsa INPS')
            if rivalsa_select:
                rivalsa_select.setByText(data['rivalsa_inps'])
            else:
                print(f"Errore: campo 'Rivalsa INPS' non trovato nel modal")

        if 'ritenuta_acconto' in data:
            ritenuta_select = self.input(modal, "Ritenuta d'acconto")
            if ritenuta_select:
                ritenuta_select.setByText(data['ritenuta_acconto'])
            else:
                print(f"Errore: campo 'Ritenuta d'acconto' non trovato nel modal")

    def input(self, element: WebElement, name=None, css_id=None):
        return self.tester.input(element, name, css_id)

    def input_exact(self, element: WebElement, name: str):
        """Find input by exact label text match"""
        element_id = element.get_attribute("id")

        prefix = ''
        if element_id:
            prefix = '//*[@id="' + element_id + '"]'

        # Use exact text match instead of contains
        prefix += f'//label[text()="{name}" or normalize-space(text())="{name}"]/parent::div/parent::div//'

        element_types = [
            {'xpath': prefix + 'select', 'class': Select},
            {'xpath': prefix + 'input[@type="checkbox"]', 'class': Checkbox},
            {'xpath': prefix + 'input', 'class': Input},
            {'xpath': prefix + 'textarea', 'class': Input}
        ]

        for elem_type in element_types:
            try:
                found_element = element.find_element(By.XPATH, elem_type['xpath'])
                return elem_type['class'](self.tester.driver, found_element)
            except NoSuchElementException:
                continue

        return None

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
