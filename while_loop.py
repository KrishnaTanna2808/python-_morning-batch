#while and for loop
#to do a repetative task

#initial value, comdition, increment / decrement

i = 1
while i <= 10: #condition
    print(i)
    i = i+1 # this is increment and decrement
i = 1

# print 1...100 natural number
while i<=100:
    print(i)
    i+=1  
    
#print 1...100 even number
i = 2
while i <= 100:
    print(i)
    i+=2
    
    #or
    
i=1
while i <= 100:
    if i % 2 == 0:
        print(i,end= ' ,' )
    i+=1 # indentation
    
 
print() # to print in a new line
 
        
#break  and continue
i=1
while i <= 5:
    if (i==3):
        break #stop the loop
    print(i)
    i+=1
    
    
    
i=1
while i <= 5:
    if (i==3):
        i+=1
        continue
    print(i,end=' ')
    i+=1
    
#print odd number between 1...100

print()


i =1
while i <= 100:
    if i %2 != 0:
        print(i, end=' ')
    i+=1
    
    
#print number between 1..100 which is divisible by 5 and 11
print()

i = 1
while i<= 100:
    if i % 5 == 0 and i % 11 == 0:
        print(i, end=' ,')
    i+=1
    
print()

# print the sum of all number between 1...100
sum = int(input("enter the number:"))
i = 1
while i <= sum:
    print(i, end=' + ')
    i+=1

    
    
#print n table using while taking user input
n = int(input("enter the number:"))
i = 1
while i <=10:
    print(f"{n} * {i} = {n*i}")
    i += 1
    

#find no. of digit in number 56790

num1 = int(input("please enter the number: "))
duplicate = num1
count =0
while num1!=0:
    num1 = num1//10
    count +=1
print(f"no of digit in{duplicate} is {count}")

#find the reverse the number and palindrome         3456

v = int(input("enter the palindrome number"))
duplicate = v
rev = 0


while v!=0:
    last_digit = v %10
    rev = rev*10 + last_digit
    v//=10
print(f"reverse of number is{rev}")

#palindrome or not

print(f"{duplicate} is {'palindrome' if duplicate==rev else'not palindrome'}")





    
    
    
    
    
    
    