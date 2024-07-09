for x in range(3,6):
    
    #space
    for z in range(x,5):
        print(" ",end="")
    
    for y in range(1,2*x):
        print("*",end="")
        
    for a in range(1,(11-2*x)):
        print(" ",end="")
        
    for b in range(1,2*x):
        print("*",end="")
        
    print()
        
    #lower
        
        
for x in range(1,9):
        
    for z in range(1,x+1):
        print(" ",end="")
        
        
    for y in range(1,(18-2*x)+1):                      #1/18  1/16  1/14  1/12
        
        
        if (x==3 or y==5):
            print("J",end="")
        elif (x==3 or y==6):
            print("I",end="")
        elif (x==3 or y==7):
            print("T",end="")
        elif (x==3 or y==8):
            print("A",end="")
        elif (x==3 or y==9):
            print("R",end="") 
        elif (x==3 or y==10):
            print("T",end="") 
        elif (x==3 or y==11):
            print("H",end="")  
        else:           
            print("*",end="")
        
    print()
    
    
    
for x in range(1,6):
    
    for y in range(1,6):
        if x==1 or x==5 or y==1 or y==5 :
            print("* ",end="")
        else:
            print("  ",end="")
        
    print()
    
    
for x in range(1,8):
    for y in range(1,x+1):
        if x==7 or  y==1 or y==x:
            print("*",end="")
        else:
            print(" ",end="")
        
    print()
    
    
    
for x in range(1,6):
    for z in range(x,6):
        print(" ",end="")
        
    for y in range(1,x+1):
        if x==1 or x==5 or y==1 or y==5 or y==x:
            print("* ",end="")
            
        else:
            print("  ",end="")
        
    print()
    
print()
        
#inverted triangle

for x in range(1,6):
    for y in range(x,6):
        print("* ",end="")
        
    print() 
    
    
print()  

#12. Hollow Inverted Right Triangle Pattern

for x in range(1,6):
    for y in range(x,6):
        if x==1 or x==5 or y==1 or y==5 or y==x:
            print("*",end="")
        else:
            print(" ",end="")
            
    print()
    
print()

#Mirrored Inverted Right Triangle

for x in range(1,6):
    
    for z in range(1,x+1):
        print(" ",end="")
        
    for y in range(x,6):
        print("*",end="")
    
    print()
    
print()


for x in range(1,6):
    
    for z in range(1,x+1):
        print(" ",end="")
        
    for  y in range(x,6):
        if x==1 or x==5 or y==1 or y==5 or y==x:
            print("*",end="")
            
        else:
            print(" ",end="")
            
    print()
    
print()


# Pyramid Pattern

for x in range(1,6):
    
    for z in range(x,6):
        print(" ",end="")
    for y in range(1,2*x):           #1/1  2/3  3/5  4/7  5/9 
        print("*",end="")
        
    print()
    
print()


# pyramid and hollow
for x in range(1,6):
    
    for z in range(x,6):
        print(" ",end="")
    for y in range(1,2*x):
        if x==1 or x==5 or y== or y==5:
            print("*",end="")
        else:
            print(" ",end="")
        
    print()


                                            
        


