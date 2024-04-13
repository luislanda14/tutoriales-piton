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
        if first_pair_left <= second_pair_left and first_pair_right >= second_pair_right:
            count += 1
        elif second_pair_left <= first_pair_left and second_pair_right >= first_pair_right:
            count += 1

    print(f'Count: {count}')

    # Count: 509