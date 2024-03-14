result = 0
num = 1
for i in range(50):
    result = result + num
    num = num + 1
print(result)

result = 0
for num in range(51):
    result = result + num
print(result)



result = 0
for num in range(100):
    if(num % 5 == 0):
    #    print(num)
       result += num 
print(result)


list = list(range(1, 10, 2))
print(list)