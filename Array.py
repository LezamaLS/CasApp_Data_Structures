class ListaRapidaSuper:
    def __init__(self):
        self.listaSuper = []

    def insertar(self, item):
        self.listaSuper.append(item)
        print(f"\n{item} agregado a la lista.")

    def mostrar(self):
        if not self.listaSuper:
            print("\nLista vacia")
        else:
            print("\nLista rapida de super:")
            for i, item in enumerate(self.listaSuper, start=1):
                print(f"{i}. {item}")

    def eliminarTodo(self):
        self.listaSuper.clear()
        print("\nLista rapida borrada")


    def menuArray(self):
        while True:
            print("\n------- Lista Rapida de Super -------")
            print("1. Agregar articulo de super")
            print("2. Ver lista")
            print("3. Borrar lista completa")
            print("4. Regresar")            

            opcion = input("\nSelecciona una opcion: ")

            if opcion == "1":
                item = input("\nArticulo a agregar: ")
                self.insertar(item)

            elif opcion == "2":
                self.mostrar()

            elif opcion == "3":
                self.eliminarTodo()

            elif opcion == "4":
                print("Regresando a Menu")
                break

            else:
                print("Opcion no valida, intenta de nuevo")