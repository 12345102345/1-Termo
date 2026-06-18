import tkinter as tk 
from tkinter import messagebox 

# 1. configurar evento 

def solicitar_informacoes():
    #.get() serve para buscar o texto que foi digitado 
    nome_usuario = campo_nome.get()
    idade_usuario = campo_idade.get()
    if nome_usuario == "" :
        messagebox.showwarning ("Aviso , " "Por favor, digite seu nome :) ")

    else:
        messagebox.showwarning ("Saudações, querido aluno (‾◡◝) " , f"Ola, {nome_usuario} seja bem-vindo ao mundo das interfaces gráficas.")


# 2. Configurações de janela 

app = tk.Tk()
app.title("Tela de Usuario")
app.geometry("300x300")

# 3. componentes 

lbl_nom_usuario = tk.Label(app, text="Digite o seu nome :)").grid (row= 0, column=0, padx=10, pady=10) #grid - posicionamento em grade 


campo_nome = tk.Entry(app, font=("Arial" , 12))
campo_nome.grid(row= 1, column=0, padx=10, pady=5)

campo_idade = tk.Entry(app, font=("Arial" , 12))
campo_idade.grid(row= 1, column=0, padx=10, pady=5)

btn_cadastrar = tk.Button(app, text="Cadastrar" , command=solicitar_informacoes)
btn_cadastrar.grid(row=2, column=0, pady=15)

btn_fechar = tk.Button(app, text="fechar" , command=app.destroy)
btn_fechar.grid(row=2, column=0, pady=15)

#app.destroy = ele serve para fechar tendo seu coando proprio 

# 4. Rodar interface

app.mainloop()

