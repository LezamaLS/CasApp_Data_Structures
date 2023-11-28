import networkx as nx
import matplotlib.pyplot as plt

class RutaRecogida:
    def __init__(self):
        self.G = nx.Graph()
        self.G.add_edge('Escuela 1', 'Escuela 2', weight=120)
        self.G.add_edge('Escuela 1', 'Escuela 3', weight=210)
        self.G.add_edge('Escuela 2', 'Escuela 3', weight=120)
        self.G.add_edge('Escuela 2', 'Escuela 4', weight=53)
        self.G.add_edge('Escuela 3', 'Escuela 4', weight=98)
        self.G.add_edge('Escuela 4', 'Escuela 5', weight=175)

        # Utilizamos networkX para calcular el minimum spanning con Kruskal
        self.mst = nx.minimum_spanning_tree(self.G)

    def mostrarGrafoOG(self):
        pos = nx.spring_layout(self.G)
        nx.draw(self.G, pos, with_labels=True, node_size=700, node_color='lightblue')
        labels = nx.get_edge_attributes(self.G, 'weight')
        nx.draw_networkx_edge_labels(self.G, pos, edge_labels=labels)
        plt.title('Grafo Original')
        plt.show()

    def mostrarKruskal(self):
        pos = nx.spring_layout(self.G)
        nx.draw(self.mst, pos, with_labels=True, node_size=700, node_color='lightgreen')
        labels = nx.get_edge_attributes(self.mst, 'weight')
        nx.draw_networkx_edge_labels(self.mst, pos, edge_labels=labels)
        plt.title('Minimum Span Tree (Kruskal)')
        plt.show()

    def menuGrafo(self):
        while True:
            print("\n------- Ruta Recoger -------")
            print("1. Ver Grafo Original")
            print("2. Ver Kruskal")
            print("3. Salir")

            opcion = input("Selecciona una opcion: ")

            if opcion == "1":
                self.mostrarGrafoOG()

            elif opcion == "2":
                self.mostrarKruskal()

            elif opcion == "3":
                break

            else:
                print("Opcion no valida, intenta de nuevo")