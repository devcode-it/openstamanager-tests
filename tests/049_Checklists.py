from common.Test import Test
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Checklists(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Strumenti")

    def test_checklists(self):
        self.navigate_to_and_wait("Checklists")
        self.checklists("Checklist di Prova da Modificare", "Attività", "Interventi svolti")
        self.checklists("Checklist di Prova da Eliminare", "Attività", "Interventi svolti")
        self.modifica_checklist("Checklist di Prova")
        self.elimina_checklist()
        self.verifica_checklist()
        
    def checklists(self, nome = str, modulo= str, plugin = str):
        self.click_add_button()
        modal = self.wait_modal()

        self.input(modal, 'Nome').setValue(nome)
        self.wait_for_dropdown_and_select('//span[@id="select2-module-container"]', option_text=modulo)
        self.wait_for_element_and_click('//div[@class="modal-footer"]//button[@type="submit"]')

    def modifica_checklist(self, modifica = str):
        self.navigate_to_and_wait("Checklists")

        self.search_by_th_and_click_first("th_Nome", 'Checklist di Prova da Modificare')

        self.input(None,'Nome').setValue(modifica)
        self.click_save_button()

        iframe = self.find(By.XPATH, '(//iframe[@class="cke_wysiwyg_frame cke_reset"])[1]')
        iframe.click()
        iframe.send_keys("TestPadre")
        self.wait_for_element_and_click('(//button[@type="submit"])[2]')

        iframe = self.find(By.XPATH, '(//iframe[@class="cke_wysiwyg_frame cke_reset"])[1]')
        iframe.click()
        iframe.send_keys("TestFiglio")
        self.wait_for_element_and_click('(//span[@class="select2-selection select2-selection--single"])[2]')
        self.wait_for_element_and_click('//li[@class="select2-results__option select2-results__option--selectable select2-results__option--highlighted"]')
        self.wait_for_element_and_click('(//button[@type="submit"])[2]')

        self.navigate_to_and_wait("Checklists")
        self.clear_filters()

    def elimina_checklist(self):
        self.navigate_to_and_wait("Checklists")

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input')))
        self.send_keys_and_wait(search_input, 'Checklist di Prova da Eliminare', wait_modal=False)
        self.click_first_table_row()

        self.delete_current_and_clear()

    def verifica_checklist(self):
        self.navigate_to_and_wait("Checklists")

        self.search_by_th("th_Nome", "Checklist di Prova")
        modificato = self.get_table_text(1, 2)
        self.assertEqual("Checklist di Prova", modificato)
        self.clear_filters()

        self.search_by_th("th_Nome", "Checklist di Prova da Eliminare")

        self.navigate_to_and_wait("Attività")

        self.wait_for_element_and_click('//div[@id="tab_0"]//tbody//tr[2]//td[2]')
        self.wait_for_element_and_click('//a[@href="#tab_checks"]')
        self.wait_for_element_and_click('(//a[@data-title="Aggiungi check"])[2]')

        self.wait_for_element_and_click('//div[@class="modal-content"]//span[@class="select2-selection__placeholder"]')
        self.wait_for_element_and_click('//li[@class="select2-results__option select2-results__option--selectable select2-results__option--highlighted"]')
        self.wait_for_element_and_click('//button[@id="check-add"]')

        TestPadre = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '(//div[@id="tab_checks"]//tbody//td[2]//span)[1]'))).text
        TestFiglio = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '(//div[@id="tab_checks"]//tbody//td[2]//span)[2]'))).text
        self.assertEqual("TestPadre", TestPadre)
        self.assertEqual("TestFiglio", TestFiglio)

        self.wait_for_element_and_click('(//input[@class="checkbox unblockable"])[2]')

        test1 = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '(//input[@class="checkbox unblockable"])[1]'))).is_selected()
        test2 = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '(//input[@class="checkbox unblockable"])[2]'))).is_selected()
        self.assertEqual(test1, False)
        self.assertEqual(test2, True)