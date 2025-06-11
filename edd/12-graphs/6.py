from collections import deque

def convertir_coordenadas(posicion):
    """Convierte una posición en formato de ajedrez (por ejemplo, 'A1') a coordenadas (fila, columna)."""
    return ord(posicion[0]) - ord('A'), int(posicion[1]) - 1

def main():
    casos = int(input())

    for _ in range(casos):
        origen, destino = input().split()

        if origen == destino:
            print(0)
            continue  # Saltar al siguiente caso si el origen y destino son iguales

        # Movimientos posibles de un caballo en el tablero
        movimientos = [(-2, -1), (-2, 1), (-1, -2), (-1, 2),
                       (1, -2), (1, 2), (2, -1), (2, 1)]

        # Convertir las posiciones a coordenadas del tablero
        inicio_x, inicio_y = convertir_coordenadas(origen)
        destino_x, destino_y = convertir_coordenadas(destino)

        # Inicializar la cola para BFS
        cola = deque([(inicio_x, inicio_y, 0)])  # (fila, columna, pasos)
        visitados = set()
        visitados.add((inicio_x, inicio_y))

        # BFS para encontrar el número mínimo de movimientos
        while cola:
            x, y, pasos = cola.popleft()

            # Explorar todos los movimientos posibles
            for dx, dy in movimientos:
                nx, ny = x + dx, y + dy

                # Verificar si la nueva posición está dentro del tablero y no ha sido visitada
                if 0 <= nx < 8 and 0 <= ny < 8 and (nx, ny) not in visitados:
                    if (nx, ny) == (destino_x, destino_y):
                        print(pasos + 1)
                        break  # Salir del BFS si se encuentra el destino
                    visitados.add((nx, ny))
                    cola.append((nx, ny, pasos + 1))
            else:
                continue  # Continuar si no se encontró el destino
            break  # Salir del BFS si se encontró el destino

if __name__ == "__main__":
    main()