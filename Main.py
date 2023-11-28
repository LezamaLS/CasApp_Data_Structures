from Arbol import ArbolBinario
from Array import ListaRapidaSuper
from Stack import HistorialLimpieza
from Queue import ControlRecetas
from Sorting import OrdenadorArchivos
from Hash import ListaContactos
from LinkedList import Inventario
from Grafo import RutaRecogida

# Clase principal del programa
class CasApp:
    def __init__(self):
        self.arbol = ArbolBinario()
        self.array = ListaRapidaSuper()
        self.stack = HistorialLimpieza()
        self.queue = ControlRecetas()
        self.sorting = OrdenadorArchivos()
        self.hasheo = ListaContactos(30)
        self.linkedList = Inventario()
        self.grafo = RutaRecogida()

    def menuPrincipal(self):
        while True:
            print("\n------- Organizacion del Hogar -------")
            print("1. Lista Rapida de Super")
            print("2. Registro de limpieza")
            print("3. Control de Recetas")
            print("4. Inventariado de Despensa")
            print("5. Lista de Contactos")
            print("6. Ordenador de Archivos")
            print("7. Organizador de Carpetas")
            print("8. Ruta para recoger Familia")
            print("9. Salir")

            opcion = int(input("\nSelecciona una opcion: "))

            if opcion == 1:
                self.array.menuArray()             

            elif opcion == 2:
                self.stack.menuStack()

            elif opcion == 3:   
                self.queue.menuQueue()

            elif opcion == 4:
                self.linkedList.menuLinkedList()

            elif opcion == 5:
                self.hasheo.menuHash()

            elif opcion == 6:
                self.sorting.menuSorting()

            elif opcion == 7:
                self.arbol.menuArbol()

            elif opcion == 8:
                self.grafo.menuGrafo()

            elif opcion == 9:
                print("Gracias por usar CasApp! Nos vemos!")
                break

            else:
                print("Opcion no valida, intenta de nuevo")


if __name__ == "__main__":
    programa = CasApp()
    programa.menuPrincipal()

