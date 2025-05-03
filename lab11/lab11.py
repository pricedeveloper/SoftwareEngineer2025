"""
Paula Rice
Lab 11
April 27, 2025
"""

# import all from files "lab11_funtions"
from lab11_functions import *

# import the 'math' module
import math 

print("\n ------ Example 1: Python Dictionary ------")
# create a dictionary
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }
    # print a complete dictionary
print(car)
    # to access items in a dictionary we use [], goes the key's name
    # update the value of the key
car["year"] = 1980
print(f"The year of the car was updated to = {car["year"]}")
print(f"The year of the car was updated to = ", car["year"])
# add key:value pair
car["color"] = "red"
print(car)
print("\nloop through each key in the dictionary")
for k in car:
    print (k)
print("\nloop through each value in the dictionary")
for k in car:
    print(car[k])
print("\nloop through each pair in the dicfionary")
for k in car:
    print(f"{k} has value = {car[k]}")

print("\n ------ Example 2: Python Dictionary Application ------")
#given the following list, crate a dictionary test that will count the number of items a word appears in the string.
# create a diction to organize the words as the keys, and the number of occurency of the wor as the value of the key.
phrase = "to be or not to be"
phrase_split =phrase.split()
print(f"original phrase = {phrase}")
phrase_split = phrase.split()
print(f"splitted phrase = {phrase_split}")
# create the dictionary
word_count_dict = {}
# loop for each word in the list
for word in phrase_split:
    print(word)
    if word in word_count_dict:
        word_count_dict[word] += 1
    else:
        word_count_dict[word] = 1
# loop to print the result
print("Result of dictionary: ")
for w in word_count_dict:
    print(f"{w} = \t{word_count_dict[w]}")

print("\n ------ Example 3: Function That Does Not Return Values ------")
# run function 'greeting'
greeting()

print("\n----- Example 4: Function with parameters -----")
# call function 'printusername'
printusername("peter pan")
printusername("Price")

print("\n ------ Example 5: Functions with Defaut Parameters ------")
user_country("Martha", "Chile")
user_country("Anna")
user_country(" ", "France")

print("\n ------ Example 6: Functions with Return Values ------")
num1 = 2
num2 = -6
prod1 = product(num1, num2)
print(f"The product of {num1} and {num2} is = {prod1}")
prod1 = product(num1)
print(f"The produc is = {prod1}")

print("\n ------ Example 7: Boolean Functions (True/False) ------")
checknum1 = multiple3(num1)
checknum2 = multiple3(num2)
print(f"Is {num1} multiple3? {checknum1}")
print(f"Is {num2} multiple3? {checknum1}")

print("\n ------ Example 8: Compostion Function ------")
# test collectnum()
# number = collection()
# print(number)
# test sumnumbers()
# sumall = sumnumbers(3)
# print(sumall)
sumall = sumnumbers(3)
printresult(sumall)

print("\n ------ Example 9: Math Built-in ------")
r = 2
a = areacircle(r)
areaprint(a,r)

print("\n ------ Example 10: Math Built-in ------")
#ratio = ratio_hour(0)
#print (ratio)
#try:
  #  ration = ratio_hour()
#except:
 #   print("Error wit the function")
#print(ratio)
r1 = ratio_hour(0)
r2 = ratio_hour(3)
r3 = ratio_hour("Peter")

print("\n ------ Example 11: Classes ------")
# create an instance of the class
user1 = Myclass()
print(f"An instance of the class = {user1}")
# call the class property
user1id = user1.id
print(f"user 1 id = {user1id}")
# call the class method
user1msg = user1.msg()
print(f"user 1 message = {user1msg}")

print("\n ------ Example 12: Instantiation Classes ------")
# create an instant of the class (create a blueprint)
paircomplexnumber = Complexnumber(2, 3)
# call for the instance object of the class "r"
real = paircomplexnumber.r
print(f"The real part is (real)")

print("\n ------ Example 13: Application Classes ------")
# create an instance of the class
car1 = Car("Tesla", "S", 2023)

# call property odometer_reading
car_reading = car1.odometer_reading
print(f"Car miles reading = {car_reading}")
# call method 'get_car_description'
print(car1.get_car_description() )
# call method "read_odometer"
print(car1.read_odometer())
# update the mileage to  = 10
car1.update_odometer(10)
print(car1.read_odometer())
car1.update_odometer(5)
print(car1.read_odometer())
# add 20 miles to the odometer
car1.increment_odometer(20)
print(car1.read_odometer())
car1.increment_odometer(-5)
print(car1.read_odometer())
car1.increment_odometer(8)
print(car1.read_odometer())