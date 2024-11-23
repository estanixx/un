from threading import Thread, get_ident
from time import sleep, perf_counter
global_sum = 0

def reset_sum():
  global global_sum
  global_sum = 0

def sumatoria(inf, sup):
  global global_sum
  print(f'Yo hago desde {inf} hasta {sup}')
  for i in range(inf, sup + 1):
    global_sum += i
  sleep(1)
  
def sumatoria_hilos(inf, sup, num_thr):
  amount = (sup - inf) // num_thr
  threads = [Thread(target=sumatoria, args=(inf + th * amount, inf + (th + 1) * amount)) for th in range(num_thr)]
  for thread in threads:
    thread.start()  
    
  for thread in threads:
    thread.join()

print('SUMATORIA SENCILLA:')
t1 = perf_counter()
sumatoria(1, 10000)
t2 = perf_counter()
print('La sumatoria es:', global_sum, 'en un tiempo:', round(t2 - t1, 2))

reset_sum()

print('SUMATORIA MULTIHILO:')
t1 = perf_counter()
sumatoria_hilos(1, 10000, 10)
t2 = perf_counter()
print('La sumatoria es:', global_sum, 'en un tiempo:', round(t2 - t1, 2))
