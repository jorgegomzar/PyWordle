from typing import List
import random
import requests


class Wordle:
    def __init__(self):
        """
        Gets the wordlist.
        """
        self.WORDS: List[bytes] = self.__get_wordlist()
        self.wordle: str = ''

    def __get_wordlist(self) -> List[bytes]:
        """
        Gets a wordlist from Internet and filters by length equal to 5.
        :return: A wordlist of words of length equal to 5.
        """
        word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
        response = requests.get(word_site)
        return list(filter(lambda x: len(x) == 5, response.content.splitlines()))

    def generate_wordle(self) -> None:
        """
        Picks a random word of 5 letters and assigns it to self.wordle
        """
        self.wordle = random.choice(self.WORDS).decode('utf-8')

    def check(self, guess: str) -> List[int]:
        """
        :param guess:
        :return: 0 - letter not present. 1 - Letter present but not in right place. 2 - Letter present and in right place
        """
        check: List[int] = [g in self.wordle for g in guess]
        for i, g in enumerate(guess):
            if g == self.wordle[i]:
                check[i] = 2
        return check

    def __repr__(self):
        return self.wordle

    def __str__(self):
        return self.wordle


class WordleLengthException(Exception):
    pass
