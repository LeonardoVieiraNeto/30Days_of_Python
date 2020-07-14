## 30 Days of Python
## Day 18 - File I/O

content = open('test.txt')
output = content.read()
print(output) # I am learning python.


## Closing Files

print('Com o mode r, apos o uso, libera a memoria')

content = open('test.txt', mode='r')
output = content.read()
print(output)
content.close()

print(' \n ')
print('Validando se o arquivo existe')

try:
    content = open('test1.txt', mode='r')
    output = content.read()
    print(output)
except FileNotFoundError as error:
    print(f'Arquivo não existe {error}')
finally:
    content.close()

print(' \n ')
print('Usando assim, a leitura do arquivo fica mais performatica')

with open('test.txt', mode='r') as content:
    output = content.read()
    print(output) # I am learning python.

## Writing to Files

print(' \n ')
print('Escrevendo em um arquivo')

with open('test.txt', mode='w', encoding='utf-8') as my_file:
    my_file.write('This is the first line\n') # \n is for creating a newline
    my_file.write('This is the second line\n')
    my_file.write('This is the third line')

print('Com o mode A podemos escrever no arquivo')
with open('test.txt', mode='a', encoding='utf-8') as my_file:
    my_file.write('This text will be appended')

print('Com o mode W, podemos escrever uma lista de itens diretamento no arquivo')

with open('test.txt', mode='w', encoding='utf-8') as my_file:
    my_file.writelines(['First line', '\n', 'Second Line'])

## Reading from files

print(' \n ')
print('Reading from files')
with open('test.txt', mode='r', encoding='utf-8') as my_file:
    content = my_file.read()
    print(content)

## Uso do método tell para busca é usado para trazer o cursor para uma posição específica no arquivo.

print(' \n ')
print('Uso do método tell')

with open('test.txt', mode='r', encoding='utf-8') as my_file:
    my_file.seek(0) # brings cursor to beginning of file
    print(my_file.tell()) # prints location of cursor
    content = my_file.read()
    print(content)


    
