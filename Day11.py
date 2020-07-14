## Day 11 - Functional Programming I

## Pure Functions

def doubler(num):
  '''
  Accepts a number and multiplies it by 2
  '''
  return num * 2

print(doubler(5))

## map()

numbers = [1,2,3,4,5]
def multiply_by5(num):
  return num * 5

result = map(multiply_by5, numbers)

print(result) # <map object at 0x7f572dcb7730> (Memory location of the map object)
print(list(result)) # [5, 10, 15, 20, 25] (to get the updated list)
print(numbers) # [1,2,3,4,5] (Unmodified)`

## filter()

color_to_remove = 'red'

colors = ['blue', 'green', 'black', 'red']

def search_color(color):
  return color != color_to_remove

result = filter(search_color, colors)

print(list(result)) # ['blue', 'green', 'black']
print(colors) # ['blue', 'green', 'black', 'red'] (Unmodified)

## zip()

emails = ['alan@gmail.com', 'ross@gmail.com']
usernames = ['alan', 'ross']

users = list(zip(emails,usernames))
print(users) # [('alan@gmail.com', 'alan'), ('ross@gmail.com', 'ross')]
print(emails) # ['alan@gmail.com', 'ross@gmail.com'] (Unmodified)
print(usernames) # ['alan', 'ross']

## reduce()


from functools import reduce

numbers = [1,2,3,4]
def accumulator(acc, curr):
  return acc + curr

sum = reduce(accumulator, numbers, 0)
print(sum) # 10

