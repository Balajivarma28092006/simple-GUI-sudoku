# Sudoku Maker & Solver

## Overview
This is a **simple GUI-based Sudoku application** built using **Python** and `tkinter`. Users can generate Sudoku puzzles, solve them using an algorithm, or input their own puzzle to be solved.

## Features
- **Generate Sudoku puzzles** of varying difficulty.
- **Solve puzzles** using a backtracking algorithm.
- **Manually input puzzles** and get solutions.
- Simple and interactive **GUI** using `tkinter`.

## Requirements
Before running the application, ensure you have the following dependencies installed:

```
pip install numpy
pip install tkinter
```

## How to Run
1. Clone this repository:
   ```
   git clone https://github.com/Balajivarma28092006/simple-GUI-sudoku.git
   ```
2. Navigate to the project directory:
   ```
   cd sudoku-maker-solver
   ```
3. Run the application:
   ```
   python main.py
   ```

## Usage
- Click **"Generate"** to create a new Sudoku puzzle.
- Fill in empty cells manually or click **"Solve"** to get the solution.
- Reset or generate new puzzles as needed.

## File Structure
```
sudoku-maker-solver/
│── main.py       # game logic
│── sudoku.py     # Sudoku generation and solving algorithm
|── gui.py        # Handles the GUI
│── README.md     # Documentation
```

## Algorithm
The Sudoku solver uses a **backtracking algorithm**, iterating through cells while checking validity.

## Future Improvements
- Add **difficulty levels** (easy, medium, hard).
- Implement **timer and score tracking**.
- Enhance UI with **better design and animations**.

