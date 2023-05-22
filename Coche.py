"""
Clase Coche base para el Examen de la UD4
Refactorización
Extrae una superclase Vehículo con los campos
    num_serie
    fabricante
    color
:autor: Jaime Rabasco
"""


class Vehiculo:
    def __init__(self):
        self.__num_serie = 1;
        self.__color = 'rojo';
        self.__fabricante = 'seat';

    @property
    def num_serie(self):
        return self.__num_serie

    @num_serie.setter
    def num_serie(self, value):
        self.__num_serie = value


class Coche(Vehiculo):

    cilindrada = 1000;

    def __init__(self):
        pass;

    def __init__(self, num_serie, cilindrada, fabricante, color):
        super().__init__()
        self.num_serie = num_serie;
        self.cilindrada = cilindrada;
        self.fabricante = fabricante;
        self.color = color;

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, value: int):
        self.__color = value

    @property
    def cilindrada(self):
        return self.__cilindrada

    @cilindrada.setter
    def cilindrada(self, value):
        self.__cilindrada = value

    @property
    def fabricante(self):
        return self.__fabricante

    @fabricante.setter
    def fabricante(self, value):
        self.__fabricante = value
