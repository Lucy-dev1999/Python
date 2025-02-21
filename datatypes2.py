# Sequence.
num1, num2, num3, = 100, 300, 500.# this has three statements so it means they will have different locations hence wastage of memory.
numbers = [100, 300, 500]# now this stores all the variables in one memory space.
numbers1 = [num1, num2, num3]
numbers2 = []
my_things = [100,"hello",300.0, True, [1, 2, 3, 4]]
print(type(numbers2))
print(type(numbers1))
print(type(num1))
print(type(my_things))
print(numbers[0]) # accessing the first element in the list.
print(numbers1[2]) # accessing the third element in the list.
print(my_things[1]) # accessing the second element in the list
print(my_things [4][2])
# in python a variable assigned more than one value is callad a list and it is identified by square brackets.eg.line 3.
# the first value in the list is in position 0.
trouble = [20, [30,[100,20,[500]]]]
print(trouble[1][1][2][0])
trouble.append(40)
print(trouble)
trouble.pop()
print(trouble)
#tuple
mytuple = (100,300,500)
print(mytuple)