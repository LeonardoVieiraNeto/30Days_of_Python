import time

useSleep = 0

'''Aula 1 '''
'''30 Days of Python'''

name = input('What is your name?') #promts user input in console and store in a variable
print('Welcome to the world of Python ' + name) # prints to console 

'''Aula 2 '''
'''30 Days of Python'''

num = 100 # variable assignement
print(type(num)) # <class 'int'>

num2 = 99.99
print(type(num2)) # <class 'float>

expression1 = num * 10
print(type(expression1)) # <class 'int'>

expression2 = num + num2
print(type(expression2)) # <class 'float'>

print(round(2.1)) # 2

print(round(5.9)) # 6

print(abs(-34)) # 34

if useSleep == 1:
    time.sleep(10)

name = 'Python' # string assignment within single quotes

name2 = "Python" # string assingment within double quotes

name3 = '''This is a a very long string and supports 
           multiline statements as well''' # string assingment within 3 single quotes

name4 = 'Hello! \"Rockstar Programmer\"' # string with escaped character sequence

print(type(name)) # <class 'str'>

print(type(name2)) # <class 'str'>

print(type(name3)) # <class 'str'>

print(type(name4)) # <class 'str'>

if useSleep == 1:
    time.sleep(10)

##String Concatenation

first_name = 'Mike'

last_name = 'Tyson'

print(first_name + ' ' + last_name) # Mike Tyson

##Type Conversion

user_name = 'John'
age = 40
print(user_name + str(age)) # TypeError: can only concatenate str (not "int") to str
# This would work in Javscript where it would convert the result to string type

if useSleep == 1:
    time.sleep(10)

user_name = 'John'
age = 40
print(user_name + str(age)) # John40
##print(str(age)) # <class 'str'>

if useSleep == 1:
    time.sleep(10)

lucky_number = 7
lucky_number_stringified = str(7)
lucky_number_extracted = int(lucky_number_stringified)
print(lucky_number_extracted) # 7

'''Aula 3 '''
'''30 Days of Python'''

if useSleep == 1:
    time.sleep(10)

first_name = 'Tom'
last_name = 'Cruise'
welcome_message = "Welcome" + " " + first_name + " " + last_name
print(welcome_message) # Welcome Tom Cruise

if useSleep == 1:
    time.sleep(10)

first_name = 'Tom'
last_name = 'Cruise'
welcome_message = f'Welcome {first_name} {last_name}'
print(welcome_message) # Welcome Tom Cruise

if useSleep == 1:
    time.sleep(10)

firstName = 'Tom';
lastName = 'Cruise';
welcomeMessage = 'Welcome ${firstName} ${lastName}';
print(welcomeMessage) # Welcome Tom Cruise

if useSleep == 1:
    time.sleep(10)

language = 'python'
first_character = language[0] # indexing starts from 0
second_character = language[1]
print(first_character) # p
print(second_character) # y
# Strings can be manipulated easily with this syntax [start:stop:step-over]
range_1 = language[0:2] # here it starts from index 0 and ends at index 2
range_2 = language[0::1] # starts at 0, stops at end with step over 1 
range_3 = language[::2] # starts at 0, till end with step 2
range_4 = language[1:] # starts at index 1 till end of string
range_5 = language[-1] # selects last character
range_6 = language[-2] # second last character
reverse_string = language[::-1] # starts from end and reverses the string
reverse_string_2 = language[::-2] # reverses string and skips 1 character

print(range_1) # py
print(range_2) # python
print(range_3) # pto
print(range_4) # ython
print(range_5) # n
print(range_6) # o
print(reverse_string) # nohtyp
print(reverse_string_2) # nhy

if useSleep == 1:
    time.sleep(10)

favorite_website = 'dev.to'
##favorite_website[0] = 'w'
print(favorite_website) # TypeError: 'str' object does not support item assignment

## Built-in string functions and methods
quote = 'javascript is awesome'
print(len(quote)) # 21 (len calculates total no of characters)
new_quote = quote.replace('javascript', 'python')
print(new_quote) # python is awesome
capitalize = new_quote.capitalize()
print(capitalize) # Python is awesome
upper_case = new_quote.upper()
print(upper_case) # PYTHON IS AWESOME

