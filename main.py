import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from random import  randint

root = tk.Tk()
root.title("Guessing Game")
root.resizable(False, False)
root.geometry("540x480")

# Canvas dimensions (resolution)
CANVAS_WIDTH = 500
CANVAS_HEIGHT = 400
CENTER_X = CANVAS_WIDTH // 2
CENTER_Y = CANVAS_HEIGHT // 2

# Helper to load and resize images to match exact canvas resolution
def load_and_resize_image(file_path):
    img_obj = Image.open(file_path)
    img_resized = img_obj.resize((CANVAS_WIDTH, CANVAS_HEIGHT), Image.Resampling.LANCZOS)
    return ImageTk.PhotoImage(img_resized)


# Load both images at exact canvas resolution
img_difficulty = load_and_resize_image("photo_2.jpg")
img_game = load_and_resize_image("photo.jpg")

# Global state variables
attempts = 0
secret_number = 0
chosen_difficulty = ""

canvas = tk.Canvas(root, width=500, height=400, bg="white")
canvas.pack(pady=20)



def show_difficulty_screen():
    """This creates the user interface for the difficulties selection to be input by the user."""
    canvas.delete("all")
    # Background image
    canvas.create_image(CENTER_X, CENTER_Y, image=img_difficulty)

    # Title and instructions
    canvas.create_text(
        CENTER_X, 60,
        text="Select Difficulty",
        font=("Ariel", 18, "bold"),
        fill="red"
    )



    def select_difficulty(level):
        """This take in the user level choose and returns the level and attempts in the level"""
        global attempts, chosen_difficulty

        if level == 'easy':
            attempts = 10
            chosen_difficulty = "Easy (10 Attempts)"
        elif level == 'hard':
            attempts = 5
            chosen_difficulty = "Hard (5 Attempts)"

        easy_btn.destroy()
        hard_btn.destroy()

        # Clear canvas
        canvas.delete("all")

        # Launch main game screen
        show_game_screen()

    easy_btn = tk.Button(root, text='Easy', font=("Ariel", 12, "bold"),
                         bg='green', fg='purple', width=10, height=1, bd=0,
                         cursor='hand2', command=lambda: select_difficulty('easy'))
    hard_btn = tk.Button(root, text='Hard', font=("Ariel", 12, "bold"),
                         bg='red', fg='violet', width=10, height=1, bd=0,
                         cursor='hand2', command=lambda: select_difficulty('hard'))

    # Place both buttons side-by-side on the canvas
    canvas.create_window(CENTER_X - 60, 180, window=easy_btn)
    canvas.create_window(CENTER_X + 60, 180, window=hard_btn)


def show_game_screen():
    """"""
    global secret_number
    secret_number = randint(1, 50)

    canvas.create_image(CENTER_X, CENTER_Y, image=img_game)

    canvas.create_text(
        CENTER_X, 40,
        text=f"Difficulty: {chosen_difficulty}",
        font=("Ariel", 14, 'bold')
    )

    canvas.create_text(
        CENTER_X, 80,
        text="Guess a number",
        font=("Ariel", 16, 'bold')
    )

    feedback_text_id = canvas.create_text(
        CENTER_X, 120,
        text="",
        font=("Ariel", 14, 'bold'),
        fill='yellow'
    )

    guess_entry = ttk.Entry(root, font=("Arial", 12), width=20)
    canvas.create_window(CENTER_X, 160, window=guess_entry)

    # Function to trigger game end and show the Play again button
    def end_game(message, color):
        canvas.itemconfig(
            feedback_text_id,
            text=message,
            fill=color
        )
        submit_btn.config(state="disabled")
        guess_entry.config(state="disabled")

        # Create 'Play Again' button and add it to canvas
        play_again_btn = ttk.Button(root, text="Play Again", command=restart_game)
        canvas.create_window(250, 200, window=play_again_btn)

    # Function to restart the game state
    def restart_game():
        canvas.delete("all")
        show_difficulty_screen()


    def check_guess():
        global attempts

        raw_input = guess_entry.get().strip()
        try:
            user_guess = int(raw_input)
        except ValueError:
                canvas.itemconfig(
                    feedback_text_id,
                    text="Please enter a valid number!",
                    fill="orange"
                )
                return

        if user_guess == secret_number:
            end_game("Correct! You won!", "lightgreen")
        else:
            attempts -= 1
            if attempts > 0 :
                hint = "Too high!" if user_guess > secret_number else "Too low!"
                canvas.itemconfig(
                    feedback_text_id,
                    text=f"Wrong! {hint} Attempts left: {attempts}",
                    fill="red"
                )
            else:
                end_game(f"Game Over! The number was {secret_number}","red")



    submit_btn = ttk.Button(root, text='Submit', command=check_guess)
    canvas.create_window(250, 200, window=submit_btn)


if __name__ == "__main__":
   show_difficulty_screen()

root.mainloop()
