from tkinter import *
import time

root=Tk()
root.title("Mi Primer Ventana")
root.geometry("500x300")

boton1 = Button(root,text="Minimizar", command=root.iconify, bg="red")
boton1.pack(side=LEFT)

def imprimir():
    Label1 = Label(root, text="Imprimiendo...")
    Label1.pack()

boton2 = Button(root, text="Imprimir", command=imprimir, bg="blue")
boton2.pack(side=RIGHT)

root.mainloop()