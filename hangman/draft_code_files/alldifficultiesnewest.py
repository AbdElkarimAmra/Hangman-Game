"""
================================================
The Macalester Hangman Game
Authors: Aram Petrosyan and Karim Amra
================================================
"""

#-------------------
#IMPORT STATEMENTS
import tkinter as tk
import random
from tkinter import PhotoImage     #Provided by Professor Ernst
import PIL                         #Provided by Professor Ernst
import PIL.Image as Image          #Provided by Professor Ernst
import PIL.ImageTk as ImageTk      #Provided by Professor Ernst
from tkinter import messagebox
import string


#Defining a class
class hangmanGUI:
    def __init__(self):
        # DATABASE of DICTIONARIES
        self.sports_dict = {"volleyball": ["Sport with a net and a ball", "Bump, set, spike!", "Beach or indoor activity", "Six players on each side"],
                            "soccer": ["Global ball game", "Goalposts and a net", "No hands allowed!", "Played with eleven players on each side"],
                            "basketball": ["Dribbling and shooting", "Slam dunks and layups", "Hoops and a round ball", "Played with 5 players on each side"]}
        self.sports_list = list(self.sports_dict.keys())

        self.library_dict = {"research": ["You need to understand citations", "Usually starts with a hypothesis", "Evaluates the existing literature"],
                             "archives": ["Access to rare materials", "Preservation and conservation", "Macalester History kept here"],
                             "worldcat": ["The default database Macalester students use", "Helps find items in other libraries as well", "This database isn't limited to storing only books"]}
        self.library_list = list(self.library_dict.keys())

        self.drc_dict={"llama":["They love this animal in the DRC","It kind of looks like a camel","Has a long neck, but isn't a giraffe"],
                       "digitization":["This word means converting something to a digital format","This process accelerates future efficiency","This process facilitates easy access from anywhere."],
                       "tinkercad":["Often used in schools and educational settings", "Popular online platform for designing 3D models", "A Computer-Aided Design (CAD) tool"]}
        self.drc_list=list(self.drc_dict.keys())

        # Initializing guessed letters
        self.guessed_letters = []
        # Initializing mistakes and number of hints
        self.num_mistakes = 0
        self.allowablemistakes = 0
        self.allowablehints = 0
        #Initializing number of hints
        self.num_hints = 0
        #Initializing chosen dictionaries
        self.all_dictionaries = ["hm"]
        # STORING THE DIFFICULTY LEVEL
        self.difficulty_level = "Default"



        #---------CODE FOR THE MAIN GAME WINDOW----------
        #------------------------------------------------
        self.mainWin=tk.Tk()
        self.mainWin.title("The Macalester Hangman Game")

        # THE HANGMAN IMAGES
        hardimg0 = Image.open("paintings/hard_level/0.jpg")
        self.hangedGuyImage0hard = ImageTk.PhotoImage(hardimg0)
        hardimg1 = Image.open("paintings/hard_level/1.jpg")
        self.hangedGuyImage1hard = ImageTk.PhotoImage(hardimg1)
        hardimg2 = Image.open("paintings/hard_level/2.jpg")
        self.hangedGuyImage2hard = ImageTk.PhotoImage(hardimg2)
        hardimg3 = Image.open("paintings/hard_level/3.jpg")
        self.hangedGuyImage3hard = ImageTk.PhotoImage(hardimg3)
        hardimg4 = Image.open("paintings/hard_level/4.jpg")
        self.hangedGuyImage4hard = ImageTk.PhotoImage(hardimg4)

        medimg0 = Image.open("paintings/medium_level/0.jpg")
        self.hangedGuyImage0med = ImageTk.PhotoImage(medimg0)
        medimg1 = Image.open("paintings/medium_level/1.jpg")
        self.hangedGuyImage1med = ImageTk.PhotoImage(medimg1)
        medimg2 = Image.open("paintings/medium_level/2.jpg")
        self.hangedGuyImage2med = ImageTk.PhotoImage(medimg2)
        medimg3 = Image.open("paintings/medium_level/3.jpg")
        self.hangedGuyImage3med = ImageTk.PhotoImage(medimg3)
        medimg4 = Image.open("paintings/medium_level/4.jpg")
        self.hangedGuyImage4med = ImageTk.PhotoImage(medimg4)
        medimg5 = Image.open("paintings/medium_level/5.jpg")
        self.hangedGuyImage5med = ImageTk.PhotoImage(medimg5)
        medimg6 = Image.open("paintings/medium_level/6.jpg")
        self.hangedGuyImage6med = ImageTk.PhotoImage(medimg6)
        medimg7 = Image.open("paintings/medium_level/7.jpg")
        self.hangedGuyImage7med = ImageTk.PhotoImage(medimg7)

        easyimg0 = Image.open("paintings/easy_level/0.jpg")
        self.hangedGuyImage0easy = ImageTk.PhotoImage(easyimg0)
        easyimg1 = Image.open("paintings/easy_level/1.jpg")
        self.hangedGuyImage1easy = ImageTk.PhotoImage(easyimg1)
        easyimg2 = Image.open("paintings/easy_level/2.jpg")
        self.hangedGuyImage2easy = ImageTk.PhotoImage(easyimg2)
        easyimg3 = Image.open("paintings/easy_level/3.jpg")
        self.hangedGuyImage3easy = ImageTk.PhotoImage(easyimg3)
        easyimg4 = Image.open("paintings/easy_level/4.jpg")
        self.hangedGuyImage4easy = ImageTk.PhotoImage(easyimg4)
        easyimg5 = Image.open("paintings/easy_level/5.jpg")
        self.hangedGuyImage5easy = ImageTk.PhotoImage(easyimg5)
        easyimg6 = Image.open("paintings/easy_level/6.jpg")
        self.hangedGuyImage6easy = ImageTk.PhotoImage(easyimg6)
        easyimg7 = Image.open("paintings/easy_level/7.jpg")
        self.hangedGuyImage7easy = ImageTk.PhotoImage(easyimg7)
        easyimg8 = Image.open("paintings/easy_level/8.jpg")
        self.hangedGuyImage8easy = ImageTk.PhotoImage(easyimg8)
        easyimg9 = Image.open("paintings/easy_level/9.jpg")
        self.hangedGuyImage9easy = ImageTk.PhotoImage(easyimg9)
        easyimg10 = Image.open("paintings/easy_level/10.jpg")
        self.hangedGuyImage10easy= ImageTk.PhotoImage(easyimg10)

        self.easy_hangman_images_list = [self.hangedGuyImage0easy,
                                           self.hangedGuyImage1easy,
                                           self.hangedGuyImage2easy,
                                           self.hangedGuyImage3easy,
                                           self.hangedGuyImage4easy,
                                           self.hangedGuyImage5easy,
                                           self.hangedGuyImage6easy,
                                           self.hangedGuyImage7easy,
                                           self.hangedGuyImage8easy,
                                           self.hangedGuyImage9easy,
                                           self.hangedGuyImage10easy]

        self.medium_hangman_images_list = [self.hangedGuyImage0med,
                                         self.hangedGuyImage1med,
                                         self.hangedGuyImage2med,
                                         self.hangedGuyImage3med,
                                         self.hangedGuyImage4med,
                                         self.hangedGuyImage5med,
                                         self.hangedGuyImage6med,
                                         self.hangedGuyImage7med]

        self.hard_hangman_images_list = [self.hangedGuyImage0hard,
                                         self.hangedGuyImage1hard,
                                         self.hangedGuyImage2hard,
                                         self.hangedGuyImage3hard,
                                         self.hangedGuyImage4hard]

        # Label for the title
        titleLabel = tk.Label(self.mainWin,
                              text="The Macalester Hangman Game",
                              font="Arial 30 bold",
                              relief=tk.SUNKEN,
                              bd=10)
        titleLabel.grid(row=0, column=0, pady=20, padx=20)

        # Label for the hanged guy image
        self.hangedGuyLabel = tk.Label(self.mainWin,
                                       image=self.hard_hangman_images_list[0],
                                       relief=tk.GROOVE,
                                       bd=10)
        self.hangedGuyLabel.grid(row=1, column=0, rowspan=5, padx=10, pady=10)

        # Label for showing description
        self.desc_label = tk.Label(self.mainWin,
                              font="Arial 16")
        self.desc_label.grid(row=2, column=1, columnspan=3, padx=5, pady=5)

        # Entry widget
        self.guess_entry = tk.Entry(self.mainWin,
                                    font="Arial 24",
                                    width=5,
                                    justify="center")
        self.guess_entry.grid(row=3, column=1)

        # Guess button
        self.guess_button = tk.Button(self.mainWin,
                                      text="GUESS",
                                      font="Arial 24",
                                      command=self.checking,
                                      width=10)
        self.guess_button.grid(row=3, column=2, padx=5, pady=5)

        # Label for showing information
        self.info_label = tk.Label(self.mainWin,
                              font="Arial 16")
        self.info_label.grid(row=4, column=1)

        #Label for showing how many mistakes are left
        self.mistakes_label = tk.Label(self.mainWin,
                                       font="Arial 16")
        self.mistakes_label.grid(row=5, column=1)

        #Label for showing how many hints are left
        self.hints_left_label=tk.Label(self.mainWin,
                                       font="Arial 16")
        self.hints_left_label.grid(row=5, column=2, padx=5, pady=5)

        # Button for the hint
        self.hint = tk.Button(self.mainWin,
                              font="Arial 24",
                              text="HINT",
                              command=self.hinting,
                              width=10)
        self.hint.grid(row=4, column=2)

        # Label for already inputted letters
        self.inputted_letters_label = tk.Label(self.mainWin,
                                               font="Arial 16",
                                               relief=tk.RIDGE,
                                               text=("You have already inputted the following letters:\n" + self.cleanString(str(self.guessed_letters))))
        self.inputted_letters_label.grid(row=6, column=1, columnspan=3)

        # Label for validity
        self.validity_label = tk.Label(self.mainWin,
                                       text="",
                                       font="Arial 16 bold",
                                       fg="red")
        self.validity_label.grid(row=7, column=0, columnspan=3)

        # Label for result
        self.result_label = tk.Label(self.mainWin)
        self.result_label.grid(row=8, column=0, columnspan=3)

        # Label for hint
        self.hint_label = tk.Label(self.mainWin,
                                   font="Arial 25")
        self.hint_label.grid(row=9, column=0, columnspan=3)

        # Label for showing the word
        self.word_label = tk.Label(self.mainWin,
                                   font="Arial 50")
        self.word_label.grid(row=1, column=1, columnspan=3)

        #Button for restarting
        self.restart_button=tk.Button(self.mainWin,
                                      text="RESTART",
                                      font="Arial 15",
                                      command=self.restartResponse,
                                      width=10)
        self.restart_button.grid(row=0, column=1)

        #Button for quitting
        self.quit_button=tk.Button(self.mainWin,
                                   text="QUIT",
                                   font="Arial 15",
                                   command=self.quitResponse,
                                   width=10)
        self.quit_button.grid(row=0, column=2)


        # ---------CODE FOR THE SPLASH SCREEN-------------
        # ------------------------------------------------
        self.mainWin.withdraw()

        self.splashScreen=tk.Toplevel(self.mainWin)
        self.splashScreen.title("Welcome to the Macalester Hangman Game")

        #Creating the heading label
        headingLabel=tk.Label(self.splashScreen,
                                   text="THE MACALESTER HANGMAN GAME",
                                   bd=10,
                                   font="Arial 50 bold",
                                   relief=tk.SUNKEN)
        headingLabel.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        #Creating the difficulty level label
        self.choose_a_level=tk.Label(self.splashScreen,
                                     text="Choose a difficulty level:",
                                     font="Arial 20",
                                     width=20)
        self.choose_a_level.grid(row=1, column=0, pady=2)

        #Creating the buttons for difficult, medium and easy
        self.easy_button = tk.Button(self.splashScreen,
                                     text="Easy level",
                                     bd=3,
                                     font="Arial 16",
                                     width=20,
                                     command=self.clicked_easy)
        self.easy_button.grid(row=2,column=0, pady=5)

        self.medium_button=tk.Button(self.splashScreen,
                                     text="Medium level",
                                     bd=3,
                                     font="Arial 16",
                                     width=20,
                                     command=self.clicked_medium)
        self.medium_button.grid(row=3,column=0, pady=5)

        self.hard_button = tk.Button(self.splashScreen,
                                     text="Hard level",
                                     bd=3,
                                     font="Arial 16",
                                     width=20,
                                     command=self.clicked_hard)
        self.hard_button.grid(row=4, column=0, pady=5)

        #Creating the START button
        self.startButton=tk.Button(self.splashScreen,
                                   text="START",
                                   bg="red",
                                   fg="white",
                                   font="Arial 25 bold",
                                   command=self.startResponse,
                                   width=8)
        self.startButton.grid(row=1, column=1)

        #Craeting the INSTRUCTIONS button
        self.instructions=tk.Button(self.splashScreen,
                                    text="Instructions",
                                    font="Arial 15",
                                    command=self.clicked_instructions,
                                    width=15)
        self.instructions.grid(row=2, column=1)

        # Creating a QUIT button
        self.quitsplash = tk.Button(self.splashScreen,
                                    text="Quit the game",
                                    font="Arial 15",
                                    command=self.quitResponse,
                                    width=15)
        self.quitsplash.grid(row=3, column=1)



        #------CODE FOR THE INSTRUCTIONS SCREEN---------
        #-----------------------------------------------
        self.instructions_screen=tk.Toplevel(self.splashScreen)
        self.instructions_screen.title("Instructions")
        self.instructions_screen.withdraw()


        instr_title=tk.Label(self.instructions_screen,
                             text="INSTRUCTIONS",
                             font="Arial 25 bold",
                             relief=tk.SUNKEN,
                             bd=10)
        instr_title.grid(row=0, column=0, pady=10)

        instructions_text = tk.Label(self.instructions_screen,
                                     text="\nWelcome to the Macalester Hangman Game and thank you for playing!\n"
                                          "The classic game was re-created in Macaelester's context by COMP 123 students Aram Petrosyan and Karim Amra.\n\n"
                                          "To start the game you need to have chosen a difficulty level and a dictionary (or multiple dictionaries).\n"
                                          "When choosing dictionaries - you can always click on the same dictionary again to remove the choice.\n"
                                          "After choosing dictionaries - you won't be able to configure settings again unless you restart the whole game through\n"
                                          "the 'Change Settings' button. After hitting the 'START' button - the game will start. You'll see information about the\n"
                                          "word, several buttons for guessing and requesting hints, as well as restarting or quitting the game. You'll be notified\n"
                                          "every time your input will be invalid (e.g. in case it's not a letter, or is a lettee you've already inputted before).\n"
                                          "You'll also see on the screen the number of hints and the number of allowable mistakes that you still have (those are\n"
                                          "based on the difficulty level you've chosen). You'll also see a list of letters you've alraedy inputted to remember them.\n\n"
                                          "You can contact the following emails to report any bugs and issues, as well as to provide feedback:\n"
                                          "apetrosy@macalester.edu  &  kamra@macalester.edu\n\n\n"
                                          "THANK YOU\n\n\n\n",
                                     font="Arial 10")
        instructions_text.grid(row=1, column=0, padx=30)

        self.back_to_menu_button=tk.Button(self.instructions_screen,
                                             text="Back to the main menu",
                                             font="Arial 8",
                                             relief=tk.GROOVE,
                                             bd=3,
                                             command=self.clicked_back)
        self.back_to_menu_button.grid(row=2,column=0, pady=10)


        # -------CODE FOR THE OTHER SPLASH SCREENS--------
        # ---------------------EASY-----------------------
        self.easy_level_screen = tk.Toplevel(self.splashScreen)
        self.easy_level_screen.title("Choose dictionaries")
        self.easy_level_screen.withdraw()

        # Heading label
        self.easy_title = tk.Label(self.easy_level_screen,
                                     text="You chose the easy level,\n please proceed by choosing as many dictionaries as you'd like",
                                     font="Arial 24 bold",
                                     bd=10,
                                     relief=tk.SUNKEN)
        self.easy_title.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        # Dictionary buttons
        self.easy_sports_button = tk.Button(self.easy_level_screen,
                                              text="Macalester Sports",
                                              font="Arial 16",
                                              bd=5,
                                              command=self.easy_clicked_sports,
                                              width=30)
        self.easy_sports_button.grid(row=1, column=0, pady=5)

        self.easy_library_button = tk.Button(self.easy_level_screen,
                                               text="DeWitt Wallace Library",
                                               font="Arial 16",
                                               bd=5,
                                               command=self.easy_clicked_library,
                                               width=30)
        self.easy_library_button.grid(row=2, column=0, pady=5)

        self.easy_drc_button = tk.Button(self.easy_level_screen,
                                           text="Digital Resources Center",
                                           font="Arial 16",
                                           bd=5,
                                           command=self.easy_clicked_drc,
                                           width=30)
        self.easy_drc_button.grid(row=3, column=0, pady=5)

        # Description label
        self.easy_list = []
        self.easy_description = tk.Label(self.easy_level_screen,
                                           text="You have chosen the following dictionaries:\n" + self.cleanString(str(self.easy_list)),
                                           font="Arial 16")
        self.easy_description.grid(row=4, column=0, pady=5)

        # OK Button
        self.easy_ok_button = tk.Button(self.easy_level_screen,
                                          text="OK!",
                                          font="Arial 20 bold",
                                          bd=10,
                                          bg="yellow",
                                          fg="red",
                                          command=self.easy_clicked_ok)
        self.easy_ok_button.grid(row=2, column=1)

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
        self.medium_title.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        # Dictionary buttons
        self.medium_sports_button = tk.Button(self.medium_level_screen,
                                            text="Macalester Sports",
                                            font="Arial 16",
                                            bd=5,
                                            command=self.medium_clicked_sports,
                                            width=30)
        self.medium_sports_button.grid(row=1, column=0, pady=5)

        self.medium_library_button = tk.Button(self.medium_level_screen,
                                             text="DeWitt Wallace Library",
                                             font="Arial 16",
                                             bd=5,
                                             command=self.medium_clicked_library,
                                             width=30)
        self.medium_library_button.grid(row=2, column=0, pady=5)

        self.medium_drc_button = tk.Button(self.medium_level_screen,
                                         text="Digital Resources Center",
                                         font="Arial 16",
                                         bd=5,
                                         command=self.medium_clicked_drc,
                                         width=30)
        self.medium_drc_button.grid(row=3, column=0, pady=5)

        #Description label
        self.medium_list=[]
        self.medium_description=tk.Label(self.medium_level_screen,
                                         text="You have chosen the following dictionaries:\n" + self.cleanString(str(self.medium_list)),
                                         bd=10,
                                         font="Arial 16")
        self.medium_description.grid(row=4,column=0, pady=5)


        # OK Button
        self.medium_ok_button = tk.Button(self.medium_level_screen,
                                        text="OK!",
                                        font="Arial 20 bold",
                                        bd=10,
                                        bg="yellow",
                                        fg="red",
                                        command=self.medium_clicked_ok)
        self.medium_ok_button.grid(row=2, column=1)

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
        self.hard_title.grid(row=0, column=0, columnspan=2, padx=10, pady=5)

        # Dictionary buttons
        self.hard_sports_button = tk.Button(self.hard_level_screen,
                                              text="Macalester Sports",
                                              font="Arial 16",
                                              bd=5,
                                              command=self.hard_clicked_sports,
                                              width=30)
        self.hard_sports_button.grid(row=1, column=0, pady=5)

        self.hard_library_button = tk.Button(self.hard_level_screen,
                                               text="DeWitt Wallace Library",
                                               font="Arial 16",
                                               bd=5,
                                               command=self.hard_clicked_library,
                                               width=30)
        self.hard_library_button.grid(row=2, column=0, pady=5)

        self.hard_drc_button = tk.Button(self.hard_level_screen,
                                           text="Digital Resources Center",
                                           font="Arial 16",
                                           bd=5,
                                           command=self.hard_clicked_drc,
                                           width=30)
        self.hard_drc_button.grid(row=3, column=0, pady=5)

        # Description label
        self.hard_list = []
        self.hard_description = tk.Label(self.hard_level_screen,
                                           text="You have chosen the following dictionaries:\n" + self.cleanString(str(self.hard_list)),
                                           bd=10,
                                           font="Arial 16")
        self.hard_description.grid(row=4, column=0, pady=5)



        # OK Button
        self.hard_ok_button = tk.Button(self.hard_level_screen,
                                          text="OK!",
                                          font="Arial 20 bold",
                                          bd=10,
                                          bg="yellow",
                                          fg="red",
                                          command=self.hard_clicked_ok)
        self.hard_ok_button.grid(row=2, column=1)


    #DEFINING FUNCTION FOR CLICKING INSTRUCTIONS
    def clicked_instructions(self):
        self.instructions_screen.deiconify()
    def clicked_back(self):
        self.instructions_screen.withdraw()

    #DEFINING FUNCTIONS FOR RESPONSE TO EASY-MEDIUM-LEVEL BUTTONS
    def clicked_easy(self):
        self.easy_level_screen.deiconify()
        self.difficulty_level="Easy"
        self.info_label.config(text="You're playing the game\n with easy level difficulty.")
        self.allowablemistakes=10
        self.mistakes_label.config(text="You have "+str(self.allowablemistakes)+" mistakes left")
        self.allowablehints=3
        self.hints_left_label.config(text="You have "+str(self.allowablehints)+" hints left")
    def clicked_medium(self):
        self.medium_level_screen.deiconify()
        self.difficulty_level="Medium"
        self.info_label.config(text="You're playing the game\n with medium level difficulty.")
        self.allowablemistakes=6
        self.mistakes_label.config(text="You have " + str(self.allowablemistakes) + " mistakes left")
        self.allowablehints = 2
        self.hints_left_label.config(text="You have " + str(self.allowablehints) + " hints left")
    def clicked_hard(self):
        self.hard_level_screen.deiconify()
        self.difficulty_level="Hard"
        self.info_label.config(text="You're playing the game\n with hard level difficulty.")
        self.allowablemistakes=4
        self.mistakes_label.config(text="You have " + str(self.allowablemistakes) + " mistakes left")
        self.allowablehints = 1
        self.hints_left_label.config(text="You have " + str(self.allowablehints) + " hints left")

    #DEFINING FUNCTIONS FOR RESPONSE TO CLICKING THE OK BUTTON IN EASY, MEDIUM, HARD SCREENS
    def easy_clicked_ok(self):
        if "hm" not in self.all_dictionaries:
            self.choose_a_level.config(text="Now start the game!")
            self.easy_button.config(state="disabled")
            self.medium_button.config(state="disabled")
            self.hard_button.config(state="disabled")
            self.easy_level_screen.withdraw()
            self.startButton.config(bg="green")
            self.choosing_word()
            # Creating a RESTART button
            self.restartsplash = tk.Button(self.splashScreen,
                                           text="Change settings",
                                           font="Arial 15",
                                           command=self.restartResponse,
                                           width=15)
            self.restartsplash.grid(row=4, column=1)
        else:
            messagebox.showwarning("WAIT!","You haven't chosen any dictionaries yet. Please choose one before proceeding.")

    def medium_clicked_ok(self):
        if "hm" not in self.all_dictionaries:
            self.choose_a_level.config(text="Now start the game!")
            self.easy_button.config(state="disabled")
            self.medium_button.config(state="disabled")
            self.hard_button.config(state="disabled")
            self.medium_level_screen.withdraw()
            self.startButton.config(bg="green")
            self.choosing_word()
            # Creating a RESTART button
            self.restartsplash = tk.Button(self.splashScreen,
                                           text="Change settings",
                                           font="Arial 15",
                                           command=self.restartResponse,
                                           width=15)
            self.restartsplash.grid(row=4, column=1)
        else:
            messagebox.showwarning("WAIT!","You haven't chosen any dictionaries yet. Please choose one before proceeding.")

    def hard_clicked_ok(self):
        if "hm" not in self.all_dictionaries:
            self.choose_a_level.config(text="Now start the game!")
            self.easy_button.config(state="disabled")
            self.medium_button.config(state="disabled")
            self.hard_button.config(state="disabled")
            self.hard_level_screen.withdraw()
            self.startButton.config(bg="green")
            self.choosing_word()
            # Creating a RESTART button
            self.restartsplash = tk.Button(self.splashScreen,
                                           text="Change settings",
                                           font="Arial 15",
                                           command=self.restartResponse,
                                           width=15)
            self.restartsplash.grid(row=4, column=1)
        else:
            messagebox.showwarning("WAIT!","You haven't chosen any dictionaries yet. Please choose one before proceeding.")



    #START BUTTON
    def startResponse(self):
        """Takes no inputs. Shows the mainWin and hides the splashScreen"""
        if "hm" in self.all_dictionaries:
            messagebox.showerror("WAIT!", "You need to have chosen a difficulty level and a dictionary before starting the game.")

        else:
            self.mainWin.deiconify()
            self.splashScreen.withdraw()

    #QUIT BUTTON
    def quitResponse(self):
        """Takes no inputs. Destroys the game"""
        self.mainWin.destroy()

    #RESTART BUTTON
    def restartResponse(self):
        #INITIALIZING EVERYTHING
        # Initializing guessed letters
        self.guessed_letters = []
        # Initializing mistakes and number of hints
        self.num_mistakes = 0
        self.allowablemistakes = 0
        self.allowablehints = 0
        # Initializing number of hints
        self.num_hints = 0
        # Initializing chosen dictionaries
        self.all_dictionaries = ["hm"]
        # STORING THE DIFFICULTY LEVEL
        self.difficulty_level = "Default"
        # Initializing the lists displayed on labels
        self.easy_list = []
        self.medium_list = []
        self.hard_list = []
        #Initializing the button colors
        self.startButton.config(bg="red", fg="white")
        self.easy_ok_button.config(bg="yellow", fg="red")
        self.medium_ok_button.config(bg="yellow", fg="red")
        self.hard_ok_button.config(bg="yellow", fg="red")
        self.choose_a_level.config(text="Choose a difficulty level:")
        self.result_label.config(text="")


        #Giving all previously disabled widgets to their normal states again
        self.easy_button.config(state="normal")
        self.medium_button.config(state="normal")
        self.hard_button.config(state="normal")
        self.guess_entry.config(state="normal")
        self.guess_button.config(state="normal")
        self.hint.config(state="normal")
        self.restartsplash.grid_remove() #NMTech Tkinter Reference

        # Applying the initialized things on labels
        self.easy_description.config(text="You have chosen the following dictionaries:\n" + self.cleanString(str(self.easy_list)))
        self.desc_label.config(text="The word could be related to one of the following topics:\n" + self.cleanString(str(self.easy_list)))
        self.medium_description.config(text="You have chosen the following dictionaries:\n" + self.cleanString(str(self.medium_list)))
        self.desc_label.config(text="The word could be related to one of the following topics:\n" + self.cleanString(str(self.medium_list)))
        self.hard_description.config(text="You have chosen the following dictionaries:\n" + self.cleanString(str(self.hard_list)))
        self.desc_label.config(text="The word could be related to one of the following topics:\n" + self.cleanString(str(self.hard_list)))
        self.inputted_letters_label.config(text=("You have already inputted the following letters:\n" + self.cleanString(str(self.guessed_letters))))

        self.updating_hangman(self.num_mistakes)

        #Withdrawing the game screen and bringing up the splashScreen again.
        self.mainWin.withdraw()
        self.splashScreen.deiconify()






    #-----------------------------------------------------------------
    #FUNCTIONS FOR THE EASY DIFFICULTY WINDOW
    def easy_clicked_sports(self):
        if "hm" in self.all_dictionaries:
            self.all_dictionaries.remove("hm")
        if "Macalester Sports" in self.easy_list:
            self.easy_list.remove("Macalester Sports")
            self.easy_description.config(text="You have chosen the following dictionaries:\n" + self.cleanString(str(self.easy_list)))
            self.desc_label.config(text="The word could be related to one of the following topics:\n" + self.cleanString(str(self.easy_list)))
            if self.sports_list in self.all_dictionaries:
                self.all_dictionaries.remove(self.sports_list)
                print(self.all_dictionaries)
            if len(self.all_dictionaries)==0:
                self.easy_ok_button.config(bg="yellow", fg="red")
                self.all_dictionaries.append("hm")
        else:
            self.easy_list.append("Macalester Sports")
            self.easy_description.config(text="You have chosen the following dictionaries:\n" + self.cleanString(str(self.easy_list)))
            self.easy_ok_button.config(bg="green", fg="white")
            self.desc_label.config(text="The word could be related to one of the following topics:\n" + self.cleanString(str(self.easy_list)))
            if self.sports_list not in self.all_dictionaries:
                self.all_dictionaries.append(self.sports_list)
                print(self.all_dictionaries)

    def easy_clicked_library(self):
        if "hm" in self.all_dictionaries:
            self.all_dictionaries.remove("hm")
        if "DeWitt Wallace Library" in self.easy_list:
            self.easy_list.remove("DeWitt Wallace Library")
            self.easy_description.config(text="You have chosen the following dictionaries:\n" + self.cleanString(str(self.easy_list)))
            self.desc_label.config(text="The word could be related to one of the following topics:\n" + self.cleanString(str(self.easy_list)))
            if self.library_list in self.all_dictionaries:
                self.all_dictionaries.remove(self.library_list)
                print(self.all_dictionaries)
            if len(self.all_dictionaries) == 0:
                self.easy_ok_button.config(bg="yellow", fg="red")
                self.all_dictionaries.append("hm")
        else:
            self.easy_list.append("DeWitt Wallace Library")
            self.easy_description.config(text="You have chosen the following dictionaries:\n" + self.cleanString(str(self.easy_list)))
            self.easy_ok_button.config(bg="green", fg="white")
            self.desc_label.config(text="The word could be related to one of the following topics:\n" + self.cleanString(str(self.easy_list)))
            if self.library_list not in self.all_dictionaries:
                self.all_dictionaries.append(self.library_list)
                print(self.all_dictionaries)

    def easy_clicked_drc(self):
        if "hm" in self.all_dictionaries:
            self.all_dictionaries.remove("hm")
        if "Digital Resources Center" in self.easy_list:
            self.easy_list.remove("Digital Resources Center")
            self.easy_description.config(text="You have chosen the following dictionaries:\n" + self.cleanString(str(self.easy_list)))
            self.desc_label.config(text="The word could be related to one of the following topics:\n" + self.cleanString(str(self.easy_list)))
            if self.drc_list in self.all_dictionaries:
                self.all_dictionaries.remove(self.drc_list)
                print(self.all_dictionaries)
            if len(self.all_dictionaries) == 0:
                self.easy_ok_button.config(bg="yellow", fg="red")
                self.all_dictionaries.append("hm")
        else:
            self.easy_list.append("Digital Resources Center")
            self.easy_description.config(text="You have chosen the following dictionaries:\n" + self.cleanString(str(self.easy_list)))
            self.easy_ok_button.config(bg="green", fg="white")
            self.desc_label.config(text="The word could be related to one of the following topics:\n" + self.cleanString(str(self.easy_list)))
            if self.drc_list not in self.all_dictionaries:
                self.all_dictionaries.append(self.drc_list)
                print(self.all_dictionaries)
    #------------------------------------------------------------------
    #FUNCTIONS FOR THE MEDIUM DIFFICULTY WINDOW
    def medium_clicked_sports(self):
        if "hm" in self.all_dictionaries:
            self.all_dictionaries.remove("hm")
        if "Macalester Sports" in self.medium_list:
            self.medium_list.remove("Macalester Sports")
            self.medium_description.config(text="You have chosen the following dictionaries:\n" + self.cleanString(str(self.medium_list)))
            self.desc_label.config(text="The word could be related to one of the following topics:\n" + self.cleanString(str(self.medium_list)))
            if self.sports_list in self.all_dictionaries:
                self.all_dictionaries.remove(self.sports_list)
                print(self.all_dictionaries)
            if len(self.all_dictionaries) == 0:
                self.medium_ok_button.config(bg="yellow", fg="red")
                self.all_dictionaries.append("hm")
        else:
            self.medium_list.append("Macalester Sports")
            self.medium_description.config(text="You have chosen the following dictionaries:\n" + self.cleanString(str(self.medium_list)))
            self.medium_ok_button.config(bg="green", fg="white")
            self.desc_label.config(text="The word could be related to one of the following topics:\n" + self.cleanString(str(self.medium_list)))
            if self.sports_list not in self.all_dictionaries:
                self.all_dictionaries.append(self.sports_list)
                print(self.all_dictionaries)

    def medium_clicked_library(self):
        if "hm" in self.all_dictionaries:
            self.all_dictionaries.remove("hm")
        if "DeWitt Wallace Library" in self.medium_list:
            self.medium_list.remove("DeWitt Wallace Library")
            self.medium_description.config(text="You have chosen the following dictionaries:\n" + self.cleanString(str(self.medium_list)))
            self.desc_label.config(text="The word could be related to one of the following topics:\n" + self.cleanString(str(self.medium_list)))
            if self.library_list in self.all_dictionaries:
                self.all_dictionaries.remove(self.library_list)
                print(self.all_dictionaries)
            if len(self.all_dictionaries) == 0:
                self.medium_ok_button.config(bg="yellow", fg="red")
                self.all_dictionaries.append("hm")
        else:
            self.medium_list.append("DeWitt Wallace Library")
            self.medium_description.config(text="You have chosen the following dictionaries:\n" + self.cleanString(str(self.medium_list)))
            self.medium_ok_button.config(bg="green", fg="white")
            self.desc_label.config(text="The word could be related to one of the following topics:\n" + self.cleanString(str(self.medium_list)))
            if self.library_list not in self.all_dictionaries:
                self.all_dictionaries.append(self.library_list)
                print(self.all_dictionaries)

    def medium_clicked_drc(self):
        if "hm" in self.all_dictionaries:
            self.all_dictionaries.remove("hm")
        if "Digital Resources Center" in self.medium_list:
            self.medium_list.remove("Digital Resources Center")
            self.medium_description.config(text="You have chosen the following dictionaries:\n" + self.cleanString(str(self.medium_list)))
            self.desc_label.config(text="The word could be related to one of the following topics:\n" + self.cleanString(str(self.medium_list)))
            if self.drc_list in self.all_dictionaries:
                self.all_dictionaries.remove(self.drc_list)
                print(self.all_dictionaries)
            if len(self.all_dictionaries) == 0:
                self.medium_ok_button.config(bg="yellow", fg="red")
                self.all_dictionaries.append("hm")
        else:
            self.medium_list.append("Digital Resources Center")
            self.medium_description.config(text="You have chosen the following dictionaries:\n" + self.cleanString(str(self.medium_list)))
            self.medium_ok_button.config(bg="green", fg="white")
            self.desc_label.config(text="The word could be related to one of the following topics:\n" + self.cleanString(str(self.medium_list)))
            if self.drc_list not in self.all_dictionaries:
                self.all_dictionaries.append(self.drc_list)
                print(self.all_dictionaries)


    #----------------------------------------------------------------
    #----FUNCTIONS FOR THE HARD DIFFICULTY WINDOW
    def hard_clicked_sports(self):
        if "hm" in self.all_dictionaries:
            self.all_dictionaries.remove("hm")
        if "Macalester Sports" in self.hard_list:
            self.hard_list.remove("Macalester Sports")
            self.hard_description.config(text="You have chosen the following dictionaries:\n" + self.cleanString(str(self.hard_list)))
            self.desc_label.config(text="The word could be related to one of the following topics:\n" + self.cleanString(str(self.hard_list)))
            if self.sports_list in self.all_dictionaries:
                self.all_dictionaries.remove(self.sports_list)
                print(self.all_dictionaries)
            if len(self.all_dictionaries) == 0:
                self.hard_ok_button.config(bg="yellow", fg="red")
                self.all_dictionaries.append("hm")
        else:
            self.hard_list.append("Macalester Sports")
            self.hard_description.config(text="You have chosen the following dictionaries:\n" + self.cleanString(str(self.hard_list)))
            self.hard_ok_button.config(bg="green", fg="white")
            self.desc_label.config(text="The word could be related to one of the following topics:\n" + self.cleanString(str(self.hard_list)))
            if self.sports_list not in self.all_dictionaries:
                self.all_dictionaries.append(self.sports_list)
                print(self.all_dictionaries)

    def hard_clicked_library(self):
        if "hm" in self.all_dictionaries:
            self.all_dictionaries.remove("hm")
        if "DeWitt Wallace Library" in self.hard_list:
            self.hard_list.remove("DeWitt Wallace Library")
            self.hard_description.config(text="You have chosen the following dictionaries:\n" + self.cleanString(str(self.hard_list)))
            self.desc_label.config(text="The word could be related to one of the following topics:\n" + self.cleanString(str(self.hard_list)))
            if self.library_list in self.all_dictionaries:
                self.all_dictionaries.remove(self.library_list)
                print(self.all_dictionaries)
            if len(self.all_dictionaries) == 0:
                self.hard_ok_button.config(bg="yellow", fg="red")
                self.all_dictionaries.append("hm")
        else:
            self.hard_list.append("DeWitt Wallace Library")
            self.hard_description.config(text="You have chosen the following dictionaries:\n" + self.cleanString(str(self.hard_list)))
            self.hard_ok_button.config(bg="green", fg="white")
            self.desc_label.config(text="The word could be related to one of the following topics:\n" + self.cleanString(str(self.hard_list)))
            if self.library_list not in self.all_dictionaries:
                self.all_dictionaries.append(self.library_list)
                print(self.all_dictionaries)

    def hard_clicked_drc(self):
        if "hm" in self.all_dictionaries:
            self.all_dictionaries.remove("hm")
        if "Digital Resources Center" in self.hard_list:
            self.hard_list.remove("Digital Resources Center")
            self.hard_description.config(text="You have chosen the following dictionaries:\n" + self.cleanString(str(self.hard_list)))
            self.desc_label.config(text="The word could be related to one of the following topics:\n" + self.cleanString(str(self.hard_list)))
            if self.drc_list in self.all_dictionaries:
                self.all_dictionaries.remove(self.drc_list)
                print(self.all_dictionaries)
            if len(self.all_dictionaries) == 0:
                self.hard_ok_button.config(bg="yellow", fg="red")
                self.all_dictionaries.append("hm")
        else:
            self.hard_list.append("Digital Resources Center")
            self.hard_description.config(text="You have chosen the following dictionaries:\n" + self.cleanString(str(self.hard_list)))
            self.hard_ok_button.config(bg="green", fg="white")
            self.desc_label.config(text="The word could be related to one of the following topics:\n" + self.cleanString(str(self.hard_list)))
            if self.drc_list not in self.all_dictionaries:
                self.all_dictionaries.append(self.drc_list)
                print(self.all_dictionaries)




    # Defining a function for randomly choosing a word
    def choosing_word(self):
        random_dict = random.choice(self.all_dictionaries)
        self.random_word = random.choice(random_dict)
        self.word_blanks = "_" * len(self.random_word)
        self.word_label.config(text=self.word_blanks)
        print(self.random_word)
        return self.random_word

    #Defining a function to update the hangman display
    def updating_hangman(self, mistakes):
        if self.difficulty_level=="Easy":
            self.hangedGuyLabel.config(image=self.easy_hangman_images_list[mistakes])
        elif self.difficulty_level=="Medium":
            self.hangedGuyLabel.config(image=self.medium_hangman_images_list[mistakes])
        elif self.difficulty_level == "Hard":
            self.hangedGuyLabel.config(image=self.hard_hangman_images_list[mistakes])


    #Creating a function to check the validity of the user's input
    def validInput(self):
        if len(self.guess_entry.get())>1:
            respond_text="You can only input one character!"
            self.validity_label.config(text=respond_text)
            self.guess_entry.delete(0, tk.END)
            vallid=False
        elif self.guess_entry.get() not in string.ascii_letters:
            respond_text = "You have to input a letter!"
            self.validity_label.config(text=respond_text)
            self.guess_entry.delete(0, tk.END)
            vallid = False
        elif self.guess_entry.get()=="":
            respond_text = "You haven't inputted anything! Input something before clicking the button"
            self.validity_label.config(text=respond_text)
            self.guess_entry.delete(0, tk.END)
            vallid = False
        elif self.guess_entry.get().lower() in self.guessed_letters:
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
        if guess in self.random_word:
            for i in range(len(self.random_word)):
                if self.random_word[i] == guess:
                    self.word_blanks = self.word_blanks[:i] + guess + self.word_blanks[i + 1:]
            self.word_label.config(text=self.word_blanks)
            self.guessed_letters.append(guess)
            self.inputted_letters_label.config(text=("You have already inputted the following letters:\n" + self.cleanString(str(self.guessed_letters))))
            if "_" not in self.word_blanks:
                self.ending("Win")
        else:
            self.guessed_letters.append(guess)
            self.inputted_letters_label.config(text=("You have already inputted the following letters:\n" + self.cleanString(str(self.guessed_letters))))
            self.num_mistakes += 1
            self.allowablemistakes -= 1
            self.mistakes_label.config(text="You have "+str(self.allowablemistakes)+" mistakes left")
            self.updating_hangman(self.num_mistakes)
            if self.difficulty_level == "Easy":
                if self.num_mistakes == 10:
                    self.ending("lose")
            elif self.difficulty_level =="Medium":
                if self.num_mistakes == 6:
                    self.ending("lose")
            elif self.difficulty_level =="Hard":
                if self.num_mistakes == 4:
                    self.ending("lose")

    #Defining an ending function
    def ending(self, result):
        if result == "Win":
            result_text="Congratulations, you WON the game!"
            self.hint_label.config(text="")
            self.result_label.config(text=result_text, fg="green", font="Arial 30 bold")
        else:
            result_text="You lost the game and the word was '"+self.random_word+"'."
            self.hint_label.config(text="")
            self.result_label.config(text=result_text, fg="red", font="Arial 30 bold")
        self.guess_entry.config(state="disabled")
        self.guess_button.config(state="disabled")
        self.hint.config(state="disabled")

    #Defining a hinting function
    def hinting(self):
        if self.difficulty_level=="Easy":
            if self.num_hints>=3:
                self.hint.config(state="disabled")
                self.hint_label.config(text="Sorry, you don't have any hints left")
            else:
                if self.random_word in self.sports_list:
                    self.num_hints+=1
                    random_hint = random.choice(self.sports_dict[self.random_word])
                    self.sports_dict[self.random_word].remove(random_hint)
                    self.hint_label.config(text="HINT: "+random_hint)
                    self.allowablehints -= 1
                    self.hints_left_label.config(text="You have " + str(self.allowablehints) + " hints left")
                if self.random_word in self.library_list:
                    self.num_hints+=1
                    random_hint = random.choice(self.library_dict[self.random_word])
                    self.library_dict[self.random_word].remove(random_hint)
                    self.hint_label.config(text="HINT: "+random_hint)
                    self.allowablehints -= 1
                    self.hints_left_label.config(text="You have " + str(self.allowablehints) + " hints left")
                if self.random_word in self.drc_list:
                    self.num_hints+=1
                    random_hint = random.choice(self.drc_dict[self.random_word])
                    self.drc_dict[self.random_word].remove(random_hint)
                    self.hint_label.config(text="HINT: "+random_hint)
                    self.allowablehints -= 1
                    self.hints_left_label.config(text="You have " + str(self.allowablehints) + " hints left")
        elif self.difficulty_level=="Medium":
            if self.num_hints>=2:
                self.hint.config(state="disabled")
                self.hint_label.config(text="Sorry, you don't have any hints left")
            else:
                if self.random_word in self.sports_list:
                    self.num_hints+=1
                    random_hint = random.choice(self.sports_dict[self.random_word])
                    self.sports_dict[self.random_word].remove(random_hint)
                    self.hint_label.config(text="HINT: "+random_hint)
                    self.allowablehints -= 1
                    self.hints_left_label.config(text="You have " + str(self.allowablehints) + " hints left")
                if self.random_word in self.library_list:
                    self.num_hints+=1
                    random_hint = random.choice(self.library_dict[self.random_word])
                    self.library_dict[self.random_word].remove(random_hint)
                    self.hint_label.config(text="HINT: "+random_hint)
                    self.allowablehints -= 1
                    self.hints_left_label.config(text="You have " + str(self.allowablehints) + " hints left")
                if self.random_word in self.drc_list:
                    self.num_hints+=1
                    random_hint = random.choice(self.drc_dict[self.random_word])
                    self.drc_dict[self.random_word].remove(random_hint)
                    self.hint_label.config(text="HINT: "+random_hint)
                    self.allowablehints -= 1
                    self.hints_left_label.config(text="You have " + str(self.allowablehints) + " hints left")
        elif self.difficulty_level=="Hard":
            if self.num_hints>=1:
                self.hint.config(state="disabled")
                self.hint_label.config(text="Sorry, you don't have any hints left")
            else:
                if self.random_word in self.sports_list:
                    self.num_hints+=1
                    random_hint = random.choice(self.sports_dict[self.random_word])
                    self.sports_dict[self.random_word].remove(random_hint)
                    self.hint_label.config(text="HINT: "+random_hint)
                    self.allowablehints -= 1
                    self.hints_left_label.config(text="You have " + str(self.allowablehints) + " hints left")
                if self.random_word in self.library_list:
                    self.num_hints+=1
                    random_hint = random.choice(self.library_dict[self.random_word])
                    self.library_dict[self.random_word].remove(random_hint)
                    self.hint_label.config(text="HINT: "+random_hint)
                    self.allowablehints -= 1
                    self.hints_left_label.config(text="You have " + str(self.allowablehints) + " hints left")
                if self.random_word in self.drc_list:
                    self.num_hints+=1
                    random_hint = random.choice(self.drc_dict[self.random_word])
                    self.drc_dict[self.random_word].remove(random_hint)
                    self.hint_label.config(text="HINT: "+random_hint)
                    self.allowablehints -= 1
                    self.hints_left_label.config(text="You have " + str(self.allowablehints) + " hints left")

    #Defining a recursive function for clearing punctuation
    def cleanString(self, inpStr):
        #items=string.punctuation.replace(',', "")
        if len(inpStr) == 0:
            return ""
        else:
            firstCh = inpStr[0]
            resStr = self.cleanString(inpStr[1:])
            if firstCh in string.punctuation and firstCh !=",":
                return resStr
            else:
                return firstCh + resStr
    def go(self):
        """Runs the whole class whenever .go() is called"""
        self.mainWin.mainloop()


#SCRIPT
if __name__ == '__main__':
    game=hangmanGUI()
    game.go()
