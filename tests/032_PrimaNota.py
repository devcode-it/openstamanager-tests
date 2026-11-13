from common.Test import Test
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class PrimaNota(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Contabilità")

    def test_creazione_prima_nota(self):
        self.navigate_to_and_wait("Prima nota")

        self.creazione_prima_nota(causale="Prima Nota da Modificare")
        self.creazione_prima_nota(causale="Prima Nota da Eliminare")
        self.modifica_prima_nota("Prima Nota di Prova (Fatt. n.1 del 01/01/2026)")
        self.elimina_prima_nota()
        self.verifica_prima_nota()

    def search_causale(self, nome: str):
        self.search_by_th("th_Causale", nome)

    def creazione_prima_nota(self, causale=str):
        self.click_add_button()
        modal = self.wait_modal()

        self.input(modal, 'Causale').setValue(causale)

        self.wait_for_dropdown_and_select(
            '//span[@id="select2-conto_add_0-container"]',
            option_text="100.000010"
        )

        avere_add__field = self.find(By.XPATH, '//input[@id="avere_add_0"]')
        self.send_keys_and_wait(avere_add__field, "100,00", wait_modal=False)

        self.wait_for_dropdown_and_select(
            '//span[@id="select2-conto_add_1-container"]',
            option_text="700.000010"
        )

        dare_add__field = self.find(By.XPATH, '//input[@id="dare_add_1"]')
        self.send_keys_and_wait(dare_add__field, "100,00", wait_modal=False)


    def modifica_prima_nota(self, modifica=str):
        self.click_back_button()
        self.wait_loader()

        self.search_causale('Prima Nota da Modificare')
        self.click_first_result()

        self.input(None, 'Causale').setValue(modifica)
        self.click_save_button()

        self.navigate_to_and_wait("Prima nota")
        self.clear_filters()

    def elimina_prima_nota(self):
        self.navigate_to_and_wait("Prima nota")
        self.search_causale('Prima Nota da Eliminare')
        self.click_first_result()

        self.delete_current_and_clear()

    def verifica_prima_nota(self):
        self.navigate_to_and_wait("Prima nota")

        self.search_causale("Prima Nota di Prova (Fatt. n.1 del 01/01/2026)")
        self.wait_for_search_results()
        modificato = self.get_table_text(1, 4)
        self.assertEqual("Prima Nota di Prova (Fatt. n.1 del 01/01/2026)", modificato)

        self.clear_filters()
        self.search_causale("Prima nota da Eliminare")
        self.wait_for_search_results()
        self.assertTrue(
            self.find(By.XPATH, '//tbody//tr//td[@class="dataTables_empty"]').is_displayed()
        )

