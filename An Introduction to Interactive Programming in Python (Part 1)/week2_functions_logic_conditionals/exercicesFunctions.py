
# %%
def miles_to_feet(miles):
    feet = miles *5280
    return feet

# %%

def total_seconds(hour,minutes,seconds):
    hourToMin = hour*60*60
    minutesToSec = minutes * 60
    totalMin = hourToMin+minutesToSec+seconds
    return totalMin

# %%
def rectangle_perimeter(width,height):
    perimerter = width*2 + height*2
    return perimerter

# %%
def rectangle_area(width,height):
    area = width*height
    return area

# %%
import math
def circle_circumference(radius):
    circunference = 2*math.pi*radius
    return circunference

# %%
import math
def circle_area(radius):
    area = math.pi*radius**2
    return area

# %%
def future_value(present_value, annual_rate, years):
    value = present_value*(1+annual_rate/100)**years
    return value
myvalue = future_value(1000,7,10)
print(myvalue)

# %%
def name_tag(first_name,last_name):
    return "My name is "+ first_name +" " +last_name
myname = name_tag("leonel", "baptista")
print(myname)

# %%
def name_and_age(name,age):
    return name +" is "+str(age)+" years old."

# %%
def point_distance(x0,y0,x1,y1):
    distance = ((x0 - x1) ** 2 + (y0 - y1) ** 2) ** 0.5
    return distance

# %%
def point_distance(x0, y0, x1, y1):
	"""Returns the Euclidian distance between two points (x0,y0) and (x1,y1)."""
	
	return ((x0 - x1) ** 2 + (y0 - y1) ** 2) ** 0.5
	
def triangle_area(x0, y0, x1, y1, x2, y2):
	"""Returns the area of a triangle with vertices (x0,y0), (x1,y1), and (x2,y2)."""
	
	# Compute the lengths of the three sides.
	a = point_distance(x0, y0, x1, y1)
	b = point_distance(x0, y0, x2, y2)
	c = point_distance(x1, y1, x2, y2)
	
	# Compute the semi-perimeter length, i.e., half of the perimeter length.
	s = (a + b + c) / 2
	
	# Compute the area according to Heron's formula.
	return (s * (s - a) * (s - b) * (s - c)) ** 0.5

# %%
def print_digits(number):
	"""Prints the tens and ones digit of an integer in [0,100)."""
	
	print ("The tens digit is " + str(number // 10) + ",")
	print ("and the ones digit is " + str(number % 10) + ".")

# %%
# Compute and print powerball numbers.

###################################################
# Powerball function
# Student should enter function on the next lines.
import random
def powerball():
    """Prints Powerball lottery numbers."""
    
    print ("Today's numbers are " + str(random.randrange(1, 60)) + ",")
    print (str(random.randrange(1, 60)) + ",")
    print (str(random.randrange(1, 60)) + ",")
    print (str(random.randrange(1, 60)) + ", and")
    print (str(random.randrange(1, 60)) + ". The Powerball number is")
    print (str(random.randrange(1, 36)) + ".")