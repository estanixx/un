
n, t = map(int, input().split())
arr = set(int(input()) for _ in range(n))
setso = set()
arrso = list()
for num in arr:
    needed = t - num
    for num2 in arr:
        num3 = needed - num2
        tup = tuple(sorted((num, num2, num3)))
        if num3 in arr and len(set(tup)) == 3 and tup not in setso:
            setso.add(tup)
            arrso.append(tup)
if len(arrso) == 0:
    print('No hay trillizas')
for tup in sorted(arrso):
    print(*tup, sep=' ')