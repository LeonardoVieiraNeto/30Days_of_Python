## Day 9 - OOP Pillars

## Encapsulamento

class Avenger:
  def __init__(self, name, knownAs):
    self.name = name
    self.knownAs = knownAs

  def reveal_identity(self):
    print(f'Eu sou o {self.name}, tambem conhecido como {self.knownAs}')

hulk = Avenger('Bruce Banner', 'Hulk')
iron_man = Avenger('Tony Stark', 'IronMan')

hulk.reveal_identity() # Eu sou o Bruce Banner, tambem conhecido como Hulk
iron_man.reveal_identity() # Eu sou o Tony Stark, tambem conhecido como IronMan

## Abstração

class Avenger:
  def __init__(self, name, knownAs):
    self.name = name
    self.knownAs = knownAs

  def reveal_identity(self):
    print(f'Eu sou o {self.name}, tambem conhecido como {self.knownAs}')

hulk = Avenger('Bruce Banner', 'Hulk')

hulk.name = 'Thanos'
hulk.knownAs = 'Loki'

hulk.reveal_identity() # Eu sou o Thanos, tambem conhecido como Loki


## Herança

class Player:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def run(self):
    return f'{self.name} correndo'

class Cricketer(Player): # Syntax to inherit a class
  def catch_ball(self):
    return f'{self.name} lançou a bola'

class Batsman(Cricketer):
  def swing_bat(self):
    return f'Que tiro por {self.name}'

player1 = Batsman('Virat Kohli', 31)

print(player1.run())
print(player1.catch_ball())
print(player1.swing_bat())


class Player:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def run(self):
    return f'{self.name} está correndo'

class Cricketer(Player):
  def catch_ball(self):
    return f'{self.name} lançou a bola'

class Batsman(Cricketer):
  def swing_bat(self):
    return f'que tiro por {self.name}'

player1 = Batsman('Virat Kohli', 31)

print(isinstance(player1, Batsman)) # True
print(isinstance(player1, Cricketer)) # True
print(isinstance(player1, Player)) # True
print(isinstance(player1, object)) # True

## Polimorfismo

class ProgrammingLanguage:
  def __init__(self, name):
    self.name = name

class JavaScript(ProgrammingLanguage):
  def comment(self):
    return(f'// Um comentário em {self.name}')

class Python(ProgrammingLanguage):
  def comment(self):
    return(f'# Um comentário em {self.name}')

language1 = JavaScript('JavaScript')
language2 = Python('Python')

def add_comment(languageObject):
  print(languageObject.comment())

add_comment(language1) # // Um comentário em JavaScript
add_comment(language2) # # Um comentário em Python

for language in [language1, language2]:
  print(language.comment())
