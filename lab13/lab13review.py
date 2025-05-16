""" 
Paula Rice
May 4, 2025 Python "Classes"
"""
# Example 1 - Review of _init_ & __string__
print("\n---- Example 1 -----")
class Person:
    def __init__(self, name, age):
        self.username = name
        self.user_age = age

    def __string__(self):
        return f"Username = {self.username}\nUser age = {self.user_age}"

    # Method
    def intro(self):
        return f"Hello! I am {self.username}"

# create an object of the class
user1 = Person("Peter", 23)
print(user1.intro())

# Example 2, Private Properties
print("\n ---- Example 2 ----")
class Chair:
# Accesible Property
    chair_color = "brown"

    def __init__(self, height, width, length):
        self.chairheight = height
        self.__width = width # __ makes property 'width' to be very private
        self.chairlength = length*2

    # methotd to pass the length
    def pass_length(self):
        return self.chairlength

    # method to return the volume of the chair
    def chair_volume(self):
        return self.chairheight * self.chairlength * self.__width

    #method to return the color of the chair
    def get_color(self):
        return self.chair_color
        
    # method to return the desciption of the chair
    def chair_description(self):
        return f"The total wolume of the chair {self.chair_volume()}. The chair color is {self.get_color()}"

    # method with a private property ( private use one underscore;very private two underscores)
    def setprice(self,price):
        self._chairprice = price

# Create an object
userchair1 = Chair(2,5,9)
print(f"The chair length is = {userchair1.chairlength}")
print(f"The chair width is = {userchair1._Chair__width}") # <== way to call very private property
# call method pass_length
print(f"The chair has a length = {userchair1.pass_length()}")
print (f"The chair volume is = {userchair1.chair_volume()} ")
print(userchair1.chair_description())
# call private method
userchair1.setprice(25)
print(f"The price of the chair is $ {userchair1._chairprice}")