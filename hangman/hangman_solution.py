import random

class Hangman:

    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = len(self.word) * ['_']
        self.num_letters = len(set(self.word))
        self.list_letters = []

        print(f'The mystery word has {len(self.word)} charecters')
        print(f'{self.word_guessed}')

    def check_letter(self, letter):
        if letter.lower() in self.word:
            for i, character in enumerate(self.word):
                if character == letter:
                    self.word_guessed[i] = letter
            print(f'Yes! {letter} is in the word, guess another.')
            print(self.word_guessed)
            
            self.list_letters.append(letter)
            self.num_letters -= 1
        else: 
            self.num_lives -= 1
            print('The letter is not in the word, guess again. ')
    
    def ask_letter(self):
        
        while True:
            letter = input('Please guess a letter. ')
            if len(letter) != 1:
                print('Please enter just one charachter. ')
            elif letter in self.list_letters:
                print(f'{letter} has already been tried. ')
            else:
                self.check_letter(letter)
                break
            
def play_game(word_list):
    game = Hangman(word_list, num_lives=5)

    while game:
        game.ask_letter()
        if game.num_lives == 0:
            print(f'Oh no! You ran out of lives. The word was {game.word}')
            break

        elif game.num_letters == 0:
            print(f'Congratulations, you got it right! The word was {game.word}')
            break

if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
    play_game(word_list)
