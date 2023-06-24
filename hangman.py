import random
from guessing_game import GuessingGame
class Hangman(GuessingGame):
    def __init__(self):
        super().__init__()
        self.word_list = ['cat', 'dog', 'rat','kid','foot']
        self.word = self.word_list[random.randint(0,4)]
        self.incorrect_list = []
        self.correct_list = []
        self.correct_guess_for_win = len(set(self.word))

