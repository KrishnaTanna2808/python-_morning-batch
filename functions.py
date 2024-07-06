#what is a functions
#function is a block of code that runs when we call it
#function can be call multiple time
#reduce the boilerplate code

def python_batch():
    print("this is coming from function") # defination of function 

python_batch()   #calling the function


def my_sum(a,b):
    print(a+b)
    
    
my_sum(12,13)
my_sum(15,13)
my_sum(17,13)
my_sum(20,13)
my_sum(12,23)


def star_pattern(a):
    for x in range(1,a+1):
        print(x,end="")
    print()
    

star_pattern(10)
star_pattern(5)
star_pattern(100)
star_pattern(6)
star_pattern(50) 

def decimal_binary(number):
    print(bin(number).replace("0b","")) 
    
decimal_binary (10) 