print(quote) # javascript is awesome (Note: Strings are immutable!) 

if useSleep == 1:
    time.sleep(10)

## Boolean

is_cool = True
is_dirty = False
print(10 > 9) # True 

## Lists

favorite_languages = ['javascript', 'python', 'typescript']
shopping_cart_items = ['pen','toothbrush', 'sanitizer','eraser']
random_things = ['football', 123, True, 'developer', 777]

first_item = shopping_cart_items[0]
print(first_item) # 'pen'

if useSleep == 1:
    time.sleep(10)

## List Slicing

soccer_stars = ['ronaldo', 'messi','ibrahimovic','zidane','beckham']
soccer_stars[0] = 'suarez'
print(soccer_stars) # ['suarez', 'messi','ibrahimovic','zidane','beckham']
range = soccer_stars[0:3]
print(range) # ['suarez', 'messi', 'ibrahimovic']
print(soccer_stars) # ['suarez', 'messi','ibrahimovic','zidane','beckham']
# Note : Slicing lists does not mutate them

if useSleep == 1:
    time.sleep(10)

clone = soccer_stars[:] # copies the list. Commonly used in Python
print(clone) # ['suarez', 'messi','ibrahimovic','zidane','beckham']
reverse_order = soccer_stars[::-1] # reverses the order of data
print(reverse_order) # ['beckham', 'zidane', 'ibrahimovic', 'messi', 'suarez']

## Matrix

matrix_2 = [[1,3,2], [1,3,2], [2,3,4], [2,3,5]]
first_item = matrix_2[0]
print(first_item) # [1,3,2]
first_item_first_element = matrix_2[0][0] # or first_item[0]
print(first_item_first_element) # 1


'''Aula 4 '''
'''30 Days of Python'''

print('Aula 4 - 30 Days of Python')

if useSleep == 1:
    time.sleep(10)

## Actions on lists

scores = [44,48,55,89,34]
scores.append(100) # Append adds a new item to the end
print(scores) # [44, 48, 55, 89, 34, 100]
scores.insert(0, 34) # Inserts 34 to index 0
scores.insert(2, 44) # Inserts 44 to index 2
print(scores) # [34, 44, 44, 48, 55, 89, 34, 100]
scores.extend([23]) # Extend takes an iterable (loopable items) and adds to end of list
print(scores) # [34, 44, 44, 48, 55, 89, 34, 100, 23]
scores.extend([12,10])
print(scores) # [34, 44, 44, 48, 55, 89, 34, 100, 23, 12, 10]

scores = [44,48,55,89,34]
newScores = scores.append(100)
print(newScores) # None 
newScores = scores.insert(0,44)
print(newScores) # None
print(scores)

## Removing items from list (pop, remove, clear)

languages = ['C', 'C#', 'C++']
languages.pop()
print(languages) # ['C', 'C#']
languages.remove('C')
print(languages) # ['C#']
languages.clear()
print(languages) # []

##Getting index and counting (index, count)

alphabets = ['a', 'b', 'c']
print('Posicao do A na lista ' + str(alphabets.index('a'))) # 0 (Returns the index of the element in list
print('Posicao do B na lista ' + str(alphabets.count('b'))) # 1 (counts the occurence of an element

##Sorting, reversing and copying lists

numbers = [1,4,6,3,2,5]
numbers.sort() # Sorts the list items in place and returns nothing
print('Numeros em ordem crescente: ')
print(numbers) # [1, 2, 3, 4, 5, 6]

#Python also has a built in sorting function that returns a new list
sorted_numbers = sorted(numbers) # note - this is not a method
print('Numeros em ordem crescente: ')
print(sorted_numbers) # [1, 2, 3, 4, 5, 6]

numbers.reverse() # reverse the indices in place
print('Numeros em ordem decrescente: ')
print(numbers) # [6, 5, 4, 3, 2, 1]

numbers_clone = numbers.copy() # another approach is numbers[:]
print('Numeros em ordem decrescente em uma lista copiada: ')
print(numbers_clone) # [6, 5, 4, 3, 2, 1]

## Some common list patterns

