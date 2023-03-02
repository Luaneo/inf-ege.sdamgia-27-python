def calcMaxSum(filename: str) -> int:
    summa = 0
    min_diff = float('inf')
    with open(filename) as file:
        file.readline()
        for line in file:
            a, b = map(int, line.split())
            summa += max(a, b)
            diff = abs(a - b)
            if diff < min_diff and diff % 5 != 0:
                min_diff = diff
    return summa if summa % 5 != 0 else summa - min_diff


print(
    calcMaxSum('27-A_1.txt'),
    calcMaxSum('27-B_1.txt')
)
