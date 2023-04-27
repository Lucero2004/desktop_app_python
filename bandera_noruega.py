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
ventana_principal.title("Bandera Noruega")

# tamaño de la mentana
ventana_principal.geometry("700x500")

# deshabiltar boton de maximizar
ventana_principal.resizable(0,0)

#color de fondode la ventana
ventana_principal.config(bg="red")
#------------------------
#Entrada de datos
#-------------------------
frame_entrada=Frame(ventana_principal)
frame_entrada.config(bg="white", width=680 , height=100)
frame_entrada.place(x=10, y=200)
frame_entrada1=Frame(ventana_principal)
frame_entrada1.config(bg="white", width=100 , height=700)
frame_entrada1.place(x=200, y=10)
frame_entrada2=Frame(ventana_principal)
frame_entrada2.config(bg="blue", width=680 , height=40)
frame_entrada2.place(x=10, y=230)
frame_entrada3=Frame(ventana_principal)
frame_entrada3.config(bg="blue", width=40 , height=680)
frame_entrada3.place(x=230, y=10)


# run
# se ejecuta la funcion(metodo)mainloop()de la clase Tk() a través de la instancia ventana_principal.
# se ejecuta la funcion(metodo)mainloop()de la clase Tk() a través de la instancia ventana_principal.

ventana_principal.mainloop()