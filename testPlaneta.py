import tkinter as tk #se importa esta libreria para generar el entorno gráfico (crea un lienzo en blanco y se le agregan componentes como los cuadros de dialogo y/o mensaje)
from tkinter import simpledialog #para los dialogos
from tkinter import messagebox #para los mensajes

from Planeta import Planeta

planetita = Planeta()

#se agisigna una variable llamada root y se asigna a la clase tk
root=tk.Tk() #es como la primera capa de fondo (pero se tiene que ocultar)
root.withdraw()#con esto se oculta y se vea AESTHETIC

messagebox.showinfo("GALAXIA","SISTEMA SOLAR") #GALAXIA es el mini titulo y SISTEMA SOLAR es el que aparece adentro del mensaje

#messagebox.showinfo
#simpledialog.ask[tipo de dato]
    
planetita.nombre = simpledialog.askstring("SISTEMA SOLAR","Nombre: ") #Sepone el tipo de dato después del ask
planetita.masa =  simpledialog.askfloat("SISTEMA SOLAR","Masa: ")
planetita.volumen = simpledialog.askfloat("SISTEMA SOLAR","Volumen: ")
planetita.distancia = simpledialog.askfloat("SISTEMA SOLAR","Distancia al sol: ")



messagebox.showinfo("","Su densidad es: "+str(planetita.calcularDensidad()))
#La otra opción es:  messagebox.showinfo("",f"Su densidad es: ",{planetita.calcularDensidad()})

messagebox.showinfo("","Es un planeta exterior" if planetita.esPlanetaExterior() else "No es un planeta exterior")

#if planetita.esPlanetaExterior():
#    print("Es un planeta exterior")
#else:
#    print("No es un planeta exterior")