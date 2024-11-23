from threading import Thread, get_ident
from time import sleep, perf_counter
def fn(num):
  sleep(2)
  print(f'Soy {get_ident()}');
thread = Thread(target=fn, args=(0,))
thread1 = Thread(target=fn, args=(0,))
thread.start()
thread1.start()
for _ in range(10):
  print('Hilo sigue en ejecución')

print('Termina')