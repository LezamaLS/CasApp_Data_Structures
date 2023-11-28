class Contacto:
    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono

class ListaContactos:
    def __init__(self, size):
        self.size = size
        self.tablaHash = [None] * size

    def hashFunc(self, nombre):
        return hash(nombre) % self.size

    def agregarContacto(self, contacto):
        indice = self.hashFunc(contacto.nombre)
        
        while self.tablaHash[indice] is not None:
            # Manejo de colisiones: buscar la siguiente posición libre
            indice = (indice + 1) % self.size
        
        self.tablaHash[indice] = contacto
        print(f"\n'{contacto.nombre}' ha sido agregado")

    def agregarAleatorio(self):
        import random
        nombres = ["Calcaneo", "Rivera", "Anaya", "Pepe", "Alejandro", "Mariana", "Alan"]
        telefono = random.randint(1000000000, 9999999999)
        nombre = random.choice(nombres)
        contacto = Contacto(nombre, telefono)
        self.agregarContacto(contacto)

#    def buscarContacto(self, nombre):
 #       indice = self.hashFunc(nombre)
  #      
   #     while self.tablaHash[indice] is not None:
    #        if self.tablaHash[indice].nombre == nombre:
     #           return self.tablaHash[indice]
      #      
       #     indice = (indice + 1) % self.size
        #
        #return None

    def eliminarContacto(self, posicion):
        if 0 <= posicion < self.size:
            if self.tablaHash[posicion] is not None:
                nombre = self.tablaHash[posicion].nombre
                self.tablaHash[posicion] = None
                print(f"\n#{posicion} ('{nombre}') ha sido eliminado")
            else:
                print(f"\nNo hay ningun contacto en #{posicion}")
        else:
            print("\nEsta posicion no existe bro")


    def verContactos(self):
        for i, contacto in enumerate(self.tablaHash):
            if contacto is not None:
                print(f"{i}: Nombre: {contacto.nombre}, Cel: {contacto.telefono}")

    def borrarContactos(self):
        self.tablaHash = [None] * self.size
        print("\nLista de contactos eliminada")

    def menuHash(self):
        while True:
            print("\n------- Lista de Contactos -------")
            print("1. Nuevo contacto")
            print("2. Agregar contacto aleatorio")
            print("3. Eliminar contacto")
            print("4. Ver lista de contactos")
            print("5. Borrar toda la lista")
            print("6. Regresar")

            opcion = input("\nSelecciona una opcion: ")

            if opcion == "1":
                nombre = input("\nNombre del contacto: ")
                telefono = input("Celular del contacto: ")
                nuevoContacto = Contacto(nombre, telefono)
                self.agregarContacto(nuevoContacto)

            elif opcion == "2":
                self.agregarAleatorio()

            elif opcion == "3":
                posicion = int(input("\nPosicion del contacto a eliminar: "))
                self.eliminarContacto(posicion)

            elif opcion == "4":
                self.verContactos()

            elif opcion == "5":
                self.borrarContactos()

            elif opcion == "6":
                print("Regresando a Menu")
                break

            else:
                print("Opcion no valida, intenta de nuevo")

