from tkinter import *

root = Tk()

root.resizable(0,0)
label = Label(root, text="Nombre de usuario")
label.grid(row=0, column=0, sticky='w')

entry = Entry(root)
entry.grid(row=0, column=1)

label2 = Label(root, text="Apellidos")
label2.grid(row=1,column=0, sticky='w')

entry2 = Entry(root)
entry2.grid(row=1,column=1)


root.mainloop()