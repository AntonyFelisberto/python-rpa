import tkinter as tk
from tkinter import ttk
import tkinter.font as font
from tkinter import messagebox
import pandas as pd

def abrir_janela_operacoes(nome,conta,cpf):
    messagebox.showerror("Mess","efetuado")

def verificar_login(entry_conta,entry_senha):
    conta = entry_conta.get()
    senha = entry_senha.get()

    entry_conta.delete(0,tk.END)
    entry_senha.delete(0,tk.END)

    arquivo_excel = "caixa eletronico\\files\\Base_Dados.xlsx"

    try:
        dados = pd.read_excel(arquivo_excel,sheet_name="Usuários")#"Usuários" é o nome da aba do excel
        for index,row in dados.iterrows(): #TESTES conta == 567 senha 555
            if str(row["Conta"]) == str(conta) and str(row["Senha"]) == str(senha):
                nome = row["Nome"]
                cpf = row["CPF"]

                janela_login.destroy()
                abrir_janela_operacoes(nome,conta,cpf)
                break
    except Exception as e:
        messagebox.showerror("Erro",f"erro com os dados dados excel {e}")

janela_login = tk.Tk()
janela_login.title("caixa eletronico")
janela_login.geometry("400x400")

janela_login.configure(bg="#FFFFFF")

custom_font = font.Font(family="Arial",size=15)

label_conta = tk.Label(janela_login,text="Numero da conta",font=custom_font,bg="#FFFFFF")
label_conta.pack(pady=10)
entry_conta = tk.Entry(janela_login,font=custom_font,bg="#FFFFFF")
entry_conta.pack(pady=5)

label_senha = tk.Label(janela_login,text="Senha",font=custom_font,bg="#FFFFFF")
label_senha.pack(pady=10)
entry_senha = tk.Entry(janela_login,show="*",font=custom_font,bg="#FFFFFF")
entry_senha.pack(pady=5)

botao_entrar = tk.Button(janela_login,text="Entrar",font=custom_font,bg="#FFFFFF",command=lambda:verificar_login(entry_conta,entry_senha))#,command=lambda:verificar_login serve para criar uma funcao anonima
botao_entrar.pack(pady=10)

janela_login.mainloop()