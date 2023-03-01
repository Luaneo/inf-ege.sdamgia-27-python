def calcMinSum(filename: str) -> int:
    with open(filename) as file:
        file.readline()
        summa = 0
        min_diff = float('inf')
        for line in file:
            a, b = map(int, line.split())
            summa += min(a, b)
            diff = abs(a - b)
            if diff < min_diff and diff % 3 != 0:
                min_diff = diff
    return summa if summa % 3 != 0 else summa + min_diff


print(
    calcMinSum('27-A_demo.txt'),
    calcMinSum('27-B_demo.txt')
)
