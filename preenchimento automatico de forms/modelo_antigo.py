import pyautogui as tempo_espera
from selenium import webdriver as opcoesSelenium

navegado_formulario = opcoesSelenium.Edge()
navegado_formulario.get("https://pt.surveymonkey.com/r/Y9Y6FFR")

tempo_espera.sleep(6)

navegado_formulario.find_element("683928983").send_keys("Nicole Ferreira")

navegado_formulario.find_element("683932318").send_keys("nicole.ferreira@gmail.com")

navegado_formulario.find_element("683930688").send_keys("(11) 11111 - 1111")

navegado_formulario.find_element("683932969").send_keys("Sei automatizar processos e planilhas com Python")

navegado_formulario.find_element("683931881_4497366119_label").click()

tempo_espera.sleep(6)

navegado_formulario.find_element('//*[@id="patas"]/main/article/section/form/div[2]/button').click()