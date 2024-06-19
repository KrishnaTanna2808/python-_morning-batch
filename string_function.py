name = "krishna patel tanna"
print(name.capitalize())
print(name.count('k',1,7))
print(name.title())
print(name.swapcase())
print(name.center(20,'*'))


#get substring
print(name[7:18])
print(name.ljust(20,'*'))
print(name.rjust(20,'*'))
print(name.zfill(20))
print(name.encode())
print(name.find('i'))
print(name.index('i'))
print(name.isalnum())
print(name.isalpha())
print(name.isdecimal())
print(name.isdigit())
print(name.isidentifier())
print(name.islower())
print(name.isnumeric())
print(name.isprintable())
print(name.isspace())
print(name.istitle())
print(name.isupper())
print(name.join('***')) 
print(name.lstrip('k'))
print(name.rstrip('a'))
#main
print(name.strip('k'))
print(name.partition('i'))
#main
print(name.replace('k','K'))
print(name.rpartition('i'))
print(name.rsplit('i')) 
print(name.split('i'))
print(name.splitlines())
print(name.startswith('k'))
print(name.endswith('a'))
print(name.translate(str.maketrans('k','K')))
#main
print(name.upper())
print(name.lower())
print(name.casefold())
print(name.format_map({'name':'krishna'}))
print(name.format(name='krishna'))
print(name.maketrans('k','K'))
print(name.translate(str.maketrans('k','K')))
print(name.encode('utf-8'))
print(name.encode('utf-16'))
print(name.encode('utf-32'))

#f string
a ='hello'
b = 'krishna'
c = 56

print(a+' '+b+' '+(str(c)))
print(a+' '+b)

#fstring
print(f"{a} : {b} :  {c}")
#print('price of my cloth is'+str(price))
price = 1388
print(f'price of my cloth is {price:.3f}')

m =12
n =24

print(f"sum of m and n {m+n}")

value = 3400
print('expensive') if value>3400 else print('cheap')# if else in one line

print(f'price is very {'expensive' if value>3400 else 'cheap'}')

salary = 246000
print(f'my salary is {salary:,} rs')

number = 34
print(f"number is {number:%} ok?")

#escape sequences
print("this is python language /nplease practice") #new line charachters

print("this is pytho n language /t please practice")#tab 

print("this is paython language /' please practice")


      
