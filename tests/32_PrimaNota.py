from common.Test import Test
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class PrimaNota(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Contabilità")

    def test_creazione_prima_nota(self):
        self.creazione_prima_nota(causale="Prima Nota da Modificare")
        self.creazione_prima_nota(causale="Prima Nota da Eliminare")
        self.modifica_prima_nota("Prima Nota di Prova (Fatt. n.1 del 01/01/2025)")
        self.elimina_prima_nota()
        self.verifica_prima_nota()

    def search_causale(self, nome: str):
        search_input = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Causale"]/input'))
        )
        search_input.clear()
        self.send_keys_and_wait(search_input, nome, wait_modal=False)

    def creazione_prima_nota(self, causale=str):
        self.navigateTo("Prima nota")
        self.wait_loader()
        self.wait_for_element_and_click('//i[@class="fa fa-plus"]')
        modal = self.wait_modal()

        self.input(modal, 'Causale').setValue(causale)
        modal = self.wait_modal()

        self.wait_for_dropdown_and_select(
            '//span[@id="select2-conto0-container"]',
            option_text="100.000010"
        )

        avere_field = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//input[@id="avere0"]'))
        )
        self.send_keys_and_wait(avere_field, "100,00", wait_modal=False)

        self.wait_for_dropdown_and_select(
            '//span[@id="select2-conto1-container"]',
            option_text="700.000010"
        )

        dare_field = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//input[@id="dare1"]'))
        )
        self.send_keys_and_wait(dare_field, "100,00", wait_modal=False)

        self.wait_for_element_and_click('button[type="submit"]', By.CSS_SELECTOR)
        self.wait_driver.until(EC.invisibility_of_element_located((By.CLASS_NAME, 'modal-dialog')))

    def modifica_prima_nota(self, modifica=str):
        self.navigateTo("Prima nota")
        self.wait_loader()
        self.search_causale('Prima Nota da Modificare')
        self.click_first_result()

        self.input(None, 'Causale').setValue(modifica)
        self.wait_for_element_and_click('//div[@id="tab_0"]//button[@id="save"]')

        self.navigateTo("Prima nota")
        self.wait_loader()
        self.clear_filters()

    def elimina_prima_nota(self):
        self.navigateTo("Prima nota")
        self.wait_loader()
        self.search_causale('Prima Nota da Eliminare')
        self.click_first_result()

        self.wait_for_element_and_click('//div[@id="tab_0"]//a[@class="btn btn-danger ask"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')
        self.clear_filters()

    def verifica_prima_nota(self):
        self.navigateTo("Prima nota")
        self.wait_loader()

        self.search_causale("Prima Nota di Prova (Fatt. n.1 del 01/01/2025)")
        self.wait_for_search_results()
        modificato = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//tbody//tr[1]//td[4]'))
        ).text
        self.assertEqual("Prima Nota di Prova (Fatt. n.1 del 01/01/2025)", modificato)

        self.clear_filters()
        self.search_causale("Prima nota da Eliminare")
        self.wait_for_search_results()
        eliminato = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//tbody//tr[1]//td[@class="dataTables_empty"]'))
        ).text
        self.assertEqual("La ricerca non ha portato alcun risultato.", eliminato)

