from common.Test import Test
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Checklists(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Strumenti")

    def test_checklists(self):
        self.navigateTo("Checklists")
        self.checklists("Checklist di Prova da Modificare", "Attività", "Interventi svolti")
        self.checklists("Checklist di Prova da Eliminare", "Attività", "Interventi svolti")
        self.modifica_checklist("Checklist di Prova")
        self.elimina_checklist()
        self.verifica_checklist()
        self.wait_for_element_and_click('//i[@class="fa fa-power-off nav-icon"]')
        
    def checklists(self, nome = str, modulo= str, plugin = str):
        self.wait_for_element_and_click('//i[@class="fa fa-plus"]')
        modal = self.wait_modal()

        self.input(modal, 'Nome').setValue(nome)
        self.wait_for_dropdown_and_select('//span[@id="select2-module-container"]', option_text=modulo)
        self.wait_for_element_and_click('//div[@class="modal-footer"]//button[@type="submit"]')

    def modifica_checklist(self, modifica = str):
        self.navigateTo("Checklists")
        self.wait_loader()

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input')))
        self.send_keys_and_wait(search_input, 'Checklist di Prova da Modificare', wait_modal=False)
        self.wait_for_element_and_click('//tbody//tr//td[2]')

        self.input(None,'Nome').setValue(modifica)
        self.wait_for_element_and_click('//div[@id="tab_0"]//button[@id="save"]')

        iframe = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '(//iframe[@class="cke_wysiwyg_frame cke_reset"])[1]')))
        iframe.click()
        iframe.send_keys("TestPadre")
        self.wait_for_element_and_click('(//button[@type="submit"])[2]')

        iframe = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '(//iframe[@class="cke_wysiwyg_frame cke_reset"])[1]')))
        iframe.click()
        iframe.send_keys("TestFiglio")
        self.wait_for_element_and_click('(//span[@class="select2-selection select2-selection--single"])[3]')
        self.wait_for_element_and_click('//li[@class="select2-results__option select2-results__option--highlighted"]')
        self.wait_for_element_and_click('(//button[@type="submit"])[2]')

        self.navigateTo("Checklists")
        self.wait_loader()
        self.wait_for_element_and_click('//th[@id="th_Nome"]/i[@class="deleteicon fa fa-times"]')

    def elimina_checklist(self):
        self.navigateTo("Checklists")
        self.wait_loader()

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input')))
        self.send_keys_and_wait(search_input, 'Checklist di Prova da Eliminare', wait_modal=False)
        self.wait_for_element_and_click('//tbody//tr//td[2]')

        self.wait_for_element_and_click('//div[@id="tab_0"]//a[@class="btn btn-danger ask"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')
        self.wait_for_element_and_click('//th[@id="th_Nome"]/i[@class="deleteicon fa fa-times"]')

    def verifica_checklist(self):
        self.navigateTo("Checklists")
        self.wait_loader()

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input')))
        self.send_keys_and_wait(search_input, "Checklist di Prova", wait_modal=False)
        modificato = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//tbody//tr[1]//td[2]'))).text
        self.assertEqual("Checklist di Prova", modificato)
        self.wait_for_element_and_click('//i[@class="deleteicon fa fa-times"]')

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input')))
        self.send_keys_and_wait(search_input, "Checklist di Prova da Eliminare", wait_modal=False)

        self.navigateTo("Attività")

        self.wait_for_element_and_click('//div[@id="tab_0"]//tbody//tr[2]//td[2]')
        self.wait_for_element_and_click('//a[@href="#tab_checks"]')
        self.wait_for_element_and_click('(//a[@data-title="Aggiungi check"])[2]')

        self.wait_for_element_and_click('//div[@class="modal-content"]//span[@class="select2-selection__placeholder"]')
        self.wait_for_element_and_click('//li[@class="select2-results__option select2-results__option--highlighted"]')
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