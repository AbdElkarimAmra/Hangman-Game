import tkinter as tk
import random

#DATABASE of DICTIONARIES
sports_dict={"volleyball":["Sport with a net and a ball", "Bump, set, spike!", "Beach or indoor activity", "Six players on each side"],
             "soccer":["Global ball game", "Goalposts and a net", "No hands allowed!", "Played with eleven players on each side"],
             "basketball":["Dribbling and shooting", "Slam dunks and layups", "Hoops and a round ball", "Played with 5 players on each side"]}
sports_list=list(sports_dict.keys())

#The hangman itself, FOR NOW IT'S DONE WITH KEYBOARD CHARACTERS
hangman_art = [
    "   +---+\n   |   |\n       |\n       |\n       |\n       |\n=========",
    "   +---+\n   |   |\n   O   |\n       |\n       |\n       |\n=========",
    "   +---+\n   |   |\n   O   |\n   |   |\n       |\n       |\n=========",
    "   +---+\n   |   |\n   O   |\n  /|   |\n       |\n       |\n=========",
    "   +---+\n   |   |\n   O   |\n  /|\\  |\n       |\n       |\n=========",
    "   +---+\n   |   |\n   O   |\n  /|\\  |\n  /    |\n       |\n=========",
    "   +---+\n   |   |\n   O   |\n  /|\\  |\n  / \\  |\n       |\n========="
]

#Defining a function to take a random word = meaning take a random key from the dictionary
def choosing_word():
    return random.choice(sports_list)

#Defining a function to update the hangman display
def updating_hangman(mistakes):
    hangman_label.config(text=hangman_art[mistakes])

#Creating a function to check the validity of the user's input
def validInput():
    global guess_entry
    if len(guess_entry.get())>1:
        respond_text="You can only input one character!"
        validity_label.config(text=respond_text)
        guess_entry.delete(0, tk.END)
        vallid=False
    elif guess_entry.get()=="":
        respond_text="You haven't inputted anything! Input something before clicking the button"
        validity_label.config(text=respond_text)
        guess_entry.delete(0, tk.END)
        vallid=False
    elif guess_entry.get() in guessed_letters:
        respond_text="You have already tried this letter. Try something else!"
        validity_label.config(text=respond_text)
        guess_entry.delete(0, tk.END)
        vallid=False
    else:
        vallid=True
        validity_label.config(text="")
        guess_entry.delete(0, tk.END)
    return vallid


#Defining a function to see if the letter is in the word or not
def checking(guess):
    assert validInput() == True
    global word_blanks
    global guessed_letters
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                word_blanks=word_blanks[:i]+guess+word_blanks[i+1:]
        word_label.config(text=word_blanks)
        guessed_letters.append(guess)
        inputted_letters_label.config(text="You have already inputted the following letters"+str(guessed_letters))
        if "_" not in word_blanks:
            ending("Win")
    else:
        guessed_letters.append(guess)
        inputted_letters_label.config(text="You have already inputted the following letters" + str(guessed_letters))
        global num_mistakes
        num_mistakes += 1
        updating_hangman(num_mistakes)
        if num_mistakes == 6:
            ending("lose")

#Defining the ending function
def ending(result):
    if result == "Win":
        result_text="You win the game!"
    else:
        result_text="You lose the game and the word was"+word
    result_label.config(text=result_text)
    guess_entry.config(state="disabled")
    guess_button.config(state="disabled")




#Creating the screen
game = tk.Tk()
game.title("Macalester Hangman Game")

#Constructing the screen
hangman_label=tk.Label(game, font=("Arial", 16))
hangman_label.grid(row=0, column=0)

#the INDICES
word=choosing_word()
word_blanks="_"*len(word)
word_label = tk.Label(game, text=word_blanks, font=("Arial", 24))
word_label.grid(row=1, column=0)

#The entry and button widgets
guessed_letters=[]
guess_entry=tk.Entry(game, width=3, font=("Arial", 24))
guess_entry.grid(row=2, column=0)
guess_entry.bind('<Return>', checking)
#guessed_letters.append(guess_entry.get())
guess_button=tk.Button(game, text="Guess", command=lambda:checking(guess_entry.get().lower()))
guess_button.grid(row=2, column=1)


#Creating the label indicating whether one WON or one LOST
result_label=tk.Label(game, font=("Arial", 24))
result_label.grid(row=3, column=0)

#creating the validity label
validity_label=tk.Label(game, font=("Arial", 16))
validity_label.grid(row=4, column=0)


#Creating a label showing alraedy inputted letters
you_have_alraedy="You have already inputted the following letters"+str(guessed_letters)
inputted_letters_label=tk.Label(game, font=("Arial", 16), text=you_have_alraedy)
inputted_letters_label.grid(row=5, column=0)


#INITIALIZATIONS
num_mistakes=0
updating_hangman(num_mistakes)



#Go
game.mainloop()