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
    
    
    
    
    
    
    