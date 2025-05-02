"""
Paula Rice
April 25 Python Loops
"""
print("\n ------ 'for' Loop as a counter -------")
# print Hello from 0 to 4
for x in range(0,5):
    print(f"Hello = {x}")

print("\n ------ Example 2: for loop in a list ------")
fruits = ['apples', 'oranges', 'grapes', 'kiwis', 'pineapple']
for eachfruitindex in range(0, len(fruits)):
    print (f"fruit with index {eachfruitindex} = {fruits[eachfruitindex]}")

    # alternative way to loop through a list
    print("\n --- Alternative way to loop through a list")
    for eachfruit in fruits:
        print(eachfruit)

print("\n ------ Example 3: 'for' loop with different increments ------")
# for loop to print from 2 to 30, with an increment of 2
for num in range(2,30,3):
    print(num)

print("\n ------ Example 4: 'for' loop  with different decrements ------")
# for loop to print from 10 to 0 with a decrement of 2
for num in range(10,0,-2):
    print(num)

print("\n ------ Example 5: 'for' loop through a string ------")
username = "yes123"
for eachcharacter in username:
        print (eachcharacter)


print("\n ------ Example 6 'for' nested conditional statement------")
# for loop to check how many negative numbers are in the list
numbers = [5, -2, 0, 8, 9, -1]
negativecoundter = 0
for eachnumber in numbers:
    if eachnumber < 0:
        negativecoundter += 1 # the same as negative mubmer = negativenumber + 1

# prompt result
print(f"There is/are {negativecoundter} negative number/s")

print("\n ------ Example 7: Nested condtional Statement: Operation -----")
# for loop to add all 'odd numbers
sumodd = 0
for eachnumber in numbers:
    if eachnumber %2 == 1:
        sumodd += eachnumber

        #prompt results
        print(f"The sum of all odd numbers is = {sumodd}")

print("\n ------ Example 8: Break and Continue Statement in a Loop-----")
# for loop to print from 9 to tend exclsive (10 will not be shown) and terminate the loop when it reaches 5
for n in range(0,10):
    if n == 5:
        print("counter reaches to 5")
        break
    else:
        print(n)

print("\n ------ Example 9: Continue Statement in a Loop-----")
# for loop to add numbers from 0-10(exclusive), except number 5
sumall = 0
for n in range(10):
    if n == 5:
        print("skipping 5")
        continue

    sumall += n
    print(n)
    print(f"\tsum = {sumall}")

print("\n ------ Example 10: Else Statement in a 'for' Loop-----")
for n in range(6):
    if (n == 3):
        break
    print(n)
else:
    print("Loop completed")

print("\n ------ Example 11: 'While' loop as a counter ----")
# print 0 to five and include the five
n = 0
while n<6:
    print(n)
    n += 1

print("\n ------ Example 12: 'While' loop as a checkpoint ----")
# while loop to collect and add numbers between -5 and 5
# if the user enters a number that is not between -5 and 5, then the while loop terminates.
sumusernumber = 0
while(True):
    number = int(input("Enter a number between -5 and 5: "))
    if number <-5 or number >5: 
        break
    sumusernumber += number

#prompt the results
print(f"The total sum is = {sumusernumber}")

print("\n ------ Example 13 'While' loop as a counting operator ----")
# While loop to count the even number in the list
numbers = [2, 0, -5, 8, -6, 7, -3]
index = 0
len_numbers = len(numbers)
evencount = 0
while index < len_numbers:
    if numbers [index]%2 == 0 and not (numbers[index] == 0):
        evencount += 1
    index += 1
else:
    print (f"There is/are {evencount} even numbers")


