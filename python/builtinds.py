def count_low_high(num_list):
    if not num_list:
        return None

    low_count = 0
    high_count = 0

    for num in num_list:
        if num > 50 or num % 3 == 0:
            high_count += 1
        else:
            low_count += 1

    return [low_count, high_count]


num_list = [20, 9, 51, 81, 50, 42, 77]


result = count_low_high(num_list)
print(result)  