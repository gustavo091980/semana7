from tkinter import *
from tkinter import messagebox
from control import *
validate_entry = lambda text: text.isdecimal()
class View:
    def __init__(self):
        #obj_control = Control()
        raiz = Tk()
        miFrame = Frame(raiz, width=600, height=400)
        raiz.title("Registro Usuario")
        miFrame.pack()

        tituloLabel = Label(miFrame, text="Crear Usuario").place(x=200, y=50)
        nombreLabel = Label(miFrame, text="Nombre").place(x=200, y=100)
        apellidoLabel = Label(miFrame, text="Apellido").place(x=200, y=150)
        documentoLabel = Label(miFrame, text="Documento").place(x=200, y=200)
        generoLabel = Label(miFrame, text="Genero").place(x=200, y=250)
        edadLabel = Label(miFrame, text="Edad").place(x=200, y=300)

        

        nombreInput = Entry(miFrame)
        nombreInput.place(x=280, y=100)
        apellidoInput = Entry(miFrame)
        apellidoInput.place(x=280, y=150)
        documentoInput = Entry(miFrame, validate="key", validatecommand=(raiz.register(validate_entry), "%S"))
        documentoInput.place(x=280, y=200)
        option = IntVar()
        Radiobutton(miFrame, text="Masculino", variable=option, value=1).place(x=280, y=250)
        Radiobutton(miFrame, text="Femenino", variable=option, value=2).place(x=360, y=250)
        edadInput = Entry(miFrame, validate="key", validatecommand=(raiz.register(validate_entry), "%S"))
        edadInput.place(x=280, y=300) 
        

        def executeSave():
            sexo = ""

            #mensajeNombre = StringVar()
            #mensajeApellido = StringVar()
            #mensajeDocumento = StringVar()
            #mensajeSexo = StringVar()
            #mensajeEdad = StringVar()
            print("Sexo ",sexo)
            print(option.get())
            if option.get() == 1:
                sexo = "M"
            elif option.get() == 2:
                sexo = "F"

            print("Sexo 2 ",sexo)
            #mensajeRequerido = "Campo Requerido"
            mensajeGenerado = 0
            
            if len(nombreInput.get()) == 0:
                """mensajeNombre = mensajeRequerido
                label1 = Label(miFrame, text=mensajeNombre).place(x=200, y=125)"""
                print("Ingresa nombreInput")
                mensajeGenerado += 1 
           

            if len(apellidoInput.get()) == 0:
                """mensajeApellido = mensajeRequerido
                Label(miFrame, text=mensajeApellido).place(x=200, y=175)"""
                print("Ingresa apellidoInput")
                mensajeGenerado += 1
          

            if len(documentoInput.get()) == 0:
                """mensajeDocumento = mensajeRequerido
                Label(miFrame, text=mensajeDocumento).place(x=200, y=225)"""
                print("Ingresa documento")
                mensajeGenerado += 1
           

            match sexo:
                case "M":
                    print("Ingresa M")
                    #mensajeGenerado -= 1            
                case "F":
                    print("Ingresa F")
                    #mensajeGenerado -= 1
                case _:
                    print("Ingresa nada")
                    mensajeGenerado += 1
            
            """if len(sexo) == 0:
                mensajeSexo = mensajeRequerido
                Label(miFrame, text=mensajeSexo).place(x=200, y=275)
                print("Ingresa sexo")
                mensajeGenerado += 1
            else:
                mensajeSexo = ""
                Label(miFrame, text=mensajeSexo).place(x=200, y=275)
                mensajeGenerado -= 1"""

            if edadInput.get() == 0 or edadInput.get() == "":
                
                print("Ingresa edad")
                mensajeGenerado += 1
           

            print(mensajeGenerado)

            if mensajeGenerado <= 0:
                #print(nombreInput.get(), apellidoInput.get(), documentoInput.get(), sexo, edadInput.get())
                Control.guardar(nombreInput.get(), apellidoInput.get(), documentoInput.get(), sexo, edadInput.get())
                #Label(miFrame, text="Usuario Guardado").place(x=200, y=380)
                clear_text()
                messagebox.showinfo("MODIFICACION","USURIO INGRESADO" )
            else:
                messagebox.showwarning("Informativo","Todos los campos son obligatorios" )

        def clear_text():
           nombreInput.delete(0, END)
           apellidoInput.delete(0, END)
           documentoInput.delete(0, END)
           edadInput.delete(0, END)
           nombreInput.focus()
        
        Button(miFrame, text="Guardar", command=executeSave, font=('Helvetica bold',10)).place(x=280, y=350)
        Button(miFrame, text="Nuevo", command=clear_text, font=('Helvetica bold',10)).place(x=350, y=350)
        
        raiz.mainloop()
      