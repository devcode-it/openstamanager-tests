from common.Test import Test, get_html
from common.RowManager import RowManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class Contratti(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Vendite")

    def test_plugin_contratto(self):
        self.consuntivo()   
        self.pianificazione_attivita()
        self.rinnovi()
        self.pianificazione_fatturazione()
        self.wait_for_element_and_click('//i[@class="fa fa-power-off nav-icon"]')

    def consuntivo(self):
        self.navigateTo("Contratti")
        self.wait_loader()

        self.send_keys_and_wait(self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))), "Contratto di Prova", wait_modal=False)

        self.wait_for_element_and_click('//tbody//tr/td[2]')
        self.wait_for_element_and_click('//a[@id="link-tab_13"]')

        budget = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_13"]//span[@class="text-success"]'))
        ).text
        self.assertEqual(budget, "+ 264,80 €")

        self.navigateTo("Contratti")
        self.wait_loader()
        self.wait_for_element_and_click('//i[@class="deleteicon fa fa-times"]')

    def pianificazione_attivita(self):
        self.navigateTo("Contratti")
        self.wait_loader()

        self.wait_for_element_and_click('//i[@class="fa fa-plus"]')
        modal = self.wait_modal()

        self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="nome"]'))).send_keys("Manutenzione")
        self.wait_for_dropdown_and_select('//span[@id="select2-idanagrafica-container"]', option_text='Cliente')
        self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="data_accettazione"]'))).send_keys("01/01/2026")
        self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="data_conclusione"]'))).send_keys("31/12/2026")
        self.wait_for_element_and_click('//button[@class="btn btn-primary"]')

        self.wait_for_element_and_click('//a[@class="btn btn-primary"]')

        self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("Manutenzione")
        self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="qta"]'))).send_keys("12")
        self.wait_for_dropdown_and_select('//span[@id="select2-um-container"]', option_text='pz')
        self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("50")
        self.wait_for_element_and_click('//button[@class="btn btn-primary pull-right"]')

        self.driver.execute_script('window.scrollTo(0,0)')
        self.wait_for_dropdown_and_select('//span[@id="select2-idstato-container"]', option_text='In lavorazione')
        self.wait_for_element_and_click('//button[@id="save"]')

        self.wait_for_element_and_click('//a[@id="link-tab_14"]')

        self.wait_for_dropdown_and_select('//span[@id="select2-id_tipo_promemoria-container"]', option_text='Generico')
        self.wait_for_element_and_click('//button[@id="add_promemoria"]')

        description_field = self.wait_for_element_and_click('(//iframe[@class="cke_wysiwyg_frame cke_reset"])[3]')
        description_field = self.wait_driver.until(EC.visibility_of_element_located(
            (By.XPATH, '(//iframe[@class="cke_wysiwyg_frame cke_reset"])[3]')
        ))
        self.send_keys_and_wait(description_field, "Test")

        self.wait_for_dropdown_and_select('//span[@id="select2-id_segment-container"]', option_text='Standard attività')
        self.wait_for_element_and_click('//div[@class="modal-content"]//button[@class="btn btn-primary"]')
        self.wait_loader()

        self.wait_for_element_and_click('//button[@class="btn btn-primary btn-sm  "]')
        description_field = self.wait_for_element_and_click('(//iframe[@class="cke_wysiwyg_frame cke_reset"])[3]')
        description_field = self.wait_driver.until(EC.visibility_of_element_located(
            (By.XPATH, '(//iframe[@class="cke_wysiwyg_frame cke_reset"])[3]')
        ))

        self.wait_for_element_and_click('(//label[@class="btn btn-default active"])[2]')
        self.wait_for_element_and_click('//div[@class="modal-footer"]//button[@class="btn btn-success"]')

        self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//tbody//tr[1]//a')))

    def rinnovi(self):
        self.navigateTo("Contratti")
        self.wait_loader()

        self.wait_for_element_and_click('//tbody//tr//td[2]')

        self.wait_for_element_and_click('(//label[@for="rinnovabile"])[2]')
        self.wait_for_element_and_click('//button[@id="save"]')

    def pianificazione_fatturazione(self):
        self.navigateTo("Contratti")
        self.wait_loader()

        self.send_keys_and_wait(self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))), "Manutenzione", wait_modal=False)

        self.wait_for_element_and_click('//tbody//tr//td[2]')
        self.wait_for_element_and_click('//a[@id="link-tab_26"]')
        self.wait_for_element_and_click('//button[@id="pianifica"]')

        self.wait_for_element_and_click('(//div[@class="nav-tabs-custom"]//a[@class="nav-link"])[2]')
        self.wait_for_element_and_click('//button[@id="btn_procedi"]')
        self.wait_for_element_and_click('(//button[@class="btn btn-primary btn-sm "])[1]')

        self.wait_for_dropdown_and_select('//span[@id="select2-idtipodocumento-container"]', option_text='Fattura immediata di vendita')
        self.wait_for_element_and_click('//button[@class="btn btn-primary pull-right"]')

        self.navigateTo("Dashboard")
        self.wait_loader()

        self.wait_for_element_and_click('(//div[@id="widget_11"]//div)[2]')
        self.wait_for_element_and_click('(//div[@class="month-button-wrapper mr-2 mb-2"])[2]')
        self.wait_for_element_and_click('//button[@class="btn btn-success btn-sm"]')

        self.wait_for_dropdown_and_select('//span[@id="select2-idtipodocumento-container"]', option_text='Fattura immediata di vendita')
        self.wait_for_element_and_click('//button[@class="btn btn-primary pull-right"]')

        self.navigateTo("Contratti")
        self.wait_loader()

        self.wait_for_element_and_click('//tbody//tr//td[2]')
        self.wait_for_element_and_click('//a[@id="link-tab_26"]')

        link = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_26"]//tbody//tr//td[2]'))).text
        self.assertEqual(link, "Fattura num. del 01/01/2026 ( Bozza)")

        self.navigateTo("Contratti")
        self.wait_loader()
        self.wait_for_element_and_click('//i[@class="deleteicon fa fa-times"]')
