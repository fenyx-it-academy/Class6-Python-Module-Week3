# Write a function, length, that takes in a list as the input. 
# If the length of the list is greater than or equal to 5, return “Longer than 5”. 
# If the length is less than 5, return “Less than 5”
def length():
    a = []
    while True:
        x = input('Write the elements of the list : ')                  
        if x == 'exit':
            break    
        a.append(x)          
    if len(a)>=5:
        return  'Longer than 5'
    else:
        return 'Less than 5'
print(length())
