student_database = {
    1001: {'name': 'Alice', 'age': 15, 'grade': 10},
    1002: {'name': 'Bob', 'age': 16, 'grade': 11},
    1003: {'name': 'Charlie', 'age': 15, 'grade': 10}
}

usernames = {'Hasan', 'Ali', 'Ringku'}
new_userName = "Alii"
if new_userName in usernames:
    print("Username is already exists..!")
else:
    usernames.add(new_userName)
    print("Username added successfully..!")

print(usernames)