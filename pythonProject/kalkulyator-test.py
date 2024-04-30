number = 5, 6, 7
print(number)

print( 5 + 8)
print(9-8)

a = 8
b = 6
c = a+b
print(c)

a = 6
b = 6
a +=b
print(a)

a = 7
b = 6
a -=b
print(a)

a = 8
b = 2
c = 8/2
print(c)

a = 5
b = 5
c = a*b
print(c)

a = 9
b = 8
c = a//b
print(c)

a = 9
b = 8
c = a%b
print(c)

a = 2
b = 3
c = a**b
print(c)

a = 2003
print(hex(a))
print(oct(a))
print(bin(a))

a ="5"
b = 2
print(int(a)+b)

a = "5.2"
b = 2
print(float(a)+b)

import math
print(math.ceil(4.5))
print(math.fabs(-4.5))
print(math.factorial(6))
print(math.floor(5.6))
print(math.pow(3,4))
print(math.sqrt(25))

a,b = 0,1
while a < 10:
    print(a)
    a,b = b,a + b

a = 10
if a ==10:
    print("True")
else:
    print("False")

a = 100
if a ==10:
    print("True")
else:
    print("False")

a = 10
if a ==10:
    print("a = 10")
elif a < 10:
    print("a < 10")
else:
    print("a > 10")

a = 100
if a ==10:
    print("a = 10")
elif a < 10:
    print("a < 10")
else:
    print("a > 10")

i = 0
while i < 10:
    i +=1
    print(i)

n = int(input("Введите число"))
i = 1
fact = 1
while i <=n:
    fact *=i
    i +=1
print("Факториал равен числу", fact)

for i in range(5):
    print("Katya")

lst = (1,3,5,7,9)
for i in lst:
    print(i ** 2)

str = "Hello world"
for i in str:
    print(i)

def add(x,y):
    return x + y

print(add(5,3))

sqrt = lambda x: x**0.5
print(sqrt(25))

l =(1,2,3,4,5,6,7,)
print(list(map(lambda x:x**3,l)))

def print_smth(name):
    print("Hello", name)

print_smth('Katya')

def print_smth(name="Kate"):
    print("Hello", name)

print_smth()



def main():
    print_smth("Katya")
    usd_rate = 50
    money = 60000
    result = exchange(usd_rate, money)
    print(result)
def print_smth(name):
    print("Hello",name)
def exchange(usd_rate, money):
    result = round(money/usd_rate, 3)
    return result
main()

s = "Spring"
print(s[1])

s = "Hello world"
print(s[6:10])

s = "Summer beach"
print(len(s))
s = "Summer beach"
exist ="Summach" in s
print(exist)

s = "Summer beach"
print(len(s))
s = "Summer beach"
exist ="Summer" in s
print(exist)

s = "Summer"
for char in s:
    print(char)

s = "Summer"
print(s.upper())

s ="Summer"
print(s.lower())

s ="Summer"
sl = s.split()
print(sl)

s = "Summer beach"
sl = s.split()
ss ="  ". join(sl)
print(ss)

s = "Summer beach"
sf = s.find("beach")
print(sf)

s = "Summer beach"
sf = s.replace("beach", "pool")
print(sf)

s = "Summe beach"
s2 = "length-{}, height-{}, width-{}"
print(s2.format(5,6,7))

