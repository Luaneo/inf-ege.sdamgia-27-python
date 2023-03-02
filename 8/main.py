def pairWithMaxSum(filename: str) -> list[int, int]:
    rem_maxs7 = [0] * 160
    rem_maxs_ = [0] * 160
    max_sum = 0
    a, b = 0, 0
    with open(filename) as file:
        file.readline()
        for line in file:
            n = int(line)
            rem7 = n % 7
            rem160 = n % 160
            if rem7 == 0:
                if n > rem_maxs7[rem160]:
                    rem_maxs7[rem160] = n
                    for i in range(160):
                        if i != rem160:
                            if n + rem_maxs7[i] > max_sum:
                                max_sum = n + rem_maxs7[i]
                                a, b = n, rem_maxs7[i]
                            if n + rem_maxs_[i] > max_sum:
                                max_sum = n + rem_maxs_[i]
                                a, b = n, rem_maxs_[i]
            else:
                if n > rem_maxs_[rem160]:
                    rem_maxs_[rem160] = n
                    for i in range(160):
                        if i != rem160:
                            if n + rem_maxs7[i] > max_sum:
                                max_sum = n + rem_maxs7[i]
                                a, b = n, rem_maxs7[i]
    return sorted([a, b])


print(*pairWithMaxSum('28129_A.txt'))
print(*pairWithMaxSum('28129_B.txt'))
