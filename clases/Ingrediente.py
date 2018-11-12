class Ingrediente:
    def __init__(
        self,
        nombreIngrediente: str,
        pesoReceta: int,
        medidaReceta: str,
        precioIngrediente: int,
        pesoDeCompra: int,
    ):
        self._nombreIngrediente = nombreIngrediente
        self._pesoReceta = pesoReceta
        self._medidaReceta = medidaReceta
        self._precioIngrediente = precioIngrediente
        self._pesoDeCompra = pesoDeCompra
        self._costoTotal: int

