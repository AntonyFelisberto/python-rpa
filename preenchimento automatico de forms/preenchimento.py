from selenium import webdriver as opcoesSelenium
from selenium.webdriver.common.keys import Keys
import pyautogui as tempo_espera
from selenium.webdriver.common.by import By
 
navegado_formulario = opcoesSelenium.Edge()
navegado_formulario.get("https://pt.surveymonkey.com/r/Y9Y6FFR")

tempo_espera.sleep(6)

navegado_formulario.find_element(By.NAME, "683928983").send_keys("Nicole Ferreira")

navegado_formulario.find_element(By.NAME, "683932318").send_keys("nicole.ferreira@gmail.com")

navegado_formulario.find_element(By.NAME, "683930688").send_keys("(11) 11111 - 1111")

navegado_formulario.find_element(By.NAME, "683932969").send_keys("Sei automatizar processos e planilhas com Python")

navegado_formulario.find_element(By.ID,"683931881_4497366119_label").click()

tempo_espera.sleep(6)

navegado_formulario.find_element(By.XPATH,'//*[@id="patas"]/main/article/section/form/div[2]/button').click()