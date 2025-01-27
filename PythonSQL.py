import tkinter as tk

from tkinter import *

from tkinter import ttk
from tkinter import messagebox

from Clientes import *

from Conexion import *

class FormularioClientes:
   global base
   base =None

   global textBoxId
   textBoxId =None
  
   global textBoxNombres
   textBoxNombres =None

   global textBoxApellidos
   textBoxApellidos =None

   global combo
   combo =None
  
   global groupBox
   groupBox =None

   global tree
   tree =None


def formulario():
  global textBoxId
  global textBoxNombres
  global textBoxApellidos
  global combo
  global base
  global groupBox
  global tree

  try:
    base = Tk()
    base.geometry("1200x300")
    base.title("Formulario")

    groupBox = LabelFrame(base,text="Datos Personales",padx=5,pady=5)
    groupBox.grid(row=0,column=5,padx=10,pady=10)

    labelId=Label(groupBox,text="ID:",width=13,font=("Helvetica",12)).grid(row=0,column=0)
    textBoxId =Entry(groupBox)
    textBoxId.grid(row=0,column=1)

    labelNombres=Label(groupBox,text="Nombres:", width=13,font=("Helvetica",12)).grid(row=1,column=0)
    textBoxNombres =Entry(groupBox)
    textBoxNombres.grid(row=1,column=1)

    labelApellidos=Label(groupBox,text="Apellidos:",width=13,font=("Helvetica",12)).grid(row=2,column=0)
    textBoxApellidos =Entry(groupBox)
    textBoxApellidos.grid(row=2,column=1)

    labelSexo=Label(groupBox,text="Sexo:",width=13,font=("Helvetica",12)).grid(row=3,column=0)
    seleccionSexo =tk.StringVar()
    combo=ttk.Combobox(groupBox,values=["Masculino","Femenino","Indefinido"],textvariable=seleccionSexo)
    combo.grid(row=3,column=1)
    seleccionSexo.set("Masculino")

    Button(groupBox,text="Guardar",width=10,command=guardarRegistros).grid(row=4,column=0)
    Button(groupBox,text="Modificar",width=10,command=modificarRegistros).grid(row=4,column=1)
    Button(groupBox,text="Eliminar",width=10,command=eliminarRegistros).grid(row=4,column=2)

    groupBox=LabelFrame (base,text = "Lista de Personas",padx=5,pady=5,)
    groupBox.grid(row=0,column=1,padx=5,pady=5)

    #Treeview

    #Configuración de columnas
    tree=ttk.Treeview(groupBox,columns=("Id","Nombres","Apellidos","Sexo"),show='headings',height=5,)
    tree.column("# 1",anchor=CENTER)
    tree.heading("# 1",text="Id")
    tree.column("# 2",anchor=CENTER)
    tree.heading("# 2",text="Nombres")
    tree.column("# 3",anchor=CENTER)
    tree.heading("# 3",text="Apellidos")
    tree.column("# 4",anchor=CENTER)
    tree.heading("# 4",text="Sexo")

    #Agregar datos a la tabla
    #Mostrar datos de la tabla

    for row in Clientes.mostrarClientes():
      tree.insert("","end",values=row)

    #Ejecutar función al hacer Click

    tree.bind("<<TreeviewSelect>>",seleccionarRegistro)

    tree.pack()

    base.mainloop()
        
  except ValueError as error:
        print("Error al mostrar la interfaz: {}".format(error))

def guardarRegistros():
    
    global textBoxNombres,textBoxApellidos,combo,groupBox


    try:
       if textBoxNombres is None or textBoxApellidos is None or combo is None:
          print("Los widgets no estan inicializados")
          return
       
       nombres = textBoxNombres.get()
       apellidos = textBoxApellidos.get()
       sexo = combo.get()

       Clientes.ingresarClientes(nombres,apellidos,sexo)
       messagebox.showinfo("Información","Los datos han sido guardados")

       actualizarTreeView()



       #Limpieza de Campos

       textBoxNombres.delete(0,END)
       textBoxApellidos.delete(0,END)

    except ValueError as error:
       print("Error al ingresar los datos {}".format(error))


def actualizarTreeView():
   global tree

   try:
      #Eliminar elementos del Tree
      tree.delete(*tree.get_children())

      #Obtener nuevos datos
      datos = Clientes.mostrarClientes()

      #Insertar los nuevos datos
      for row in Clientes.mostrarClientes():
       tree.insert("","end",values=row)
   except ValueError as error:
      print("Error al actualizar tabla{}".format(error))

def seleccionarRegistro(event):
   try:
      seleccion = tree.focus()

      if seleccion:
         values = tree.item(seleccion)['values']

         #Establecer valores
         textBoxId.delete(0,END)
         textBoxId.insert(0,values[0])
         textBoxNombres.delete(0,END)
         textBoxNombres.insert(0,values[1])
         textBoxApellidos.delete(0,END)
         textBoxApellidos.insert(0,values[2])
         combo.set(values[3])

   except ValueError as error:
      print("Error al seleccionar registro {}".format(error))
      

def modificarRegistros():
    
    global textBoxId,textBoxNombres,textBoxApellidos,combo,groupBox


    try:
       if textBoxId is None or textBoxApellidos is None or combo is None:
          print("Los widgets no estan inicializados")
          return
       

       idUsuario = textBoxId.get()
       nombres = textBoxNombres.get()
       apellidos = textBoxApellidos.get()
       sexo = combo.get()

       Clientes.modificarClientes(idUsuario,nombres,apellidos,sexo)
       messagebox.showinfo("Información","Los datos han sido actualizados")

       actualizarTreeView()



       #Limpieza de Campos
       textBoxId.delete(0,END)
       textBoxNombres.delete(0,END)
       textBoxApellidos.delete(0,END)

    except ValueError as error:
       print("Error al modificar los datos {}".format(error))


def eliminarRegistros():
    
    global textBoxId,textBoxNombres,textBoxApellidos


    try:
       if textBoxId is None:
          print("Los widgets no estan inicializados")
          return
       

       idUsuario = textBoxId.get()

       Clientes.eliminarClientes(idUsuario)
       messagebox.showinfo("Información","Los datos han sido eliminados")

       actualizarTreeView()

       #Limpieza de Campos
       textBoxId.delete(0,END)
       textBoxNombres.delete(0,END)
       textBoxApellidos.delete(0,END)

    except ValueError as error:
       print("Error al modificar los datos {}".format(error))


formulario()