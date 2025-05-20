from gui import SudokuSolver
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    root.resizable(False,False)
    game = SudokuSolver(root)
    root.mainloop()

