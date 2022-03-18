import random
from hangman_art import logo, stages
from hangman_words import word_list

print(logo)

word = random.choice(word_list)
word_length = len(word)

# store
display = []
for letters in range(word_length):
    display.append('-')

lives = 6
stage = stages[lives]
guessed_letters = []
# repeat until user wins
while '-' in display and lives > 0:
    print('')
    guess = input('Guess a letter: ').lower()
    found = []
    lose_life = True
    print("\n" * 5)
    if guess in guessed_letters:
        print(f'You\'ve already guessed {guess}. Try again.')
    else:
        for pos in range(word_length):
            if word[pos] == guess:
                display[pos] = guess
                lose_life = False

        if lose_life:
            lives -= 1
            print(f'\nYou guessed {guess}. That\'s not in the word. You lose a life.')
            stage = stages[lives]

    guessed_letters.append(guess)
    print(*display)
    print(stage)



if lives == 0:
    print(f'\nYou lose. The word was: {word}.')
else:
    print('\nYou win!')
