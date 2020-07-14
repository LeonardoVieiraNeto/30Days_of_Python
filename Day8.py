## 30 Days of Python
## Day 8 - OOP Basics

print(type(2)) # <class 'int'>
print(type(2.5)) # <class 'float'>
print(type('Python')) # <class 'str'>
print(type(True)) # <class 'bool'>
print(type({})) # <class 'dict'>
print(type([])) # <class 'list'>
print(type(())) # <class 'tuple'>
print(type(None)) # <class 'NoneType'>


class Avenger:
  def __init__(self, name):
    self.name = name

  def fight(self):
    print('Soquinho')

spiderman = Avenger('Spiderman')

print(type(Avenger)) # <class 'type'>
print(type(spiderman)) # <class '__main__.Avenger'> --> instance of Avenger

