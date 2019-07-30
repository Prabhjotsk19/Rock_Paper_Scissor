# Rock Paper Scissor Game
# Prabhjot Singh

import tkinter as tk
import random

YOUR_SCORE = 0
COMPUTER_SCORE = 0

random_choice = random.choice(["ROCK", "PAPER", "SCISSOR"])


def random_choice_by_computer():
    random_label = tk.Label(text=random_choice, fg="white", bg="grey")
    random_label.config(font=("Source code pro", 15))
    random_label.grid(row=4, column=1)


def for_rock():
    global YOUR_SCORE
    global COMPUTER_SCORE

    random_choice_by_computer()

    if "ROCK" == random_choice:
        YOUR_SCORE = 0
        COMPUTER_SCORE = 0
    elif random_choice == "PAPER":
        YOUR_SCORE = 0
        COMPUTER_SCORE += 1
    elif random_choice == "SCISSOR":
        YOUR_SCORE += 1
        COMPUTER_SCORE = 0


def for_paper():
    global YOUR_SCORE
    global COMPUTER_SCORE

    random_choice_by_computer()

    if "PAPER" == random_choice:
        YOUR_SCORE = 0
        COMPUTER_SCORE = 0
    elif random_choice == "ROCK":
        YOUR_SCORE += 1
        COMPUTER_SCORE = 0
    elif random_choice == "SCISSOR":
        YOUR_SCORE = 0
        COMPUTER_SCORE += 1


def for_scissor():
    global YOUR_SCORE
    global COMPUTER_SCORE

    random_choice_by_computer()

    if "SCISSOR" == random_choice:
        YOUR_SCORE = 0
        COMPUTER_SCORE =0
    elif random_choice == "ROCK":
        YOUR_SCORE = 0
        COMPUTER_SCORE += 1
    elif random_choice == "PAPER":
        YOUR_SCORE += 1
        COMPUTER_SCORE = 0


# Creating frame
window = tk.Tk()

# Creating frame geometry
window.geometry("600x400")

# Set the title of frame
window.title("ROCK PAPER SCISSOR")

# Adding labels
greeting = tk.Label(text="Welcome to Rock Paper Scissor Game", fg="purple")
greeting.config(font=("Source code pro", 22))
greeting.grid(columnspan=2)

player = tk.Label(text="You", fg="red")
player.config(font=("Source code pro", 18))
player.grid(row=1, column=0)

computer = tk.Label(text="Computer", fg="red")
computer.config(font=("Source code pro", 18))
computer.grid(row=1, column=1)

choice_of_player = tk.Label(text="Pick any One!", fg="orange")
choice_of_player.config(font=("Source code pro", 15))
choice_of_player.grid(row=2, column=0)

choice_of_computer = tk.Label(text="Computer choose!", fg="orange")
choice_of_computer.config(font=("Source code pro", 15))
choice_of_computer.grid(row=2, column=1)

your_score = tk.Label(text=f"YOUR SCORE = {YOUR_SCORE}", fg="purple", bg="yellow")
your_score.config(font=("Source code pro", 14))
your_score.grid(row=6, columnspan=2)

computer_score = tk.Label(text=f"COMPUTER SCORE = {COMPUTER_SCORE}", fg="purple", bg="yellow")
computer_score.config(font=("Source code pro", 14))
computer_score.grid(row=7, columnspan=2)

# Creating buttons
rock_button = tk.Button(text="ROCK", fg="white", bg="grey", command=for_rock)
rock_button.config(width=12)
rock_button.grid(row=3, column=0)

paper_button = tk.Button(text="PAPER", fg="white", bg="grey", command=for_paper)
paper_button.config(width=12)
paper_button.grid(row=4, column=0)

scissor_button = tk.Button(text="SCISSOR", fg="white", bg="grey", command=for_scissor)
scissor_button.config(width=12)
scissor_button.grid(row=5, column=0)

window.mainloop()
