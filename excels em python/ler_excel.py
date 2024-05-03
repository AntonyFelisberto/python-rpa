from openpyxl import load_workbook
import os

caminho_arquivo = "excels em python\\excels\\Exemplos.xlsx"
planilha = load_workbook(filename=caminho_arquivo)
sheet_selecionada = planilha["dados"]#nome da aba do excel que fica na parte de baixo

for linha in range(2,len(sheet_selecionada["A"])+1):
    nome = sheet_selecionada["A%s" % linha].value
    email = sheet_selecionada["B%s" % linha].value
    telefone = sheet_selecionada["C%s" % linha].value
    sexo = sheet_selecionada["D%s" % linha].value
    sobre = sheet_selecionada["E%s" % linha].value

    print(nome,email,telefone,sexo,sobre)