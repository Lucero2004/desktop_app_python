# se importa la libreria de tkinter con todas sus funcioones
from tkinter import*

#-------------------------
#funciones de la app
#-------------------------

#--------------------------
#ventana principal
#--------------------------

# se declara una variable llamada ventana principal, que adquiere las caracteristicas de un objeto Tk()
ventana_principal=Tk()

# titulo de la ventana
ventana_principal.title("Sistemas uis Socorro")

# tamaño de la mentana
ventana_principal.geometry("500x500")

# deshabiltar boton de maximizar
ventana_principal.resizable(0,0)

#color de fondode la ventana
ventana_principal.config(bg="yellow")
#------------------------
#frame operaciones
#-------------------------
frame_operaciones=Frame(ventana_principal)
frame_operaciones.config(bg="blue", width=500 , height=125)
frame_operaciones.place(x=0, y=250)
#------------------------
#frame resultados
#-------------------------
frame_resultados=Frame(ventana_principal)
frame_resultados.config(bg="red", width=500 , height=125)
frame_resultados.place(x=0, y=375)
# run
# se ejecuta la funcion(metodo)mainloop()de la clase Tk() a través de la instancia ventana_principal.
# se ejecuta la funcion(metodo)mainloop()de la clase Tk() a través de la instancia ventana_principal.

ventana_principal.mainloop()
