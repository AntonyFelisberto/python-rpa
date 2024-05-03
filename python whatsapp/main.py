from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyautogui as control_device
from selenium.webdriver.common.by import By
from openpyxl import load_workbook

caminho_arquivos_contatos = "python whatsapp\\files\\contatos.xlsx"
planilha_contatos = load_workbook(caminho_arquivos_contatos)

sheet_selecionada = planilha_contatos["Dados"] # nome da aba do excel que fica na parte de baixo

navegador = webdriver.ChromiumEdge()
navegador.get("https://web.whatsapp.com/")

while len(navegador.find_elements(By.ID,"side")) < 1: # vai pedir pra logar no whatsapp e enquanto não achar o id side de dentro do whats vai ficar em loop, procure um id ou xpath que não se repita
    control_device.sleep(3)

control_device.sleep(3)
for linha in range(2,len(sheet_selecionada["A"])+1):
    nome_contato = sheet_selecionada["A%s" % linha].value
    mensagem_contato = sheet_selecionada["B%s" % linha].value

    navegador.find_element(By.XPATH,"//*[@id='side']/div[1]/div/div/div[2]/div/div[1]/p").send_keys(nome_contato)
    control_device.sleep(3)
    control_device.press("enter")
    control_device.sleep(3)
    