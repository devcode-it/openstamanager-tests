from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebElement
from selenium.webdriver.support.ui import Select
from .Test import Test, get_input, get_text
from .functions import get_cache_directory
import json
import os
import sys


class RowManager:
    def __init__(self, tester: Test):
        self.tester = tester

    def get_button(self, name):
        xpath = ''.join(['//a[contains(., "', name, '")]'])
        return self.tester.find(By.XPATH, xpath)

    def add_sconto(self, data: dict):
        ''' Aggiunge un nuovo sconto. '''
        self.get_button('Sconto/maggiorazione').click()
        modal = self.tester.wait_modal()

        if 'descrizione' in data:
            self.setValue(get_input(modal, 'Descrizione'), data['descrizione'])

        if 'sconto_percentuale' in data:
            self.setValue(get_input(modal, 'Sconto/maggiorazione percentuale'),
                          data['sconto_percentuale'])
        else:
            self.setValue(get_input(modal, 'Sconto/maggiorazione unitario'),
                          data['sconto_unitario'])

        # Submit
        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        self.tester.wait_loader()

    def add_descrizione(self, data: dict):
        ''' Aggiunge una nuova descrizione. '''
        self.get_button('Descrizione').click()
        modal = self.tester.wait_modal()

        self.setValue(get_input(modal, 'Descrizione'), data['descrizione'])

        # Submit
        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        self.tester.wait_loader()

    def add_riga(self, data: dict):
        ''' Aggiunge una nuova riga. '''
        self.get_button('Riga').click()
        modal = self.tester.wait_modal()

        # Completamento informazioni
        self.fill(modal, data)

        # Submit
        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        self.tester.wait_loader()

    def add_articolo(self, data: dict):
        ''' Aggiunge un nuovo articolo. '''
        self.get_button('Articolo').click()
        modal = self.tester.wait_modal()

        # Selezione articolo
        select = get_input(modal, 'Articolo')
        select.send_keys(data['articolo'])
        select.send_keys(Keys.ENTER)

        # Completamento informazioni
        self.fill(modal, data)

        # Submit
        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        self.tester.wait_loader()

    def fill(self, modal, data: dict):
        ''' Completa le informazioni per la creazione di un nuovo elemento. '''
        self.setValue(get_input(modal, 'Descrizione'), data['descrizione'])

        if 'qta' in data:
            self.setValue(get_input(modal, 'Q.tà'), data['qta'])

        self.setValue(get_input(modal, 'Prezzo unitario di vendita'),
                      data['prezzo_unitario'])

        sconto = get_input(modal, 'Sconto unitario')
        tipo_sconto = 'UNT'
        if 'sconto_unitario' in data:
            self.setValue(sconto, data['sconto_unitario'])
        elif 'sconto_percentuale' in data:
            self.setValue(sconto, data['sconto_percentuale'])
            tipo_sconto = 'PRC'
    
        self.tester.driver.execute_script('$("#tipo_sconto").select2("destroy")')
        select = Select(modal.find_element(By.ID, 'tipo_sconto'))
        select.select_by_value(tipo_sconto)
        
        # Selezione IVA
        if 'iva' in data:
            select = get_input(modal, 'IVA')
            select.send_keys(data['iva'])
            select.send_keys(Keys.ENTER)

        # Selezione Rivalsa INPS
        if 'rivalsa_inps' in data:
            select = get_input(modal, 'Rivalsa INPS')
            select.send_keys(data['rivalsa_inps'])
            select.send_keys(Keys.ENTER)

        # Selezione Ritenuta d'acconto
        if 'ritenuta_acconto' in data:
            select = get_input(modal, "Ritenuta d'acconto")
            select.send_keys(data['ritenuta_acconto'])
            select.send_keys(Keys.ENTER)

    def setValue(self, element: WebElement, value: str):
        self.tester.setValue(element, value)

    def compile(self, filename: str):
        ''' Compila il documento secondo la configurazione del file indicato.'''
        importi = self.read(filename)

        for riga in importi['righe']:
            if riga['tipo'] == 'riga':
                self.add_riga(riga)
            elif riga['tipo'] == 'articolo':
                self.add_riga(riga)
            elif riga['tipo'] == 'descrizione':
                self.add_descrizione(riga)
            elif riga['tipo'] == 'sconto':
                self.add_sconto(riga)

        tablePattern = "//div[@class='panel-heading' and contains(string(), 'Righe')]/parent::*//table//tr[contains(., '|name|')]//td[2]"
        for key, value in importi['totali'].items():
            totale = self.tester.find(
                By.XPATH, tablePattern.replace('|name|', key.upper() + ':'))
            valore = get_text(totale).split()[0]

            self.tester.assertEqual(valore, value)

    def read(self, filename: str) -> dict:
        ''' Restituisce la configurazione delle righe contenuta dal file indicato.'''
        directory = get_cache_directory()
        directory = os.path.dirname(directory)

        path = directory + '/' + filename

        if os.path.exists(path):
            with open(path, 'r') as json_file:
                data = json.load(json_file)

                return data
        else:
            return dict()
