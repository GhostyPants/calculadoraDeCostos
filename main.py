from clases.Receta import Receta
from clases.Ingrediente import Ingrediente
from typing import Dict, List
import os

Recetario: Dict[str, Receta] = {}

# precio del articulo / peso del articulo * la cantidad que desea usar


def clearConsole():
    os.system("cls")


def menuPrincipal():
    print(
        """
    ====== Menu Principal ======
      1) Crear Receta
      2) Ver Recetas Creadas
      3) Agregar ingredientes
      4) Calcular costo de recetas
      5) Salir
      """)


def crearReceta(recetario: Dict):
    nombreReceta: str = input("Cual es el nombre de la receta: ")
    abreviacionNombre: str = input("\nIngrese una abreviacion del nombre de la receta: ")
    recetario[abreviacionNombre] = Receta(nombreReceta)
    # recetario.append({abreviacionNombre: Receta(nombreReceta)})


def mostrarRecetas(recetario: Dict):
    i = 1
    for clave, receta in recetario.items():
        if receta.costo <= 0:
            print("{2})\n Clave: {0}\n Receta de: {1}".format(clave, receta.nombre, i))
        else:
            print("{2})\n Clave: {0}\n Receta de: {1}\n Costo de la receta: {3}".format(clave, receta.nombre, i, receta.costo))
        i += 1


def agregarIngredientes(recetario: Dict):
    clearConsole()
    mostrarRecetas(recetario)
    opc: str = input("\nIngrese la clave de la receta que desea agregar los ingredientes: ")
    if recetario[opc]:
        nombreIngredientes = input("Ingrese el nombre del ingrediente: ")
        pesoReceta = int(input("Ingrese el peso que utiliza la receta: "))
        medidaReceta = input("Ingrese la medida utilizada en la receta: ")
        precioCompra = int(input("Ingrese cuanto costo el articulo: "))
        pesoDeCompra = int(input("Ingrese el peso del articulo comprado: "))
        recetario.get(opc).agregarIngredientes(nombreIngredientes,  medidaReceta, precioCompra, pesoReceta, pesoDeCompra)
        input("\nPresione enter para continuar\n")
    repetir = int(input(
    """====== Desea agregar otro ingrediente =====
    1) Si
    2) No
    
    Ingrese el numero: """))
    if repetir == 1:
        agregarIngredientes(recetario)


while True:
    clearConsole()
    menuPrincipal()
    opc: int = int(input("Selecciona una opcion: "))
    if opc == 1:
        clearConsole()
        crearReceta(Recetario)
    elif opc == 2:
        clearConsole()
        mostrarRecetas(Recetario)
        input("\nPresione enter para continuar\n")
    elif opc == 3:
        agregarIngredientes(Recetario)
    elif opc == 4:
        # mostrarRecetas(Recetario)
        Recetario["pan"].mostrarIngredientes()
        input()
    elif opc == 5:
        break

