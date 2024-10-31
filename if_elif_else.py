# Write a program to classify the weather based on temperature input. If the temperature is above 30°C,
#  it’s "Hot"; if it’s between 15°C and 30°C, it’s "Warm"; if it’s between 0°C and 15°C, it’s "Cool"; 
# and if it’s below 0°C, it’s "Cold."

# weather = int(input("Enter temperature: "))

# if weather>=30:
#     print("It's Hot")
# elif weather >15<30:
#     print("It's Warm")
# elif weather>0<15:
#     print("It's Cool")
# else:
#     print("It's Cold")

# Write a program to apply a discount based on a user’s purchase amount. If the amount is over $500, 
# apply a 20% discount; if it’s between $200 and $500, apply a 10% discount; and if it’s below $200, 
# no discount applies.

purchase = int(input("Enter your purchase amount: "))

if purchase >=500:
    print(f"20% is on ${purchase} ")
elif purchase >200 <500:
    print(f"10 % discount on ${purchase}")
else:
    print("No discount")
