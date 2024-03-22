# # Positive/ Negative 
# number = float(input("Enter your number: "))
# if number > 0:
#     print("This is positive number")
# elif number < 0:
#         print("This is Negative number")
# else:
#     print("This is Zero")


# # Even / Odd Number 
# number = input("Enter your Number: ")
# number = int(number)

# if number % 2 == 0:
#     print("This is even number")
# else:
#     print("This is odd number")

# # Leap year 
# year = input("Enter your year: ")
# year = int(year)
# if year % 4 != 0:
#     print("No")
# else:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Yes")
#         else:
#             print("No")
#     else:
#         print("Yes")


# # Leap year different way 
# year = input("Enter your year: ")
# year = int(year)
# if year % 100 != 0 and year % 4 == 0:
#     print("Yes")
# elif year % 100 == 0 and year % 400 == 0:
#     print("Yes")
# else:
#     print("No")



str = "Bangladeshljsldfjlsdjflsjdflkjsd"
result = ""
for i in range(0, len(str), 2):
    result =  result + str[i+1]
    result = result + str[i]

print(result)


result = ""
result2 = ""
newresult = ""
for i, char in enumerate(str):
    if i % 2 == 0:
        result += char
    else:
        result += char


for r1 in result:
    newresult += r1
    for r2 in result2:
        newresult += r2


print(newresult)

result = str[1] + str[0] + str[3] + str[2]
print(result)
