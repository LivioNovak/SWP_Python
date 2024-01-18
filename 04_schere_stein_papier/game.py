from handsign import Handsign
import random
import statistic as stat


def init_sings():
    signs = {'0': Handsign(0, **{'name': 'scissors', 'character': 'sc'}),
             '1': Handsign(1, **{'name': 'paper', 'character': 'p'}),
             '2': Handsign(2, **{'name': 'rock', 'character': 'r'}),
             '3': Handsign(3, **{'name': 'lizard', 'character': 'l'}),
             '4': Handsign(4, **{'name': 'spock', 'character': 'sp'})}

    return signs


def play(statistics, mode, *inputs):
    signs = init_sings()

    if mode == 1:
        # player vs player
        p1 = signs[str(inputs[0])]
        p2 = signs[str(inputs[1])]

        # save stats
        statistics['signs'][p1.character] += 1
        statistics['signs'][p2.character] += 1

        res = p1.compare(p2.value)
        if res == 1:
            statistics['pvp']['p1'] += 1
        elif res == 0:
            statistics['pvp']['d'] += 1
        else:
            statistics['pvp']['p2'] += 1

        return res, statistics

    elif mode == 2:
        # player vs com/cpu
        p = signs[str(inputs[0])]
        statistics['signs'][p.character] += 1

        # generate sign (value) randomly
        c = random.randint(0, 5)

        res = p.compare(c)

        if res == 1:
            statistics['pvc']['p'] += 1
        elif res == 0:
            statistics['pvc']['c'] += 1
        else:
            statistics['pvc']['d'] += 1

        return res, statistics
