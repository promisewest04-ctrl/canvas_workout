# Number Guessing Game GUI
A graphical Number Guessing Game built using Python and Tkinter. Players select a difficulty level and try to guess a randomly generated secret number between 1 and 50 before running out of attempts.

---

## Features

- Graphical User Interface: Built using Tkinter with a custom fixed-size canvas (500x400).
- Difficulty Selection:
  - Easy Mode: 10 attempts
  - Hard Mode: 5 attempts
- Custom Visual Assets: Automatically scales background images (photo.jpg and photo_2.jpg) using Pillow (PIL) to match exact canvas resolution.
- Dynamic Real-Time Feedback: Interactive guidance giving hints ("Too high!", "Too low!") and remaining attempt updates.
- Input Validation: Gracefully handles non-numeric or invalid inputs without crashing.
- Replayability: Built-in game reset functionality with "Play Again" state management.

---

## Project Structure

.
├── rough.py        # Main Python GUI game implementation├── photo.jpg       # Gameplay background image└── photo_2.jpg     # Difficulty selection background image

---

## Prerequisites & Dependencies

- Python 3.x
- Pillow (PIL)

---

## Installation & Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/number-guessing-game.git
   cd number-guessing-game
   ```

2. Install required dependencies:
   ```bash
   pip install pillow
   ```

3. Asset Verification:
   Ensure photo.jpg and photo_2.jpg are present in the project root directory.

---

## How to Run

Execute the main script:
python rough.py

---

## How to Play

1. Choose Difficulty: Select either Easy (10 tries) or Hard (5 tries).
2. Make a Guess: Input an integer between 1 and 50 into the text field and click Submit.
3. Follow Hints: Use the real-time feedback to adjust your next guess.
4. Game Over / Win: Upon completion, click Play Again to restart a new round.