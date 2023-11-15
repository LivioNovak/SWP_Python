import random
import constants


###############
# combinations
###############

def royal_flush(cards):
    # 1. check for being a straight_flush
    if straight_flush(cards):
        # highest possible straights starts with a 10
        return cards[0].value == 10

    return False


def straight_flush(cards):
    # 1. check for being a flush
    if flush(cards):
        # 2. check for being a straight
        if straight(cards):
            return True

    return False


def four_of_a_kind(cards):
    for selected_card in cards[:2]:
        same_value = 0
        for compare_card in cards:
            if selected_card.value == compare_card.value:
                same_value += 1

        if same_value == 4:
            return True

    return False

    # check for being a 4 of a kind
    return cards_match_base == 4


def full_house(cards):
    # full house is a combination of one pair and one three-of-a-kind
    # 1. check for containing a three of a kind
    if three_of_a_kind(cards):
        # 2. check for containing a pair
        if pair(cards):
            return True

    return False


def straight(cards):
    # special case: a street can start with an ace. has to continue with 2, 3, 4, 5
    if cards[0].value == 14:
        match_list = [2, 3, 4, 5]
        for i in range(len(cards) - 2):
            if cards[1 + i].value != match_list[i]:
                return False

        return True

    # every following card must be one value higher than the previous
    for i in range(len(cards) - 1):
        if cards[i].value != cards[i + 1].value - 1:
            return False

    return True


def flush(cards):
    color = cards[0].color
    for sel_card in cards[1:]:
        if color != sel_card.color:
            return False

    return True


def three_of_a_kind(cards):
    for sel_card in cards:
        same_value = 0
        for compare_card in cards:
            if sel_card.value == compare_card.value:
                same_value += 1

        if same_value == 3:
            return True

    return False


def two_pairs(cards):
    num_of_cards_of_pairs = 0
    for sel_card in cards:
        same_value = 0
        for compare_card in cards:
            if sel_card.value == compare_card.value:
                same_value += 1

        # a pair has 2 cards, so this gets called twice per pair
        if same_value == 2:
            num_of_cards_of_pairs += 1

        # if 4 cards belong to pairs, there's a total of 2 pairs
        if num_of_cards_of_pairs == 4:
            return True

    return False


def pair(cards):
    for sel_card in cards:
        same_value = 0
        for compare_card in cards:
            if sel_card.value == compare_card.value:
                same_value += 1

        if same_value == 2:
            return True

    return False


##############
# others
##############

class card:
    def __init__(self, numerical_card, symbols):
        self.value = get_value(numerical_card, symbols)
        self.color = get_color(numerical_card, symbols)

    def __str__(self):

        if self.value == 11:
            tmp_str = 'J_'
        elif self.value == 12:
            tmp_str = 'Q_'
        elif self.value == 13:
            tmp_str = 'K_'
        elif self.value == 14:
            tmp_str = 'A_'
        else:
            tmp_str = f'{str(self.value)}_'

        if self.color == 0:
            tmp_str += constants.CLUB
        elif self.color == 1:
            tmp_str += constants.DIAMOND
        elif self.color == 2:
            tmp_str += constants.HEART
        elif self.color == 3:
            tmp_str += constants.SPADE
        else:
            tmp_str += str(self.color)

        return tmp_str


def get_color(numerical_card, symbols):
    return (numerical_card - 1) // symbols


def get_value(numerical_card, symbols):
    tmp_val = numerical_card % symbols
    # special cases
    if tmp_val == 0:  # when it's king
        return 13
    elif tmp_val == 1:  # when it's ace
        return 14
    return tmp_val


def init_cards(colors, symbols):
    # colors and symbols equal their quantities
    poker_cards = []
    for num in range(1, (colors * symbols) + 1):
        poker_cards.append(card(num, symbols))

    return poker_cards


def draw_cards(cards, total_draws):
    for i in range(total_draws):
        index = random.randint(0, (len(cards) - 1) - i)  # generate random index; card at that pos got selected
        # switch pos of selected number with number at the (now) last index
        cards[index], cards[(len(cards) - 1 - i)] = cards[(len(cards) - 1 - i)], cards[index]

    return cards[-total_draws:]


def check_combination(combinations, cards):
    if royal_flush(cards):
        combinations["royal_flush"] += 1
        print("royal flush")
    elif straight_flush(cards):
        combinations["straight_flush"] += 1
        print("straight_flush")
    elif four_of_a_kind(cards):
        combinations["four_of_a_kind"] += 1
        print("4 of a kind")
    elif full_house(cards):
        combinations["full_house"] += 1
        print("full house")
    elif flush(cards):
        combinations["flush"] += 1
        print("flush")
    elif straight(cards):
        combinations["straight"] += 1
        print("straight")
    elif three_of_a_kind(cards):
        combinations["three_of_a_kind"] += 1
        print("3 of a kind")
    elif two_pairs(cards):
        combinations["two_pairs"] += 1
        print("2 pairs")
    elif pair(cards):
        combinations["pair"] += 1
        print("pair")
    else:
        combinations["high_card"] += 1
        print("high card")

    return combinations


def print_statistics(actual, calculated):
    print("-------------------------------------------\nacutal Statistics:\n")
    for comb_type in actual:
        print('%15s: %10.5f %%' % (comb_type, actual[comb_type]))
    # print(actual_statistics)

    print("-------------------------------------------\ncalculated Statistics:\n")
    for comb_type in calculated:
        percentage = (calculated[comb_type] / constants.TOTAL_PLAYS) * 100
        calculated[comb_type] = percentage
        print('%15s: %10.5f %%' % (comb_type, percentage))
    # print(calculated_statistics)

    print("-------------------------------------------\ndifference:\n")
    for comb_type in calculated:
        difference = abs(calculated[comb_type] - actual[comb_type])
        print('%15s: %10.5f %%' % (comb_type, difference))


##############
# main
##############

def main():
    # initialize poker_cards
    poker_cards = init_cards(constants.COLORS, constants.SYMBOLS)

    # initialize dictionaries for statistics
    calculated_statistics = {
        'high_card': 0,
        'pair': 0,
        'two_pairs': 0,
        'three_of_a_kind': 0,
        'straight': 0,
        'flush': 0,
        'full_house': 0,
        'four_of_a_kind': 0,
        'straight_flush': 0,
        'royal_flush': 0
    }
    actual_statistics = {
        'high_card': 50.1177,
        'pair': 42.2569,
        'two_pairs': 4.7539,
        'three_of_a_kind': 2.1128,
        'straight': 0.3925,
        'flush': 0.1965,
        'full_house': 0.1441,
        'four_of_a_kind': 0.0240,
        'straight_flush': 0.00139,
        'royal_flush': 0.0000154
    }

    # actual game logic: draw cards, check combination, increase statistics-counter
    for i in range(constants.TOTAL_PLAYS + 1):
        drawn_cards = draw_cards(poker_cards, constants.DRAW_CARDS)

        # sort hand
        drawn_cards.sort(key=lambda c: c.value, reverse=False)

        # print hand cards
        output = ''
        for drawn_card in drawn_cards:
            output += f'{str(drawn_card)}, '

        print(output)

        # check for combination and increase it by 1
        calculated_statistics = check_combination(calculated_statistics, drawn_cards)

    # prepare and print statistics
    print_statistics(actual_statistics, calculated_statistics)


if __name__ == '__main__':
    main()