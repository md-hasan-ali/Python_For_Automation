# Positive/ Negative 
number = float(input("Enter your number: "))
if number > 0:
    print("This is positive number")
elif number < 0:
        print("This is Negative number")
else:
    print("This is Zero")


# Even / Odd Number 
number = input("Enter your Number: ")
number = int(number)

if number % 2 == 0:
    print("This is even number")
else:
    print("This is odd number")

# Leap year 
year = input("Enter your year: ")
year = int(year)
if year % 4 != 0:
    print("No")
else:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Yes")
        else:
            print("No")
    else:
        print("Yes")


# Leap year different way 
year = input("Enter your year: ")
year = int(year)
if year % 100 != 0 and year % 4 == 0:
    print("Yes")
elif year % 100 == 0 and year % 400 == 0:
    print("Yes")
else:
    print("No")
