## 30 Days of Python
## Day 12 - Lambda Expressions & Comprehensions

## Lamba Expressions
print('Lambda Expressions')

names = ['John', 'Peter', 'Elon', 'Joseph']

# make all names upper cased
print('Faz um upper cased na lista de nomes usando expressão lambda')

uppercased = list(map(lambda name: str.upper(name), names))

print(uppercased)

users = [('Mary', 23), ('Emilie', 10), ('Katie', 30)]

sorted_by_name = sorted(users)
print(' \n ')
print('Lista de nomes ordenados por Nome')

print(sorted_by_name)

# [('Emilie', 10), ('Katie', 30), ('Mary', 23)]

sorted_by_age = sorted(users, key = lambda item: item[1]) 
# using age as key for sorting 

print(' \n ')

print('Lista de nomes ordenados por idade')
print(sorted_by_age)
print(' \n ')
# [('Emilie', 10), ('Mary', 23), ('Katie', 30)]

print('Usando a lista [23, 55, 20, 90, 34, 53], imprime apenas os menores que 50')
scores = [23, 55, 20, 90, 34, 53]
scores_under50 = list(filter(lambda x: x < 50, scores))
print(scores_under50) # [23, 20, 34]f

## Comprehensions
## List Comprehension

print(' \n ')
print('Usando List Comprehension')
name = 'python'

new_list = []
for character in name:
  new_list.append(character)

print(new_list) 
# ['p', 'y', 't', 'h', 'o', 'n']

print(' \n ')
name = 'python'
new_list = [item for item in name] # here item can be any name

print(new_list)

print(' \n ')
print('Gerando uma lista com 10 itens rapidamente e espaçados entre eles')
# Quickly generates a list of 10 items with their values squared
new_list = [item**2 for item in range(10)]
print(new_list) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

numbers = [2,34,23,53,34,12,22,89]

even_numbers = [num for num in numbers if num % 2 == 0]
print(' \n ')
print('imprimindo apenas os números pares de uma lista')
print(even_numbers) # [2, 34, 34, 12, 22]

print(' \n ')

brands = [
  {'name': 'Nike', 'category': 'shoes'},
  {'name': 'Reebok', 'category': 'shoes'},
  {'name': 'Tesla', 'category': 'cars'},
  {'name': 'Adidas', 'category': 'shoes'},
  ]

print('Na lista que possui name e categoria, imprime apenas os tenis')

car_brands = [item for item in brands if item['category'] =='shoes']

print(car_brands) # imprime apenas os tenis da lista

names = ['Rick', 'Alan', 'Rick', 'Mike']

print(' \n ')
print('Imprimi os nomes retirando a repetição(Rick)')

new_set = {item for item in names}

print(new_set) # {'Mike', 'Alan', 'Rick'}

attendance = {
    'John': True,
    'David': False,
    'Nick': True,
    'Tom': False,
    'Marie': False,
    'Nancy': True
}

students_present = {key:value for key,value in attendance.items() if value}
print(' \n ')
print('Em uma lista com nomes de alunos e se estão presentes ou não, imprimi apenas os alunos presentes')
print(students_present)

names = [
    'Harry', 'Johnny', 'Lewis', 'Harry', 'Buck', 'Nick', 'David', 'Harry',
    'Lewis', 'Michael'
]

print(' \n ')
print('Imprimi os nomes de uma lista que estão repetidos mais de 1 vez')
duplicate_names = list(set([name for name in names if names.count(name) > 1]))

print(duplicate_names) # ['Lewis', 'Harry']


