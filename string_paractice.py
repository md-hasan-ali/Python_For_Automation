country = "North South"
new_country = country.replace("South", "Korea")
print(new_country)
print(country)

name = "Md Hasan Ali"
if name.startswith("Md"):
    print("Dear Md.")

str = "a quick brown fox jumps over the lazy dog"
for c in "abcdefghijklmnopqrstuvwxyz":
    print(c, str.count(c))

str1 = "HelloTestsldfj.65d656d4f6g4@#$%^&*()f123123good"
upper_count = ""
lower_count = ""
digit_count = ""
other_count = ""

for char in str1:
    if char.isupper():
        upper_count += char
    elif char.islower():
        lower_count += char
    elif char.isdigit():
        digit_count += char
    else:
        other_count += char

print(upper_count)
print(lower_count)
print(digit_count)
print(other_count)