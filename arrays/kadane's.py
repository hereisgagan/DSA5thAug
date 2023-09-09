ar = [-2, -3, 4, -1, -2, 1, 5, -3]


ans = float("-inf")

for i in range(len(ar)):
    sum1 = 0
    for j in range(i, len(ar)):
        sum1 = sum1 + ar[j]

        ans = max(ans, sum1)

print(ans)
