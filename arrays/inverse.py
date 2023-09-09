x = [3, 4, 0, 1, 2]

y = [x[idx] for idx in range(len(x))]

for idx in range(len(x)):
    y[x[idx]] = idx

print(y)
