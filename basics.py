# print()
# Operators
# if-elif-else
# For loop
# While loop

a = 10
b = 20
print(a+b)


# +, -, *, /, //, %, **

print(5/2)
print(5//2)
print(5%2)
print(2**4)

# If elif else

a = 10

if a % 2 ==0 :
    print("Even")
else:
    print("Odd")


x = 15

if x%15==0:
    print("X is divisible by 15")

if x%3==0:
    print("X is divisible by 3")
elif x%5==0:
    print("X is divisible by 5")
else:
    print("X is not divisible by 2")


# For loop

print("Hello")
print("Hello")
print("Hello")
print("Hello")
print("Hello")
print("Hello")
print("Hello")
print("Hello")
print("Hello")
print("Hello")


for i in range(10):
    print("hello"*i)


print("hello")
print("world")

# range(10) -> [0.......9]
# range(1,10) -> [1,, ...,9]
# range(2,10,2) -> [2,3... 8]


i = 0

# while i< 10:
#     print("hello"*10**5)
    # i+=1

# Input

# Input + 5
# Invalid -> Readable error


# 1234 -> 12345

# try:
#     a = int(input("Enter any number"))
# except ValueError:
#     print("You entered an invalid integer")
# else:
#     print(a+5)

try:
    a = int(input("Enter any number"))
    c = a +"5"
except ValueError:
    print("You entered a string")
except TypeError:
    print("You entered a number")



# print(int("3ad"))

# print("5"+3)

# print(int("hgdiuadbib"))