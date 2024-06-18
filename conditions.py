#operators
#symbolys
#< > <= >= != ==
#a = b is a assign operators
a = 12
b = 13


#if else all opreators give boolean value

if a > b:
    print("a is greater than b")
else:
    print("a is less than b ")
    
x = 10
y = 20

#casting (int is converted into string )basically type int<float<confir<string 
# there are two type of casting 1. implicit and explicit

#if, elif, else

x =34
y =56
if x<y:
    print("x is less than y")
elif x==y:
    print("x is equal to y")
else:
    print("x ix greater than y")    
    
    
#nested if


#find max 3 values
a =34
b =45
c =14


if a>b:
    if a>c:
        print("a is max")
    else:
        print("c is max")
else:#a<b
    if b<c:
        print("c is max")
    else:
        print("b is max")
        
#take input from user        
a = int(input("enter a number =>"))
print(a)
print(type(a)) 

#check whether the number is even or odd

num = int(input("please enter number : "))
if num%2==0:
   print("even number")
else:
    print("odd number")
    
# check where the number is between 0..100

num = int(input("enter number to check in range ;"))

#if 0<=num<=100
#if 0<=num and num<=100:
if num in range(0,100):
    print("in range")
else:
    print("outrange")  
    
      

 
    