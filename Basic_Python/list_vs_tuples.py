# Example list
my_list = ['apple', 'banana', 'cherry', 'date']

for item in my_list:
    if item == "banana":
        print(item)


index = 0
while index < len(my_list):
    print(my_list[index])
    index +=1


# Lists are mutable, meaning you can change their contents after they've been created.
# Tuples are immutable, meaning once they are created, their contents cannot be changed.