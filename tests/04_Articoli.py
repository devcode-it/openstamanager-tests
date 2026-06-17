from common.Test import Test
from selenium.webdriver.common.by import By

class Articoli(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Magazzino")
        self.wait_loader()

    def test_creazione_articolo(self):
        self._creazione_articolo("001", "Articolo 1", "2")
        self._creazione_articolo("002", "Articolo di Prova da Eliminare", "2")
        self._modifica_articolo("20", "1")
        self._elimina_articolo()
        self._verifica_articolo()

    def _creazione_articolo(self, codice: str, descrizione: str, qta: str):
        self.navigateToAndWait("Articoli")

        self.click_add_button()
        modal = self.wait_modal()

        self.input(modal, 'Codice').setValue(codice)
        self.input(modal, 'Descrizione').setValue(descrizione)

        self.wait_for_element_and_click('//button[@class="btn btn-tool"]')
        self.find(By.XPATH, '//label[contains(text(), "Quantità iniziale")]/following-sibling::div/input')

        self.input(modal, 'Quantità iniziale').setValue(qta)
        self.wait_for_element_and_click('//button[@type="submit"]')

    def _modifica_articolo(self, acquisto: str, coefficiente: str):
        self.navigateToAndWait("Articoli")

        self.search_by_th_and_click_first("th_Descrizione", 'Articolo 1')

        self.close_tour()

        self.input(None, 'Prezzo di acquisto').setValue(acquisto)
        self.input(None, 'Coefficiente').setValue(coefficiente)

        self.click_save_button()
        self.click_back_button()

        verificaqta = self.find(By.XPATH, '//div[@id="tab_0"]//tbody//td[10]//div[1][1]').text
        self.assertEqual(verificaqta, "2,00")

        self.clear_filters()

    def _elimina_articolo(self):
        self.navigateToAndWait("Articoli")

        self.search_by_th_and_click_first("th_Descrizione", 'Articolo di Prova da Eliminare')

        self.delete_current_and_clear()

    def _verifica_articolo(self):
        self.navigateToAndWait("Articoli")

        self.search_by_th("th_Codice", '001')

        modificato = self.get_table_text(1, 9)
        self.assertEqual("20,00", modificato)
        self.clear_filters()

        self.verify_deleted_by_th("th_Descrizione", 'Articolo di prova da Eliminare')