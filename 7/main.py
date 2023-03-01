def maxPair(filename: str) -> tuple[int, int]:
    with open(filename) as file:
        file.readline()
        even17 = 0
        odd17 = 0
        even_ = 0
        odd_ = 0
        for line in file:
            n = int(line)
            if n % 17 == 0:
                if n % 2 == 0:
                    even17 = max(even17, n)
                else:
                    odd17 = max(odd17, n)
            else:
                if n % 2 == 0:
                    even_ = max(even_, n)
                else:
                    odd_ = max(odd_, n)
    if even17 + even_ > odd17 + odd_:
        return sorted((even17, even_), reverse=True)
    else:
        return sorted((odd17, odd_), reverse=True)


print(*maxPair('27991_A.txt'))
print(*maxPair('27991_B.txt'))
