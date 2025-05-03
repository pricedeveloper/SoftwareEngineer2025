"""Paula Rice
April 27, Functions
"""
#import 'math' module
import math

# Example 3
def greeting():
    print("Welcome to Functions")

# Example 4 Function with parameter "username"
def printusername(username):
    print(f"Welcome to function {username}")

# Example 5 Function with default parameters
def user_country(username = ("John Doe"), country = "unknown country"):
    print(f"{username} is living in {country}")
    return #return empty is a voic

# Example 6: Function that Returns A Value
# function that takes two number and return the product
def product (n1, n2=1):
    return n1*n2

# Example 7: Boolean Function
# Function to check if a number is a multiple of 3
def multiple3(n):
    if n%3 == 0 and n!=0:
        return True
    else:
        return False

# Example 8: Compensation functioon
# Define fuunction to collect, validate and return a number between 1 and 8
def collectnum():
    n = float(input("Enter a number between 1 and 9(inclusive)"))
    # validate the number
    while(not(1 <=n <=9)):
        n = float(input("Re-enter a number again: "))
    return n

# Function that adds 'totalnumber3' amount of numbers and returns the sum of the numbers
def sumnumbers(totalnumbers=0):
        sum = 0
        for n in range(totalnumbers):
            sum += collectnum()  # composition function
        return sum

# Function to print result
def printresult(totalsum):
    print(f"Sum of all nuumbers is = {totalsum}")

# Example 9: Math bult-in functions
# define a function to calculate and return the areea of a circle
# forumula = radius ^2 pi
def areacircle(radius):
    a = math.pow(radius,2) * math.pi
    return round (a,2)

#function to print result
def areaprint(area, radius=0):
    print(f"The area of the circle with {radius} radius is {area}")

# Example 10
#Function to return the ratio of two numbers (hours)
def ratio_hour(hour):
    try:
        dayhour = 24
        r = dayhour/hour
    except ZeroDivisionError:
        print('ZERO EXCEPTION')
        print("number can't be divided by zero")
        return 0
    except ValueError:
        print('VALUE EXCEPTION')
        print("Number was not provided")
        return 0
    except:
        print('GENERAL EXCEPTION')
        print("There was an error in the division")
    else:
        print('DIVISION IS FINE')
        return r
    finally:
        print(" ------- Process completed! ------")

# Example 11: Classes
# defining a class name"MyClass"
class Myclass:
    # property (attribute)
    id = 12345

    # method
    def msg(self):
        return "Welcome to Python Class"

# Example 12:
class Complexnumber():
    #instantiate of the class
    def __init__(self, realnumber, imgnumber):
        self.r = realnumber
        self.i = imgnumber

# Example 13: 
class Car:
    # instantiate of the class
    def __init__(self, make, model, year):
        self.carmake = make
        self.carmodel = model
        self.caryear = year

    # set property 'odometer'
    odometer_reading = 0

    # method to return 'description of the car
    def get_car_description(self):
        return f"{self.carmake} model {self.carmodel} was made on {self.caryear}"

    # method to read the odometer
    def read_odometer(self):
        return f"This car has {self.odometer_reading} miles on it"

    # method to update the odometer
    def update_odometer(self, mileage):
        if mileage > self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('Odometer CAN\'T roll back')

    # method to add miles into the odometer
    def increment_odometer(self,miles):
        if miles >0:
            self.odometer_reading += miles
        else:
            print("Can't add negative miles")


