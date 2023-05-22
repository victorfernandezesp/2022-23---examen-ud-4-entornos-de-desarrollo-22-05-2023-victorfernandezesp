"""
Clase Perro.

:author: Victor Fernandez España
"""


class Perro:
    """
    Clase Perro
    """
    def __init__(self):
        """
        Constructor con el atributo ladra, contiene una cadena
        """
        self.ladra = 'Guau'

    def ladrar(self):
        """
        metodo ladrar
        :return: ladra, printea el atributo ladra que contiene la cadena guau
        """
        print(self.ladra);


p = Perro();
p.ladrar();
