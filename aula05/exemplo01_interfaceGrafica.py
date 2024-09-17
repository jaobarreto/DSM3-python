from tkinter import *

tela = Tk()

tela.title("Aula interface")
tela.configure(background="#1e3743")
tela.geometry("700x300")
# define para não redimensionar a tela
tela.resizable(false, false)

tela.maxsize(width=800, height=600)
tela.minsize(width=300, height=300)


tela.mainloop()
