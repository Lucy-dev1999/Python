#All theses are static functions. They have hard-coded values.su
def add():
    var1, var2 = 60, 70
    return var1 + var2
# return exposes a value to be accessed out of the function.

print(add())
#we are printing the value exposed in the function add.

mynum = add()
print(mynum)

def sub():
    var1, var2 = 60, 70
    return var2- var1

print(sub())

def both():
    var1, var2 = 60, 70
    return sub() + add()

print(both())

def add1():
    var3 = int(input("please enter a number"))
    var4 = int(input("please enter another number"))
    return var3 + var4

print(add1())

def sub1():
    var3 = int(input("please enter a number"))
    var4 = int(input("please enter another number"))
    return var3 - var4

print(sub1())

def both1():
    return sub1() + add()

print(both1())





























"""def mult():
    var1, var2 = 60, 70
    return var1 * var2

print(mult())

def div():
    var1, var2 = 60, 70
    return var1 / var2

print(div())

def mod():
    var1, var2 = 60, 70
    return var1 % var2

print(mod())

def power():
    var1, var2 = 60, 70
    return var1 ** var2

print(power())

def floor_div():
    var1, var2 = 60, 70
    return var1 // var2

print(floor_div())

def round_div():
    var1, var2 = 60, 70
    return round(var1 / var2)

print(round_div())

def round_power():
    var1, var2 = 60, 70
    return round(var1 ** var2)

print(round_power())

def round_floor_div():
    var1, var2 = 60, 70
    return round(var1 // var2)

print(round_floor_div())"""
