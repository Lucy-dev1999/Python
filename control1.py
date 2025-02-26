#code/program to interpret.
num1 = int(input("input your first number"))
num2 = int(input("input your second number"))
#
#operator = input("choose the operator")

if num1 >= num2:
   print(f"Error: First number {num1} should be less than the second number {num2}.")
#
if num1 % num2 == 0:
   print(f"{num1} is divisible by {num2}")
#  
if num1 != 0:
    num2 += num1
    print(num2)