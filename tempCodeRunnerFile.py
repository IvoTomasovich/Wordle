
import random

from WordleWordlist import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_ROWS, N_COLS
from WordleGraphics import CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR


def enter_action(guessedword):
    """ This function is called any time the enter button
    is clicked/typed in the game. guessedword is the player's most
    recent guess which needs to be checked.
    """

    global game_complete
    if guessedword.lower() not in FIVE_LETTER_WORDS:
        gw.show_message("Not in word list.")
        return
    if guessedword.lower() in words_attempted:
        gw.show_message("Already guessed.")  # These 2 if statements check if the guessed word is in the list
        return
    solution_number = 0  # Used to iterate between columns
    break_caller = 0  # Used later to break out of a loop
    if game_complete is False and guessedword.lower() != solution and guessedword.lower() in FIVE_LETTER_WORDS:  # Main part here, checks if game still needs to continue, and if it can via the word input
        if guessedword.lower() not in words_attempted:
            words_attempted.append(guessedword.lower())  # Adds word to list if not in already
        gw.set_current_row(len(words_attempted) - 1)  # Sets row via amount of items in the words guessed list (-1 for accuracy)
        guessedword = guessedword.lower()  # lowercases guessedword
        guesses.append(len(words_attempted))
        for item in guessedword.lower():  # This loop goes through all the characters in the word
            gw.set_square_letter(len(words_attempted) - 1, solution_number, item.upper())  # sets the square
            if item == solution[solution_number]:  # changes the color of the square and key to green
                gw.set_square_color(len(words_attempted) - 1, solution_number, CORRECT_COLOR)
                solution_number += 1
                gw.set_key_color(item.upper(), CORRECT_COLOR)
            elif item != solution[solution_number] and item in solution: # changes the color of the square and key to yellow
                gw.set_square_color(len(words_attempted) - 1, solution_number, PRESENT_COLOR)
                solution_number += 1
                if gw.get_key_color(item.upper()) != CORRECT_COLOR: # checks if the key color was already set as correct, so nothing is overwritten
                    gw.set_key_color(item.upper(), PRESENT_COLOR)
            else: # changes the color of the square and key to grey
                gw.set_square_color(len(words_attempted) - 1, solution_number, MISSING_COLOR)
                solution_number += 1
                if gw.get_key_color(item.upper()) != CORRECT_COLOR and gw.get_key_color(item.upper()) != PRESENT_COLOR:
                    gw.set_key_color(item.upper(), MISSING_COLOR)
        if len(words_attempted) == 6 and guessedword != solution:  # This is what happens when you suck
            gw.show_message("Game Over")
            with open('Wordle-log.txt', 'a') as my_file:
                my_file.write(f'{solution},L,{len(guesses)}\n')
            printer = open("Wordle-log.txt", "r+")
            printers = printer.readlines()
            for line in printers:  # How all this works is explained in the lines 98, 101, and 110
                num_of_wins.append(line.split(','))
            for item in num_of_wins:
                if 'W' in item:
                    actual_num_of_wins.append('W')
                if 'L' in item:
                    actual_num_of_losses.append('L')
            printer.close()
            print(f'Number of Wins: {len(actual_num_of_wins)}, Number of Losses: {len(actual_num_of_losses)}')
            for letter in guessedword:  # Sets the keys to the correct color
                gw.set_key_color(letter.upper(), MISSING_COLOR)
                gw.get_key_color(letter.upper())
            return
    if guessedword.lower() == solution:  # Sets game complete equal to true so you can exit the game
        guesses.append(len(words_attempted))
        game_complete = True
        game_complete_list.append("yay")
        words_attempted.append(guessedword.lower())
        with open('Wordle-log.txt', 'a') as my_file:  # opens file to add the line with the word, W, and num of guesses
            my_file.write(f'{solution},W,{len(guesses)}\n')
        printer = open("Wordle-log.txt", "r+")
        printers = printer.readlines()  # this chunk takes eah line in the file, adds it to a list, then loops through each item to check if win or loss to add it to a specific win or loss list so the length of those lists can be printed later
        for line in printers:
            num_of_wins.append(line.split(','))
        for item in num_of_wins:
            if 'W' in item:
                actual_num_of_wins.append('W')
            if 'L' in item:
                actual_num_of_losses.append('L')
        printer.close()
        print(f'Number of Wins: {len(actual_num_of_wins)}, Number of Losses: {len(actual_num_of_losses)}')  # Prints win loss record
        for letter in guessedword.lower():  # loops through the entire word so you can set it to the correct colors
            gw.set_square_color(len(words_attempted) - 1, solution_number, CORRECT_COLOR)
            gw.set_key_color(letter.upper(), CORRECT_COLOR)
            gw.get_key_color(letter.upper())
            solution_number += 1
            break_caller += 1
            gw.show_message("You win!")
        if game_complete is True:
            return
    gw.set_current_row(len(words_attempted))  # sets current row to make sure it doesn't get overwritten
    if guessedword.lower() not in FIVE_LETTER_WORDS:  # tells you if word in list or not
        gw.show_message("Not in word list")
    else:
        gw.show_message("")







solution = random.choice(FIVE_LETTER_WORDS)  # Gets random word
print(solution)  # Used for tests
words_attempted = []  # Used to store all the words that were attempted
global game_complete  # Used to check if the game is complete
game_complete = False
game_complete_list = []  # Used just in case to check if a game is complete
guesses = []  # Keeps track of the amount of guesses made per game
num_of_wins = []  # puts the whole file of text per line in the text file and splits it into items for the list
actual_num_of_wins = []  # Used to track number of wins
actual_num_of_losses = []  # Used to track number of losses
possibilities = []  # In progress, but used for 6.2

gw = WordleGWindow()
gw.add_enter_listener(enter_action)
