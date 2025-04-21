print('\n----Example 5: Input Command ----')
print("Paula Rice")
username = input()
print(f"Collected username ={username}")

luckynumber = input("Enter a lucky number: ")
print(f"Lucky Numeber ={luckynumber}")

# Cast from string to integer
luckynumber = int(input("Enter a lucky number: "))

#double the lucky number
dblucky = luckynumber*2
print(f"Double of lucky = (dblucky )")

# Cast ineger (cor float) into a string
triplenumber = str(dbluckey) * 3
print(f"(tripled the casted number ={triplenumber}")

# cast integer to bool value
# zero is equal to False, any other number = True
completed_task = 0
print(f"completed task = {bool(completed_task)}")

#Order of operations (PEDMAS)

pring('\n---- Exasmple 6: Artithmetic Operators')
num1 = 5
numb2 = 9

print(f"he sum of {num1} and {numb2} is {num1+nm2}")
print(f"The difference between {num1} and {num2} is {num1-num2}")
print(f"The product of {num1} and {numb2} is {num1xnum2} ")




print('\n---- Example7: Finding the Hyopotues----')
#declare and assign valuues
x = float(input("Enter side 1: "))
y = float(input("Enter side 2: "))
# Caculate the Hyoputenuse
hyp = (x**2 + y**2)**0.5
# prompt result
print(f"The hypotenuse of {x:0.1f} and {y:0.1f} is {hyp:0.2f}")

print('\n---- Example 8: Assignment Operators ------')
#assign and operator to a variable that has an operator
n = 2
print(f"number =        {}")
#assignment operate +
n +=3
print(f"updated  + number = {n}")
#assignment operator -
n -=4
print(f"updated - number = {n}")
#assignment operator for multiplication (x)
n *=2
print(f"updated * number = {n}")
#