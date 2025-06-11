import heapq
pstgs = [] 
while (cmd:=input()) != 'fin':
    match cmd:
        case cmd if cmd.startswith('ingresa'):
            pst = int(cmd.split()[1])
            highest_pst = abs(pstgs[0]) if len(pstgs) > 0 else 0
            if pst >= highest_pst / 2:
                heapq.heappush(pstgs, -pst)
                print('adelante')
            else:
                print('denegado')
        case _:
            if len(pstgs) > 0:
                heapq.heappop(pstgs)
                print('hasta pronto')