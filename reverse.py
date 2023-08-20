def count_of_digits(n):
    ans = 0
    while n > 0:
        n = n // 10
        ans += 1

    return ans


def reverse(n):
    count = count_of_digits(n)
    k = 1
    ans = 0
    while n > 0:
        r = n % 10
        target_idx = count - k
        ans = ans + r * 10**target_idx
        n = n // 10
        k += 1

    return ans


num = int(input())

print(reverse(num))
