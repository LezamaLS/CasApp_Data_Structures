import random

class Nodo:
    def __init__(self, articulo):
        self.articulo = articulo
        self.siguiente = None

class Inventario:
    def __init__(self):
        self.cabeza = None
        self.contadorRandom = 1

    def agregarArticulo(self, articulo):
        nuevo_nodo = Nodo(articulo)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo
        print(f"\n'{articulo}' Agregado")

    def agregarAleatorio(self):
        articuloAleatorio = f"Art Aleatorio #{self.contadorRandom}"
        self.contadorRandom += 1
        self.agregarArticulo(articuloAleatorio)

    def buscarArticulo(self, articulo):
        actual = self.cabeza
        while actual:
            if actual.articulo == articulo:
                print(f"\nSi tienes '{articulo}' en la despensa")
                return
            actual = actual.siguiente
        print(f"\nNo tienes '{articulo}' en la despensa")

    def eliminarArticulo(self, articulo):
        actual = self.cabeza
        anterior = None

        while actual:
            if actual.articulo == articulo:
                if anterior:
                    anterior.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente
                print(f"\n'{articulo}' eliminado de la despensa")
                return
            anterior = actual
            actual = actual.siguiente

        print(f"\nNo hay '{articulo}' en la despensa")

    def eliminarInventario(self):
        self.cabeza = None
        print("\nDespensa borrada xd")

    def verInventario(self):
        actual = self.cabeza
        print("\nTu Inventario:")
        while actual:
            print(actual.articulo)
            actual = actual.siguiente

    def menuLinkedList(self):
        while True:
            print("\n------- Inventario de Despensa -------")
            print("1. Nuevo articulo de despensa")
            print("2. Nuevo articulo aleatorio")
            print("3. Buscar en la despensa")
            print("4. Eliminar de la despensa")
            print("5. Ver despensa")
            print("6. Borrar la despensa")
            print("7. Regresar")

            opcion = input("\nSelecciona una opcion: ")

            if opcion == "1":
                articulo = input("\nArticulo a registrar: ")
                self.agregarArticulo(articulo)

            elif opcion == "2":
                self.agregarAleatorio()

            elif opcion == "3":
                articulo = input("\nArticulo a buscar: ")
                self.buscarArticulo(articulo)

            elif opcion == "4":
                articulo = input("\nArticulo a eliminar: ")
                self.eliminarArticulo(articulo)

            elif opcion == "5":
                self.verInventario()

            elif opcion == "6":
                self.eliminarInventario()

            elif opcion == "7":
                print("Regresando a Menu")
                break

            else:
                print("Opcion no valida, intenta de nuevo")
