npersonas = int(input())
personas = dict()
for _ in range(npersonas):
    nombre, cantidad = input().split(':')
    personas[nombre] = int(cantidad)
ntransact = int(input())
multiplicadores = {
    'RETIRO': -1,
    'DEPOSITO': 1
}
signos = {
    'RETIRO': '-',
    'DEPOSITO': '+'
}
for _ in range(ntransact):
    nombre, comando, cantidad = input().split()
    texto_bono = ''
    cantidad = int(cantidad)
    if personas[nombre] < cantidad and comando == 'RETIRO':
        print(f'{nombre} no tiene suficiente saldo disponible.')
        continue
    if cantidad > 60_000 and comando == 'DEPOSITO':
        cantidad += int(cantidad * 1.1)
        texto_bono = '+ 10%'
    personas[nombre] += cantidad * multiplicadores[comando]
    print(f'{nombre} {signos[comando]} {cantidad} {texto_bono}. Nuevo saldo {personas[nombre]}')