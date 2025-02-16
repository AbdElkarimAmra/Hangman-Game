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


#Defining a class
class hangmanGUI:
    def __init__(self):
        self.mainWin=tk.Tk()
        self.mainWin.title("Macalester Hangman Game")

        #Label for the title
        titleLabel=tk.Label(self.mainWin,
                            text="Macalester Hangman Game",
                            font="Arial 30 bold",
                            relief=tk.SUNKEN,
                            bd=10)
        titleLabel.grid(row=0, column=0, columnspan=3, padx=5, pady=5)

        #Label for the image
        img=Image.open("paintings/hard_level/0.jpg")
        self.hangedGuyImage=ImageTk.PhotoImage(img)
        hangedGuyLabel=tk.Label(self.mainWin, image=self.hangedGuyImage)
        hangedGuyLabel.grid(row=1, column=0, padx=5, pady=5)


    def go(self):
        """Runs the whole class whenever .go() is called"""
        self.mainWin.mainloop()


#SCRIPT
if __name__ == '__main__':
    game=hangmanGUI()
    game.go()
