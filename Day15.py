## 30 Days of Python
## Day 15 - Generators


def my_infinite_generator():
  num = 0
  while True:
    yield num
    num +=1

result = my_infinite_generator()
print(next(result)) # 0
print(next(result)) # 1
print(next(result)) # 2
print(next(result)) # 3
print(next(result)) # 4

## Stop Iteration Error

print('Parando a iteracao com um erro')

def my_generator(max):
  num = 0
  while num < 3:
    yield num
    num +=1

result = my_generator(3)
print(next(result)) # 0
print(next(result)) # 1
print(next(result)) # 2
## print(next(result)) # Stop Iteration Error

## Performance benefits of using generators

print('Performance benefits of using generators')

print('Fibonacci com um for normal')

def fibonacci(num):
  sequence = []
  a,b = 0,1
  for item in range(num):
    sequence.append(a)
    temp = a
    a = b
    b = temp + b
  return sequence

result = fibonacci(20)
print(result) # prints the fibonacci sequence

print('Fibonacci com uso de generators')

def fibonacci_generator(num):
  a,b = 0,1
  for item in range(num):
    yield a
    temp = a
    a = b
    b = temp + b

for num in fibonacci_generator(20):
  print(num)

## Composition

print('Uso de Composition, usa o resultado de um function como parametro de entrada da outra')

def fibonacci_generator(num):
  a,b = 0,1
  for item in range(num):
    yield a
    temp = a
    a = b
    b = temp + b

def square(nums):
  for num in nums:
    yield num**2

result = square(fibonacci_generator(5))

for num in result:
  print(num) # 0 1 1 4 9
