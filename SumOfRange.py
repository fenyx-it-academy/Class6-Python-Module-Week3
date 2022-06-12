# Write a recursive function sum_of_numbers to calculate the sum of numbers within a given range 
# that takes start and end as parameters.
# The function should work whether start is less or greater than end.

def sum_of_numbers(x,y):
    sum_range = 0
    if x>=y:
        while x>=y:
            sum_range = sum_range+x
            x=x-1
        return (print(sum_range))
    elif y>x:
        while y>=x:
            sum_range = sum_range+y
            y=y-1
        return (print(sum_range))
# Write a function called input_function to ask the user to enter the starting and ending numbers and call sum_of_numbers with those 
# arguments and prints the result.
x = int(input('Please Enter the First Number :' ))
y = int(input('Please Enter the Second Number :' ))
sum_of_numbers(x,y)

# Write the same function sum_of_numbers to calculate the sum of numbers but this time it takes a list of integers as an argument 
# and calculates the sum of the integers in the list. Invoke the function in the main program.

a = []
while True:
    x = int(input('Write the elements of the list : '))                  
    if x == 0:
        break    
    a.append(x)
        
print(sum(a))




