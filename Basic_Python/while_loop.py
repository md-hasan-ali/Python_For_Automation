# i = 0
# while i <= 5:
#     print (i)
#     i +=1

# i = 5
# while i>=0:
#     i-=1
#     print(i)

# n = input("Please enter a positive integer: ")
# n = int(n)

# m = 1
# while m <= 10:
#     print(n, "x", m, "=", n*m)
#     m += 1

# while True:
#     n = input("Please enter a positive number (0 to exit): ")
#     n = int(n)

#     if n<0:
#         print("We only allow the positive number. Please try agin.")
#         continue
#     if n==0:
#         break
#     print("Square of", n, "is", n*n)


terminate_program = False
while not terminate_program:
    number1 = input("Please enter a number: ")
    number1 = int(number1)
    number2 = input("Please enter a another number: ")
    number2 = int(number2)

    while True:
        operation = input("Please enter add/sub or quit to exit: ")
        if operation == "quit":
            terminate_program = True
            break
        if operation not in ["add", "sub"]:
            print("Unknown Operation!")
            continue
        if operation== "add":
            print("Result is", number1 + number2)
            break
        if operation == "sub":
            print("Result is", number1 - number2)
            break