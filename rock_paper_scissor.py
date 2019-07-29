# Rock Paper Scissor Game
# Prabhjot Singh
import tkinter as tk
import random










def random_choice_by_computer():
    choice_randomly_by_computer = random.choice(["ROCK", "PAPER", "SCISSOR"])





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

# Creating buttons
rock_button = tk.Button(text="ROCK", fg="white", bg="grey")
rock_button.config(width=12)
rock_button.grid(row=3, column=0)

paper_button = tk.Button(text="PAPER", fg="white", bg="grey")
paper_button.config(width=12)
paper_button.grid(row=4, column=0)

scissor_button = tk.Button(text="SCISSOR", fg="white", bg="grey")
scissor_button.config(width=12)
scissor_button.grid(row=5, column=0)

window.mainloop()
