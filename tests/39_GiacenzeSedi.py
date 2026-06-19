from common.Test import Test
from common.RowManager import RowManager
from selenium.webdriver.common.by import By

class GiacenzeSedi(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Magazzino")

    def test_giacenze_sedi(self):
        self.aggiunta_sede()
        importi = RowManager.list()
        self.creazione_ddt_uscita("Admin spa", "Vendita", importi[0])
        self.trasporto()
        self.verifica_movimenti()

    def aggiunta_sede(self):
        self.navigate_to_and_wait("Anagrafiche")
        self.search_entity_and_click_first("Admin spa")

        self.wait_for_element_and_click('//a[@id="link-tab_4"]')
        self.wait_for_element_and_click('//div[@id="tab_4"]//i[@class="fa fa-plus"]')
        modal = self.wait_modal()

        self.input(None, 'Nome sede').setValue("Sede di Roma")

        cap_field = self.find(By.XPATH, '(//input[@id="cap"])[2]')
        cap_field.send_keys("35042")

        citta_field = self.find(By.XPATH, '(//input[@id="citta"])[2]')
        citta_field.click()
        citta_field.send_keys("Roma")

        self.wait_for_dropdown_and_select('(//span[@id="select2-id_nazione-container"])[2]', option_xpath='//li[@class="select2-results__option select2-results__option--selectable select2-results__option--highlighted"]')
        self.wait_for_element_and_click('(//div[@id="form_2-4"]//i[@class="fa fa-plus"])[4]')

    def creazione_ddt_uscita(self, cliente: str, causale: str, file_importi: str):
        self.expandSidebar("Magazzino")
        self.navigate_to_and_wait("Ddt in uscita")

        self.click_add_button()
        modal = self.wait_modal()

        select = self.input(modal, 'Destinatario')
        select.setByText(cliente)
        self.wait_for_element_and_click('//li[@class="select2-results__option select2-results__option--selectable select2-results__option--highlighted"]')

        select = self.input(modal, 'Causale trasporto')
        select.setByText(causale)

        self.submit_modal(modal)

        row_manager = RowManager(self)
        self.valori = row_manager.compile(file_importi)

        self.wait_for_dropdown_and_select('//span[@id="select2-id_sede_destinazione-container"]', option_text='Roma')
        self.select_state('Evaso')

        self.wait_for_element_and_click('//button[@id="save"]')

    def trasporto(self):
        self.navigate_to_and_wait("Ddt in uscita")

        self.click_first_result()
        self.wait_for_element_and_click('//button[@onclick="completaTrasporto()"]')

        self.wait_for_dropdown_and_select('//span[@id="select2-id_segment-container"]', option_text='Standard ddt in entrata')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-success"]')

    def verifica_movimenti(self):
        self.navigate_to_and_wait("Articoli")

        self.search_by_th_and_click_first("th_Codice", "001")
        self.wait_for_element_and_click('//a[@id="link-tab_10"]')

        scarico = self.find(By.XPATH, '//div[@id="tab_10"]//tbody//tr[4]//td[3]').text
        carico = self.find(By.XPATH, '(//div[@id="tab_10"]//tbody//tr[2]//td[2])[4]').text

        self.assertEqual(scarico, "1,00")
        self.assertEqual(carico, "1,00")