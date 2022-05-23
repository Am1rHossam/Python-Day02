num = int(input("Enter the number: "))

def fizzbuzz(num):
    if num %5 == 0 and num %3 == 0:
        print("fizzbuzz")
    elif num %3 == 0:
        print("fizz")
    elif num %5 == 0:
        print("buzz")    
    else:
        print("number isn't divisible by 3 nor 5")

fizzbuzz(num)