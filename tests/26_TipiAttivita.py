from common.Test import Test, get_html
from selenium.webdriver.common.keys import Keys
from common.RowManager import RowManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TipiAttivita(Test):
    def setUp(self):
        super().setUp()

        self.expandSidebar("Attività")
        
    def test_creazione_tipiattività(self):
        # Creazione tipi di attività *Required*
        self.creazione_tipi_attività(codice="001", descrizione="Tipo di Prova da Modificare", tempostandard="2,00", addebitoorario="10,00", addebitokm="5,00", addebitodirittoch="20,00", costoorario="12,00", costokm="6,00", costodirittoch="13,00" )
        self.creazione_tipi_attività(codice="002", descrizione="Tipo di Prova da Eliminare", tempostandard="2,00", addebitoorario="10,00", addebitokm="5,00", addebitodirittoch="20,00", costoorario="12,00", costokm="6,00", costodirittoch="13,00")
        
        # Modifica tipi di attività
        self.modifica_tipi_attività("Tipo di Attività di Prova")

        # Cancellazione tipi di attività
        self.elimina_tipi_attività()

        # Verifica tipi di attività
        self.verifica_tipi_attività()

    def creazione_tipi_attività(self, codice=str, descrizione=str, tempostandard=str, addebitoorario=str, addebitokm=str, addebitodirittoch=str, costoorario=str, costokm=str, costodirittoch=str):
        self.navigateTo("Tipi di attività")
        self.wait_loader()  

        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click()
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
        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        self.wait_loader()

    def modifica_tipi_attività(self, modifica:str):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Tipi di attività")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input'))).send_keys('Tipo di Prova da Modificare', Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//tbody//tr//td[2]').click()
        self.wait_loader()
        
        self.input(None,'Descrizione').setValue(modifica)
        self.find(By.XPATH, '//div[@id="tab_0"]//button[@id="save"]').click()
        self.wait_loader()

        self.navigateTo("Tipi di attività")
        self.wait_loader()  

        self.find(By.XPATH, '//th[@id="th_Descrizione"]/i[@class="deleteicon fa fa-times"]').click()
        sleep(2)

    def elimina_tipi_attività(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Tipi di attività")
        self.wait_loader()  

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input'))).send_keys('Tipo di Prova da Eliminare', Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//tbody//tr//td[2]').click()
        sleep(1)
        
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_0"]//a[@class="btn btn-danger ask"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))).click()
        self.wait_loader()

        self.find(By.XPATH, '//th[@id="th_Descrizione"]/i[@class="deleteicon fa fa-times"]').click()
        sleep(2)
        
    def verifica_tipi_attività(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Tipi di attività")
        self.wait_loader()    

        #verifica elemento modificato
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input'))).send_keys("Tipo di Attività di Prova", Keys.ENTER)
        sleep(1)

        modificato=self.driver.find_element(By.XPATH,'//tbody//tr[1]//td[3]').text
        self.assertEqual("Tipo di Attività di Prova",modificato)
        self.find(By.XPATH, '//i[@class="deleteicon fa fa-times"]').click()
        sleep(2)

        #verifica elemento eliminato
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input'))).send_keys("Tipo di Attività di Prova da Eliminare", Keys.ENTER)
        sleep(1)

        eliminato=self.driver.find_element(By.XPATH,'//tbody//tr[1]//td[@class="dataTables_empty"]').text
        self.assertEqual("La ricerca non ha portato alcun risultato.",eliminato)