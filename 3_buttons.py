from tkinter import *

# -- Functions --

def hola():
    print("Hola universo")

def create_label():
    Label(root, text="Etiqueta al vuelo").pack()

root = Tk()

Button(root, text="Click", command=hola).pack()


root.mainloop()