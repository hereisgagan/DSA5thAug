a = int(input("enter total numbers"))
# consider your 1st answer as infinity so that any number entered by user will be smaller than infinity.
ans = float('inf')
for i in range(a):
    b = int(input("enter number"))
    ans = min(b,ans)

print (ans)
