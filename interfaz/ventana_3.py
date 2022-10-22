from tkinter import *
from tkinter import ttk
import tkinter as tk
# Interfaz (1)
raiz = Tk()
raiz.title("Ventana")
raiz.iconbitmap("img/icono.ico")
raiz.state('zoomed')
# Funcion (3)
txt_nombre = tk.StringVar()
def mostrar_texto():
    ttk.Label(frm, text=txt_nombre.get()).grid(column=0, row=3)
#Formulario (2)
frm = ttk.Frame(raiz, padding=10)
frm.grid()
ttk.Label(frm, text="Hola Mundo!").grid(column=0, row=0)

ttk.Entry(frm,textvariable=txt_nombre ).grid(column=1, row=0)
ttk.Button(frm, text="Aceptar", command=mostrar_texto).grid(column=0, row=2)
ttk.Button(frm, text="Quitar", command=raiz.destroy).grid(column=1, row=2)
raiz.mainloop()