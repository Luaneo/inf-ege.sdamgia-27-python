def pairWithMaxSum(filename: str) -> tuple[int, int]:
    max_rems = [0] * 120
    max_sum = 0
    pair_with_max_sum = (0, 0)
    with open(filename) as file:
        file.readline()
        for line in file:
            aj = int(line)
            ai = max_rems[-(aj % 120)]
            if ai != 0 and ai > aj and ai + aj > max_sum:
                max_sum = ai + aj
                pair_with_max_sum = (ai, aj)
            max_rems[aj % 120] = max(max_rems[aj % 120], aj)
    return pair_with_max_sum

print(*pairWithMaxSum('28131_A.txt'))
print(*pairWithMaxSum('28131_B.txt'))
