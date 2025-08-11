# Wordle clone

A minimal Wordle-style game built with Tkinter for the frontend and a Python backend that handles game logic.
Frontend (Tkinter UI)
The frontend is a grid-based interface created with Tkinter's Entry widgets.

Rows (6) → Each row represents one guess.
Columns (5) → Each column is a letter.

Colors:

🟩 Green → Correct letter, correct position.

🟨 Yellow → Correct letter, wrong position.

⬜ Gray → Letter not in the word.

⚪ Empty → Unused cell.

## UI Behavior:

Acts as input and passes parameters to backend codes
User types letters in a row.
On pressing Enter, the row is sent to the backend for evaluation.
The backend returns a list of colors for each letter in that row, which updates the cell backgrounds.

## Backend (Game Logic)
Stores the secret word - generated randomly.
Receives guesses from the frontend.

Checks:

✅ Correct letter + position → Green.

⚠️ Correct letter, wrong position → Yellow.

❌ Letter not in word → Gray.

Returns a color list to the frontend.
Backend output: for example ["green", "yellow", "gray", "gray", "gray"]
then it gets rendered in the GUI using Tkinter library in python

conditions: if the word input is not equal to 5 letters or not in the dataset we give the user his trial back to guess
if he guessed a 5 letter word but not the secret generated one we consume one trial up until 6 and game over
if he guessed right then we congratulate him!
