from model import *
from view import View

class Control:
    obje_modelo = Model("","","","","")
    obje_vista = View()
    obje_modelo.nombre = obje_vista.nombre
    obje_modelo.apellidos = obje_vista.apellidos
    obje_modelo.documento = obje_vista.documento
    obje_modelo.genero = obje_vista.genero
    obje_modelo.edad = obje_vista.edad

    miLista=ListaPersonas()
    persona = Model(obje_modelo.nombre, obje_modelo.apellidos, obje_modelo.documento, obje_modelo.genero, obje_modelo.edad)
    miLista.agregarPersonas(persona)

    miLista.mostrarData()