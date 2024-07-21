**Wordle Game**
This repository contains a Python implementation of the popular word puzzle game, Wordle. The game randomly selects a five-letter word, and the player has six attempts to guess it correctly. After each guess, the game provides feedback indicating which letters are correctly placed, which letters are in the word but misplaced, and which letters are not in the word.

**Features**
**Graphical User Interface**: The game uses a Tkinter-based GUI for an interactive experience.
**Feedback on Guesses**: Letters are color-coded to indicate correct, misplaced, and incorrect letters.
**Win/Loss Record**: The game keeps track of wins and losses and logs them to a file.

**Files**
**wordle.py**
This is the main game file. It initializes the game, handles user input, checks guesses, and provides feedback.

**WordleGraphics.py**
This file contains the WordleGWindow class, which manages the graphical display for the game. It includes methods for setting and getting the color and letter of each square, handling keyboard input, and displaying messages.

**Getting Started**
**Prerequisites**
Python 3.x
Tkinter 

**Installation**
Clone the repository:
git clone https://github.com/your-username/wordle-game.git
cd wordle-game

Install the required dependencies (if any):
pip install -r requirements.txt

**Running the Game**
To start the game, run the following command in your terminal:
python wordle.py

**How to Play**
**Objective**: Guess the five-letter word chosen by the game.
**Input**: Type your guess using the keyboard and press Enter.
**Feedback**:
**Green**: Correct letter in the correct position.
**Yellow**: Correct letter in the wrong position.
**Gray**: Incorrect letter.
**Win/Loss**: You have six attempts to guess the word. If you guess correctly, you win. If you fail to guess within six attempts, you lose. The game logs the result to a file.

**Logging**
The game logs each game result to Wordle-log.txt with the format word, result, guesses, where result is either W (win) or L (loss), and guesses is the number of attempts made.
