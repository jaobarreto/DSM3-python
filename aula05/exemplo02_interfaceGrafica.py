from tkinter import *

tela = Tk()

tela.title("Exemplo 2 interface")
tela.configure(background="#e5e5e5")
tela.geometry("700x500")
# criando o label bg = cor de fundo fg = cor da letr
lbl_nome = Label(tela, text="Nome :", bg="#1e3743", fg="#fff")
# lbl_nome é o nome do label place = define a posição na tela
lbl_nome.place(x=10, y=20)

lbl_tel = Label(tela, text="Telefone: ", bg="#000", fg="#fff")
lbl_tel.place(x=10, y=40)

tela.mainloop()
