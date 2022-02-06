import random

def game_guess(x,y):
    p = random.randint(x,y)
    return p

l = int(input("Enter the starting number of guess game : "))
m = int(input("Enter the ending number of guess game :"))

game_guess(l,m)

z = game_guess(l,m)


if z == 1:
    print("HINT : The number can divide every thinkable number completely")
    l = int(input("Enter your guessed number : "))
    q = input("Are you ready to see the answer(y/n) : ")
    if q == 'y':
        print(z)
    else : 
        print("OK")
        
if z == 2:
    print("HINT : The number is the smallest prime number")
    l = int(input("Enter your guessed number : "))
    q = input("Are you ready to see the answer(y/n) : ")
    if q == 'y':
        print(z)
    else : 
        print("OK")
        
if z == 3:
    print("HINT : The number is basically a factor samllest factor of 81")
    l = int(input("Enter your guessed number : "))
    q = input("Are you ready to see the answer(y/n) : ")
    if q == 'y':
        print(z)
    else : 
        print("OK")
        
if z == 4:
    print("HINT : It is an even number which divides the 64 on its 16th time")
    l = int(input("Enter your guessed number : "))
    q = input("Are you ready to see the answer(y/n) : ")
    if q == 'y':
        print(z)
    else : 
        print("OK")
        
if z == 5:
    print("HINT : Its smallest factor of 978236814785")
    l = int(input("Enter your guessed number : "))
    q = input("Are you ready to see the answer(y/n) : ")
    if q == 'y':
        print(z)
    else : 
        print("OK")
        
if z == 6:
    print("HINT : It is the product of the two smallest prime number where one of the number is the smallest prime number and the other's number table contains 18,12,6,24")
    l = int(input("Enter your guessed number : "))
    q = input("Are you ready to see the answer(y/n) : ")
    if q == 'y':
        print(z)
    else : 
        print("OK")
        
if z == 7:
    print("HINT : Its one of the prime numbers and is the divisor of 14 which also divides 35")
    l = int(input("Enter your guessed number : "))
    q = input("Are you ready to see the answer(y/n) : ")
    if q == 'y':
        print(z)
    else : 
        print("OK")
        
if z == 8:
    print("HINT : The number is even as well as it divides 16 in its twice and is the cubic value of 2")
    l = int(input("Enter your guessed number : "))
    q = input("Are you ready to see the answer(y/n) : ")
    if q == 'y':
        print(z)
    else : 
        print("OK")
        
if z == 9:
    print("HINT : The number is divisible by 3 in its thrice")
    l = int(input("Enter your guessed number : "))
    q = input("Are you ready to see the answer(y/n) : ")
    if q == 'y':
        print(z)
    else : 
        print("OK")
        
if z == 10:
    print("HINT : It is the product of smallest prime number and the number which can divide 978643165135 which also divides 125 in its 25th multiplication by itself")
    l = int(input("Enter your guessed number : "))
    q = input("Are you ready to see the answer(y/n) : ")
    if q == 'y':
        print(z)
    else : 
        print("OK")
        
        
else:
    print(z)