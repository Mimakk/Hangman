import string
from hangman_visual import lives_visual
import random
import json
import requests

def main():
    
    # Getting worlds from json
    response = requests.get(
        "https://www.randomlists.com/data/words.json"
    )
    o = response.json()
    
    # Assigning the leters, used letter, and alphabet
    word = get_word(o)
    word_letters = set(word) # the set of letters in the word
    alphabet = set(string.ascii_uppercase) # Making the set of alphabetical characters
    used_letters = set() # what the user has guessed
    lives = 9 # assigning the lives of hangman
    
    # Getting user input
    while len(word_letters) > 0 and lives > 0:
        # Letters used
        # " ".join(['a', 'b', 'cd']) --> 'a b cd'
        print("You have", lives, "lives left and you have used these letters: ", " ".join(used_letters))
        
        # Checking if the letter is in used letters if so print letter else print - 
        word_list = word_dashes(word,used_letters)
        # Getting the visual correspond of lives of hangman
        print(hangman(lives))
        print('Current word: ', " ".join(word_list))
        
        # Assingning letter that user gives
        user_letter = get_guess(used_letters,alphabet)
        # If the letter that user gave us is in alphabet but not used yet add the letter in used letters set
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            # If the letter that user gave us is in letters of word remove letter from user letter
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
    
def word_dashes(word,used_letters):
    word_list = [letter if letter in used_letters else '-' for letter in word]
    return word_list
    
def hangman(lives):
    return lives_visual[lives]
    
def get_word(o):
    game_words=[]
    for word in o["data"]:
        
        word = without_dash(word)
        
        game_words.append(word)
    
    selected_word = random.choice(game_words)
    return selected_word.upper()


def without_dash(word):
    # This looks every word in wordlist and every letter in words if
    # there is a - in word replaces it with space and assign it with 
    # new_word
    for letter in word:
            if "-" in letter:
                without_dash = word.replace("-", " ")
                word = without_dash
    return word


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
