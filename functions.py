def add():
    a, b = 20, 40
    print(a + b)
add()  

def add1():
    a =(input("please enter your first name:\n"))
    b =(input("please enter your second name:\n"))
    print(a + b)
add1()

def add2():
    a = int(input("please enter your first number\n"))
    b = int(input("please enter your second number\n"))
    if a % b == 0:
       print(a + b)
       print(f"{a} is divisible by {b}")
       print(f"{a} doesnot give a remainder ")
    else:
        print(f"{a} does give a remainder ")
add2()












