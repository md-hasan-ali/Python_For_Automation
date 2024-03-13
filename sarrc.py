saarc = ["Bangladesh", "Afghanistan", "Bhutan", "Nepal", "India", "Pakistan",
"Sri Lanka"]

country = input("Enter your country name: ")
if country in saarc:
    print(country, "is a member of SAARC")
else: 
    print(country, "is not a member of SAARC")