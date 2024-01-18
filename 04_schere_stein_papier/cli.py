import os
from game import play
import statistic as stat


def start(statistics, *set_mode):
    print('START NEW GAME:\n------------')
    mode = 0
    # get game-data and compute
    while True:
        # when empty, define game mode
        if set_mode == ():
            print('(player)\t-\tplay against another player\n'
                  '(cpu)\t\t-\tplay against the cpu\n'
                  '----')

            mode = input().strip().lower()
        else:
            mode = set_mode[0]

        # read inputs and compare
        if (mode == 'player') | (mode == 'p'):
            clear_console()

            p1 = get_value(1)
            p2 = get_value(2)
            res, statistics = play(statistics, 1, p1, p2)

            if res == 1:
                print(f'{p1} beats {p2}\nPlayer 1 wins!')
            elif res == -1:
                print(f'{p2} beats {p1}\nPlayer 2 wins!')
            else:
                print('Draw!')

            break

        elif (mode == 'cpu') | (mode == 'c'):
            clear_console()

            p1 = get_value(1)
            # play game
            res, statistics = play(statistics, 2, p1)

            if res == 1:
                print('You win!')
            elif res == -1:
                print('You lose!')
            else:
                print('Draw!')

            break

        else:
            print('invalid command')

    # replay
    while True:
        print('Wanna play again? [y/n]\n'
              '----')

        replay = input().strip().lower()

        if (replay == 'yes') | (replay == 'y'):
            start(statistics, mode)
            return statistics

        elif (replay == 'no') | (replay == 'n'):
            return statistics

        else:
            print('invalid command')


def get_value(player):
    while True:
        print(f'Player {player}, choose your symbol:\n'
              '[0 = scissors, 1 = paper, 2 = rock, 3 = lizard, 4 = spock]\n'
              '----')

        p_in = input().strip().lower()
        try:
            p_in = int(p_in)
        except:
            print('invalid input, not a number!')
        else:
            if (p_in < 0) | (p_in > 4):
                print('invalid number, not a sign!')
            else:
                clear_console()
                return p_in


def clear_console():
    os.system('cls')


def stats(statistics):
    print('STATISTICS:\n------------')
    # TODO: anzuzeigende Statistiken abfragen (gezogene Zeichen, pvp, pvc)
    print(statistics)
    print('------\nproceed? [y/n]')
    proceed = input().strip().lower()



def rules():
    print('RULES:\n------------')
    print('Rock\t\t>\tScissors, Lizard\n'
          'Scissors\t>\tPaper, Lizard\n'
          'Paper\t\t>\tRock, Spock\n'
          'Lizard\t\t>\tPaper, Spock\n'
          'Spock\t\t>\tRock, Scissors\n')
    print('----')


def menu():
    statistics = stat.get_stats()

    # running cli
    run = True
    while run:
        clear_console()

        print('MENU:\n------------')
        print('(Play)\t-\tstart a game\n'
              '(Stats)\t-\tshow statistics\n'
              '(Rules)\t-\tshow game rules\n'
              '(Exit)\t-\tend game\n'
              '------------')

        menu_in = input().strip().lower()

        if (menu_in == 'play') | (menu_in == 'p'):
            start(statistics)
        elif (menu_in == 'stats') | (menu_in == 's'):
            stats(statistics)
        elif (menu_in == 'rules') | (menu_in == 'r'):
            rules()
        elif (menu_in == 'exit') | (menu_in == 'e'):
            print('bye!!')
            run = False
        else:
            print('Unrecognized input!')

    # end game
    stat.save_stats(statistics)


if __name__ == '__main__':
    menu()
