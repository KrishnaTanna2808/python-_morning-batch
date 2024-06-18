# str
a = "bascom"


print(type(a))

a =12.234
print(type(a))

a=23

print(type(a))

a = 12+2j

print(type(a))

value=[12,'hello',12.34]

print(value)# list is a mutable

print(value[2])
print(type(value))

value[2]=67
print(value)

print(value[0:3])

value.append("krishna") #if you want to add new value in list , use append function

print(value)

value.insert(2,5.7) #if we want to add some values inbetween the value then use insert (index,value)


value.remove('krishna')
 
print(value)

value.remove(value[3])

print(value)

del value[2]

print(value)

data = [12,15,'hello',24.34]

new_data = data[1:4] #part range reassign

print(new_data)

print(type(new_data))

f = data[2]
print(type(f))
list1=[1,2,45.45]
list2=[7,7,9,9]

list3=list1+list2

print(list3)

#tuple nonmutable used to store the information that is does not need to alter over tab

fruit = (23,76,'hello')
print(fruit)
print(type(fruit))


x = range(8) #used for loops
print(x)

#dictionary
#key : value

employee = {"name":"krishna",
            "email" : "krishna.123@gmail.com", 
            "address": "satellite",
            3 : "hello"}
print(employee)
print(type(employee))

name = []  #empty list // append // insert
addresses = {} #empty dictionary

print(employee[3])

employee[3] = "hi"   #directry value re assign
print(employee[3])

mydata = {}
mydata.update({"first_name" : "krishna"})

employee.update({"age" : "25"})
print(mydata)
print(employee)


employee.pop("age")
print(employee)

employee.popitem()  #it remove the last list or last item of key and value
print(employee)

del employee["address"]
print(employee)

employee.clear() #empty the value and key of dictionary

#del employee #delete the variable

print(employee)

#set datatype #do not change the value but we can add and remove, but it not change the existing 
#value like first it was hello,then we update again hello it will not take 

voo = {"hello", 23, 45,56.56}  #unorder

print(voo)

print(type(voo))
voo.add('coco')#add new item

print(voo)

voo.add('hello')
print(voo)
#voo.remove(voo[1])

voo.remove(23)
print(voo)
print(len(voo))  #find the length

#frozenset function
my_list = [1,4,8,89.9,'hello']
my_new_list = frozenset(my_list)
print(my_list)
print(type(my_list))
print(my_new_list)
print(type(my_new_list)) #frozenset freeze the value and does not aLLOW TO crud operation

#boolean datatype
islogin = 1
print(bool(islogin))

my_expression = 12<14
print(my_expression)
my_expression = 10 < 9
print(my_expression)
print(type(my_expression))

#none
x=None
print(x)
print(type(x))



