def myfnc(x):
    print("inside myfnc", x)
    x = 10
    print("inside myfnc", x)

x = 20
myfnc(x)
print(x)

def myfnc(x, y=10, z=0):
    print("x =", x, "y =", y, "z =", z)
x = 5
y = 6
z = 7
myfnc(x, y, z)
myfnc(x, y)
myfnc(x)

def add_numbers(numbers):
    result = 0
    for number in numbers:
        result += number
        return result

result = add_numbers([1,2,3,4,5,6,7,8,9])


print(result)

def Namota(number=1):
    for i in range(1, 11):
       print(number, "x" , i, "=", number * i)

user_input = input("Enter your number: ")
user_input = int(user_input)     
Namota(user_input)