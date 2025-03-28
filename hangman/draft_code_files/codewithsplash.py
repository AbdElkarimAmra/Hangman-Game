"""=========================================
Macalester Hangman Game
Authors: Aram Petrosyan and Karim Amra
"""

#-------------------
#IMPORT STATEMENTS
import tkinter as tk
import random
from tkinter import PhotoImage
import PIL
import PIL.Image as Image
import PIL.ImageTk as ImageTk


#DATABASE of DICTIONARIES
sports_dict={"volleyball":["Sport with a net and a ball", "Bump, set, spike!", "Beach or indoor activity", "Six players on each side"],
             "soccer":["Global ball game", "Goalposts and a net", "No hands allowed!", "Played with eleven players on each side"],
             "basketball":["Dribbling and shooting", "Slam dunks and layups", "Hoops and a round ball", "Played with 5 players on each side"]}
sports_list=list(sports_dict.keys())

library_dict={"research":["You need to understand citations", "Usually starts with a hypothesis", "Evaluates the existing literature"],
              "archives":["Access to rare materials", "Preservation and conservation", "Macalester History kept here"],
              "worldcat":["The default database Macalester students use", "Helps find items in other libraries as well", "This database isn't limited to storing only books"]}
library_list=list(library_dict.keys())


all_dictionaries=[]

# Defining a function for randomly choosing a word
def choosing_word():
    return random.choice(sports_list)



