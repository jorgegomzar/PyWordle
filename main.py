from typing import List
from wordle import Wordle, WordleLengthException


class bcolors:
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'


def print_guess_check(guess: str, check: List[int]) -> None:
    """
    Pretty prints the guess of the user depending on its accuracy
    :param guess:
    :param check:
    """
    print(f''.join([f'{bcolors.OKGREEN if check[i] == 2 else bcolors.WARNING if check[i] == 1 else bcolors.FAIL} {g} {bcolors.ENDC}' for i, g in enumerate(guess.upper())]))


def game_loop(wordle: Wordle) -> None:
    """
    Game loop. Asks the user for a guess until he does it right or it has no more tries left.
    """
    # print(wordle)

    tries_left = 5
    while tries_left > 0:
        try:
            guess = input(f'What is your guess? - (Lives: {tries_left}): ')
            if len(guess) != 5:
                raise WordleLengthException('Length should be 5 characters')

            check = wordle.check(guess)
            print_guess_check(guess, check)

            if sum(check) == 10:
                print('CORRECT!')
                break

            tries_left -= 1

        except Exception as e:
            print('ERROR:', e)

        if tries_left == 0:
            print('Too bad, I am sorry...')
            print(f'The solution was {wordle}')


if __name__ == '__main__':
    choice = True
    wordle = Wordle()
    while choice:
        wordle.generate_wordle()
        game_loop(wordle)
        choice = 1 if input('Do you want another round? (y/N) ') == 'y' else 0

    print('Thanks for playing!')
