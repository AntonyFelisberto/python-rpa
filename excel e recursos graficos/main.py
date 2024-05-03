import tkinter as tk
from tkinter import *
from tkinter import filedialog,messagebox,simpledialog
import pandas as pd
import numpy as np
from pandastable import Table

janela = Tk()
janela.title("Editor excel com pandas")
janela.attributes("-fullscreen",False)

class ExcelEditor:
    def __init__(self,janela_principal):
        self.janela_principal = janela_principal
        self.resultado_label = Label(self.janela_principal,text="Total: ",font="Arial 16",bg="#F5F5F5")
        self.resultado_label.pack(side=TOP,padx=10,pady=10)
        self.df = pd.DataFrame()
        self.tree = None
        self.table = None
        self.filename = ""
        self.cria_widgets()

    def cria_widgets(self):
        menu_bar = tk.Menu(self.janela_principal)
        menu_arquivos = tk.Menu(menu_bar,tearoff=0)#tearoff para desativar ou nao funcao de arrastar
        menu_edicao = tk.Menu(menu_bar,tearoff=0)
        menu_merge = tk.Menu(menu_bar,tearoff=0)
        menu_relatorios = tk.Menu(menu_bar,tearoff=0)

        menu_arquivos.add_command(label="Abrir",command=self.carregar_excel)
        menu_arquivos.add_separator()
        menu_arquivos.add_command(label="Salvar Como",command=janela.destroy)
        menu_arquivos.add_separator()
        menu_arquivos.add_command(label="Sair",command=janela.destroy)
        menu_arquivos.add_separator()

        menu_edicao.add_command(label="Renomear Coluna",command=self.renomear_coluna)
        menu_edicao.add_command(label="Remover Coluna",command=janela.destroy)
        menu_edicao.add_command(label="Filtrar",command=janela.destroy)
        menu_edicao.add_command(label="Pivot",command=janela.destroy)
        menu_edicao.add_command(label="Group",command=janela.destroy)
        menu_edicao.add_command(label="Remover linhas em branco",command=self.remover_linhas_branco)
        menu_edicao.add_command(label="Remover linhas alternadas",command=self.remover_linhas)
        menu_edicao.add_command(label="Remover Duplicados",command=janela.destroy)

        menu_merge.add_command(label="Inner Join",command=janela.destroy)
        menu_merge.add_command(label="Join Full",command=janela.destroy)
        menu_merge.add_command(label="Left Join",command=janela.destroy)
        menu_merge.add_command(label="Merge Outer",command=janela.destroy)

        menu_relatorios.add_command(label="Consolidar",command=janela.destroy)
        menu_relatorios.add_command(label="Quebrar",command=janela.destroy)

        menu_bar.add_cascade(label="Arquivo",menu=menu_arquivos)
        menu_bar.add_cascade(label="Editar",menu=menu_edicao)
        menu_bar.add_cascade(label="Merge",menu=menu_merge)
        menu_bar.add_cascade(label="Merge",menu=menu_relatorios)

        self.janela_principal.config(menu=menu_bar)

        self.tree = tk.ttk.Treeview(self.janela_principal)

        self.tree.pack(expand=False)

    #-----------------------------FUNCOES COM O PANDAS-----------------------------------
    def funcao_renomear_colunas(self,column,novo_nome,janela_renomear_colunas):
        if novo_nome:
            self.df = self.df.rename(columns={column:novo_nome})
            self.atualiza_treeview()
            janela_renomear_colunas.destroy()
    
    def soma_coluna_valores(self):
        resultados = []
        for coluna in self.df.columns:
            if pd.api.types.is_numeric_dtype(self.df[coluna]):
                valores_numericos = self.df[coluna][0:]
                valores_numericos = pd.to_numeric(valores_numericos,errors="coerce")#errors="coerce" permite tratar o erro de valores que nao sao numericos
                valores_numericos = valores_numericos[~np.isnan(valores_numericos)]#~ é usado para inverter os resultados retornados,tranformando valores em True os false
                soma = valores_numericos.sum()
                resultado = f"A soma da coluna {coluna} é {soma}"
                resultados.append(resultado)

        self.resultado_label.config(text="\n".join(resultados))

    def atualiza_treeview(self):
        self.tree.delete(*self.tree.get_children())
        self.tree["columns"]=list(self.df.columns)
        for column in self.df.columns:
            self.tree.heading(column,text=column)
        
        for i,row in self.df.iterrows():
            values = list(row)

            for j, value in enumerate(values):
                if isinstance(value,np.generic):    #np.generic é para garantir que os tipos da tabelas sejam respectivos ao do python
                    values[j] = np.asscalar(value)

            self.tree.insert("",tk.END,values=values)

    def funcao_remover_linhas(self,linha_inicio,linha_fim,janela_remover_linhas):
        primeira_linha = int(linha_inicio)
        ultima_linha = int(linha_fim)
        self.df = self.df.drop(self.df.index[primeira_linha-1:ultima_linha]) #primeira_linha - 1 pq o indice sempre começa em 0
        self.atualiza_treeview()
        self.soma_coluna_valores()
        janela_remover_linhas.destroy()

    def remover_linhas_branco(self):
        response = messagebox.askyesno("Remover linhas em branco","Tem certeza que quer remover linhas em branco")
        
        if response == 1:
            self.df = self.df.dropna(axis=0) #deleta as linhas com valores em branco
            self.atualiza_treeview()
            self.soma_coluna_valores()

     #-----------------------------FUNCOES PARA A TELA-----------------------------------
    def renomear_coluna(self):
        #criar tela em segundo plano
        janela_renomear_coluna = tk.Toplevel(self.janela_principal)
        janela_renomear_coluna.title("Renomear Coluna")
        largura_janela = 450
        altura_janela = 250

        largura_tela = janela_renomear_coluna.winfo_screenmmwidth()
        altura_tela = janela_renomear_coluna.winfo_screenmmheight()

        posicao_x = (largura_tela // 2) - (largura_janela // 2) 
        posicao_y = (altura_tela // 2) - (altura_janela // 2) 

        janela_renomear_coluna.geometry(f"{largura_janela}x{altura_janela}+{posicao_x}+{posicao_y}")

        janela_renomear_coluna.configure(bg="#FFFFFF")

        label_coluna = tk.Label(janela_renomear_coluna,text="Digite o nome da coluna que quer renomear: ",font=("Arial",12),bg="#FFFFFF")
        label_coluna.pack(pady=10)
        entry_coluna = Entry(janela_renomear_coluna,font=("Arial",12))
        entry_coluna.pack()

        label_novo = tk.Label(janela_renomear_coluna,text="Digite o novo nome da coluna: ",font=("Arial",12),bg="#FFFFFF")
        label_novo.pack(pady=10)
        entry_novo = Entry(janela_renomear_coluna,font=("Arial",12))
        entry_novo.pack()

        botao_renomear = Button(janela_renomear_coluna,text="Renomear",font=("Arial",12),command=lambda:self.funcao_renomear_colunas(entry_coluna.get(),entry_novo.get(),janela_renomear_coluna))
        botao_renomear.pack(pady=20)

        janela_renomear_coluna.mainloop()

    def remover_linhas(self):
        #criar tela em segundo plano
        janela_remover_linhas = tk.Toplevel(self.janela_principal)
        janela_remover_linhas.title("Renomear Coluna")
        largura_janela = 450
        altura_janela = 250

        largura_tela = janela_remover_linhas.winfo_screenmmwidth()
        altura_tela = janela_remover_linhas.winfo_screenmmheight()

        posicao_x = (largura_tela // 2) -(largura_janela // 2) 
        posicao_y = (altura_tela // 2) -(altura_janela // 2) 

        janela_remover_linhas.geometry(f"{largura_janela}x{altura_janela}+{posicao_x}+{posicao_y}")

        janela_remover_linhas.configure(bg="#FFFFFF")

        label_linha_inicio = tk.Label(janela_remover_linhas,text="Digite o numero da primeira linha a ser removida: ",font=("Arial",12),bg="#FFFFFF")
        label_linha_inicio.pack(pady=10)
        entry_linha_inicio = Entry(janela_remover_linhas,font=("Arial",12))
        entry_linha_inicio.pack()

        label_linha_fim = tk.Label(janela_remover_linhas,text="Digite o numero da ultima linha a ser removida: ",font=("Arial",12),bg="#FFFFFF")
        label_linha_fim.pack(pady=10)
        entry_linha_fim = Entry(janela_remover_linhas,font=("Arial",12))
        entry_linha_fim.pack()

        botao_remover = Button(janela_remover_linhas,text="Remover",font=("Arial",12),command=lambda:self.funcao_remover_linhas(entry_linha_inicio.get(),entry_linha_fim.get(),janela_remover_linhas))
        botao_remover.pack(pady=20)

        janela_remover_linhas.mainloop()

    def carregar_excel(self):
        tipo_arquivo = (("Excel files","*.xlsx;*.xls"),("All files","*.*"))
        self.nome_arquivo = filedialog.askopenfilename(title="Selecione o arquivo",filetypes=tipo_arquivo)

        try:
            self.df = pd.read_excel(self.nome_arquivo)
            self.atualiza_treeview()
        except Exception as e:
            messagebox.showerror("Erro",f"Nao foi possivel abrir o arquivo: {e}")

        self.soma_coluna_valores()


editor = ExcelEditor(janela)
janela.mainloop()

