# If a person’s age is 18 or older, they are eligible for a car license; otherwise, they are not eligible.

age = int(input("Enter you age: "))

if(age>=18):
    print("You are eligibal for car license")
else:
    print("You are not eligibal for car license")

# ***If a person has passed both the written and driving tests, they qualify for a car license; otherwise, they do not qualify***.

write = input("Have you passed written test? (Yes/No): ")
drive = input("Have you passed driving test?(Yes/No): ")

if write.lower() == "yes" and drive.lower() == "yes":
    print("You are qualify for a car license")
elif write.lower() == "yes" and drive.lower() == "no":
    print("Complete your dirving test")
elif write.lower() == "no" and drive.lower() == "yes":
    print("Completer your writting test")
else:
    ("You are disqualify for car license")

# ***If a person’s license has expired, prompt them to renew it; otherwise, their license is still valid.***

person = input("Has your license is expired?(Yes/No): ")

if person.upper() == "YES":
    print("You license has expired. \n So renew it.")
else:
    print("Your license is valid")

# ***If a person has completed driving hours and passed the road test, they qualify for a
#  license. If they’ve only completed driving hours, prompt them to take the test. If neither
# is completed, they do not qualify.***

hours = input("Have you complete your driving hours? (Yes/No): ")
road = input("Have you complete your road test?(Yes/No): ")

if hours.lower() == "yes" and road.lower() == "yes":
    print("You are qualify for license.")
elif hours.lower() == "yes" and road.lower() == "no":
    print("You are completed your driving hours so you take rest.")
else:
    print("You are disqualify")

# ***If a person has received three or more driving violations, suspend the license; otherwise, it remains active.***
violation = int(input("Enter the number of driving violations: "))

if violation >=3:
    print("Your license is suspended due to excessive violations.")
else:
    print("Your license remains active.")