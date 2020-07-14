## 30 Days of Python
## Day 14 - Error Handling


print('Teste de conversão de inteiro para string')
age = int(input('Enter your age'))
if age > 18:
  print('You are an adult')
else:
  print('You are a minor')

## Try except block

try:
  age = int(input('Enter your age'))
  if age > 18:
    print('You are an adult')
  else:
    print('You are a minor')
except:
  print('Invalid value provided')


## Else block

try:
  age = int(input('Enter your age'))
  if age > 18:
    print('You are an adult')
  else:
    print('You are a minor')
except:
  print('Invalid value provided')
else:
  print('Thank You!')

## Finally block


try:
  age = int(input('Enter your age'))
  if age > 18:
    print('You are an adult')
  else:
    print('You are a minor')
except:
  print('Invalid value provided')
finally:
  print('Sendiing dummy log to server') # always gets printed

## Built-in Exceptions


from functools import reduce

def calc_average(number_list):
  '''
  Aceita uma lista de numeros e retorna a média entre eles
  '''
  sum = reduce(lambda acc, curr: acc + curr, number_list)
  average = sum/len(number_list)
  return average

print(calc_average([1,2,3,4,5])) # 3.0

# Passing invalid arguments would result in errors
## print(calc_average(['1','2','3','4','5'])) # TypeError
## print(calc_average(None)) # TypeError
## print(calc_average(3/0)) # ZeroDivisionError

## To make the function more defensive, we can catch (handle) those specific exceptions.
print('To make the function more defensive, we can catch (handle) those specific exceptions.')

from functools import reduce

def calc_average(number_list):
  '''
  accepts a list of numbers and returns average
  '''
  try:
    sum = reduce(lambda acc, curr: acc + curr, number_list)
    average = sum/len(number_list)
    return average
  except TypeError:
    print('Only a list of numbers is valid')


print(calc_average('hello world')) # Only a list of numbers is valid


from functools import reduce

def calc_average(number_list):
  '''
  accepts a list of numbers and returns average
  '''
  try:
    sum = reduce(lambda acc, curr: acc + curr, number_list)
    average = sum/len(number_list)
    1.0/0 # Bug
    return average
  except TypeError:
    print('Only a list of numbers is valid')
  except ZeroDivisionError:
    print('cannot divide by zero')


print(calc_average([1,2,3,4,5])) # cannot divide by zero'


print('Multiple exceptions can be handled together in a single except block as well')

from functools import reduce

def calc_average(number_list):
  '''
  accepts a list of numbers and returns average
  '''
  try:
    sum = reduce(lambda acc, curr: acc + curr, number_list)
    average = sum/len(number_list)
    return average
  except (TypeError, ZeroDivisionError): # handles both cases
    print('Only a list of numbers is valid')

print(calc_average(['asdfasdf'])) # Only a list of numbers is valid

from functools import reduce

def calc_average(number_list):
  '''
  accepts a list of numbers and returns average
  '''
  try:
    sum = reduce(lambda acc, curr: acc + curr, number_list)
    average = sum/len(number_list)
    return average
  except TypeError as type_error:
    print(f'Only a list of numbers is valid {type_error}')
  except ZeroDivisionError as zero_div_error:
    print(f'cannot divide by zero {zero_div_error}')  

print(calc_average('hello world')) 
# Only a list of numbers is valid unsupported operand type(s) for /: 'str' and 'int'

## raise
print('Exemplo de uso de raise')
name = input('Enter your name')
if name.lower() == 'god':
  raise('Name cannot be GOD!')
else:
  print(name)
