from common.Test import Test
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class StampeContabili(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Contabilità")
        self.navigateTo("Stampe contabili")
        self.wait_loader()

    def test_stampecontabili(self):
        self.apri_stampe_contabili()

    def _get_viewer_text(self, xpath: str) -> str:
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.wait_loader()
        self.wait(EC.visibility_of_element_located((By.XPATH, xpath)))
        text = self.find(By.XPATH, xpath).text
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        return text

    def apri_stampe_contabili(self):
        self.wait_for_element_and_click('//button[@data-title="Stampa registro IVA vendite"]')
        self.wait_for_dropdown_and_select('//span[@id="select2-id_sezionale-container"]', '//ul[@id="select2-id_sezionale-results"]//li[1]')
        self.wait_for_dropdown_and_select('//span[@id="select2-format-container"]', '//ul[@id="select2-format-results"]//li[1]')
        self.wait_for_dropdown_and_select('//span[@id="select2-orientation-container"]', '//ul[@id="select2-orientation-results"]//li[1]')
        self.wait_for_element_and_click('//button[@class="btn btn-primary btn-lg"]')

        stampa = self._get_viewer_text('//div[@id="viewer"]//span[7]')
        self.assertEqual(stampa, "REGISTRO IVA VENDITE DAL 01/01/2026 AL 31/12/2026 - STANDARD VENDITE")

        self.wait_for_element_and_click('//button[@data-title="Stampa registro IVA acquisti"]')
        self.wait_for_dropdown_and_select('//span[@id="select2-id_sezionale-container"]', '//ul[@id="select2-id_sezionale-results"]//li[1]')
        self.wait_for_element_and_click('//button[@class="btn btn-primary btn-lg"]')

        stampa = self._get_viewer_text('//div[@id="viewer"]//span[7]')
        self.assertEqual(stampa, "REGISTRO IVA ACQUISTI DAL 01/01/2026 AL 31/12/2026 - STANDARD ACQUISTI")

        self.wait_for_element_and_click('//button[@data-title="Stampa liquidazione IVA"]')
        self.wait_for_element_and_click('//button[@class="btn btn-primary btn-lg"]')

        stampa = self._get_viewer_text('(//div[@id="viewer"]//span)[6]')
        self.assertEqual(stampa, "PROSPETTO LIQUIDAZIONE IVA DAL 01/01/2026 AL 31/12/2026")

        self.wait_for_element_and_click('//button[@data-title="Stampa Bilancio"]')
        self.wait_for_element_and_click('//button[@class="btn btn-primary btn-lg"]')

        stampa = self._get_viewer_text('//div[@id="viewer"]//span')
        self.assertEqual(stampa, "STAMPA BILANCIO")

        self.wait_for_element_and_click('//button[@class="close"]')

        self.wait_for_element_and_click('//button[@class="btn btn-primary btn-block"]')

        stampa = self._get_viewer_text('//div[@id="viewer"]//span')
        self.assertEqual(stampa, "STAMPA BILANCIO")

        self.wait_for_element_and_click('(//button[@class="btn btn-primary btn-block"])[2]')

        stampa = self._get_viewer_text('(//div[@id="viewer"]//span)[1]')
        self.assertEqual(stampa, "STAMPA BILANCIO")

        self.wait_for_element_and_click('(//button[@class="btn btn-primary btn-block"])[3]')

        stampa = self._get_viewer_text('(//div[@id="viewer"]//span)[9]')
        self.assertEqual(stampa, "FATTURATO MENSILE DAL 01/01/2026 AL 31/12/2026")

        self.wait_for_element_and_click('(//button[@class="btn btn-primary btn-block"])[4]')

        stampa = self._get_viewer_text('(//div[@id="viewer"]//span)[9]')
        self.assertEqual(stampa, "ACQUISTI MENSILI DAL 01/01/2026 AL 31/12/2026")

        self.wait_for_element_and_click('//button[@data-title="Libro giornale"]')
        self.wait_for_element_and_click('//button[@class="btn btn-primary btn-lg"]')

        stampa = self._get_viewer_text('(//div[@id="viewer"]//span)[1]')
        self.assertEqual(stampa, "STAMPA LIBRO GIORNALE")

        self.wait_for_element_and_click('//button[@data-title="Stampa scadenzario"]')
        self.wait_for_element_and_click('//button[@class="btn btn-primary btn-lg"]')

        stampa = self._get_viewer_text('(//div[@id="viewer"]//span)[6]')
        self.assertEqual(stampa, "SCADENZE DAL 01/01/2026 AL 31/12/2026")

        self.wait_for_element_and_click('//button[@class="close"]')
