from clases.Ingrediente import Ingrediente
from typing import Dict

# precio del articulo / peso del articulo * la cantidad que desea usar


class Receta:
    def __init__(self, nombreReceta: str):
        self.__nombreReceta = nombreReceta
        self.__ingredientes: Dict[str, Ingrediente] = {}
        self.__costoReceta = 0

    @property
    def nombreReceta(self):
        return self.__nombreReceta

    @nombreReceta.setter
    def nombreReceta(self, nombreRecetaNuevo):
        self.__nombreReceta = nombreRecetaNuevo
        return nombreRecetaNuevo

    @property
    def costoReceta(self):
        return self.__costoReceta

    @costoReceta.setter
    def costoReceta(self, nombreRecetaNuevo):
        self.__costoReceta = nombreRecetaNuevo
        return nombreRecetaNuevo

    def mostrarIngredientes(self):
        for clave, ingrediente in self.__ingredientes.items():
            ingredienteActual = self.__ingredientes[clave]
            print('''
Nombre del ingrediente: {0}
Precio del ingrediente: {1} pesos
Peso de la receta: {2} gramos
Medida Utilizada: {3}
Peso del articulo comprado: {4} gramos
Costo usado en la receta: {5} pesos
            '''.format(ingredienteActual.nombreIngrediente, ingredienteActual.precioIngrediente, ingredienteActual.pesoReceta, ingredienteActual.medidaReceta, ingredienteActual.pesoDeCompra, ingredienteActual.costoTotal))

    def agregarIngredientes(self, nombreIngrediente: str, medidaReceta: str, precioIngrediente: int, pesoReceta: int, pesoDeCompra: int):
        ing = Ingrediente(nombreIngrediente, medidaReceta, pesoReceta, precioIngrediente, pesoDeCompra)
        self.__ingredientes[nombreIngrediente] = ing
