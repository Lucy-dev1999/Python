number = int(input ("number of entries"))
dict = {input("enter key: "): input ("enter value.")for _ in range(number)}
# we are trying to create a dictionary but the user is the one to put in the details.
print(dict)

# defining a function
def enter_number():
    enter_number = int(input ("number of entries: ")) 
    capture = {input("enter key: "): input ("enter value.")for _ in range(number)}
    print(capture)
#
print (enter_number)