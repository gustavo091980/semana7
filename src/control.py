from model import *

class Control:
   
    def guardar( nombre, apellidos, documento, genero, edad):
        miLista=ListaPersonas()
        persona = Model(nombre, apellidos, documento, genero, edad)
        miLista.agregarPersonas(persona)
        miLista.mostrarData()
        #return "Guardado"
            