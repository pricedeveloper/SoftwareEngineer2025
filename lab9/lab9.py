"""
Paula Rice
April 24 - Conditional Statement
"""

print(f"\n------ Example 1 and 2: if Statement ------")
age = 20
agecode = 123

if age>= 21:
    print("You are an adult!")
    agecode = 200
else:
    print("You are under 21!")
    agecode = 100

print(f"After the 'if' statement, ageceode = {agecode}")

print(f"\n------ Example 3: Multiple Statements ------")
age = 50
if 0 <= age < 21:
    print("You are a minor!")
elif 21 <= age < 65:
    print("You are a senior citizen")
elif 65 <= age <= 130:
    print("You are a senior citizen")
else:
    print("unable to read age!")

print(f"\n------ Example 4: 'And' Operator' ------")
temperature = 80
humidity = 100

if 70 <= temperature <= 90 and humidity < 80:
    print("The weather is pleasant")
else:
    print("The weather is not ideal")

print(f"\n------ Example 5: 'Or' Operator' ------")
day = "Momday"
is_holiday = True

if day == "Saturday" or day == "Sunday" or is_holiday:
    print("You can relax today!")
else:
    print("It is a workday")

print(f"\n------ Example 6: 'Nested' Conditional Statement------")
number = int(input( "Enter a number:  "))
if (number >= 0):
    if number == 0:
        print("The number is zero")
    else:
        print(f"{number} is positive")
else:
        print(f"{number} is negative")

print(f"\n------ Example 7: 'Username' Validation'------")
#username validation. username numst have 3+ characters
username = input( "Enter a username:  ")
username = username.strip()
len_username = len(username)
if len_username >= 3:
    print(f"{username} has 3+ characters")
    index_whitespace = username.find(" ")
    if index_whitespace == -1:
        print (f"{username} is valid.")
    else:
        print(f"Username CANNOT have whitespace")
else:
    print(f"{username} is INVALID. Username must have 3+ characters")

print(f"\n------ Example 8: Match-Case Statememt------")
response_code = 404

match response_code:
    case 400:
        print(f"Code = {response_code}. Server CANNOT understand")
    case 401 | 403:
        print(f"Code = {response_code}. Server refuse to send back")
    case 404:
        print(f"Code = {response_code}. Server can't find")
    case _:
        print(f"INVALID CODE")

print(f"\n------ Example 9: Lab Exercise------")
print("GPA Calculator")
print("Enter your grades to calculate your GPA")

grade1 = float(input("Enter your first grade: "))
grade2 = float(input("Enter your second grade: "))

average = (grade1 + grade2) / 2

if 90 <= average <= 100:
    gpa = "A"
    print(f"For the average of {(grade1 + grade2) / 2}, your GPA is {gpa}")
    print("Way to go!")
elif 70 <= average < 90:
    gpa = "B"
    print(f"For the average of {(grade1 + grade2) / 2}, your GPA is {gpa}")
    print("Good job!")
elif 60 <= average < 70:
    gpa = "C"
    print(f"For the average of {(grade1 + grade2) / 2}, your GPA is {gpa}")
    print("You passed.")
elif 0 <= average < 60:
    gpa = "FAIL!"
    print(f"For the average of {(grade1 + grade2) / 2}, your GPA is {gpa}")
    print("Your grade needs improvement")
else:
    gpa = "UNDEFINED!"
    print(f"For the average of {(grade1 + grade2) / 2}, your GPA is {gpa}")
    print("The average is outside of the range (0-100).")
