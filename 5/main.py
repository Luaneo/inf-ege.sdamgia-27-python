def countPairs(filename: str) -> int:
    count26 = 0
    count13 = 0
    count2 = 0
    count_ = 0
    with open(filename) as file:
        file.readline()
        for line in file:
            n = int(line)
            if n % 26 == 0:
                count26 += 1
            elif n % 13 == 0:
                count13 += 1
            elif n % 2 == 0:
                count2 += 1
            else:
                count_ += 1
    return (
        count26 * (count13 + count2 + count_)
        + count26 * (count26 - 1) // 2
        + count13 * count2
    )


print(
    countPairs('27989_A.txt'),
    countPairs('27989_B.txt')
)
