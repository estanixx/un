import numpy as np
from datetime import datetime
letras: list[str] = list('A B C D E'.split(' '))
digitos: list[str] = list('4 5 6 7 8'.split(' '))

def combinate(*sets: list[str]) -> list[str]:
  """Combinate: Función recursiva que recibe una lista de caracteres
  y los combina en diferentes strings.

  Returns:
      list[str]: Combinaciones posibles entre los dos conjuntos.
  """
  actualCombinations = []
  head: list[str] = sets[0]
  if len(sets) == 1:
    return head
  tail: list[list[str]] = list(sets[1:])
  possibleCombinations: list[str] = combinate(*tail)
  for element in head:
    for combination in possibleCombinations:
      actualCombinations.append(f'{element}{combination}')
  return actualCombinations

def format(tex: str) -> str:
  """Función que, dado un string, crea un pasaporte

  Args:
      tex (str): Código generado.

  Returns:
      str: Pasaporte.
  """
  hora = datetime.now().strftime('%H:%M')
  return f'PAS-{tex}-{hora}'

args = [letras for _ in range(2)] + [digitos for _ in range(6)]
res = np.array(combinate(*args))
passports = np.vectorize(format)(res)

print('POSIBLES CÓDIGOS:')
print(passports)

print('TAMAÑO DE LA LISTA:')
print(len(passports))
print(5**8)