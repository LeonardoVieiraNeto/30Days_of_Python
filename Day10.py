## Day 10 - OOP Missing Pieces


## super()

## Without using super


class Employee:
  def __init__(self, name):
    self.name = name
    print(f'{self.name} is an employee')

class Manager(Employee):
  def __init__(self, department, name):
    self.department = department
    self.name = name
    Employee.__init__(self, name)
    print(f'Manager, {self.department} department')

staff_1 = Manager('HR', 'Andy')
# Andy is an employee
# Manager, HR department

## Using super (Compact syntax - No need to pass self)

class Employee:
  def __init__(self, name):
    self.name = name
    print(f'{self.name} is an employee')

class Manager(Employee):
  def __init__(self, department, name):
    self.department = department
    self.name = name
    super().__init__(name)
    print(f'Manager, {self.department} department')

staff_1 = Manager('HR', 'Andy')
# Andy is an employee
# Manager, HR department

## Introspection

class Developer:
  def __init__(self, name, language):
    self.name = name
    self.language = language

  def introduce(self):
    print(f'Hi! I am {self.name}. I code in {self.language}')

dev = Developer('Matt', 'Python')

print(dir(dev)) # Try this in any Python REPL

## Dunder Methods

class Sentence:
  words = []

  def add_word(self, word):
    self.words.append(word)

  def __len__(self):
    return len(self.words)

new_sentence = Sentence()
new_sentence.add_word('Hello')
new_sentence.add_word('World')
print(len(new_sentence))

## Multiple Inheritance

class Batsman:
  def swing_bat(self):
    return 'What a shot!'

class Bowler:
  def bowl_bouncer(self):
    return 'What a bouncer!'

class AllRounder(Batsman, Bowler):
  pass

player = AllRounder()

print(player.bowl_bouncer()) # What a shot!
print(player.swing_bat()) # What a bouncer!

class Batsman:
  def __init__(self, hitting_power):
    self.hitting_power = hitting_power

  def swing_bat(self):
    return f'Shot with power {self.hitting_power}'

class Bowler:
  def __init__(self, delivery_speed):
    self.delivery_speed = delivery_speed

  def bowl_bouncer(self):
    return f'Bowled with speed of {self.delivery_speed} kmph'

class AllRounder(Batsman, Bowler):
  def __init__(self, hitting_power, delivery_speed):
    Batsman.__init__(self, hitting_power)
    Bowler.__init__(self, delivery_speed)

player = AllRounder(90, 80)
print(player.swing_bat())
print(player.bowl_bouncer())

## Method Resolution Order

class Employee:
  secret_code = 'secret'

class Manager(Employee):
  secret_code = 'm123'

class Accountant(Employee):
  secret_code = 'a123'

class Owner(Manager, Accountant):
  pass

person = Owner()
print(person.secret_code) # m123

print(Owner.mro()) # try in a python console with above code to see the result

