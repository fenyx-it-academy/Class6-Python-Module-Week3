#Write a function, accum, that takes a list of integers as input and returns the sum of those integers.
def accum():
    sum_integers = 0
    while True:
        num = int(input('Please Enter a Number :'))
        sum_integers = sum_integers+num
        if num == 0:
            break
    return sum_integers
print(accum())