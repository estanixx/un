from collections import deque

def calcular_componentes(grafo, nodo, visitados):
    cola = deque([nodo])
    visitados.add(nodo)
    tamaño = 1
    while cola:
        actual = cola.popleft()
        for vecino in grafo[actual]:
            if vecino not in visitados:
                visitados.add(vecino)
                cola.append(vecino)
                tamaño += 1
    return tamaño

def main():
    num_casos = int(input())
    resultados = []

    for _ in range(num_casos):
        num_relaciones = int(input())
        pares = [tuple(map(int, input().split())) for _ in range(num_relaciones)]
        
        grafo = {}
        nodos_totales = set()
        
        for a, b in pares:
            if a not in grafo:
                grafo[a] = set()
            if b not in grafo:
                grafo[b] = set()
            grafo[a].add(b)
            grafo[b].add(a)
            nodos_totales.add(a)
            nodos_totales.add(b)
        
        visitados = set()
        num_familias = 0
        tamaño_maximo = 0
        
        for nodo in nodos_totales:
            if nodo not in visitados:
                num_familias += 1
                tamaño_maximo = max(tamaño_maximo, calcular_componentes(grafo, nodo, visitados))

        resultados.append(f"{num_familias} {tamaño_maximo}")

    print("\n".join(resultados))

if __name__ == "__main__":
    main()