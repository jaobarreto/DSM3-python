from tkinter import *

tela = Tk()
tela.title("Exemplo 3 interface")
tela.configure(background="#e5e5e5")


largura = 800
altura = 300

largura_screen = tela.winfo_screenwidth()
altura_screen = tela.winfo_screenwidth()
posx = largura_screen / 2 - largura / 2
posy = altura_screen / 2 - altura / 2

tela.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))
lbl_nome = Label(tela, text="Nome: ", font="Aarial 25 bold italic")
lbl_nome.place(x=10, y=10)

lbl_end = Label(tela, text="Endereço: ", font=("Comic Sans MC", "20", "bold"))
lbl_end.place(x=50,y=60)

tela.mainloop()
