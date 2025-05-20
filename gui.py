import tkinter as tk
from tkinter import Tk, messagebox
from sudoku import generate_maze,solve_sudoku_board

class SudokuSolver:
    def __init__(self,master):
        master.resizable(False,False)
        self.master = master
        self.master.title("Sudoku Solver")
        self.grid = [[0]*9 for _ in range(9)]
        self.entries = [[None]*9 for _ in range(9)]
        self.clue_positions = []
        self.default_puzzle = generate_maze()
        self.create_widgets()
        self.load_default_puzzle()
    
    def create_widgets(self):
        frame = tk.Frame(self.master, bg="#f0f0f0")
        frame.pack(padx=10, pady=10)
        for i in range(9):
            for j in range(9):
                border_color = "black" if i % 3 == 0 and j % 3 == 0 else "#ccc"
                entry = tk.Entry(frame, width=2, font=('Arial', 24),bd=1,relief='solid', justify='center')
                entry.grid(row=i, column=j, padx=(2 if j%3==0 else 1), pady=(2 if i%3==0 else 1))
                self.entries[i][j] = entry

        button_frame = tk.Frame(self.master, bg="#f0f0f0")
        button_frame.pack(pady=10)

        solve_maze = tk.Button(button_frame, text='Verify',command=self.verify_user_solved_maze,bg="#4caf50", fg="white", font=("Arial", 12), padx=10, pady=5)
        solve_maze.grid(row=10,column=0,columnspan=3,sticky="nsew")

        solve_maze = tk.Button(button_frame, text='Solve maze',command=self.solve_puzzle,bg="#4caf50", fg="white", font=("Arial", 12), padx=10, pady=5)
        solve_maze.grid(row=11,column=0,columnspan=3,sticky="nsew")

        generate_button = tk.Button(button_frame, text='Generate New Puzzle', command=self.generate_new_puzzle, bg="#4caf50", fg="white", font=("Arial", 12), padx=10, pady=5)
        generate_button.grid(row=12, column=0, columnspan=3)

    def load_default_puzzle(self):
        self.grid = generate_maze()  # Copy default puzzle
        self.clue_positions = [(i, j) for i in range(9) for j in range(9) if self.grid[i][j] != 0]
        self.update_ui()

    def update_ui(self):
        for i in range(9):
            for j in range(9):
                self.entries[i][j].delete(0, tk.END)
                value = self.grid[i][j]
                if value != 0:
                    self.entries[i][j].insert(0, str(value))
                    self.entries[i][j].config(fg="blue", state="readonly")  # Make clues read-only
                else:
                    self.entries[i][j].config(fg="black", state="normal")

    def generate_new_puzzle(self):
        self.default_puzzle = generate_maze()
        self.grid = [row[:] for row in self.default_puzzle]
        self.clue_positions = [(i, j) for i in range(9) for j in range(9) if self.grid[i][j] != 0]
        self.update_ui()

    def solve_puzzle(self):
        self.grid = []

        #read the values from gui itself
        is_empty = True
        for i in range(9):
            row = []
            for j in range(9):
                value = self.entries[i][j].get()
                if value.isdigit() and 1<=int(value)<=9:
                    row.append(int(value))
                    is_empty = False
                else:
                    row.append(0)
            self.grid.append(row)
        
        if is_empty:
            messagebox.showwarning("Empty Board", "Please press generate one before solving.")
            return

        if solve_sudoku_board(self.grid):
            for i in range(9):
                for j in range(9):
                    self.entries[i][j].config(state="normal")
                    self.entries[i][j].delete(0, tk.END)
                    self.entries[i][j].insert(0, str(self.grid[i][j]))
                    self.entries[i][j].config(fg="green")
                    if (i, j) in self.clue_positions:
                        self.entries[i][j].config(state="readonly")
            self.default_puzzle = self.grid
        else:
            messagebox.showerror("Error","There are no solutions for this ")

    def verify_user_solved_maze(self):
        self.grid = []

        #read the values from gui itself
        for i in range(9):
            row = []
            for j in range(9):
                value = self.entries[i][j].get()
                if value.isdigit() and 1<=int(value)<=9:
                    row.append(int(value))
                else:
                    row.append(0)
            self.grid.append(row)
        
        for i in range(9):
            for j in range(9):
                if self.grid[i][j] == 0:
                    messagebox.showwarning("Incomplete Board", "Please fill all cells before verifying.")
                    return

        def is_valid_sudoku(grid):
            for i in range(9):
                if not is_valid_unit([grid[i][j] for j in range(9)]):#valid row
                    return False
                
            for j in range(9):
                if not is_valid_unit([grid[i][j] for i in range(9)]):#valid column
                    return False
                
            for box_i in range(0,9,3):#valid sub 3x3 matrix
                for box_j in range(0,9,3):
                    unit = [grid[i][j] for i in range(box_i,box_i+3) for j in range(box_j,box_j+3)]
                    if not is_valid_unit(unit):
                        return False
            
            def is_valid_unit(unit):
                seen = set()
                for num in unit:
                    if num!=0 and num in seen:
                        return False
                    seen.add(num)
                return True
            if not is_valid_sudoku(self.grid):
                messagebox.showerror("Error", "The puzzle is not correctly solved. Check for duplicates in rows, columns, or 3x3 grids.")
                return
            
        expected_solution = [row[:] for row in self.default_puzzle]
        if solve_sudoku_board(expected_solution):
            if self.grid == expected_solution:
                for i in range(9):
                    for j in range(9):
                        self.entries[i][j].config(fg="green")
                messagebox.showinfo("Victory", "You successfully solved the puzzle!")
            else:
                messagebox.showerror("Error", "The solution is valid but does not match the puzzle's intended solution.")
        else:
            messagebox.showerror("Error", "The default puzzle has no solution (this should not happen).")




