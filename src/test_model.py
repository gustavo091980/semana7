import pytest
from model import *

def test_agregarPersona_no_null():
    persona = Model("Prueba", "Test", "123456789","M",65)
    #persona = None
    assert persona != None

def test_getNombre_no_null():
    obje_modelo = Model("","","","",0)
    obje_modelo.nombre = "Tavo"
    assert obje_modelo.nombre != None

def test_getNombre_no_vacio():
    obje_modelo = Model("","","","",0)
    obje_modelo.nombre = "Tavo"
    assert len(obje_modelo.nombre) > 0

def test_getApellido_no_null():
    obje_modelo = Model("","","","",0)
    obje_modelo.apellidos = "Perez"
    assert obje_modelo.apellidos != None

def test_getApellido_no_vacio():
    obje_modelo = Model("","","","",0)
    obje_modelo.apellidos = "Rodriguez"
    assert len(obje_modelo.apellidos) > 0

def test_getDocumento_no_null():
    obje_modelo = Model("","","","",0)
    obje_modelo.documento = "2534667"
    assert obje_modelo.documento != None

def test_getDocumento_no_vacio():
    obje_modelo = Model("","","","",0)
    obje_modelo.documento = "43565767"
    assert len(obje_modelo.documento) > 0

def test_getGenero_no_null():
    obje_modelo = Model("","","","",0)
    obje_modelo.genero = "F"
    assert obje_modelo.genero != None

def test_getGenero_no_vacio():
    obje_modelo = Model("","","","",0)
    obje_modelo.genero = "M"
    assert len(obje_modelo.genero) > 0

def test_getGenero_M_F():
    obje_modelo = Model("","","","",0)
    obje_modelo.genero = "F"
    assert obje_modelo.genero == "M" or obje_modelo.genero == "F"

def test_getEdad_no_null():
    obje_modelo = Model("","","","",0)
    obje_modelo.edad = 20
    assert obje_modelo.edad != None

def test_getEdad_no_vacio():
    obje_modelo = Model("","","","",0)
    obje_modelo.edad = 20
    assert obje_modelo.edad > 0

def test_getListPersona_no_nulo():
    listPersona = ListaPersonas.personas
    print(listPersona)
    assert listPersona != None

def test_getListPersona_no_vacio():
    listPersona = ListaPersonas.personas
    obje_modelo = Model("Pedro","Perez","3543545","M",22)
    listPersona.append(obje_modelo)
    #lista = ListaPersonas.mostrarData()
    assert len(listPersona) > 0