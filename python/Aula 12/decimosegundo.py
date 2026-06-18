# tkinter 

#componentes principais 

# tl : a janela 
# label : texto em rotulo
# button: Um botão para o usuário clicar
# entry: Um campo de texto para o usuário digitar algo

#blobioteca 

import tkinter as tk 
from tkinter import messagebox 

# 1. Criar janela principal"

janela = tk.Tk()
janela.configure(bg="blue")
janela.title ("Minha primeira janela em GUI") #titulo da janela 
janela.geometry("400x350") #Largura e Altura


#2. Criar a função que o botão vai executar (evento)
def mostrar_mensagem():
    messagebox.showinfo ("Sucesso!", "Você clicou no botão")


# 3. Criar componentes 
lbl_titulo = tk.Label(janela, text= "Bem-vindo á aula Tkinter!", font=("Arial" , 14, "bold"), bg="#2e80cc")
btn_clique = tk.Button(janela, text="Clique Aqui :) ", font=("Arial",14), bg="#1d959e", fg="white", command=mostrar_mensagem)

# bg = titulo grifado 
# fg = cor do texto 

# 4. Posicionar os componentes 

lbl_titulo.pack(pady=20)
btn_clique.pack(pady=10)
#pady - pocisioanr vertical 
# padx - posicionar horizontal 

# 5. Rodar o loop da interface 
janela.mainloop()



