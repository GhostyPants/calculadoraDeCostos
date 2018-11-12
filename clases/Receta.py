from clases.Ingrediente import Ingrediente
from typing import Dict


class Receta:
    def __init__(self, nombreReceta: str):
        self.nombreReceta = nombreReceta
        self.ingredientes: Dict[str, Ingrediente] = {}

    def agregarIngredientes(
        self,
        nombreIngrediente: str,
        precioIngrediente: int,
        pesoReceta: int,
        medidaReceta: str,
        pesoDeCompra: int,
    ):
        ing = Ingrediente(
            nombreIngrediente, pesoReceta, medidaReceta, precioIngrediente, pesoDeCompra
        )
        self.ingredientes[nombreIngrediente] = ing
        print(self.ingredientes[nombreIngrediente]._nombreIngrediente)

