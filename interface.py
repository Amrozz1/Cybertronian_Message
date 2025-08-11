import tkinter as tk
import main
# Colors
GREEN = "#6aaa64"
YELLOW = "#c9b458"
GRAY = "#787c7e"
EMPTY = "#d3d6da"

root = tk.Tk()
root.title("Wordle Clone")

# Grid: 6 attempts × 5 letters
labels = [[None for _ in range(5)] for _ in range(6)]

for r in range(6):
    for c in range(5):
        lbl = tk.Label(root, text=" ", width=4, height=2,
                       font=("Helvetica", 24, "bold"),
                       bg=EMPTY, fg="white", relief="solid", bd=2)
        lbl.grid(row=r, column=c, padx=3, pady=3)
        labels[r][c] = lbl

entry = tk.Entry(root, font=("Helvetica", 18), width=10, justify="center")
entry.grid(row=6, column=0, columnspan=5, pady=10)

current_row = 0
target_word = main.pick_word()

def submit_guess(event=None):
    global current_row
    guess = entry.get().lower()

    if len(guess) != 5 or guess not in main.set_message:
        print("Invalid word")
        return

    colors = main.check_guess(guess, target_word)
  # Update the row
    for col in range(5):
        labels[current_row][col].config(text=guess[col].upper(), bg=colors[col])

    if guess == target_word:
        print("You win!")
        entry.config(state="disabled")
    elif current_row >= 5:
        print("Game over! The word was:", target_word)
        entry.config(state="disabled")
    
    current_row += 1
    entry.delete(0, tk.END)

entry.bind("<Return>", submit_guess)

root.mainloop()
