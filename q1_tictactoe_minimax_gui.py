# Q1: AI Tic-Tac-Toe with GUI (Minimax)
import tkinter as tk
from tkinter import messagebox

HUMAN, AI = "X", "O"
LINES = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]


def winner(b):
    for a, c, d in LINES:
        if b[a] != " " and b[a] == b[c] == b[d]:
            return b[a]
    return "Draw" if " " not in b else None

def minimax(b, is_ai):
    w = winner(b)
    if w == AI: return 1
    if w == HUMAN: return -1
    if w == "Draw": return 0
    scores = []
    for i in range(9):
        if b[i] == " ":
            b[i] = AI if is_ai else HUMAN
            scores.append(minimax(b, not is_ai))
            b[i] = " "
    return max(scores) if is_ai else min(scores)

def best_move(b):
    best, move = -2, None
    for i in range(9):
        if b[i] == " ":
            b[i] = AI
            s = minimax(b, False)
            b[i] = " "
            if s > best:
                best, move = s, i
    return move

class Game:
    def __init__(self, root):
        self.root = root
        root.title("Tic-Tac-Toe : Human (X) vs AI (O, Minimax)")
        self.status = tk.Label(root, text="Your turn (X)", font=("Arial", 14))
        self.status.grid(row=0, column=0, columnspan=3, pady=8)
        self.btns = []
        for i in range(9):
            b = tk.Button(root, text=" ", font=("Arial", 28, "bold"), width=4, height=2,
                          command=lambda i=i: self.human_move(i))
            b.grid(row=1 + i // 3, column=i % 3)
            self.btns.append(b)
        tk.Button(root, text="Restart", command=self.reset).grid(row=4, column=0, columnspan=3, pady=8)
        self.reset()

    def reset(self):
        self.board = [" "] * 9
        self.over = False
        for b in self.btns: b.config(text=" ", state="normal")
        self.status.config(text="Your turn (X)")

    def refresh(self):
        for i, b in enumerate(self.btns):
            b.config(text=self.board[i], state="disabled" if self.board[i] != " " or self.over else "normal")

    def check_end(self):
        w = winner(self.board)
        if w:
            self.over = True
            msg = "It's a draw!" if w == "Draw" else ("You win!" if w == HUMAN else "AI wins!")
            self.status.config(text=msg)
            self.refresh()
            messagebox.showinfo("Result", msg)
            return True
        return False

    def human_move(self, i):
        if self.over or self.board[i] != " ": return
        self.board[i] = HUMAN
        self.refresh()
        if self.check_end(): return
        self.status.config(text="AI thinking...")
        self.root.after(300, self.ai_move)

    def ai_move(self):
        m = best_move(self.board)
        if m is not None: self.board[m] = AI
        self.refresh()
        if not self.check_end():
            self.status.config(text="Your turn (X)")

if __name__ == "__main__":
    root = tk.Tk()
    Game(root)
    root.mainloop()
