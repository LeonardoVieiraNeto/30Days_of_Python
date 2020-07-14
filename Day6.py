import emoji

##30 Days of Python
## Day 6 - Loops II & Functions

##While Loops

hungry = False
while(hungry): # This is always true so it keeps printing until system crashes!
  print('Give me something to eat!!')


hungry = True
while(hungry):
    print('Give me something to eat!!')
    break # prints only once and stops the loop execution
hungry = True
satisfaction = 0
while(satisfaction < 10):
  satisfaction += 1
  print('Give me something to eat!!') # prints 10 times


  hungry = True
satisfaction = 0
while satisfaction < 10:
  satisfaction += 1
  print('Give me something to eat!!')
else:
    print('I am super satisfied now') # gets printed once condition is falsy

    
hungry = True
satisfaction = 0
while satisfaction < 10:
  satisfaction += 1
  print('Give me something to eat!!')
else:
    print('I am super satisfied now') # gets printed once condition is falsy

##While vs For Loop
while True:
  response_from_user = input('Enter some message. Enter bye to exit')
  if(response_from_user == 'bye'):
    break

## Quick Coding Exercise
##Procura o email que está duplicado e o imprime na tela
email_list = ['roger@hey.com','michael@hey.com','roger@hey.com','prince@gmail.com']
duplicate_emails = []
for email in email_list:
  if email_list.count(email) > 1 and email not in duplicate_emails:
    duplicate_emails.append(email)
print(duplicate_emails)

def blow_fire(): # This part is called function definition
  print('fire ')

blow_fire() # This part is called function invocation

blow_fire() # It can be called any number to times to perform some action

## Arguments and Parameters

def blower(name, emoji): # parameters
  print(f'{name} {emoji} {emoji} {emoji}')

blower('fire', 'adad')

##Return

def multiplier(num1, num2):
  return num1 * num2

result = multiplier(2,3)
print(result) # 6

def sum(num1):
  def child(num2):
    return num1 + num2
  return child

add_10 = sum(10)
print(add_10(20)) # 30  (Closure!!!)
print(add_10(50)) # 60
print(add_10(100)) # 110

def test_function():
  '''
  This function just prints test to the console.
  '''
  print('test')

test_function()

##*args and **kwargs
def powerful_function(*args):
  print(args)

powerful_function(1,3,2) # (1, 3, 2) --> Returns a tuple

def super_function(**kwargs):
  print(kwargs)

super_function(name='John', age='45') # {'name': 'John', 'age': '45'} --> Returns a dict
