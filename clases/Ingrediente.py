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

    @property
    def nombreIngrediente(self):
        return self._nombreIngrediente

    @nombreIngrediente.setter
    def nombreIngrediente(self, nombreIngredienteNuevo):
        self._nombreIngrediente = nombreIngredienteNuevo

    @property
    def pesoReceta(self):
        return self._pesoReceta

    @pesoReceta.setter
    def pesoReceta(self, pesoRecetaNuevo):
        self._pesoReceta = pesoRecetaNuevo

    @property
    def medidaReceta(self):
        return self._medidaReceta

    @medidaReceta.setter
    def medidaReceta(self, medidaRecetaNuevo):
        self._medidaReceta = medidaRecetaNuevo

    @property
    def precioIngrediente(self):
        return self._precioIngrediente

    @precioIngrediente.setter
    def precioIngrediente(self, precioIngredienteNuevo):
        self._precioIngrediente = precioIngredienteNuevo

    @property
    def pesoDeCompra(self):
        return self._pesoDeCompra

    @pesoDeCompra.setter
    def pesoDeCompra(self, pesoDeCompraNuevo):
        self._pesoDeCompra = pesoDeCompraNuevo
