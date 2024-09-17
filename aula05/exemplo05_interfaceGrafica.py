from tkinter import *

tela = Tk()
tela.title("Cálculo de Soma")
tela.geometry("700x500")

lbl_num1 = Label(tela, text="Digite um número: ", font="Arial 15 bold")
lbl_num1.place(x=50, y=50)

txt_num1 = Entry(tela, width=20, borderwidth=10, fg="blue", bg="white")
txt_num1.place(x=280, y=45)

lbl_num2 = Label(tela, text="Digite outro número: ", font="Arial 15 bold")
lbl_num2.place(x=50, y=85)

txt_num2 = Entry(tela, width=20, borderwidth=10, fg="blue", bg="white")
txt_num2.place(x=350, y=85)

lbl_resul = Label(tela, text="Resultado: ", font="Arial 15 bold")
lbl_resul.place(x=50, y=150)

txt_resul = Entry(tela, width=20, borderwidth=10, fg="blue", bg="white")
txt_resul.place(x=350, y=150)

def calcularSoma():
    soma = float(txt_num1.get()) + float(txt_num2.get())
    txt_resul.delete(0, END)
    txt_resul.insert(0, str(soma))  

btn_resultado = Button(tela, text="Calcular", command=calcularSoma)
btn_resultado.place(x=50, y=200)

tela.mainloop()
