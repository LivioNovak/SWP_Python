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


def play(statistics, input):
    signs = init_sings()

    # player vs com/cpu
    p = signs[str(input)]
    statistics['signs'][p.character] += 1

    # generate sign (value) randomly
    c = random.randint(0, 5)

    res = p.compare(c)

    if res == 1:
        statistics['results']['win'] += 1
    elif res == 0:
        statistics['results']['lose'] += 1
    else:
        statistics['results']['draw'] += 1

    return c, res, statistics