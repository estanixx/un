from collections import deque

class Nodo:
    def __init__(self, nombre, visitado=False, saltos=-1):
        self.nombre = str(nombre)
        self.visitado = visitado
        self.saltos = saltos
        self.color = None
    
    def __str__(self):
        return f"Nodo: {self.nombre}"

class Grafo:
    def __init__(self):
        self.enlaces = {}  # nombre_nodo: (set(nombres_nodos), set(nodos))
        self.nodos = (set(), set())  # (set(nombres_nodos), set(nodos))
    
    def agregar_nodo(self, nodo):
        if not isinstance(nodo, Nodo):
            nodo = Nodo(nodo)
        if nodo.nombre not in self.enlaces:
            self.enlaces[nodo.nombre] = (set(), set())
            self.nodos[0].add(nodo.nombre)
            self.nodos[1].add(nodo)
    
    def obtener_nodo(self, nombre):
        if str(nombre) not in self.nodos[0]:
            return None
        for nodo in self.nodos[1]:
            if nodo.nombre == str(nombre):
                return nodo
    
    def agregar_enlace(self, origen, destino):
        if not isinstance(origen, Nodo):
            origen = Nodo(origen)
        if not isinstance(destino, Nodo):
            destino = Nodo(destino)

        if origen.nombre not in self.enlaces:
            self.agregar_nodo(origen)

        if destino.nombre not in self.enlaces[origen.nombre][0]:
            self.enlaces[origen.nombre][0].add(destino.nombre)
            self.enlaces[origen.nombre][1].add(destino)
            if destino.nombre not in self.nodos[0]:
                self.agregar_nodo(destino)
            self.enlaces[destino.nombre][0].add(origen.nombre)
            self.enlaces[destino.nombre][1].add(origen)
    
    def BFS(self, nodo):
        nodo.visitado = True
        cola = deque()
        cola.append(nodo)
        while cola:
            actual = cola.popleft()
            for vecino in self.enlaces[actual.nombre][1]:
                vecino = self.obtener_nodo(vecino.nombre)
                if not vecino.visitado:
                    vecino.visitado = True
                    cola.append(vecino)
    
    def DFS(self, nodo):
        nodo.visitado = True
        pila = deque()
        pila.append(nodo)
        while pila:
            actual = pila.pop()
            if not actual.visitado:
                actual.visitado = True
                for vecino in self.enlaces[actual.nombre][1]:
                    vecino = self.obtener_nodo(vecino.nombre)
                    if not vecino.visitado:
                        pila.append(vecino)
    
    def contar_saltos(self, nodo):
        nodo.visitado = True
        nodo.saltos = 0
        cola = deque()
        cola.append(nodo)
        while cola:
            actual = cola.popleft()
            for vecino in self.enlaces[actual.nombre][1]:
                vecino = self.obtener_nodo(vecino.nombre)
                if not vecino.visitado:
                    vecino.visitado = True
                    vecino.saltos = actual.saltos + 1
                    cola.append(vecino)
    
    def reiniciar_nodos(self):
        for nodo in self.nodos[1]:
            nodo.visitado = False
            nodo.saltos = -1

    def es_bipartito(self):
        for nombre_nodo in self.enlaces:
            nodo = self.obtener_nodo(nombre_nodo)
            if nodo.color is None:
                nodo.color = 0
            cola = deque()
            cola.append(nodo)

            while cola:
                nodo_actual = cola.popleft()
                for vecino in self.enlaces[nodo_actual.nombre][1]:
                    if vecino.color is None:
                        vecino.color = 1 - nodo_actual.color
                        cola.append(vecino)
                    elif nodo_actual.color == vecino.color:
                        return False
        return True

    def __str__(self):
        cadena = "Grafo:"
        for nombre_nodo in self.enlaces:
            cadena += f"\n{nombre_nodo}: "
            for nombre_vecino in self.enlaces[nombre_nodo][0]:
                cadena += f"{nombre_vecino} "
        return cadena

def main():
    casos = int(input())
    for _ in range(casos):
        N, M = map(int, input().split())
        grafo = Grafo()
        for _ in range(M):
            u, v = map(int, input().split(", "))
            grafo.agregar_enlace(u, v)
        if grafo.es_bipartito():
            print("bipartito")
        else:
            print("no bipartito")

if __name__ == "__main__":
    main()