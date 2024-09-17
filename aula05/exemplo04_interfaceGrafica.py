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

txt_nome = Entry(tela, width=40, borderwidth=5, fg="blue", bg="white")
txt_nome.pack()
txt_nome.insert(0, "Digite seu nome: ")

def mostratMsg():
    lbl_msg = Label(tela, text="Bem Vindo " + txt_nome.get())
    lbl_msg.place(x=80, y=100)
    

btn_botao= Button(tela,text="Aperte Aqui", command=mostratMsg)
btn_botao.pack()

tela.mainloop()
