from common.Test import Test
from selenium.webdriver.common.by import By


class PianiScontoMagg(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Magazzino")

    def test_creazione_piano_sconto_magg(self):
        self.creazione_piano_sconto_magg("Piano di sconto di Prova da Modificare", "10")
        self.creazione_piano_sconto_magg("Piano di sconto di Prova da Eliminare", "5")
        self.modifica_piano_sconto("Piano di sconto di Prova")
        self.elimina_piano_sconto()
        self.verifica_piano_sconto()
        self.plugin_sconto_maggiorazione()

    def creazione_piano_sconto_magg(self, nome: str, sconto: str):
        self.navigate_to_and_wait("Piani di sconto/magg.")
        self.click_add_button()
        modal = self.wait_modal()

        self.input(modal, 'Nome').setValue(nome)
        self.input(modal, 'Sconto/magg. combinato').setValue(sconto)
        self.submit_modal(modal)

    def modifica_piano_sconto(self, modifica=str):
        self.navigate_to_and_wait("Piani di sconto/magg.")

        self.search_by_th_and_click_first("th_Nome", 'Piano di sconto di Prova da Modificare')

        self.input(None, 'Nome').setValue(modifica)
        self.click_save_button()

        self.navigate_to_and_wait("Piani di sconto/magg.")
        self.clear_filters()

    def elimina_piano_sconto(self):
        self.navigate_to_and_wait("Piani di sconto/magg.")

        self.search_by_th_and_click_first("th_Nome", 'Piano di sconto di Prova da Eliminare')

        self.delete_current_and_clear()

    def verifica_piano_sconto(self):
        self.navigate_to_and_wait("Piani di sconto/magg.")

        self.search_by_th("th_Nome", "Piano di sconto di Prova")
        modificato = self.get_table_text(1, 2)
        self.assertEqual("Piano di sconto di Prova", modificato)
        self.clear_filters()

        self.verify_deleted_by_th("th_Nome", "Piano di sconto di Prova da Eliminare")

    def plugin_sconto_maggiorazione(self):
        self.navigate_to_and_wait("Articoli")

        self.search_by_th("th_Descrizione", 'Articolo 1')
        self.wait_for_element_and_click('//tbody//td[2]//div[1]')
        self.wait_for_element_and_click('//a[@id="link-tab_33"]')

        prezzo_nuovo = self.find(By.XPATH, '(//div[@id="tab_33"]//tr[3]//td[2])[2]').text
        self.assertEqual(prezzo_nuovo, "18,00 €")

        self.navigate_to_and_wait("Articoli")
        self.clear_filters()