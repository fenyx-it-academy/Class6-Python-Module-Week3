# I. Write a recursive function sum_of_numbers to calculate the sum of numbers within a given range that takes start and end as parameters.
# The function should work whether start is less or greater than end.


def sum_of_numbers(start,end):
    if start == end:
        return end
    elif start<end:
        return start+sum_of_numbers((start+1), end)

    elif start>end:
        return start + sum_of_numbers((start-1), end)
        
    

# II. Write a function called input_function to ask the user to enter the starting and ending numbers 
# and call sum_of_numbers with those arguments and prints the result.




def input_function():
    start = int(input("enter start: "))
    end = int(input("enter end: "))
        
    result= sum_of_numbers(start,end)
    print(result)

input_function()
# III. Write the same function sum_of_numbers to calculate the sum of numbers
# but this time it takes a list of integers as an argument and calculates the sum of the integers in the list.
# Invoke the function in the main program.

lst=[1,2,3,4,5,6,7,8,9]
def sum_of_numbers(lst):
    total = sum(lst)
    return total
print(sum_of_numbers(lst))



