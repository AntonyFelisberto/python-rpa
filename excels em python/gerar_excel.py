import xlsxwriter
import os

caminho_excel = "excels em python\\excels\\Exemplos.xlsx"
planilha = xlsxwriter.Workbook(caminho_excel)
planilha_criada = planilha.add_worksheet()
planilha_criada.write("A1","NOME")
planilha_criada.write("B1","CARGA")
planilha_criada.write("A2","PREÇO")
planilha_criada.write("B2","DOLAR")
planilha_criada.write("A3","DOLAR ATUAL")
planilha_criada.write("B3","PREÇOS")
planilha_criada.write("A4","ESTOQUES")
planilha_criada.write("B4",27)
planilha_criada.write("A5","ESTOQUES")
planilha_criada.write("B5",27.4)
planilha.close()
os.startfile(caminho_excel)