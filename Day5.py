## 30 Days of Python
## Day 5 - Conditions & Loops I

## Conditional Logic

age = input('Por favor, informe a sua idade ')
if(int(age) >= 18):
  print('Você pode entrar no nosso clube')
else:
  print('Desculpe ! Você não pode entrar no nosso clube !')


exam_score = input('Informe sua nota')
if(int(exam_score) > 90):
  print('Você passou com A+')
elif(int(exam_score) > 80):
  print('Você passou com A')
else:
  print('Você passou com B')



is_adult = True

is_licensed = True

if(is_adult and is_licensed): ## In JavaScript && is used instead of 'and'
  print('Você pode dirigir ')
else:
  print('Você não pode dirigir')

if(10 > 8):
  print('Uma lógica tão boba. Eu serei impresso')
else:
  print('Eu nunca serei impresso')

# The above line gets printed always as interpreter treats it as a new line

##Truthy and Falsy
username = 'santa' # bool('santa') => True
password = 'superSecretPassword' # bool('superSecretPassword') => True
if username and password:
  print('Detalhes pode ser exibidos')
else:
  print('Detalhes não podem ser exibidos')

##Ternary Operator
is_single = True
message = 'você pode namorar' if is_single else 'você não pode namorar'
# result = (value 1) if (condition is truthy) else (value 2)
print(message) # You can date

## Short Circuiting

knows_javascript = True
knows_python = True

if(knows_javascript or knows_python): # doesn't depend on value of knows_python
  print('Desenvolvedor Javscript ou python ')
else:
  print('Desenvolvedor de alguma outra linguagem')
knows_javascript = False
knows_python = True

if(knows_javascript and knows_python): # doesn't depend on value of knows_python
  print('Desenvolvedor Javscript e python')
else:
  print('Desenvolvedor de alguma outra linguagem')

## Logical Operators

print(10 > 100) # False
print(10 < 100) # True
print(10 == 10) # True
print(10 != 50) # True
print(2 > 1 and 2 > 0) # True
print(not(True)) # False
print(not False) # True

##Some quirky operations

print(True == True) #True
print('' == 1) # False
print([] == 1) # False
print(10 == 10.0) # True
print([] == []) # True

print(True is True) # True
print('' is 1) # False
print([] is 1) # False
print(10 is 10.0) # False
print([] is []) # False

##For Loops

print('------ ------ ------ ------ ------ ------ ------ ------ ------ ------ ')
print('Imprimi todos os caracteres de uma palavra')
for item in 'Python': # String is iterable
  print(item) # prints all characters of the string

print('------ ------ ------ ------ ------ ------ ------ ------ ------ ------ ')
print('Imprimi todos os numeros de uma sequencia')
for item in [1,2,3,4,5]: # List is iterable
    print(item) # prints all numbers one at a time

#Set is iterable
for item in {1,2,3,4,5}: 
    print(item)

# Tuple is iterable
for item in (1,2,3,4,5): 
    print(item)

##Iterable
player = {
  'firstname': 'Virat',
  'lastname': 'Kohli',
  'role': 'captain'
}

for item in player: # iterates over the keys of player
  print(item) # prints all keys

for item in player.keys(): 
  print(item) # prints all keys

for item in player.values():
  print(item) # prints all values

for item in player.items():
  print(item) # prints key and value as tuple

for key, value in player.items():
  print(key, value) # prints key and value using unpacking

## range

print('------ ------ ------ ------ ------ ------ ------ ------ ------ ------ ')
print('Imprimi a palavra Pyton dez vezes')
for item in range(10):
  print('python') # prints python 10 times

print('------ ------ ------ ------ ------ ------ ------ ------ ------ ------ ')
print('Imprimi a palavra Pyton dez vezes')
for item in range(0,10,1):
    print('Olá') # prints hello 10 times

print('------ ------ ------ ------ ------ ------ ------ ------ ------ ------ ')
print('Imprimi a palavra  5 vezes')
for item in range(0, 10, 2):
    print('Olá') # prints hii 5 times 

print('------ ------ ------ ------ ------ ------ ------ ------ ------ ------ ')
print('Imprimi uma sequencia reversa')
for item in range(10, 0, -1):
    print(item) # prints in reverse order

print('------ ------ ------ ------ ------ ------ ------ ------ ------ ------ ')
print('Gera e imprime um list com 10 numeros em sequencia')
print(list(range(10))) # generates a list of 10 items

## enumerate

print('------ ------ ------ ------ ------ ------ ------ ------ ------ ------ ')
for key, value in enumerate(range(10)): # using unpacking techique 
  print(f'key is {key} and value is {value}') # prints key and value at the same time

  

  


