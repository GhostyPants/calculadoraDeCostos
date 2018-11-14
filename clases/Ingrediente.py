class Ingrediente:
    def __init__(self, nombreIngrediente: str, medidaReceta: str, pesoReceta: int, precioIngrediente: int, pesoDeCompra: int):
        self.__nombreIngrediente = nombreIngrediente
        self.__pesoReceta = pesoReceta
        self.__medidaReceta = medidaReceta
        self.__precioIngrediente = precioIngrediente
        self.__pesoDeCompra = pesoDeCompra
        self.__costoTotal = self.__calcularCostoIngrediente()

    @property
    def nombreIngrediente(self):
        return self.__nombreIngrediente

    @nombreIngrediente.setter
    def nombreIngrediente(self, nombreIngredienteNuevo):
        self.__nombreIngrediente = nombreIngredienteNuevo

    @property
    def pesoReceta(self):
        return self.__pesoReceta

    @pesoReceta.setter
    def pesoReceta(self, pesoRecetaNuevo):
        self.__pesoReceta = pesoRecetaNuevo

    @property
    def medidaReceta(self):
        return self.__medidaReceta

    @medidaReceta.setter
    def medidaReceta(self, medidaRecetaNuevo):
        self.__medidaReceta = medidaRecetaNuevo

    @property
    def precioIngrediente(self):
        return self.__precioIngrediente

    @precioIngrediente.setter
    def precioIngrediente(self, precioIngredienteNuevo):
        self.__precioIngrediente = precioIngredienteNuevo

    @property
    def pesoDeCompra(self):
        return self.__pesoDeCompra

    @pesoDeCompra.setter
    def pesoDeCompra(self, pesoDeCompraNuevo):
        self.__pesoDeCompra = pesoDeCompraNuevo

    @property
    def costoTotal(self):
        return self.__costoTotal
    
    @costoTotal.setter
    def costoTotal(self, nuevoCosto):
        print('Estableciendo costo')
        self.__costoTotal = nuevoCosto
    
    def __calcularCostoIngrediente(self):
        # print(ingrediente.pesoReceta)
        return self.__precioIngrediente / self.__pesoDeCompra * self.__pesoReceta