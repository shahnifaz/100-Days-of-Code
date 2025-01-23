def prime_number(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True
       
number = int(input("Enter a number: "))

if prime_number (number) == False:
    print("It's not a prime number.")
else:
    print("It's a prime number.")