avengers = ['ironman', 'spiderman', 'antman', 'hulk']
cloned_avengers = avengers[::1] # very commonly used pattern
reversed_avengers = avengers[::-1] # discussing again because it is also very common
merge_avengers = ' '.join(avengers) # used to join list into string
print(cloned_avengers) # ['ironman', 'spiderman', 'antman', 'hulk']
print(reversed_avengers) # ['hulk', 'antman', 'spiderman', 'ironman']
print(merge_avengers) # ironman spiderman antman hulk

## Não consegui executar essa parte do código, deu erro no list
## range_of_numbers =  list(range(0, 9)) # quickly generates a list of specific range
## print(range_of_numbers) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
## another_range = list(range(0,5)) # with start stop
## print(another_range) # [0, 1, 2, 3, 4]

## List Unpacking

first,second,third = ['tesla','ford','ferarri']
print(first) # tesla
print(second) # second
print(third) # ferarri

a,*others = [1,2,3,4,5] # remaining values are stored in others
print(a) # 1
print(others) # [2, 3, 4, 5]

## Dictionaries
user = {'name': 'Max', 'age': 40, 'married': False}
print(user['name'])
print(user['married'])

abstract = {
 'first': 123,
 True: 'hello',
 777: [1,3,4,5]
}

print(abstract['first']) # 123
print(abstract[True]) # 'hello
print(abstract[777]) # [1,3,4,5]

sample = {
    'username': 'hisenberg',
    'username': 'james'
}
print(sample['username']) # james


##Dictionary Methods

house = {
    'rooms' : 4,
    'occupants': 2,
    'doors': 6
}

##Caso tente Executar essa linha vai dar erro, não existe  a key Windows
## print(house['windows']) # KeyError: 'windows'

#instead
print(house.get('windows')) # None
print(house.get('windows', 5)) # 5 (This sets a default value if no value is found)


user = {'name': 'Raghav', 'age': 20, 'country': 'India'}
print('name' in user.keys()) # True
print('gender' in user.keys()) # False
print('Raghav' in user.values()) # True

##Some other useful dictionary methods are copy, clear, pop, update
cat = {
    'name': 'Tom',
    'greet': 'meow',
    'health': 100
}
cat_copy = cat.copy()
print(cat_copy) # {'name': 'Tom', 'greet': 'meow', 'health': 100}

cat.pop('name')
print(cat) # {'greet': 'meow', 'health': 100}

cat.clear()
print(cat) # {}

cat_copy.update({'name': 'Polo'})
print(cat_copy) # {'name': 'Polo', 'greet': 'meow', 'health': 100}
cat_copy.update({'color': 'Black'}) # adds key value if not present
print(cat_copy) # {'name': 'Polo', 'greet': 'meow', 'health': 100, 'color': 'Black'}

##Tuples

my_tuple = (1,2,3) # Can be any no of items
print(my_tuple[1]) # 2 (Values can be accessed just like lists)
print(1 in my_tuple) # True (Checks if element is present)

colors = ('red', 'orange', 'blue', 'yellow')
new_colors = colors[1:4]
print(new_colors) # ('orange', 'blue', 'yellow')

color_1, * others = colors # unpacking!
print(color_1) # 'red'
print('Antes de imprimir o others')
print(others) # ['orange', 'blue', 'yellow']

print(len(colors)) # 4
print(colors.count('red')) # 1 
print(colors.index('orange')) # 1

set_of_numbers = {1,2,3,4,5,5}
print(set_of_numbers) # {1,2,3,4,5}  (Only unique values are stored)

emails = ['samantha@hey.com', 'rock@hey.com', 'samantha@hey.com']
emails_set = set(emails)
unique_emails = list(emails_set)
print(unique_emails) # ['rock@hey.com', 'samantha@hey.com']

set_a = {1,2,3,4,5}
set_b = {4,5,6,7,8}
print(set_a.union(set_b)) # {1, 2, 3, 4, 5, 6, 7, 8}
print(set_a | set_b) # same as above just a compact syntax

print(set_a.intersection(set_b)) # {4, 5}
print(set_a & set_b) # same as above

set_a.discard(1)
print(set_a) # {2,3,4,5}



'''Aula 5 '''
'''30 Days of Python'''


'''Aula 6 '''
'''30 Days of Python'''


'''Aula 7'''
'''30 Days of Python'''

