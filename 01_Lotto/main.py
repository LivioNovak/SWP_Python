import random

lotto_numbers = list(range(1, 46))  # list of lotto numbers
# initialize dictionary and fill automatically
drawn_times = {}
for i in range(45):
    drawn_times[f'{i+1}'] = 0


# one lotto playthrough = draw 6 times:
def lotto_draw(draws):
    for i in range(draws):
        index = random.randint(0, 44 - i)    # generate random index (= lotto numbers left)
        # switch number at generated index with number at the (now) last index
        lotto_numbers[index], lotto_numbers[(44 - i)] = lotto_numbers[(44 - i)], lotto_numbers[index]

    # print out all 6 lotto-numbers
    print(f'drawn numbers: {lotto_numbers[39:]}')


# statistics of one or more lotto playthroughs
def lotto_statistic(total_draws):
    for i in range(total_draws):
        lotto_draw(6)  # one lotto playthrough

        # increment times the numbers got drawn by one
        for j in range(6):
            index = f'{lotto_numbers[44 - j]}'  # index of drawn number in dictionary (as string)
            drawn_times[index] += 1  # increment by one


# execute a lotto playthrough 1000 times
lotto_statistic(1000)

# print how many times any number got drawn
print(drawn_times)