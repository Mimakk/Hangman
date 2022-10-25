from project import hangman, without_dash, word_dashes
from hangman_visual import lives_visual


def test_hangman():
    assert hangman(9) == lives_visual[9]
    assert hangman(7) == lives_visual[7]
    assert hangman(0) == lives_visual[0]


def test_without_dash():
    assert without_dash("Hello-World!") == "Hello World!"
    assert without_dash("Mina") == "Mina"
    assert without_dash("I-love-my-wife") == "I love my wife"

used_letters = ['a', 'b', 'c', 'd', 'i']

def test_word_dashes():
    assert word_dashes("hey",used_letters) == ['-', '-', '-']
    assert word_dashes("Mina",used_letters) == ['-', 'i', '-', 'a']
    assert word_dashes("Rukiye",used_letters) == ['-', '-', '-', 'i', '-', '-']
    assert word_dashes("",used_letters) == []
    
