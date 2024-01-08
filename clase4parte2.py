from tkinter import *

root=Tk()
root.title("Entrada")
root.geometry("300x300")
root.resizable(0,0)

def saludar():
    saludo.set("Hola "+nombre.get()+" "+apellido.get())

apellido = StringVar()
nombre = StringVar()
saludo = StringVar()

etiqueta1 = Label(root, text="Escribe aqui tu Nombre: ", bd=4, bg="red", font=("Curier 10"))
etiqueta1.place(x=10, y=10)
entrada1= Entry(root, textvariable=nombre, bd=5)
entrada1.place(x=170, y=10)



etiqueta2 = Label(root, text="Escribe aqui tu Apellido: ", bd=4, bg="red", font=("Curier 10"))
etiqueta2.place(x=10, y=40)
entrada2 = Entry(root, textvariable=apellido, bd=5)
entrada2.place(x=170, y=40)

boton1 = Button(root, text="Saludar ahora", command=saludar, bd=5, bg="red")
boton1.place(x=112, y=123)


entrada3 = Entry(root, bd=20, font=("Curier 10"), textvariable=saludo, state="disable")
entrada3.place(x=70, y=221)


root.mainloop()