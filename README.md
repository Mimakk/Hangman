# Hangman Game

### Description:
The final project is a hangman game made using python and is playable in the terminal by running the project.py file.
The words are randomly choosen by jason file (https://www randomlists.com/data/words.json). You have 9 lives and a visual hangman assingned to your lives.

Program requires a letter from you to guess a word. Every time you should enter just a letter. If the letter you give is the same letter as you gave program prints an error massage.

Basically program loops throug every word in json file and look if there is a - between words if so remove it with space. After that program randomly choose a word from wordlist.
In that chosen word for every letter program prints - untill the letter guessed true.


<h1 align='center'><b>How To Run</b></h1>
In terminal write "python project.py" to run project and "pytest project.py" to run test code.

### Requirements:
to run this project you need pytest, string, random, json, requests

## Description #2
My project is implemented in Python. It is a simple, command-line interface application program.

The `main()` function is located in **project.py** file as well as other functions. They are nested on the same indentation level as main function (an exception is `load_data_from_csv()` function which is executable from `save_pdf()`. Each of the functions is accompanied by tests that can be executed with `pytest`, and they are located in **test_project.py**. The functions have the same name as custom functions, they are prepended with `test_` (for instance, `test_create_csv()` is a test for `create_csv()` function). Required `pip`-installable libraries are listed in `requirements.txt`.
## The manual
1. Open the terminal emulator (Terminal, Windows Console etc.).
2. `cd` to `project` directory.
3. Type the following:
```
python project.py
```
4. Type a space after typing `python project.py` you can start playing by giving one only one character.
5. Confirm by "enter" key.

## What files are included:
- project.py,
- test_project.py,
- requirements.txt,
- hangman_visual.py,
- README.md.
