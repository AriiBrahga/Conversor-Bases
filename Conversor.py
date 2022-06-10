from tkinter import *
from tkinter import messagebox

import tkinter as tk

janela = tk.Tk()

def converter():
    num=int(numero.get())
    basee=int(base.get())
    
    
    
    list_1 = '0123456789ABCDEF'
    list_2 = []
    list_3=[]


    while num != 0:
        resto = num % basee
        num = num // basee
        

        


        list_2.append(list_1[resto])

    list_2.reverse()    
    list_3.append(list_2)
    
 
    result["text"] = list_3











numero = Entry(janela)
numero.place(x=320, y=163)

texto1 = Label(janela, font=100, width=30, height=1, text="Digite o numero em decimal aqui: ")
texto1.place(x=45, y=160)
texto1["bg"] = "grey"

base = Entry(janela)
base.place(x=320, y=203)

texto2 = Label(janela, font=100, width=30, height=1, text="Digite em qual base quer a conversão: ")
texto2.place(x=45, y=200)
texto2["bg"] = "grey"

result = Label(janela, font=100, width=30, height=1, text="")
result.place(x=200, y=340)
result["bg"] = "grey"







bt = Button(janela, width=20, text="converter", command=converter)
bt.place(x=315, y=240)



















# titulo da janela
janela.title("Conversor de bases")

# cor da janela
janela["bg"] = "grey"

# LargxAlt+DistE+DistTop
janela.geometry("800x800+350+25")


janela.mainloop()