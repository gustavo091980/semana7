class View:
    def __init__(self):

        print("******** Formulario Crear Usuario ********")
        print("Datos Básicos")
        print("")
        print("*******************************************")
        print("")
        print("")
        print("Nombre: ")

        self.nombre = input()
        print("Apellidos")
        self.apellidos = input()
        print("Número Documento")
        self.documento = input()
        print("Sexo M ó F")
        self.genero = input()
        print("Edad")
        self.edad = input()