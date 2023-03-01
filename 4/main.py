def calcX(filename: str) -> int:
    with open(filename) as file:
        file.readline()
        mx14 = 0
        mx2 = 0
        mx7 = 0
        mx = 0
        for line in file:
            n = int(line)
            if n % 14 == 0:
                mx14 = max(mx14, n)
            elif n % 7 == 0:
                mx7 = max(mx7, n)
            elif n % 2 == 0:
                mx2 = max(mx2, n)
            else:
                mx = max(mx, n)
    return max(
        mx14 * max(mx7, mx2, mx),
        mx2 * mx7
    )


print(
    calcX('27-A_2.txt'),
    calcX('27-B_2.txt')
)
