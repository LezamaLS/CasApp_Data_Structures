from collections import deque

class ControlRecetas:
    def __init__(self):
        self.pasosReceta = deque()

    def insertarPaso(self, paso):
        self.pasosReceta.append(paso)
        print(f"\nNuevo paso agregado: '{paso}'")

    def mostrarSiguiente(self):
        if self.pasosReceta:
            siguientePaso = self.pasosReceta[0]
            print(f"\nSiguiente paso: {siguientePaso}")
        else:
            print("\nYa terminaste la receta. Ahora esta vacia")

    def realizarPaso(self):
        if self.pasosReceta:
            pasoRealizado = self.pasosReceta.popleft()
            print(f"\n'{pasoRealizado}' fue realizado")
        else:
            print("\nYa terminaste la receta. Ahora esta vacia")

    def eliminarReceta(self):
        self.pasosReceta.clear()
        print("\nLa receta ha sido reiniciada.")

    def verReceta(self):
        if self.pasosReceta:
            print("\nReceta completa:")
            for paso in self.pasosReceta:
                print(f"- {paso}")
        else:
            print("\nReceta Vacia")

    def menuQueue(self):
        while True:
            print("\n------- Control de Receta -------")
            print("1. Agregar paso a la receta")
            print("2. Mostrar siguiente paso")
            print("3. Terminar paso actual")
            print("4. Borrar toda la receta")
            print("5. Ver la Receta")
            print("6. Regresar")

            opcion = input("\nSelecciona una opcion: ")

            if opcion == "1":
                paso = input("\nPaso nuevo para la receta: ")
                self.insertarPaso(paso)
                self.verReceta()

            elif opcion == "2":
                self.mostrarSiguiente()

            elif opcion == "3":
                self.realizarPaso()
                self.mostrarSiguiente()

            elif opcion == "4":
                self.eliminarReceta()

            elif opcion == "5":
                self.verReceta()

            elif opcion == "6":
                print("Regresando a Menu")
                break
            
            else:
                print("Opcion no valida, intenta de nuevo")