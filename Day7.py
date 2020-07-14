## 30 Days of Python
## Day 8 - OOP Basics

print(type(2)) # <class 'int'>
print(type(2.5)) # <class 'float'>
print(type('Python')) # <class 'str'>
print(type(True)) # <class 'bool'>
print(type({})) # <class 'dict'>
print(type([])) # <class 'list'>
print(type(())) # <class 'tuple'>
print(type(None)) # <class 'NoneType'>

## Coding Exercise

class SoccerPlayer:
  def __init__(self, name, goals):
    self.name = name
    self.goals = goals


def calculateMaxGoals(*args):
  print(args)
  return max(*args)

messi = SoccerPlayer('messi', 10)
ronaldo = SoccerPlayer('ronaldo',22)
neymar = SoccerPlayer('neymar', 50)

max_goals = calculateMaxGoals(messi.goals, ronaldo.goals, neymar.goals)
print(f'The highest number of goals is {max_goals} goals')

## @classmethod and @staticmethod

class Calculator:
  def __init__(self,type):
    self.type = type

  @classmethod
  def calculate_sum(cls, num1, num2): 
        return num1 + num2
    # cls is just like self which needs to passed as 1st parameter

print(Calculator.calculate_sum(3,5)) # 8

class Calculator:
  def __init__(self,type):
    self.type = type

  @staticmethod
  def multiply(num1, num2): 
        return num1 * num2
    # cls is just like self which needs to passed as 1st parameter

print(Calculator.multiply(3,5)) # 15
