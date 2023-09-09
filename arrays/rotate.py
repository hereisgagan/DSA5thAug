def rotate(ar):
    temp = ar[-1]

    for idx in range(len(ar)-2,-1,-1):
        ar[idx+1] = ar[idx]

    ar[0] = temp

x = [1,2,3,4,5,6]
r = 20

r = r % len(x)
# ans = [5,6,1,2,3,4]
for call in range(r):
    print("hello")
    rotate(x)
print(x)
