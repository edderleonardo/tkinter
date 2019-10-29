from tkinter import *
from tkinter.ttk import *

 
root = Tk()
root.title("Mi primera Ventana")
# no redimencinar 
root.resizable(0,0)
root.geometry("400x400")

label = Label(root, text="Hola Mundo")
label.place(x=120, y=0)

label1 = Label(root, text="Hola Mundo")
label1.place(x=120, y= 30)

label2 = Label(root, text="Hola Universo")
label2.place(x=120, y= 60)

label3 = Label(root, text="Hola Mundo")
label3.place(x=120, y= 90)

# Agregando imagenes 
image = PhotoImage(file='logo.gif')
Label(root, image=image).place(x=120, y=180)


root.mainloop()