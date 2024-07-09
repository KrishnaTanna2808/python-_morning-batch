#return type of fuction

def display(a):
    print(a)
    
display(12)

def multi(x,y):
    return x*y      #function gives us value agter completing
x = multi(12,29)
print(x)
print(multi(10,30))

z = 12 + multi(12,10)     #function as value

#alone return

def play(x,y):
    print(f"x is {x} and y is {y}")
    
    return x/y
print(play(23,10))
print(type(play(10,20)))


def goa(a,b):
    if a<b:
         print("budget nathi")
        
    else:
       print("kem cho")

print(goa(10,8))
    
print(type(goa(10,20)))   
    