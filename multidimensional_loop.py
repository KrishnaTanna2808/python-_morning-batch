for x in range(1,6):
    for y in range(1,6):
        print('*', end="")
    print()
    
    
    
    
for x in range(1,6):
    for y in range(1,x+1):
        print(f"{y} ",end="")
    print()
    
    
for x in range(1,6):
    for y in range(1,6):
        if (x==1 or x==5 or y==1 or y==5):
            print("* ",end="")
        else:
            print("  ",end="")
    print()
    
    
for x in range(1,6):
    for y in range(1,6):
        if (x==y or x+y==6):
            print("* ",end="")
        else:
            print("  ",end="")
    print()
    
print()   

for x in range(1,6):
    
    for z in (range(x,5)):
        print("  ",end="")
    
    for y in range(1,x+1):
        print("* " ,end="")
        
    print()
    
print() 
    
    
for x in range(1,6):
    
    for z in range(x,6):
        print("* ",end="")
        
    for y in range(1,x+1):
        print("  ",end="") 
        
    print() 
    
    
for x in range(1,6):
    
    for z in range(1,x):
        print("  ",end="")
        
    for y in range(x,6):
        print("* ",end="")
        
        
    print()
