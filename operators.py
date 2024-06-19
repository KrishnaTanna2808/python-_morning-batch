#symbols
#+ - / * %
# ** exponentional
# // floor division

a =12
b = 7

print(a**b)

print(a//b)

a = 12
a +=12
a %=10 #4565
print(a)

print(a:=4)

#membership operator

print(12 in range(13,45))
print(12 not in range(13,45))

list=[2,3,46,75,8,73,957,'car']
print('car' in list)

print(56 in list)

#assignment operators
#= += -= *= /= //= **=

#logical operator
#and or not
a = 34
print(not a>5)

#identity operator
#is is not
a = 5
b = 5
print(a is b)
print(a is not b)
print(a == b)
print(a != b)
print(type(a))
print(type(a) is int)

#what else can i do in is operators
#is operator checks if both variables are pointing to the same object in memory
a = [1,2,3]
b = [1,2,3]
print(a is b) #false because they are different objects in memory
print(a == b) #true because they have the same value
a = b
print(a is b) #true because they are pointing to the same object in memory

