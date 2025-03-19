# The Macalester Hangman Game

## Authors:
**Karim Amra** and **Aram Petrosyan**  
**Course:** Core Concepts in Computer Science (COMP 123)  
**Professor:** Elizabeth Ernst  
**Institution:** Macalester College  

---

## Overview
The **Macalester Hangman Game** is a GUI-based implementation of the classic Hangman word-guessing game, developed in **Python** using the **tkinter** library. This version is customized with **Macalester-themed word dictionaries**, featuring categories related to **Macalester Sports, the DeWitt Wallace Library, and the Digital Resources Center (DRC).**

Players can choose from **three difficulty levels**—Easy, Medium, and Hard—each with varying mistake allowances and hint availability. The game provides **graphical feedback** with a dynamic Hangman display that updates with each incorrect guess.

---

## Features
- **Graphical User Interface (GUI):** Built with tkinter for an intuitive and visually appealing experience.
- **Three Difficulty Levels:**
  - **Easy:** 10 mistakes allowed, 3 hints.
  - **Medium:** 6 mistakes allowed, 2 hints.
  - **Hard:** 4 mistakes allowed, 1 hint.
- **Macalester-Themed Dictionaries:**
  - **Macalester Sports:** Includes words like *volleyball, soccer, basketball* with related hints.
  - **DeWitt Wallace Library:** Words like *research, archives, worldcat* with library-specific hints.
  - **Digital Resources Center (DRC):** Words like *llama, digitization, tinkercad* with DRC-related hints.
- **Dynamic Gameplay:**
  - Players can guess letters, request hints, restart the game, or quit at any time.
  - Visual feedback updates the Hangman image based on incorrect guesses.
- **Input Validation:** Ensures only valid single-letter inputs are accepted, providing error feedback if necessary.

---

## Prerequisites
To run the **Macalester Hangman Game**, ensure you have the following installed:

- **Python 3.x** (Required to run the game)
- **Required Libraries:**
  - `tkinter` (Included in Python standard library)
  - `Pillow` for image handling (Install via: `pip install Pillow`)
- **Image Files:**
  - The game requires a **paintings** directory with Hangman images organized by difficulty level and a Macalester College logo.

---

## Installation
### 1. Clone or Download the Repository
Download the code and accompanying image files or clone the repository using:
```bash
git clone <repository_url>
cd your_project_folder
```

### 2. Install Dependencies
Open a terminal and run:
```bash
pip install Pillow
```
To check if `tkinter` is installed, run:
```bash
python -m tkinter
```
(A small window should appear.)

### 3. Prepare the Directory Structure
Ensure the following structure is maintained:
```
your_project_folder/
├── hangman_game.py         # The main Python script
├── paintings/
│   ├── Macalester_College_Logo.png
│   ├── easy_level/
│   │   ├── 0.jpg
│   │   ├── 1.jpg
│   │   ├── ... (up to 10.jpg)
│   ├── medium_level/
│   │   ├── 0.jpg
│   │   ├── 1.jpg
│   │   ├── ... (up to 6.jpg)
│   ├── hard_level/
│   │   ├── 0.jpg
│   │   ├── 1.jpg
│   │   ├── ... (up to 4.jpg)
```
Verify all image files are correctly placed, as the game will fail to load missing files.

---

## Usage
### 1. Run the Game
Navigate to the project folder in your terminal and execute:
```bash
python hangman_game.py
```
A **splash screen** will appear, welcoming you to the **Macalester Hangman Game**.

### 2. Game Flow
- **Splash Screen:** Choose a difficulty level (Easy, Medium, or Hard) by clicking the corresponding button.
- **Dictionary Selection:** Select one or more themed dictionaries (Macalester Sports, DeWitt Wallace Library, Digital Resources Center). Click again to deselect. Press "OK!" to confirm.
- **Start the Game:** Click "START" to begin.

### 3. Gameplay Mechanics
- Enter a single letter in the text box and click **"GUESS"** to submit.
- Click **"HINT"** to receive a clue (limited per difficulty level).
- The **Hangman image updates** with each incorrect guess.
- Use **"RESTART"** to reset the game or **"QUIT"** to exit.
- **Winning/Losing:** The game ends when:
  - You guess the full word (**Win** 🎉)
  - You run out of mistakes (**Lose** ❌)

### 4. Instructions
Click the **"Instructions"** button on the splash screen for detailed rules.

---

## Screenshots

### Home Screen
![Splash Screen](gameScreenShots/InitialConditionScreenShot.png)

### Gameplay (Easy Level)
![Gameplay Easy](gameScreenShots/WinningScreenshot.png)

### Win Screen
![Win Screen](gameScreenShots/WinningScreenshot.png)
---

## Troubleshooting
| Issue | Solution |
|--------|---------|
| **Images Not Loading** | Verify the `paintings` directory and image names match the expected structure. |
| **Module Not Found** | Ensure Pillow is installed (`pip install Pillow`). |
| **Game Crashes** | Check for typos in file paths or missing images. Contact the authors if issues persist. |

---

## Contributing
This project was developed as part of a course assignment. If you would like to report bugs, suggest improvements, or contribute, please contact:

- **Aram Petrosyan:** apetrosy@macalester.edu
- **Karim Amra:** kamra@macalester.edu

---

## Acknowledgments
- **Professor Elizabeth Ernst:** For guidance and support throughout COMP 123.
- **Macalester College:** For providing the inspiration and context for this project.

---

## License
This project is for educational purposes and does not include a formal license. Feel free to use and modify it for **non-commercial purposes**, giving credit to the original authors.

