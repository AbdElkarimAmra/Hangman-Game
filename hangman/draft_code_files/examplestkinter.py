'''
import tkinter as tk
from tkinter import messagebox

instructions = "Grab the laces, and wrap them around your ankles."
messagebox.showinfo("This is how to tie your shoe", instructions)

messagebox.showerror("Incorrect number type",
                     "The number must be an integer")

messagebox.showwarning("Warning", "The wumpus is near!")

ans4 = messagebox.askquestion("Question example", "Is this a question?")
print("askquestion answer:", ans4)
ans5 = messagebox.askokcancel("Okay/Cancel example", "Okay or cancel?")
print("askokcancel answer:", ans5)
ans6 = messagebox.askyesno("Yes/No example", "Answer yes or no?")
print("askyesno answer:", ans6)
ans7 = messagebox.askretrycancel("Retry/Cancel", "Retry or cancel?")
print("askretrycancel answer:", ans7)
'''

import tkinter as tk
from tkinter import ttk    # Creates widgets with OS look-and-feel

class FrameExample:
    def __init__(self):
        self.rootWin = tk.Tk()
        self.rootWin.title("Frame example")
        f1 = tk.Frame(self.rootWin, bg = "lightblue", bd=5,
                      relief=tk.SUNKEN, padx = 10, pady = 10)
        f1.grid(row = 1, column = 1)
        f2 = tk.Frame(self.rootWin, bg = "pink", bd=5,
                      relief=tk.SUNKEN, padx = 10, pady = 10)
        f2.grid(row = 1, column = 2)


        # Builds lists containing Button objects
        self.frame1Buttons = []
        self.frame2Buttons = []
        for i in range(3):
            bName = "F1 Button" + str(i)
            button = ttk.Button(f1, text = bName) # font="Arial 14")
            button.grid(row = i, column = 1, padx=10, pady=10)
            self.frame1Buttons.append(button)
        for i in range(3):
            bName = "F2 Button" + str(i)
            button = ttk.Button(f2, text = bName) # font="Arial 14")
            button.grid(row = 1, column = i, padx=10, pady=10)
            self.frame2Buttons.append(button)

    def run(self):
        self.rootWin.mainloop()


# Main program:
frameGui = FrameExample()
frameGui.run()