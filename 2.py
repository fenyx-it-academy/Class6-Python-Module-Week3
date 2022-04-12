def computepay(hour,rate):
    if hour > 40:
        payment = 1.5 * rate * (hour - 40) + (40 *rate)
    else:
        payment = hour * rate
    return payment
    
hours = float(input("Enter Hours:"))
rates = float(input("Enter rate per hour:"))


print('Aldiginiz para miktari', computepay(hours,rates) )