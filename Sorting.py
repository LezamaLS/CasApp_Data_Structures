import random

class OrdenadorArchivos:
    def __init__(self):
        self.datos = []

    def agregarId(self, dato):
        self.datos.append(dato)

    def agregarRandom(self, cantidad):
        self.datos.extend(random.sample(range(1, 1000), cantidad))

    def ordenarId(self):
        for i in range(1, len(self.datos)):
            actual = self.datos[i]
            j = i - 1
            while j >= 0 and actual < self.datos[j]:
                self.datos[j + 1] = self.datos[j]
                j -= 1
            self.datos[j + 1] = actual
        print("\nDatos Ordenados")

    def verId(self):
        print("\nEstos son los IDs de los archivos:", self.datos)

    def eliminarTodo(self):
        self.datos = []
        print("\nArchivero eliminado")

    def menuSorting(self):
        while True:
            print("\n------- Ordenador de Archivos -------")
            print("1. Agregar nuevo ID de Archivo")
            print("2. Agregar 300 IDs aleatorios")
            print("3. Ordenar Archivos por ID")
            print("4. Ver todos los Archivos")
            print("5. Eliminar todos los datos")
            print("6. Salir")
            opcion = int(input("\nSelecciona una opcion: "))

            if opcion == 1:
                nuevoId = int(input("\nNuevo ID de archivo: "))
                self.agregarId(nuevoId)

            elif opcion == 2:
                self.agregarRandom(300)

            elif opcion == 3:
                self.ordenarId()

            elif opcion == 4:
                self.verId()
            elif opcion == 5:
                self.eliminarTodo()

            elif opcion == 6:
                print("Regresando a Menu")
                break

            else:
                print("Opcion no valida, intenta de nuevo")

