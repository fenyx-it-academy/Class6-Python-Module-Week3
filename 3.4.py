"""def sum_of_numbers(a,b):
    result=0
    if a<=b:
        result=a+ sum_of_numbers(a+1,b)
    return result
print(sum_of_numbers(1,4))"""

"""def input_function(a=int(input("Please entere a number")),b=int(input("Please enter a number "))):
    if a<b:
        return sum_of_numbers(a,b)
    if a>=b:
        return sum_of_numbers(b,a)
print(input_function())"""

myList=[2,4,5,78,8]
def sum_of_numbers(x):
    result=0
    for i in x:
        result+=i
    return result
print(sum_of_numbers(myList))