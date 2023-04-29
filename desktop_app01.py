# se importa la libreria de tkinter con todas sus funcioones
from tkinter import*
from tkinter import messagebox
#-------------------------
#funciones de la app
#-------------------------
def calcular():
    messagebox.showinfo("Minicalculadora 1.0","Hizo click el el Botón calcular")
    S=int(a.get())+int(b.get())
    r=int(a.get())-int(b.get())
    m=int(a.get())*int(b.get())
    D=int(a.get())/int(b.get())
    P=int(a.get())**int(b.get())
    mod=int(a.get())%int(b.get())
    N=int(a.get())//int(b.get())
    t_resultados.insert(INSERT,f"{a.get()}+{b.get()}={S}\n")
    t_resultados.insert(INSERT,f"{a.get()}-{b.get()}={r}\n")
    t_resultados.insert(INSERT,f"{a.get()}*{b.get()}={m}\n")
    t_resultados.insert(INSERT,f"{a.get()}/{b.get()}={D}\n")
    t_resultados.insert(INSERT,f"{a.get()}**{b.get()}={P}\n")
    t_resultados.insert(INSERT,f"{a.get()}%{b.get()}={mod}\n")
    t_resultados.insert(INSERT,f"{a.get()}//{b.get()}={N}\n")
def Borrar():
    messagebox.showinfo("Minicalculadora 1.0","Los datos borrará")
    a.set("")
    b.set("")
    t_resultados.delete("1.0","end")
def Salir():
    messagebox.showinfo("Minicalculadora 1.0","La app se cerrará")

    ventana_principal.destroy()
#--------------------------
#ventana principal
#--------------------------

# se declara una variable llamada ventana principal, que adquiere las caracteristicas de un objeto Tk()
ventana_principal=Tk()

# titulo de la ventana
ventana_principal.title("Minicalcladora 1.0")

# tamaño de la mentana
ventana_principal.geometry("500x500")

# deshabiltar boton de maximizar
ventana_principal.resizable(0,0)

#color de fondode la ventana
ventana_principal.config(bg="gray") 
#------------------------
# Variables de control
#-------------------------
a=StringVar()
b=StringVar()
#------------------------
# Entrada de Datos
#-------------------------
frame_entrada=Frame(ventana_principal)
frame_entrada.config(bg="white", width=480 , height=180)
frame_entrada.place(x=10, y=10)

# Logo de la appp
logo=PhotoImage(file="logo_uis.png")
lb_logo=Label(frame_entrada, image=logo, bg="white")
lb_logo.place(x=11, y=40)

# Etiquta para logo
lb_titulo=Label(frame_entrada, text="Minicalculadora1.0")
lb_titulo.config(bg="white" , fg="green", font=("Helvetica",20))
lb_titulo.place(x=240,y=10)

#Etiqueta para el primer numero
lb_a=Label(frame_entrada, text="a :")
lb_a.config(bg="white" , fg="green", font=("Helvetica",20 ))
lb_a.place(x=250, y=60)

# Caja de texto
entry_a=Entry(frame_entrada, textvariable=a)
entry_a.config(bg="white" , fg="green", font=("Helvetica",20 ))
entry_a.focus_set()
entry_a.place(x=290, y=60, width=100 ,height=30)

# Etiqueta 2 numero
lb_b=Label(frame_entrada, text="b :")
lb_b.config(bg="white" , fg="green", font=("Helvetica",20 ))
lb_b.place( x=250, y=100)

# Caja de texto
entry_b=Entry(frame_entrada, textvariable=b)
entry_b.config(bg="white" , fg="green", font=("courier",20 ))
entry_b.place(x=290, y=100, width=100 ,height=30)
#-------------------------------
#Freame operaciones
#---------------------------
frame_operaciones=Frame(ventana_principal)
frame_operaciones.config(bg="white", width=480 , height=100)
frame_operaciones.place(x=10, y=200)

#boton calcular"
bt_calcular=Button(frame_operaciones, text="calcular",
command=calcular)
bt_calcular.place(x=45, y=35, width=100 ,height=30)

# boton borrar
bt_borrar=Button(frame_operaciones, text="Borrar",
command=Borrar)
bt_borrar.place(x=190, y=35, width=100 ,height=30)

# boton salir
bt_salir=Button(frame_operaciones, text="Salir",
command=Salir)
bt_salir.place(x=335, y=35, width=100 ,height=30)
#------------------------
#frame resultados
#-------------------------
frame_resultados=Frame(ventana_principal)
frame_resultados.config(bg="white", width=480 , height=180)
frame_resultados.place(x=10, y=310)

#area de texto para resultados
t_resultados=Text(frame_resultados)
t_resultados.config(bg="black",fg="green",font=("courier",20))
t_resultados.place(x=10, y=10, width=460, height=160)
# run
# se ejecuta la funcion(metodo)mainloop()de la clase Tk() a través de la instancia ventana_principal.
# se ejecuta la funcion(metodo)mainloop()de la clase Tk() a través de la instancia ventana_principal.

ventana_principal.mainloop()
