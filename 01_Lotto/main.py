import random


# one lotto playthrough = draw 6 times (= draws param):
def lotto_draw(lotto_numbers, draws):
    for i in range(draws):
        real_len = len(lotto_numbers)-1  # for better overview
        index = random.randint(0, real_len - i)    # generate random index (= lotto numbers left)
        # switch number at generated index with number at the (now) last index
        lotto_numbers[index], lotto_numbers[(real_len - i)] = lotto_numbers[(real_len - i)], lotto_numbers[index]

    # print out all drawn lotto-numbers
    print(f'drawn numbers: {lotto_numbers[-draws:]}')
    return lotto_numbers


# statistics of one or more lotto playthroughs
def lotto_statistic(total_draws, play_draws, max_num):
    # init dictionary and number-list
    lotto_numbers = list(range(1, max_num+1))  # list of lotto numbers
    drawn_times = {}  # dictionary for how many times a number got drawn
    for i in range(1, max_num+1):
        drawn_times[i] = 0

    for i in range(total_draws):
        lotto_numbers = lotto_draw(lotto_numbers, play_draws)  # one lotto playthrough

        # get previously drawn numbers (saved at the end of the list)
        drawn_numbers = lotto_numbers[-play_draws:]
        # increment times the numbers got drawn by one
        for drawn_num in drawn_numbers:
            drawn_times[drawn_num] += 1  # increment by one

    return drawn_times


# execute a lotto playthrough 1000 times
statistic = lotto_statistic(1000, 6, 45)

# print how many times any number got drawn
print(statistic)