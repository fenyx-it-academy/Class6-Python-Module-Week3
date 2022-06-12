# Write a function called greet that takes any name (string), and greets the person. 
# E.g. “Hello Bob! Nice to meet you!” (Only returns the greeting string, printing is done in the main program.)
def greet(name):
    name = input('Please Enter a Name : ')
    return 'Hello {}! Nice to meet you'.format(name)
print(greet('name'))