#compute the area of a triangle
# %%
def triangle_area(base, height):
    area = (1.0/2) * base * height
    return area

al =  triangle_area(5,5)
print (al)

# %%
# converts fahrenheit to celcius
def fahrenheit2celcius(fahrenheit):
    celcius = (5.0/9) * (fahrenheit-32)
    return celcius
cel = fahrenheit2celcius(10)
print (cel)

# %%
# convert fahrenheit to kelvin
def fahrenheit2kelvin(fahrenheit):
    celcius = fahrenheit2celcius(fahrenheit)
    kelvin = celcius + 273.15
    return kelvin
Kel = fahrenheit2kelvin(10)
print (Kel)

# %%
# Remainder application - 24 hour clock
# http://en.wikipedia.org/wiki/24-hour_clock

hour = 20
shift = 8
print ((hour + shift) % 24)

# %%
# Data conversion operations

# convert an integer into string - str
# convert an hour into 24-hour format "03:00", always print leading zero
hour = 3
ones = hour % 10
tens = hour // 10
print (str(tens),str(ones), ":00")
print (str(tens)+str(ones)+":00") #the correct with + to get strings togheter
