for x in range (0,11):
    print(x)
    
  
 
   
for x in range (0,20,2):
    print(x)
    
sum = 0

for x in range (0,100):
    sum=sum+x
print("sum of value ",sum)

sum=0
for x in range(0,15):
    sum=sum=x*x
print("sum of square ",sum)

sum=0
for x in range(0,15):
    sum=sum=x*x*x
print("sum of square ",sum)

values=[3,5,7,9,11]
for x in values:
    print(x)
    
# find 9 position 
values=[3,5,7,9,11]
for x in values:
    if x==9:
        print("9 position is ",values.index(x))
        
        
#while for loop
i = 1
while i<=10:
    print(i)
    i+=1
    
    
for i in range(1,11):
    print(i)
    
#check whether the number is prime or not
#2,3,4,5,7,11...

#num = int(input("enter number to check prime or not :"))

#if num<2:
    print("not prime")
#else:
    
 #   flag = 0
    
  #  for i in range(2,num):
   #     if (num % i==0):
    ##       break
        
        
    #if(flag==0):
     #   print("prime number")
    #else:
     #   print("not prime number") 
        #big number divided by small number then it is a prime or else not prime
        
        
#find number of vowel consonant or symbol or number inside a string

#str = input("enter the string : ")

#v =0
#c =0
#d =0
#s =0
#vowels =["a","e","i","o","u","A","E","I","O","U"] 

#for i in str:
 #   if(i.isalpha()):
        
  #      if(i in vowels):
   #         v = v+1
    #    else:
     #       c = c+1
            
    #elif(i.isdigit()):
     #   d = d +1
        
    #else:
     #   s = s+1
        
#print(f"vowel are : {v}\nConsonents are : {c}\nDigits are : {d}\nSymbols are : {s}")

# conversion of decimal to binary

i = int(input("Enter decimal number: "))
binary = " "
list = []
original = i



while i !=0:
    reminder = i%2
    list.append(reminder)
    i = i//2
    
list.reverse()

for i in list:
    binary = binary + str(i)
    
print(int(binary))
print(bin(original).replace("0b", " "))


#convert binary into decimal

mybin = int(input("enter binary number: "))
list = []
decimal = 0
while mybin!=0:
    reminder = mybin%10
    list.append(reminder)
    mybin = mybin//10
    
for i in range(0,len(list)):
    decimal = decimal + list[i]*(2**i)
    
print(f"decimal value is: {decimal}")



    
    
    
           
    