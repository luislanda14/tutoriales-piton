# how many overlap

with open('input.txt') as f:
    lines = f.readlines()
    count = 0
    for line in lines:
        fist_pair = line.strip().split(',')[0]
        second_pair = line.strip().split(',')[1]
        first_pair_left = int(fist_pair.split('-')[0])
        first_pair_right = int(fist_pair.split('-')[1])
        second_pair_left = int(second_pair.split('-')[0])
        second_pair_right = int(second_pair.split('-')[1])
        first_pair = list(range(first_pair_left, first_pair_right + 1))
        second_pair = list(range(second_pair_left, second_pair_right + 1))
        if first_pair_left in second_pair or first_pair_right in second_pair:
            count += 1
        elif second_pair_left in first_pair or second_pair_right in first_pair:
            count += 1
    print(f'Count: {count}')

    # Count: 870