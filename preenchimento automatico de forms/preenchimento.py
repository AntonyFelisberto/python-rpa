from selenium import webdriver as opcoesSelenium
from selenium.webdriver.common.keys import Keys
import pyautogui as tempoEspera
from selenium.webdriver.common.by import By
 
navegadorFormulario = opcoesSelenium.Edge()
navegadorFormulario.get("https://pt.surveymonkey.com/r/Y9Y6FFR")
 
#Aguardar para o computador processar as informações
tempoEspera.sleep(6)
 
#Preenche Nome
navegadorFormulario.find_element(By.NAME, "683928983").send_keys("Nicole Ferreira")
 
#Preenche Email
navegadorFormulario.find_element(By.NAME, "683932318").send_keys("nicole.ferreira@gmail.com")
 
#Preenche Telefone
navegadorFormulario.find_element(By.NAME, "683930688").send_keys("(11) 11111 - 1111")
 
#Preenche Sobre
navegadorFormulario.find_element(By.NAME, "683932969").send_keys("Sei automatizar processos e planilhas com Python")
 
 
#Preenche Radio Button Feminino
navegadorFormulario.find_element(By.ID,"683931881_4497366119_label").click()
 
#Aguardar para o computador processar as informações
tempoEspera.sleep(6)
 
#Clica para enviar as informações
navegadorFormulario.find_element(By.XPATH,'//*[@id="patas"]/main/article/section/form/div[2]/button').click()