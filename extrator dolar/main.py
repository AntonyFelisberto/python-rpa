from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyautogui as controlar_device
from selenium.webdriver.common.by import By
import xlsxwriter
import os

def abrir_navegador_em_background():
    options = webdriver.EdgeOptions()
    options.use_chromium = True
    options.add_argument('--headless')
    navegador = webdriver.ChromiumEdge(options=options)
    return navegador

caminho_excel = "extrator dolar\\excels\\Dolar e Euro.xlsx"

navegador = webdriver.ChromiumEdge()
navegador.get("https://www.google.com/")

controlar_device.sleep(1)
navegador.find_element(By.NAME,"q").send_keys("Dolar hoje")
controlar_device.sleep(1)
navegador.find_element(By.NAME,"q").send_keys(Keys.RETURN)
controlar_device.sleep(1)
valor_dolar = navegador.find_elements(By.XPATH,"/html/body/div[5]/div/div[11]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div/div/div/div[3]/div[1]/div[1]/div[2]/span[1]")[0].text
print(valor_dolar)

controlar_device.sleep(1)
navegador.find_element(By.NAME,"q").send_keys("")
controlar_device.sleep(1)
controlar_device.press("tab")
controlar_device.sleep(1)
controlar_device.press("enter")
controlar_device.sleep(1)
navegador.find_element(By.NAME,"q").send_keys("Euro hoje")
controlar_device.sleep(1)
navegador.find_element(By.NAME,"q").send_keys(Keys.RETURN)
controlar_device.sleep(1)
valor_euro = navegador.find_elements(By.XPATH,"//*[@id='knowledge-currency__updatable-data-column']/div[1]/div[2]/span[1]")[0].text
print(valor_euro)

planilha = xlsxwriter.Workbook(caminho_excel)
planilha_criada = planilha.add_worksheet()
planilha_criada.write("A1","Dolar")
planilha_criada.write("B1","Euro")
planilha_criada.write("A2",float(valor_dolar.replace(",",".")))
planilha_criada.write("B2",float(valor_euro.replace(",",".")))
planilha.close()
os.startfile(caminho_excel)