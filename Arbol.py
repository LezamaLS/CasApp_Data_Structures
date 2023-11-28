class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor, nodo=None):
        #verificador de si el nodo actual es null o no, si si es, comenzamos en la raiz
        if not nodo:
            nodo = self.raiz

        #Comparamos el valor a insertar con los ya existentes para decidir si lo signamos como 
        # hijo izquierdo o derecho y de que nodo
        if not nodo:
            self.raiz = Nodo(valor)
        elif valor < nodo.valor:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(valor)
            else:
                self.insertar(valor, nodo.izquierda)
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(valor)
            else:
                self.insertar(valor, nodo.derecha)

    def buscar(self, valor, nodo=None):
        if not nodo:
            nodo = self.raiz

        #Hacemos un checkeo del valor dado, metemos recursividad dependiendo si es mayor o manor para
        # ✨eficientizzar ✨
        if not nodo:
            return None
        elif valor == nodo.valor:
            return nodo
        elif valor < nodo.valor:
            return self.buscar(valor, nodo.izquierda)
        else:
            return self.buscar(valor, nodo.derecha)

    def eliminar(self, valor):
        self.raiz = self.eliminamos(valor, self.raiz)

    def eliminamos(self, valor, nodo):
        if not nodo:
            return None

        #Decidimos que nodo toma el lugar del padre dependiendo de cual sea mayor y reacomodamos al otro hijo
        # utilizamos una funcion para encontrar al minimo revisando la izquierda para esto
        if valor < nodo.valor:
            nodo.izquierda = self.eliminamos(valor, nodo.izquierda)
        elif valor > nodo.valor:
            nodo.derecha = self.eliminamos(valor, nodo.derecha)
        else:
            if nodo.izquierda is None:
                return nodo.derecha
            elif nodo.derecha is None:
                return nodo.izquierda

            nodo.valor = self.encontrarMinimo(nodo.derecha)
            nodo.derecha = self.eliminamos(nodo.valor, nodo.derecha)

        return nodo

    def encontrarMinimo(self, nodo):
        while nodo.izquierda:
            nodo = nodo.izquierda
        return nodo.valor

    def mostrar(self, nodo=None, nivel=0, prefijo='Raiz: '):
        if not nodo:
            nodo = self.raiz

        #Nomas hacemos que sea vea bonito en impresion indentando basado en el nivel del nodo
        # en un recorridito y poniendole si es izquierda o derecha para enseñarle al profe ya que 
        # lo imprimimos en vertical je
        if nodo:
            print(' ' * (nivel * 4) + prefijo + str(nodo.valor))
            if nodo.izquierda:
                self.mostrar(nodo.izquierda, nivel + 1, 'Izq: ')
            if nodo.derecha:
                self.mostrar(nodo.derecha, nivel + 1, 'Der: ')

    def inorder(self, nodo=None):
        if not nodo:
            nodo = self.raiz

        #Basicamente guardamos el recorrido en un array normalon y vamos agregando, recorriendo siempre hasta la izquierda, luego nodo actual y luego derecha
        elementos = []
        if nodo.izquierda:
            elementos += self.inorder(nodo.izquierda)
        elementos.append(nodo.valor)
        if nodo.derecha:
            elementos += self.inorder(nodo.derecha)
        return elementos

    def postorden(self, nodo=None):
        if not nodo:
            nodo = self.raiz

        #Lo mismo que antes, pero recorremos primero izquierda, luego derecha y luego el nodo actual
        elementos = []
        if nodo.izquierda:
            elementos += self.postorden(nodo.izquierda)
        if nodo.derecha:
            elementos += self.postorden(nodo.derecha)
        elementos.append(nodo.valor)
        return elementos

    def preorden(self, nodo=None):
        if not nodo:
            nodo = self.raiz

        #Aqui similar a los otros, pero primero va el nodo actual, luego izquierda y luego derecha
        elementos = [nodo.valor]
        if nodo.izquierda:
            elementos += self.preorden(nodo.izquierda)
        if nodo.derecha:
            elementos += self.preorden(nodo.derecha)
        return elementos

    def menuArbol(self):
        #Menu basico
        while True:
            print("\n------- Organizador de Carpetas -------")
            print("1. Insertar")
            print("2. Buscar")
            print("3. Eliminar")
            print("4. Ver Arbol")
            print("5. Recorrido Inorder")
            print("6. Recorrido Postorden")
            print("7. Recorrido Preorden")
            print("8. Regresar a Menu")

            opcion = int(input("\nSelecciona una opcion: "))

            if opcion == 1:
                valor = int(input("\nCarpeta a insertar: "))
                self.insertar(valor)
                self.mostrar()

            elif opcion == 2:
                valor = int(input("\nCarpeta a buscar: "))
                nodoEncontrado = self.buscar(valor)
                if nodoEncontrado:
                    print("\nCarpeta encontrada:", nodoEncontrado.valor)
                else:
                    print("\nCarpeta no encontrada")

            elif opcion == 3:
                valor = int(input("\nCarpeta a eliminar: "))
                self.eliminar(valor)
                print("\nCarpeta eliminada")

            elif opcion == 4:
                self.mostrar()
                
            elif opcion == 5:
                print("\nRecorrido Inorder:", self.inorder())

            elif opcion == 6:
                print("\nRecorrido Postorden:", self.postorden())

            elif opcion == 7:
                print("\nRecorrido Preorden:", self.preorden())

            elif opcion == 8:
                print("Regresando a Menu")
                break
            
            else:
                print("Opcion no valida, intenta de nuevo")

