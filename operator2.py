# Comparison operator.
# These compare two values and return a boolean.
num1, num2 = 100, 200

print(num1<num2)
print(num1>num2)

print(num1>=num2) 
print(num1<=num2)

print(num1==num2)
#This is how we say not equal to.
print(num1!=num2)

# Logical operators.

#We have and, or, not=(&,|,!)
log1, log2 = 5, 6
print((log1>log2) & (log2<log1))
print((log1>log2) and (log2<log1))
# We use & when all statements are true.

print(not (log1>log2))

# We use not when we want to reverse the truth value of a statement.

print((log1>log2) or (log2<log1))
print((log1>log2) | (log2<log1))

print(True and True)

print(True and False)
print(True or True)

print(False or False)

print(not True)
print(not False)

# or is when one of the statements is true.
# and is when all of the statements are true.
#not is when the statements is true.

# Membership operators. here we only have is and not.
mem = (20,30,40,50)
print(20 in mem)
print(20 not in mem)

name = "Ozzy"

print("o" in name)
print("o" not in name)
print("O" in name)
print("O" not in name)

# Identity operators.

a = 10
b = 10
print(a is b)
print(a is not b)

a = [10,20,30]
b = [1,2,3]
print(a is b)
print(a is not b)


