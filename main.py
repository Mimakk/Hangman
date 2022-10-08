import string
from hangman_visual import lives_visual
import random
import json
import requests

def main():
    
    
    response = requests.get(
        "https://www.randomlists.com/data/words.json"
    )
    o = response.json()
    get_word(o)
    
    # Assigning the leters, used letter, and alphabet
    word = get_word(o)
    word_letters = set(word) # the set of letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # what the user has guessed
    lives = 7
    
    # Getting user input
    while len(word_letters) > 0 and lives > 0:
        # Letters used
        # " ".join(['a', 'b', 'cd']) --> 'a b cd'
        print("You have", lives, "left and you have used these letters: ", " ".join(used_letters))
        
        word_list = [letter if letter in used_letters else '-' for letter in word]
        hangman(lives)
        print('Current word: ', " ".join(word_list))
        
        user_letter = get_guess(used_letters,alphabet)
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
        
            else:
                lives -= 1 
                print("Letter not in word!!")
                
    if lives == 0:
        hangman(lives)
        print("You LOSE!! the man has died. The word was", word, "!!")
    else:
        print("You guessed the word", word, "!!")
    
def hangman(lives):
    print(lives_visual[lives])
    
def get_word(o):
    game_words=[]
    for word in o["data"]:
        
        # This looks every word in wordlist and every letter in words if
        # there is a - in word replaces it with space and assign it with 
        # new_word
        for letter in word:
            if "-" in letter:
                without_dash = word.replace("-", " ")
                word = without_dash

        game_words.append(word)
    
    selected_word = random.choice(game_words)
    return selected_word.upper()


def get_guess(used_letters,alphabet):
    # Returns the letter the player entered. This function makes sure the
    # player entered a single letter and not something else.
    while True:
        guess = input('Guess a letter: ').upper()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in used_letters:
            print('You have already guessed that letter. Choose again.')
        elif guess not in alphabet:
            print('Invalid character. Please try again! ')
        else:
            return guess
 
if __name__ == "__main__":
    main()
