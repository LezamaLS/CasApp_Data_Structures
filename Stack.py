from collections import deque

class HistorialLimpieza:
    def __init__(self):
        self.histLimpieza = deque()

    def insertarLugar(self, lugar):
        if lugar not in self.histLimpieza:
            self.histLimpieza.append(lugar)
            print(f'\n{lugar}" ha sido limpiado')
        else:
            print(f'\n{lugar}" ya se habia limpiado')

    def buscarLugar(self, lugar):
        if lugar in self.histLimpieza:
            print(f'\n{lugar}" ya se ha limpiado')
        else:
            print(f'\n{lugar}" no se ha limpiado')

    def popTop(self):
        if self.histLimpieza:
            lugarEliminado = self.histLimpieza.pop()
            print(f'\n{lugarEliminado}" se ha borrado')
        else:
            print('\nHistorial vacio, no se puede eliminar nada crack')

    def verUltimo(self):
        if self.histLimpieza:
            ultimo = self.histLimpieza[-1]
            print(f'\n"{ultimo}" fue el ultimo lugar limpiado')
        else:
            print('\nNo has limpiado nada, puerco')

    def menuStack(self):
        while True:
            print("\n------- Historial de Limpieza -------")
            print("1. Registrar Limpio")
            print("2. Buscar lugar limpiado")
            print("3. Cancelar ultimo registrado (control zetazo)")
            print("4. Regresar")

            opcion = input("\nSelecciona una opcion: ")

            if opcion == "1":
                lugarNuevo = input("\nNombre del lugar limpiado: ")
                self.insertarLugar(lugarNuevo)

            elif opcion == "2":
                lugarExistente = input("\nNombre del lugar que quieres ver si ya limpiaste: ")
                self.buscarLugar(lugarExistente)

            elif opcion == "3":
                self.popTop()

            elif opcion == "4":
                print("Regresando a Menu")
                break
            
            else:
                print("Opcion no valida, intenta de nuevo")


