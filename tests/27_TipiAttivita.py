from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from common.Test import Test


class TipiAttivita(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Attività")
        self.wait_loader()

    def test_creazione_tipiattività(self):
        self.creazione_tipi_attività(
            "001", "Tipo di Prova da Modificare", "2,00", "10,00", "5,00", "20,00", "12,00", "6,00", "13,00"
        )
        self.creazione_tipi_attività(
            "002", "Tipo di Prova da Eliminare", "2,00", "10,00", "5,00", "20,00", "12,00", "6,00", "13,00"
        )
        self.modifica_tipi_attività("Tipo di Attività di Prova")
        self.elimina_tipi_attività()
        self.verifica_tipi_attività()
        self.wait_for_element_and_click('//i[@class="fa fa-power-off nav-icon"]')

    def creazione_tipi_attività(self, codice: str, descrizione: str, tempostandard: str, addebitoorario: str, addebitokm: str, addebitodirittoch: str, costoorario: str, costokm: str, costodirittoch: str):
        self.navigateTo("Tipi di attività")
        self.wait_loader()
        self.wait_for_element_and_click('//i[@class="fa fa-plus"]')
        modal = self.wait_modal()

        self.input(modal, 'Codice').setValue(codice)
        self.input(modal, 'Descrizione').setValue(descrizione)
        self.input(modal, 'Tempo standard').setValue(tempostandard)
        self.input(modal, 'Addebito orario').setValue(addebitoorario)
        self.input(modal, 'Addebito km').setValue(addebitokm)
        self.input(modal, 'Addebito diritto ch.').setValue(addebitodirittoch)
        self.input(modal, 'Costo orario').setValue(costoorario)
        self.input(modal, 'Costo km').setValue(costokm)
        self.input(modal, 'Costo diritto ch.').setValue(costodirittoch)
        self.wait_for_element_and_click('button[type="submit"]', By.CSS_SELECTOR)

    def search_tipo_attivita(self, nome: str):
        self.navigateTo("Tipi di attività")
        self.wait_loader()
        search_input = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input'))
        )
        search_input.clear()
        self.send_keys_and_wait(search_input, nome, wait_modal=False)

    def modifica_tipi_attività(self, modifica: str):
        self.search_tipo_attivita('Tipo di Prova da Modificare')
        self.click_first_result()
        self.input(None, 'Descrizione').setValue(modifica)
        self.wait_for_element_and_click('//div[@id="tab_0"]//button[@id="save"]')

        self.navigateTo("Tipi di attività")
        self.wait_loader()
        self.clear_filters()

    def elimina_tipi_attività(self):
        self.search_tipo_attivita('Tipo di Prova da Eliminare')
        self.click_first_result()
        self.wait_for_element_and_click('//div[@id="tab_0"]//a[@class="btn btn-danger ask"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')
        self.clear_filters()

    def verifica_tipi_attività(self):
        self.search_tipo_attivita("Tipo di Attività di Prova")
        modificato = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//tbody//tr[1]//td[3]'))
        ).text
        self.assertEqual("Tipo di Attività di Prova", modificato)
        self.clear_filters()

        self.search_tipo_attivita("Tipo di Attività di Prova da Eliminare")
        eliminato = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//tbody//tr[1]//td[@class="dataTables_empty"]'))
        ).text
        self.assertEqual("Nessun dato presente nella tabella", eliminato)
        self.clear_filters()