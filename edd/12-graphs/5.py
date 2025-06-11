def calcular_area(grid, x, y, visitados):
    pila = [(x, y)]
    visitados.add((x, y))
    tamaño = 1
    
    direcciones = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while pila:
        cx, cy = pila.pop()
        for dx, dy in direcciones:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and (nx, ny) not in visitados and grid[nx][ny] == 'X':
                visitados.add((nx, ny))
                pila.append((nx, ny))
                tamaño += 1
    
    return tamaño

def main():
    casos = int(input())
    resultados = []

    for _ in range(casos):
        filas, columnas = map(int, input().split())
        mapa = [input() for _ in range(filas)]

        visitados = set()
        area_maxima = 0
        
        for i in range(filas):
            for j in range(columnas):
                if mapa[i][j] == 'X' and (i, j) not in visitados:
                    area_maxima = max(area_maxima, calcular_area(mapa, i, j, visitados))

        resultados.append(str(area_maxima))

    print("\n".join(resultados))

if __name__ == "__main__":
    main()