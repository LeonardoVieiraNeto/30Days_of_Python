## 30 Days of Python
## Day 13 - Decorators

## Functions as first-class citizens

def multiplier(num1, num2):
  return num1 * num2

some_variable = multiplier # (a reference to the function is created)

del multiplier # (deletes the function)

print(some_variable(2,4)) # 8 (still able to call the function!)

## Higher-Order Functions

def logger(func): # higher order function
  print(f'O resultado passado pela função é {func}')

def sum(num1, num2):
  return num1 + num2

logger(sum(1,5))

def random(): # Higher order function
  def special():
    print('Eu sou algo especial')
  return special

random_value = random()
random_value() # I am something special
# One line way
random()() # I am something special

## Custom Decorators

def starmaker(func):
  '''
  Uma função decoradora que aceita uma função
  e depois envolve alguma bondade nele e
  devolve!
  '''
  def wrapper():
    func()
    print('Você é uma estrela agora!')
    print('*********')
  return wrapper

@starmaker
def layman():
  print('Eu sou apenas um leigo')

layman()

def starmaker(func):
  '''
  Uma função decoradora que aceita uma função
  e depois envolve alguma bondade nele e
  devolve!
  '''
  def wrapper():
    func()
    print('Você é uma estrela agora!')
    print('*********')
  return wrapper

def layman():
  print('Eu sou apenas um leigo')

starmaker(layman)() # This is the underlying decorator magic!

## Why decorators are useful?

# Create an @authenticated decorator that only allows 
# the function to run is user1 has 'valid' set to True:
test_user = {
    'name': 'Jackson',
    'valid': True
}

another_user = {
  'name': 'Nathan',
  'valid': False
}

def authenticated(fn):
  def wrapper(*args, **kwargs):
    if args[0]['valid']:
      fn(args)
  return wrapper

@authenticated
def message_friends(user):
    print('Mensagem enviada')

message_friends(test_user) # message has been sent
message_friends(another_user) # (Does nothing)
