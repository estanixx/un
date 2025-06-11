def generar_primos(n):
    """
    Genera todos los números primos menores o iguales a n usando la criba de Eratóstenes.
    """
    if n < 2:
        return []
    es_primo = [True] * (n + 1)
    es_primo[0] = es_primo[1] = False
    for p in range(2, int(n**0.5) + 1):
        if es_primo[p]:
            for i in range(p * p, n + 1, p):
                es_primo[i] = False
    primos = [p for p, es_p in enumerate(es_primo) if es_p]
    return primos

def contar_parejas(N, primos):
    """
    Cuenta las parejas de primos que suman N.
    """
    conteo = 0
    for p in primos:
        if p > N // 2:
            break
        if (N - p) in primos:
            conteo += 1
    return conteo

# Precalcular todos los primos hasta 10,000
primos = set(generar_primos(10000))

# Leer la cantidad de casos de prueba
C = int(input())
for _ in range(C):
    N = int(input())
    print(contar_parejas(N, primos))