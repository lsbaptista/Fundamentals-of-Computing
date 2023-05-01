# %%
# Compute whether an integer is even.

###################################################
# Is even formula
# Student should enter function on the next lines.
def is_even(number):
    if number%2==0:
        return number

# %%
# Compute whether a person is cool.

###################################################
# Is cool formula
# Student should enter function on the next lines.

def is_cool(name):
    if name == "Joe" or name == "John" or name == "Stephen":
        return name

# %%
# Compute whether the given year is a leap year.

###################################################
# Is leapyear formula
# Student should enter function on the next lines.
def is_leap_year(year):
    if (year % 400) == 0:
        return True
    elif (year % 100) == 0:
        return False
    elif (year % 4) == 0:
        return True
    else:
        return False

# %%
# Compute whether the given time is lunchtime.

###################################################
# Is lunchtime formula
# Student should enter function on the next lines.
def is_lunchtime(hour,is_am):
    if (hour==11 and is_am) or (hour==12 and not is_am):
        return True

# %%

# Compute whether two intervals intersect.

###################################################
# Interval intersection formula
# Student should enter function on the next lines.


def interval_intersect(a,b,c,d):
    if b>=c and d>=a:
        return True

# %%
# Compute the statement about a person's name and age, given the person's name and age.

###################################################
# Name and age formula
# Student should enter function on the next lines.

def name_and_age(name,age):
    if age>= 0:
        return "{} is {} years old.".format(name,str(age))
    else:
        return "Error: Invalid age"

def test(name, age):
    """Tests the name_and_age function."""
    
    print (name_and_age(name, age))
    
test("Joe Warren", 52)
test("Scott Rixner", 40)
test("John Greiner", -46)

# %%
# Compute and print tens and ones digit of an integer in [0,100).

###################################################
# Digits function
# Student should enter function on the next lines.

def print_digits(number):
    if number >= 0 and number<=100:
        tendigit = number//10
        onedigit = number%10
        print ("The tens digit is {}, and the ones digit is {}.".format(str(tendigit),str(onedigit)))
    else:
        print ("Error: Input is not a two-digit number.")

print_digits(42)
print_digits(99)
print_digits(5)
print_digits(459)


# %%
# Compute instructor's last name, given the first name.

###################################################
# Name lookup formula
# Student should enter function on the next lines.
def name_lookup(first_name):
    firstname = ["Joe", "Scott","John","Stephen"]
    print(first_name)
    if first_name in firstname:
        indexname = firstname.index(first_name)
        lastname = ["Warren", "Rixner","Greiner","Wong"]
        last_name = lastname[indexname]
        return last_name
    else:
        return  "Error: Not an instructor"

def test(first_name):
    """Tests the name_lookup function."""
    
    print (name_lookup(first_name))
    

test("Scott")


# %%
# Compute a (simplified) Pig Latin version of a word.

###################################################
# Pig Latin formula
def pig_latin(word):
    if word[0] in ["a","e","i","o","u"]:
        return word+"way"
    else:
        return word[1 : ]+word[0]+"ay"
    

def test(word):
    print (pig_latin(word))
    

test("pig")
test("owl")
test("python")


# %%
# Compute the smaller root of a quadratic equation.

###################################################
# Smaller quadratic root formula
# Student should enter function on the next lines.
def smaller_root(a, b, c):
    """
    Returns the smaller root of a quadratic equation with the
    given coefficients.
    """
    
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0 or a == 0:
        print ("Error: No real solutions")
    else:
        discriminant_sqrt = discriminant ** 0.5
        # Choose the positive or negative square root that leads to a smaller root.
        if a > 0:
            smaller = - discriminant_sqrt
        else:
            smaller = discriminant_sqrt
        return (-b + smaller) / (2 * a)

# %%
