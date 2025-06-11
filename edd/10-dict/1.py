
trans = {(prompt:=input().split())[0]: prompt[1]  for _ in range(int(input()))}
while (cmd:=input()) != '#':
    try:
        print(trans[cmd])
    except:
        print('Entrada no encontrada')