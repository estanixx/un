from functools import reduce
from typing import Callable
class Pokemon:
  _name: str
  _level: int
  _type: list[str]
  _exp: int
  _hp: int
  _ep: int
  _alive: bool
  def __init__(self, name, level, type):
    self.name = name
    self.level = level
    self.type = [*type]
    self.exp = 0
    
  @property
  def name(self):
    return self._name
  
  @name.setter
  def name(self, newName: str):
    self._name = newName
    
  @property
  def level(self) -> int:
    return self._level
  
  @level.setter
  def level(self, newLevel: int):
    if newLevel < 0:
      raise ValueError('no se puede tener nivel negativo')
    self._level = newLevel
    
  @property
  def type(self) -> list[str]:
    return self._type
  
  @type.setter
  def type(self, newType: list[str]):
    self._type = newType
    self._type.sort()
  
  @property
  def exp(self) -> int:
    return self._exp
  
  @exp.setter
  def exp(self, newExp: int):
    if newExp < 0:
      raise ValueError('no puedes tener experiencia negativa')
    self._exp = newExp
    while self._exp > self.next_levelup:
      self._exp -= self.next_levelup
      self.level += 1
      
  @property
  def hp(self) -> int:
    return self._hp

  @hp.setter
  def hp(self, nuevo_hp: int):
    if nuevo_hp >= 0: 
      self._hp = nuevo_hp
    else:
      self._hp = 0
      self._alive = False

  @property
  def ep(self) -> int:
    return self._ep 

  @ep.setter
  def ep(self, nuevo_ep: int):
    if nuevo_ep >= 0:
      self._ep = nuevo_ep
    else:
      raise ValueError("no tienes puntos de energía")
      
  @property
  def alive(self) -> bool:
    return self._alive 

  @alive.setter
  def alive(self, estado: bool):
    self._alive = estado
    
  @property
  def max_hp(self) -> int:
    return (self.level + 1) * 150
  
  @property
  def max_ep(self) -> int:
    return (self.level - 1) * 3
  
  @property
  def next_levelup(self) -> int:
    return self._level * 50
  
  def __str__(self) -> str:
    typeStr = reduce(lambda acc, t: acc + t[0].upper(), self._type, '')
    return f'{self._name} lv.{self._level} {typeStr}'
  
  def take(self, i: "Item"):
    i.effect(self)
    
    
    
class Item:
  _name: str
  effect: Callable[[Pokemon], None]
  def __init__(self, name: str, effect: Callable[[Pokemon], None]):
    self._name = name
    self.effect = effect
    