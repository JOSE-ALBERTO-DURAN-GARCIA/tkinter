from tkinter import*

root = Tk()

root.title=("Mi primer Ventana") #poniendo nuestro primer tutulo

root.geometry("500x300") #dandole las dimensiones a nuestra ventana

root.iconbitmap("python.ico") #colocando nuestro logo
root.resizable(0,0)#Hacemos que nuestra ventana no se modifique ni a lo ancho ni a lo alto

root.config(bg="red", cursor="mouse")#cambiamos el dibujo del raton
root.mainloop() #nos visualiza la ventana