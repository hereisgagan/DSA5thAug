print("Enter 3 numbers line by line")
a = int(input())
b = int(input())
c = int(input())

# print("Minimum number is ", min(min(a, b), c))

# 1st approach

if a<b:
    if a<c:
        print(f"{a} is min")
    else:
        print(f"{c} is min")
else:
    if b<c:
        print(f"{b} is min")
    else:
        print(f"{c} is min")


if a<b and a<c:
    print(f"{a} is min")
elif b<c and b<a:
    print(f"{b} is min")
else:
    print(f"{c} is min")


#