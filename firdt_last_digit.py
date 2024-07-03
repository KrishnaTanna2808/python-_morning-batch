num = int(input("please enter the number: "))

last_digit = 0
new_last_digit = 0
while num!=0:
    new_last_digit = num % 10
    num = num//0
    
print(f"first digit is : {new_last_digit}")
print(f"last digit is : {last_digit}")