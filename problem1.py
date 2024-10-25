print ("Hello World")

# agr hum ne pre paragraph or
#  koe poem likhni ha to hum triple single quotes ka use kren gy

# print ('''Twinkle, twinkle, little star,
# How I wonder what you are!
# Up above the world so high,
# Like a diamond in the sky.

# When the blazing sun is gone,
# When he nothing shines upon,
# Then you show your little light,
# Twinkle, twinkle, all the night.

# Then the traveler in the dark
# Thanks you for your tiny spark,
# How could he see where to go,
# If you did not twinkle so?

# In the dark blue sky you keep,
# Often through my curtains peep
# For you never shut your eye,
# Till the sun is in the sky.

# As your bright and tiny spark
# Lights the traveler in the dark,
# Though I know not what you are,
# Twinkle, twinkle, little star.''') 

# is me text ki awaz ati ha jo double quotes me likha hta ha
#  pyttsx3 module ko pip ki madad c install krny c ye use kia jaa skta ha

# import pyttsx3
# engine = pyttsx3.init()
# engine.say(" I will speak this text: I am good girl")
# engine.runAndWait()

import os
# specify the directory you want to list
directory_path = '/users'
contents = os.listdir(directory_path)
for item in contents:
    print(item)

import os
directory_path = '/Program Files'
contents = os.listdir (directory_path)
for items in contents:
    print (items)