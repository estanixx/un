from collections import deque

def main():
    P = int(input())
    relaciones = []

    for _ in range(P):
        amigos = list(map(int, input().split()))
        relaciones.append(amigos if amigos != [-1] else [])

    fuentes = list(map(int, input().split(', ')))
    resultados = []

    for fuente in fuentes:
        dias = [-1] * P
        dias[fuente] = 0
        cola = deque([fuente])
        conteo_niveles = {}

        while cola:
            persona = cola.popleft()
            dia_actual = dias[persona]

            for amigo in relaciones[persona]:
                if dias[amigo] == -1:
                    dias[amigo] = dia_actual + 1
                    cola.append(amigo)
                    conteo_niveles[dias[amigo]] = conteo_niveles.get(dias[amigo], 0) + 1

        if not conteo_niveles:
            resultados.append("0")
        else:
            max_conteo = max(conteo_niveles.values())
            dia_minimo = min(dia for dia, conteo in conteo_niveles.items() if conteo == max_conteo)
            resultados.append(f"{dia_minimo} {max_conteo}")

    print("\n".join(resultados))

if __name__ == "__main__":
    main()