#Defining a class
class hangmanGUI:
    def __init__(self):
        # Initializing guessed letters
        self.guessed_letters = []
        # Initializing mistakes
        self.num_mistakes = 0
        #Initializing number of hints
        self.num_hints = 0
        #Choosing a random word, creating its blanks
        self.word = choosing_word()
        self.word_blanks = "_" * len(self.word)



        #---------CODE FOR THE MAIN GAME WINDOW----------
        #------------------------------------------------
        self.mainWin=tk.Tk()
        self.mainWin.title("Macalester Hangman Game")

        # THE HANGMAN IMAGES LIST
        img0 = Image.open("paintings/hard_level/0.jpg")
        self.hangedGuyImage0 = ImageTk.PhotoImage(img0)

        img1 = Image.open("paintings/hard_level/1.jpg")
        self.hangedGuyImage1 = ImageTk.PhotoImage(img1)

        img2 = Image.open("paintings/hard_level/2.jpg")
        self.hangedGuyImage2 = ImageTk.PhotoImage(img2)

        img3 = Image.open("paintings/hard_level/3.jpg")
        self.hangedGuyImage3 = ImageTk.PhotoImage(img3)

        img4 = Image.open("paintings/hard_level/4.jpg")
        self.hangedGuyImage4 = ImageTk.PhotoImage(img4)

        self.hangman_images_list = [self.hangedGuyImage0,
                               self.hangedGuyImage1,
                               self.hangedGuyImage2,
                               self.hangedGuyImage3,
                               self.hangedGuyImage4]


        #Label for the title
        titleLabel=tk.Label(self.mainWin,
                            text="Macalester Hangman Game",
                            font="Arial 30 bold",
                            relief=tk.SUNKEN,
                            bd=10)
        titleLabel.grid(row=0, column=0, columnspan=4)

        #Label for the hanged guy image
        self.hangedGuyLabel = tk.Label(self.mainWin,
                                       image=self.hangman_images_list[0],
                                       relief=tk.GROOVE,
                                       bd=10)
        self.hangedGuyLabel.grid(row=1, column=0, rowspan=5)

        #Label for showing the word
        self.word_label=tk.Label(self.mainWin,
                            font = "Arial 50",
                            text=self.word_blanks)
        self.word_label.grid(row=1, column=1, columnspan=3)

        #Label for showing description
        desc_label=tk.Label(self.mainWin,
                            font="Arial 16",
                            text="The word could be related to either the library, the campus center or the Olin-Rice building.")
        desc_label.grid(row=2, column=1, columnspan=3)

        #Entry widget
        self.guess_entry=tk.Entry(self.mainWin,
                              font="Arial 24")
        self.guess_entry.grid(row=3, column=1, columnspan=2)


        #Guess button
        self.guess_button=tk.Button(self.mainWin,
                               text="GUESS",
                               font="Arial 24",
                               command=self.checking)
        self.guess_button.grid(row=3, column=2)


        #Label for showing information
        info_label=tk.Label(self.mainWin,
                            font="Arial 16",
                            text="You're playing the game with medium difficulty.\nYou have only 1 attempt left for a mistake.\nYou have one opportunity for a hint.\nClick the button if needed.")
        info_label.grid(row=4, column=1, columnspan=2)

        #Button for the hint
        self.hint=tk.Button(self.mainWin,
                       font="Arial 24",
                       text="HINT",
                       command=self.hinting)
        self.hint.grid(row=4, column=2)

        #Label for already inputted letters
        self.inputted_letters_label=tk.Label(self.mainWin,
                               font="Arial 16",
                               relief=tk.RIDGE,
                               text=("You have already inputted the following letters: "+str(self.guessed_letters)))
        self.inputted_letters_label.grid(row=5, column=1)

        #Label for validity
        self.validity_label=tk.Label(self.mainWin,
                                text="",
                                font="Arial 16 bold",
                                fg="red")
        self.validity_label.grid(row=6, column=1)

        #Label for result
        self.result_label=tk.Label(self.mainWin,
                                   font="Arial 30")
        self.result_label.grid(row=7, column=1)

        #Label for hint
        self.hint_label=tk.Label(self.mainWin,
                                 font="Arial 16")
        self.hint_label.grid(row=8, column=1)

        # #Calling updating_hangman
        # self.updating_hangman(self.num_mistakes)

        # ---------CODE FOR THE SPLASH SCREEN-------------
        # ------------------------------------------------
        self.mainWin.withdraw()

        self.splashScreen=tk.Toplevel(self.mainWin)
        self.splashScreen.title("Welcome to the Macalester Hangamn Game")

        #Creating the heading label
        headingLabel=tk.Label(self.splashScreen,
                                   text="MACALESTER HANGMAN GAME",
                                   bd=10,
                                   font="Arial 50 bold",
                                   relief=tk.SUNKEN)
        headingLabel.grid(row=0, column=0, columnspan=2)

        #Creating the difficulty level label
        self.choose_a_level=tk.Label(self.splashScreen,
                                     text="Choose a difficulty level",
                                     bd=7,
                                     relief=tk.GROOVE,
                                     font="Arial 16",
                                     width=20)
        self.choose_a_level.grid(row=1, column=0)

        #Creating the buttons for difficult, medium and easy
        self.easy_button = tk.Button(self.splashScreen,
                                     text="Easy level",
                                     bd=3,
                                     font="Arial 16",
                                     width=20,
                                     command=self.clicked_easy)
        self.easy_button.grid(row=2,column=0)

        self.medium_button=tk.Button(self.splashScreen,
                                     text="Medium level",
                                     bd=3,
                                     font="Arial 16",
                                     width=20,
                                     command=self.clicked_medium)
        self.medium_button.grid(row=3,column=0)

        self.hard_button = tk.Button(self.splashScreen,
                                     text="Hard level",
                                     bd=3,
                                     font="Arial 16",
                                     width=20,
                                     command=self.clicked_hard)
        self.hard_button.grid(row=4, column=0)

        #Creating the START button
        self.startButton=tk.Button(self.splashScreen,
                                   text="START",
                                   bg="green",
                                   fg="white",
                                   font="Arial 20 bold",
                                   command=self.startResponse)
        self.startButton.grid(row=3, column=1)

        # -------CODE FOR THE OTHER SPLASH SCREENS--------
        # ---------------------EASY-----------------------
        self.easy_level_screen=tk.Toplevel(self.splashScreen)
        self.easy_level_screen.title("Choose dictionaries")
        self.easy_level_screen.withdraw()
        #Heading label
        self.easy_title=tk.Label(self.easy_level_screen,
                                 text="You chose the easy level,\n please proceed by choosing as many dictionaries as you'd like",
                                 font="Arial 24 bold",
                                 bd=10,
                                 relief=tk.SUNKEN)
        self.easy_title.grid(row=0, column=0, columnspan=2)

        #Dictionary buttons
        self.easy_sports_button=tk.Button(self.easy_level_screen,
                                          text="Macalester Sports",
                                          font="Arial 16",
                                          bd=5)
        self.easy_sports_button.grid(row=1,column=0)

        self.easy_library_button = tk.Button(self.easy_level_screen,
                                            text="DeWitt Wallace Library",
                                            font="Arial 16",
                                            bd=5)
        self.easy_library_button.grid(row=2, column=0)

        self.easy_drc_button = tk.Button(self.easy_level_screen,
                                            text="Digital Resources Center",
                                            font="Arial 16",
                                            bd=5)
        self.easy_drc_button.grid(row=3, column=0)

        #OK Button
        self.easy_ok_button=tk.Button(self.easy_level_screen,
                                      text="OK!",
                                      font="Arial 20 bold",
                                      bd=10,
                                      bg="green",
                                      command=self.easy_clicked_ok)
        self.easy_ok_button.grid(row=4,column=1)

        # --------------------MEDIUM-----------------------
        self.medium_level_screen = tk.Toplevel(self.splashScreen)
        self.medium_level_screen.title("Choose dictionaries")
        self.medium_level_screen.withdraw()

        # Heading label
        self.medium_title = tk.Label(self.medium_level_screen,
                                   text="You chose the medium level,\n please proceed by choosing as many dictionaries as you'd like",
                                   font="Arial 24 bold",
                                   bd=10,
                                   relief=tk.SUNKEN)
        self.medium_title.grid(row=0, column=0, columnspan=2)

        # Dictionary buttons
        self.medium_sports_button = tk.Button(self.medium_level_screen,
                                            text="Macalester Sports",
                                            font="Arial 16",
                                            bd=5,
                                            command=self.medium_clicked_sports)
        self.medium_sports_button.grid(row=1, column=0)

        self.medium_library_button = tk.Button(self.medium_level_screen,
                                             text="DeWitt Wallace Library",
                                             font="Arial 16",
                                             bd=5,
                                             command=self.medium_clicked_library)
        self.medium_library_button.grid(row=2, column=0)

        self.medium_drc_button = tk.Button(self.medium_level_screen,
                                         text="Digital Resources Center",
                                         font="Arial 16",
                                         bd=5,
                                         command=self.medium_clicked_drc)
        self.medium_drc_button.grid(row=3, column=0)

        #Description label
        self.medium_list=[]
        self.medium_description=tk.Label(self.medium_level_screen,
                                         text="You have chosen the following dictionaries:\n"+str(self.medium_list),
                                         bd=10,
                                         font="Arial 16")
        self.medium_description.grid(row=4,column=0)


        # OK Button
        self.medium_ok_button = tk.Button(self.medium_level_screen,
                                        text="OK!",
                                        font="Arial 20 bold",
                                        bd=10,
                                        bg="green",
                                        command=self.medium_clicked_ok)
        self.medium_ok_button.grid(row=4, column=1)

        # --------------------HARD------------------------
        self.hard_level_screen = tk.Toplevel(self.splashScreen)
        self.hard_level_screen.title("Choose dictionaries")
        self.hard_level_screen.withdraw()

        # Heading label
        self.hard_title = tk.Label(self.hard_level_screen,
                                     text="You chose the hard level,\n please proceed by choosing as many dictionaries as you'd like",
                                     font="Arial 24 bold",
                                     bd=10,
                                     relief=tk.SUNKEN)
        self.hard_title.grid(row=0, column=0, columnspan=2)

        # Dictionary buttons
        self.hard_sports_button = tk.Button(self.hard_level_screen,
                                              text="Macalester Sports",
                                              font="Arial 16",
                                              bd=5)
        self.hard_sports_button.grid(row=1, column=0)

        self.hard_library_button = tk.Button(self.hard_level_screen,
                                               text="DeWitt Wallace Library",
                                               font="Arial 16",
                                               bd=5)
        self.hard_library_button.grid(row=2, column=0)

        self.hard_drc_button = tk.Button(self.hard_level_screen,
                                           text="Digital Resources Center",
                                           font="Arial 16",
                                           bd=5)
        self.hard_drc_button.grid(row=3, column=0)

        # OK Button
        self.hard_ok_button = tk.Button(self.hard_level_screen,
                                          text="OK!",
                                          font="Arial 20 bold",
                                          bd=10,
                                          bg="green",
                                          command=self.hard_clicked_ok)
        self.hard_ok_button.grid(row=4, column=1)


    def clicked_easy(self):
        self.easy_level_screen.deiconify()
    def clicked_medium(self):
        self.medium_level_screen.deiconify()
    def clicked_hard(self):
        self.hard_level_screen.deiconify()
    def easy_clicked_ok(self):
        self.easy_level_screen.withdraw()
    def medium_clicked_ok(self):
        self.medium_level_screen.withdraw()
    def hard_clicked_ok(self):
        self.hard_level_screen.withdraw()
    def startResponse(self):
        """Takes no inputs. Shows the mainWin and hides the splashScreen"""
        self.mainWin.deiconify()
        self.splashScreen.withdraw()

    def medium_clicked_sports(self):
        if "Macalester Sports" in self.medium_list:
            self.medium_list.remove("Macalester Sports")
            self.medium_description.config(text= "You have chosen the following dictionaries:\n" + str(self.medium_list))
            if sports_list in all_dictionaries:
                all_dictionaries.remove(sports_list)
                print(all_dictionaries)
        else:
            self.medium_list.append("Macalester Sports")
            self.medium_description.config(text="You have chosen the following dictionaries:\n" + str(self.medium_list))
            if sports_list not in all_dictionaries:
                all_dictionaries.append(sports_list)
                print(all_dictionaries)

    def medium_clicked_library(self):
        if "DeWitt Wallace Library" in self.medium_list:
            self.medium_list.remove("DeWitt Wallace Library")
            self.medium_description.config(text= "You have chosen the following dictionaries:\n" + str(self.medium_list))
            if library_list in all_dictionaries:
                all_dictionaries.remove(library_list)
                print(all_dictionaries)
        else:
            self.medium_list.append("DeWitt Wallace Library")
            self.medium_description.config(text="You have chosen the following dictionaries:\n" + str(self.medium_list))
            if library_list not in all_dictionaries:
                all_dictionaries.append(library_list)
                print(all_dictionaries)

    def medium_clicked_drc(self):
        if "Digital Resources Center" in self.medium_list:
            self.medium_list.remove("Digital Resources Center")
            self.medium_description.config(text= "You have chosen the following dictionaries:\n" + str(self.medium_list))
        else:
            self.medium_list.append("Digital Resources Center")
            self.medium_description.config(text="You have chosen the following dictionaries:\n" + str(self.medium_list))
    #Defining a function to update the hangman display
    def updating_hangman(self, mistakes):
        self.hangedGuyLabel.config(image=self.hangman_images_list[mistakes])


    #Creating a function to check the validity of the user's input
    def validInput(self):
        if len(self.guess_entry.get())>1:
            respond_text="You can only input one character!"
            self.validity_label.config(text=respond_text)
            self.guess_entry.delete(0, tk.END)
            vallid=False
        elif self.guess_entry.get()=="":
            respond_text = "You haven't inputted anything! Input something before clicking the button"
            self.validity_label.config(text=respond_text)
            self.guess_entry.delete(0, tk.END)
            vallid = False
        elif self.guess_entry.get() in self.guessed_letters:
            respond_text = "You have already tried this letter. Try something else!"
            self.validity_label.config(text=respond_text)
            self.guess_entry.delete(0, tk.END)
            vallid = False
        else:
            vallid=True
            self.validity_label.config(text="")

        return vallid

    #Defining a function to check if the letter is in the word or not
    def checking(self):
        assert self.validInput() == True
        guess=self.guess_entry.get().lower()
        self.guess_entry.delete(0, tk.END)
        if guess in self.word:
            for i in range(len(self.word)):
                if self.word[i] == guess:
                    self.word_blanks = self.word_blanks[:i] + guess + self.word_blanks[i + 1:]
            self.word_label.config(text=self.word_blanks)
            self.guessed_letters.append(guess)
            self.inputted_letters_label.config(text="You have already inputted the following letters" + str(self.guessed_letters))
            if "_" not in self.word_blanks:
                self.ending("Win")
        else:
            self.guessed_letters.append(guess)
            self.inputted_letters_label.config(text="You have already inputted the following letters" + str(self.guessed_letters))
            self.num_mistakes += 1
            self.updating_hangman(self.num_mistakes)
            if self.num_mistakes == 4:
                self.ending("lose")

    #Defining an ending function
    def ending(self, result):
        if result == "Win":
            result_text="You win the game!"
            self.hint_label.config(text="")
        else:
            result_text="You lost the game and the word was "+self.word
            self.hint_label.config(text="")
        self.result_label.config(text=result_text)
        self.guess_entry.config(state="disabled")
        self.guess_button.config(state="disabled")

    #Defining a hinting function
    def hinting(self):
        if self.num_hints>=2:
            self.hint.config(state="disabled")
            self.hint_label.config(text="Sorry, you don't have any hints left")
        else:
            self.num_hints+=1
            random_hint = random.choice(sports_dict[self.word])
            sports_dict[self.word].remove(random_hint)
            self.hint_label.config(text="HINT:"+random_hint)
    def go(self):
        """Runs the whole class whenever .go() is called"""
        self.mainWin.mainloop()


#SCRIPT
if __name__ == '__main__':
    game=hangmanGUI()
    game.go()
