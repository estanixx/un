import unittest
from poke import Pokemon, Item
class TestPokemon(unittest.TestCase):
  def setUp(self):
    self.pokemones = [
      Pokemon(
        name='Gloom',
        level=4,
        type=['planta', 'veneno'],
      ),
      Pokemon(
        name='Blaziken',
        level=54,
        type=['fuego', 'lucha'],
      ),
      Pokemon(
        name='Rapidash Galar',
        level=120,
        type=['psíquico', 'hada'],
      )
    ]
    def volcano_binding(poke: Pokemon):
      poke.type = ['roca', 'fuego']
      
    def ditto_berries(poke: Pokemon):
      poke.name = 'Ditto'
      poke.type = ['normal']
      
    def rare_candy(poke: Pokemon):
      poke.level += 1
    
    self.items = [
      Item(
        name='Piedra volcán',
        effect=volcano_binding
      ),
      Item(
        name='Bayas Ditto',
        effect=ditto_berries
      ),
      Item(
        name='Caramelorraro',
        effect=rare_candy
      ),
    ]

  def test_crear_poke(self):
    # Comportamiento de creación de pokemon.
    datatext = [str(p) for p in self.pokemones]
    self.assertEqual(datatext, ['Gloom lv.4 PV', 'Blaziken lv.54 FL', 'Rapidash Galar lv.120 HP']) # Valido que la clase interiorice los datos en el str.
  
  def test_level_stats(self):
    # Estadísticas según el nivel del pokemon.
    levelups = [ p.next_levelup for p in self.pokemones ]
    maxhps = [p.max_hp for p in self.pokemones]
    maxeps = [p.max_ep for p in self.pokemones]
    self.assertEqual(levelups, [200, 2700, 6000]) # El pokemon sube de nivel cuando su experiencia es igual a nivel actual * 50.
    self.assertEqual(maxhps, [750, 8250, 18150])
    self.assertEqual(maxeps, [9, 159, 357])
    
  def test_item(self):
    # Comportamiento de afección de pokemones ante items.
    for pkm, item in zip(self.pokemones, self.items):
      pkm.take(item)
    datatext = [str(p) for p in self.pokemones]
    self.assertEqual(datatext, ['Gloom lv.4 FR', 'Ditto lv.54 N', 'Rapidash Galar lv.121 HP'])

    
    
if __name__ == '__main__':
  unittest.main()