import utilities

result = utilities.tagify('hello world', 'p')

emoji_result = utilities.emojifier('python', '')

print(result)  # <p>hello world</p>
print(emoji_result)  #  python 
