def print_square(n):
    for row in range(n):
        for col in range(n):
            if row + col < n:
                print("*", end=" ")
            else:
                print(" ", end=" ")

        print()


print_square(4)
