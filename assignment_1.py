# I. Write a function called int_return that takes an integer as input and returns the same integer.

def int_return(n):
    return n
print(int_return(5))


# II. Write a function called add that takes any number as its input and returns that sum with 2 added.

def add(n):
    sum = n + 2
    return sum
print(add(5))


# III. Write a function called greet that takes any name (string), and greets the person.
#      E.g. “Hello Bob! Nice to meet you!” (Only returns the greeting string, printing is done in the main program.)
name=input("Enter a name: ")
def greet(name):
    print("Hello", name,"! Nice to meet you!")
greet(name)


# IV. Write a function, accum, that takes a list of integers as input and returns the sum of those integers.

def accum(list):
    sum = 0
    for i in list:
        sum = sum + i
    print("Sum is: ", sum)
list_1=[1,2,3,4,5,6,7,8,9,10]
accum(list_1)

# V. Write a function, length, that takes in a list as the input.
# If the length of the list is greater than or equal to 5, return “Longer than 5”. If the length is less than 5, return “Less than 5”.


def length(list):
    if len(list)>=5:
        return "Longer than 5" 
    else:
        return  "Less than 5" 

list_1=["Tugrul", "Emrah","Ali","Emre"]
print(length(list_1))


# VI. You will need to write two functions for this problem.
# The first function, divide that takes in any number and returns that same number divided by 2.
# The second function called sum should take any number, divide it by 2, and add 6.
# It should return this new number. You should call the divide function within the sum function. Do not worry about decimals.

def diveded_by_2(n):
    return n/2

def sum(n):
    return n+6

n=int(input("Enter a n: "))
print(sum(diveded_by_2(n)))

