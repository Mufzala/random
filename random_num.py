import random
min_id = 88888888
max_id = 99999999

eng_min = 2222
eng_max = 9999
random_num = random.randint(min_id, max_id)
random_eng = random.randint(eng_min, eng_max)
# print("Licence Number: " , random_num)
# print("Engine No: ", random_eng)

owner = input("Owner First Name: ")
owner_last = input("Owner Last Name: ")
Model_Name = input("Model Name: ")
Registration_no = random_num
print("Licence Number: " , random_num)
print("Engine No: ", random_eng)

print('''vahicle_class = Motor Car 
Car_insuranceDate = 29-8-23
insurance_expiry = 31-12-30
Licence Current Type: Car/Jeep
Licence Current/Renewal Date: 26-10-24
Licence Expiry Date:  26-10-29
RTO : Islamabad''')
message = ''' Congratulation! <|Name|>  
On your new car
                      Warmest regards,
                      hamna
                        Yaya Luxury Wheels '''
print(message.replace("<|Name|> ",owner))










