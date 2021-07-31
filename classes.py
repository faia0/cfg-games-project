import random


class WordGuesser:
    def __init__(self, username, words_list):
        self.words_list = words_list
        self.username = username
        self.chosen_word = None
        self.display_word = None
        self.attempts = 9  # could be modified according to difficulty lvl
        self.past_guesses = None  # not implemented, but could be used to warn user if they have guessed a letter twice
        self.guess = None
        # self.difficulty = 0
        # self.password = 0

    def pick_word(self):
        """chooses a random word from given list & returns hidden version of the word"""
        self.chosen_word = random.choice(self.words_list)
        self.display_word = len(self.chosen_word) * "_ "
        return self.display_word

    def replace_letter(self):
        """replaces _ with the guessed letter wherever that letter appears in the word"""
        self.display_word = self.display_word.replace(' ', '')
        new_display_word = ''

        for i in range(0, len(self.chosen_word)):
            if self.chosen_word[i] == self.guess or self.display_word[i] != '_':
                new_display_word += self.chosen_word[i]
            else:
                new_display_word += '_'
            new_display_word += ' '

        self.display_word = new_display_word

    def guess_letter(self, letter):
        """takes an input (letter or word), and decides whether it is correct or not"""
        self.guess = letter.lower().strip()
        if not self.guess.isalpha():  # could allow numbers & multiple words for a higher difficulty level
            return "No special characters\n"  # no numbers, special characters or multiple words allowed

        self.attempts -= 1

        if self.guess == self.chosen_word:  # they guess the whole word correctly
            self.display_word = self.chosen_word  # process will continue until it reaches ***

        if self.guess in self.chosen_word:
            self.replace_letter()  # replaces display_word with correctly guessed letters

            if self.display_word.replace(' ', '') == self.chosen_word:  # *** guessed all characters
                return "\n{} \n\nWell done! The word was {}\n".format(self.display_word, self.chosen_word)
            else:
                return "\ncorrect! \n\n{}".format(self.display_word)

        elif self.attempts <= 0:
            return "Run out of guesses, the word was: {}. \n".format(self.chosen_word)  # run out of guesses
        else:
            return "\nWrong guess\n\n{}".format(self.display_word)

