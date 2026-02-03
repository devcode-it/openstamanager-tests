from common.Test import Test
from common.RowManager import RowManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

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
        self.wait_for_element_and_click('//i[@class="fa fa-power-off nav-icon"]')

    def aggiunta_sede(self):
        self.navigateTo("Anagrafiche")
        self.wait_loader()

        self.search_entity("Admin spa")
        self.click_first_result()

        self.wait_for_element_and_click('//a[@id="link-tab_4"]')
        self.wait_for_element_and_click('//div[@id="tab_4"]//i[@class="fa fa-plus"]')
        modal = self.wait_modal()

        self.input(None, 'Nome sede').setValue("Sede di Roma")

        cap_field = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '(//input[@id="cap"])[2]')))
        cap_field.send_keys("35042")

        citta_field = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '(//input[@id="citta"])[2]')))
        citta_field.click()
        citta_field.send_keys("Roma")

        self.wait_for_dropdown_and_select('(//span[@id="select2-id_nazione-container"])[2]', option_xpath='//li[@class="select2-results__option select2-results__option--highlighted"]')
        self.wait_for_element_and_click('(//div[@id="form_2-4"]//i[@class="fa fa-plus"])[4]')

    def creazione_ddt_uscita(self, cliente: str, causale: str, file_importi: str):
        self.expandSidebar("Magazzino")
        self.navigateTo("Ddt in uscita")
        self.wait_loader()

        self.wait_for_element_and_click('//i[@class="fa fa-plus"]')
        modal = self.wait_modal()

        select = self.input(modal, 'Destinatario')
        select.setByText(cliente)
        self.wait_for_element_and_click('//li[@class="select2-results__option select2-results__option--highlighted"]')

        select = self.input(modal, 'Causale trasporto')
        select.setByText(causale)

        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        self.wait_loader()

        row_manager = RowManager(self)
        self.valori = row_manager.compile(file_importi)

        self.wait_for_dropdown_and_select('//span[@id="select2-idsede_destinazione-container"]', option_text='Roma')
        self.wait_for_dropdown_and_select('//span[@id="select2-idstatoddt-container"]', option_text='Evaso')

        self.wait_for_element_and_click('//button[@id="save"]')

    def trasporto(self):
        self.navigateTo("Ddt in uscita")
        self.wait_loader()

        self.click_first_result()
        self.wait_for_element_and_click('//button[@onclick="completaTrasporto()"]')

        self.wait_for_dropdown_and_select('//span[@id="select2-id_segment-container"]', option_text='Standard ddt in entrata')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-success"]')

    def verifica_movimenti(self):
        self.navigateTo("Articoli")
        self.wait_loader()

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Codice"]/input')))
        self.send_keys_and_wait(search_input, "001", wait_modal=False)

        self.click_first_result()
        self.wait_for_element_and_click('//a[@id="link-tab_10"]')

        scarico = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_10"]//tbody//tr[2]//td[7]'))).text
        carico = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_10"]//tbody//tr[7]//td[7]'))).text

        self.assertEqual(scarico, "Sede legale")
        self.assertEqual(carico, "Sede di Roma")