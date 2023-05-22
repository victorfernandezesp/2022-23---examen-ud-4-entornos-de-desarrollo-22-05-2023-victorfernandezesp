"""
Clase Coche base para el Examen de la UD4
Refactorización
Extrae una superclase Vehículo con los campos
    num_serie
    fabricante
    color
:autor: Victor Fernandez España
"""


class Vehiculo:
    """
    Clase Vehiculo
    """
    def __init__(self):
        """
        Constructor con los atributos num_serie, color y fabricante
        """
        self.__num_serie = 1;
        self.__color = 'rojo';
        self.__fabricante = 'seat';

    @property
    def num_serie(self):
        """
        Propiedad num_serie
        :return: num_serie
        """
        return self.__num_serie

    @num_serie.setter
    def num_serie(self, value):
        """
        propiedad num_serie
        :param value: el valor a substituir en el objeto num_serie
        :return: self.__num_serie
        """
        self.__num_serie = value


class Coche(Vehiculo):
    """
    Clase Coche que hereda de Vehiculo
    """
    cilindrada = 1000;

    def __init__(self):
        """
        Constructor vacio
        """
        pass;

    def __init__(self, num_serie, cilindrada, fabricante, color):
        """
        Constructor de la clase  Vehiculo
        :param num_serie: Numero de serie del coche
        :param cilindrada: Numero de cilindros
        :param fabricante: fabricante del coche
        :param color: color del coche
        """
        self.num_serie = num_serie;
        self.cilindrada = cilindrada;
        self.fabricante = fabricante;
        self.color = color;

    @property
    def color(self):
        """
        Propiedad color de coche
        :return: self.__color
        """
        return self.__color

    @color.setter
    def color(self, value: int):
        """
        propiedad color
        :param value: el valor a substituir en el objeto color
        :return: self.__color
        """
        self.__color = value

    @property
    def cilindrada(self):
        """
        Propiedad cilindrada de coche
        :return: self.__cilindrada
        """
        return self.__cilindrada

    @cilindrada.setter
    def cilindrada(self, value):
        """
        propiedad cilindrada
        :param value: el valor a substituir en el objeto cilindrada
        :return: self.__cilindrada
        """
        self.__cilindrada = value

    @property
    def fabricante(self):
        """
        Propiedad fabricante de coche
        :return: self.__fabricante
        """
        return self.__fabricante

    @fabricante.setter
    def fabricante(self, value):
        """
        propiedad fabricante
        :param value: el valor a substituir en el objeto fabricante
        :return: self.__fabricante
        """
        self.__fabricante = value
