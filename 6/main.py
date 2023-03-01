def countPairs(filename: str) -> int:
    with open(filename) as file:
        count_all = int(file.readline())
        count62 = 0
        count31 = 0
        count2 = 0
        for line in file:
            n = int(line)
            if n % 62 == 0:
                count62 += 1
            elif n % 31 == 0:
                count31 += 1
            elif n % 2 == 0:
                count2 += 1
    return (
        count62 * (count_all - count62)
        + count62 * (count62 - 1) // 2
        + count31 * count2
    )


print(
    countPairs('27990_A.txt'),
    countPairs('27990_B.txt')
)
