#name = (input("enter the name:"))

#print(name)
#print(type(name))

#num1 = int(input("enter first number:"))
#num2 = int(input("enter second number:"))
#x = [num1+num2]
#print("total marks:" +str(x))

#num1 = int(input("enter the first number: "))

#num2 = int(input("enter the second number: "))


#print("addition:" + str(num1 + num2))
#print("substraction:" + str(num1 - num2))
#print("multiplication:" + str(num1 * num2))
#print("division:" + str(num1 / num2))
#write the program of finding the perimeter
#n1 = int(input("length of rectangle: "))
#n2 = int(input("breadth of the rectangle: "))

#n3 = 2*(n1 + n2)
#print("perimeter of rectangle:" + str(n3))

#to find its area
#n3 = n1 * n2
#print("area of reactangle:" + str(n3))

#calculate the radius,diameter,circumference and area

#circle = int(input("enter the number: "))

#print("radius: " + str(circle/2))
#print("diameter: " + str(2*circle))

#convert = int(input("enter the lenght in centimeter: "))

#print("in meters: " + str(convert/100))
#print("in kilometers: " + str(convert/10000))


#num = float(input("enter into celsius: "))
#h = (9/5)*num + 32
#print("in fahrenheit:" + str(h))

#g = num+32*(5/9)
#fahrenheit = float(input("enter into fahrenheit:"))

#print("in celsius: " + str(g))

#find the armstrong number

#num = int(input("Enter one number: "))
#original = num
#another = num

#count = 0


#while num!=0:
 #   count +=1
  #  num = num//10
    
#print(f"no of Digit is: {count}")

#sum = 0 

#while original!=0:
 #   last = original % 10
    
  #  sum = sum + pow(last,count)
   # original = original //10


#if another == sum:
 #   print("Number is Armstrong: ")
#else:
 #   print("Number is not Armstrong: ")
    
    
#find first number and last number of digit

n = int(input("enter the digit of number: "))
first_digit = n
last_digit = n % 10 

             

   
while first_digit > 9:
    first_digit = first_digit // 10
print(f"enter the first number {n}: {first_digit}")
print(f"enter the last number{n}: {last_digit}") 

n = int(input("enter the decimal: "))
i = 1
while n!=0:
    reminder = n % 2
    list.append(reminder)
    reminder = n // 2
    n = n //2
    
for n in list:
    
    print(reminder,end="")
      
         
