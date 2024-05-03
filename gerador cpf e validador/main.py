import re
import sys


cpf = "400.000.000-07".replace(".","").replace("-","").replace(" ","")
cpf = re.sub(r"[^0-9]","",cpf)

entrada_sequencial = cpf == cpf[0] * len(cpf)

if entrada_sequencial:
    print("dados sequenciais")
    sys.exit()

nove_digitos = cpf[0:9]
contador_regressivo_um = 10
resultado_digito_um = 0

for digito in nove_digitos:
    resultado_digito_um += int(digito) * contador_regressivo_um
    contador_regressivo_um -= 1
digito = (resultado_digito_um*10) % 11
digito = digito if digito <= 9 else 0
print(digito)


def gerar_cpf():
    entrada = input()