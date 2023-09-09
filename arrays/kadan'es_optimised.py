ar = [-2, -3, 4, -1, -2, 1, 5, -3]

csum = ar[0]
osum = ar[0]

ostart = 0
oend = 0


cstart = 0
cend = 0


for i in range(len(ar)):
    if csum > 0:
        csum = csum + ar[i]
        cend = i
    else:
        csum = ar[i]
        cstart = i
        cend = i

    if osum < csum:
        osum = csum
        ostart = cstart
        oend = cend

print(osum)
print(ostart)
print(oend)

print(ar[ostart:oend+1])