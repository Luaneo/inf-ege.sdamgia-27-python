# !!! НЕ ВЫДАЕТ ПРАВИЛЬНЫЙ РЕЗУЛЬТАТ ДЛЯ ФАЙЛА B

def countPairs(filename: str) -> int:
    rem_counts_gt = [0] * 80
    rem_counts_lt = [0] * 80
    with open(filename) as file:
        file.readline()
        for line in file:
            n = int(line)
            if n > 50:
                rem_counts_gt[n % 80] += 1
            else:
                rem_counts_lt[n % 80] += 1
    count_pairs = rem_counts_gt[0]* rem_counts_lt[0] + rem_counts_gt[0] * (rem_counts_gt[0] - 1) // 2
    count_pairs = rem_counts_gt[40]* rem_counts_lt[40] + rem_counts_gt[40] * (rem_counts_gt[40] - 1) // 2
    for i in range(1, 40):
        count_pairs += rem_counts_gt[i] * (rem_counts_gt[-i] + rem_counts_lt[-i])
        count_pairs += rem_counts_gt[-i] * (rem_counts_gt[i] * rem_counts_lt[i])
    return count_pairs

print(
    countPairs('28130_A.txt'),
    countPairs('28130_B.txt')
)
