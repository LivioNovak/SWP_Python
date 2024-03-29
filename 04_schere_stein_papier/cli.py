import os
from game import play
import statistic as stat


def start(statistics, *set_mode):
    print('START NEW GAME:\n------------')

    # prepare
    clear_console()
    p1 = get_value()  # read input

    # play game
    c, res, statistics = play(statistics, p1)
    print(f'Computer choose: \t{c}')

    if res == 1:
        print('You win!')
    elif res == -1:
        print('You lose!')
    else:
        print('Draw!')

    # replay
    while True:
        print('Wanna play again? [y/n]\n'
              '----')

        replay = input().strip().lower()

        if (replay == 'yes') | (replay == 'y'):
            start(statistics)
            return statistics

        elif (replay == 'no') | (replay == 'n'):
            return statistics

        else:
            print('invalid command')


def get_value():
    while True:
        print(f'Player, choose your symbol:\n'
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
    print(statistics)
    while True:
        print('------\nSave Statistics in Database? [y/n]')
        saving = input().strip().lower()

        if saving == 'y' or saving == 'yes':
            print('Save in db...')
            stat.save_in_db(statistics)
            break

        elif saving == 'n' or saving == 'no':
            break

        else:
            print('invalid command')

    print('Back to Menu')


def rules():
    print('RULES:\n------------')
    print('Rock\t\t>\tScissors, Lizard\n'
          'Scissors\t>\tPaper, Lizard\n'
          'Paper\t\t>\tRock, Spock\n'
          'Lizard\t\t>\tPaper, Spock\n'
          'Spock\t\t>\tRock, Scissors\n')
    print('----')
    print('Press [Enter] to proceed...')
    input()


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
