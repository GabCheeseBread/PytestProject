from validar_login import *

def test_nome():
    assert validar_nome("magrôncio") == False

def test_senha():
    assert validar_senha("cUF3d0r333nt*nc!o")
