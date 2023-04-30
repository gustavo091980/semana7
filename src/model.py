import pickle

class Model:
    def __init__(self, nombre, apellidos, documento, genero, edad):
        self.nombre = nombre
        self.apellidos = apellidos
        self.documento = documento
        self.genero = genero
        self.edad = edad
        print("Se ha creado una usuario nuevo con el nombre de ", self.nombre)

    def __str__(self):
        return "{} {} {}".format(self.nombre, self.genero, self.edad)
    
    def setNombre(self, nombre):
        self.nombre = nombre

    def getNombre(self):
        return self.nombre
    
class ListaPersonas:
    personas=[]

    def __init__(self):
        
        listadoDePersonas=open("data", "ab+")
        listadoDePersonas.seek(0)

        try:
            self.personas=pickle.load(listadoDePersonas)
            print("El total de usuarios almacenados es: {} Usuarios".format(len(self.personas)))
        except:
            print("No hay registros almacenados")
        finally:
            listadoDePersonas.close()
            del(listadoDePersonas)

    def agregarPersonas(self, p):
        self.personas.append(p)
        self.guardarPersonas()

    def mostrarPersonas(self):
        for p in self.personas:
            print(p)

    def guardarPersonas(self):
        listadoDePersonas=open("data", "wb")
        pickle.dump(self.personas, listadoDePersonas)
        listadoDePersonas.close()
        del(listadoDePersonas)

    def mostrarData(self):
        print("Los usuarios guardados son los siguiente:")
        for p in self.personas:
            print(p)

