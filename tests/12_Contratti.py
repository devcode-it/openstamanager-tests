from common.Test import Test, get_html
from common.RowManager import RowManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class Contratti(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Vendite")

    def test_creazione_contratto(self):
        importi = RowManager.list()
        self.creazione_contratto("Contratto di Prova da Modificare", "Cliente", importi[0])
        self.duplica_contratto()
        self.modifica_contratto("Contratto di Prova")
        self.elimina_contratto()
        self.verifica_contratto()
        self.contratti_del_cliente()


    def creazione_contratto(self, nome:str, cliente: str, file_importi: str):
        self.navigateTo("Contratti")
        self.wait_loader()

        self.wait_for_element_and_click('//i[@class="fa fa-plus"]')
        modal = self.wait_modal()

        self.input(modal, 'Nome').setValue(nome)
        select = self.input(modal, 'Cliente')
        select.setByText(cliente)
        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

        row_manager = RowManager(self)
        self.valori = row_manager.compile(file_importi)

    def duplica_contratto(self):
        self.navigateTo("Contratti")
        self.wait_loader()

        self.wait_for_element_and_click('//tbody//tr//td[2]')
        self.wait_for_element_and_click('//div[@id="pulsanti"]//button[@class="btn btn-primary ask"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-primary"]')

        element = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//input[@id="nome"]'))
        )
        element.clear()
        element.send_keys("Contratto di Prova da Eliminare")
        self.wait_for_element_and_click('//button[@id="save"]')

    def modifica_contratto(self, modifica=str):
        self.navigateTo("Contratti")
        self.wait_loader()

        self.send_keys_and_wait(self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))), '=Contratto di Prova da Modificare', wait_modal=False)

        self.wait_for_element_and_click('//tbody//tr//td[2]')

        element = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//input[@id="nome"]'))
        )
        element.clear()
        element.send_keys(modifica)
        self.wait_for_element_and_click('//div[@id="tab_0"]//button[@id="save"]')

        sconto = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="righe"]//tbody[2]//tr[2]//td[2]'))
        ).text
        totale_imponibile = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="righe"]//tbody[2]//tr[3]//td[2]'))
        ).text
        iva = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="righe"]//tbody[2]//tr[4]//td[2]'))
        ).text
        totale = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_0"]//div[@id="righe"]//tbody[2]//tr[5]//td[2]'))
        ).text

        self.assertEqual(sconto, (self.valori["Sconto/maggiorazione"] + ' €'))
        self.assertEqual(totale_imponibile, (self.valori["Totale imponibile"] + ' €'))
        self.assertEqual(iva, (self.valori["IVA"] + ' €'))
        self.assertEqual(totale, (self.valori["Totale documento"] + ' €'))

        self.navigateTo("Contratti")
        self.wait_loader()
        self.wait_for_element_and_click('//th[@id="th_Nome"]/i[@class="deleteicon fa fa-times"]')

    def elimina_contratto(self):
        self.navigateTo("Contratti")
        self.wait_loader()

        self.send_keys_and_wait(self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))), 'Contratto di Prova da Eliminare', wait_modal=False)

        self.wait_for_element_and_click('//tbody//tr//td[2]')
        self.wait_for_element_and_click('//div[@id="tab_0"]//a[@class="btn btn-danger ask"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')

        self.wait_for_element_and_click('//th[@id="th_Nome"]/i[@class="deleteicon fa fa-times"]')

    def verifica_contratto(self):
        self.navigateTo("Contratti")
        self.wait_loader()

        self.send_keys_and_wait(self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))), "Contratto di Prova", wait_modal=False)

        modificato = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//tbody//tr[1]//td[3]'))
        ).text
        self.assertEqual("Contratto di Prova", modificato)
        self.wait_for_element_and_click('//i[@class="deleteicon fa fa-times"]')

        self.send_keys_and_wait(self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))), "Contratto di Prova da Eliminare", wait_modal=False)

        eliminato = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//tbody//tr[1]//td[@class="dataTables_empty"]'))
        ).text
        self.assertEqual("La ricerca non ha portato alcun risultato.", eliminato)
        self.wait_for_element_and_click('//th[@id="th_Nome"]/i[@class="deleteicon fa fa-times"]')

    def contratti_del_cliente(self):
        self.navigateTo("Anagrafiche")
        self.wait_loader()

        self.send_keys_and_wait(self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Ragione-sociale"]/input'))), "Cliente", wait_modal=False)

        self.wait_for_element_and_click('//tbody//tr//td[2]')
        self.wait_for_element_and_click('//a[@id="link-tab_35"]')

        self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_35"]//tbody//tr/td[2]')))
