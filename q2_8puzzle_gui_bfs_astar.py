# Q2: GUI 8-Puzzle Solver (BFS + A*, with comparison)
import tkinter as tk
from tkinter import messagebox
from collections import deque
import heapq, random, time

GOAL = (1, 2, 3, 4, 5, 6, 7, 8, 0)
MOVES = [("Up", -1, 0), ("Down", 1, 0), ("Left", 0, -1), ("Right", 0, 1)]

def neighbors(s):
    i = s.index(0); r, c = divmod(i, 3)
    for name, dr, dc in MOVES:
        nr, nc = r + dr, c + dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            j = nr * 3 + nc
            l = list(s); l[i], l[j] = l[j], l[i]
            yield name, tuple(l)

def solvable(s):
    a = [x for x in s if x]
    inv = sum(1 for i in range(8) for j in range(i + 1, 8) if a[i] > a[j])
    return inv % 2 == 0

def manhattan(s):
    d = 0
    for i, v in enumerate(s):
        if v:
            g = v - 1
            d += abs(i // 3 - g // 3) + abs(i % 3 - g % 3)
    return d

def build(parent, s):
    path, moves = [], []
    while parent[s][0] is not None:
        p, m = parent[s]
        path.append(s); moves.append(m); s = p
    path.append(s)
    return path[::-1], moves[::-1]

def bfs(start):
    t = time.perf_counter()
    q = deque([start]); parent = {start: (None, None)}; explored = 0
    while q:
        s = q.popleft(); explored += 1
        if s == GOAL:
            p, m = build(parent, s)
            return p, m, explored, time.perf_counter() - t
        for m, n in neighbors(s):
            if n not in parent:
                parent[n] = (s, m); q.append(n)

def astar(start):
    t = time.perf_counter()
    h = [(manhattan(start), 0, 0, start)]; parent = {start: (None, None)}
    best = {start: 0}; explored = 0; cnt = 0
    while h:
        f, _, g, s = heapq.heappop(h)
        if g > best.get(s, 1e9): continue
        explored += 1
        if s == GOAL:
            p, m = build(parent, s)
            return p, m, explored, time.perf_counter() - t
        for m, n in neighbors(s):
            ng = g + 1
            if ng < best.get(n, 1e9):
                best[n] = ng; parent[n] = (s, m); cnt += 1
                heapq.heappush(h, (ng + manhattan(n), cnt, ng, n))

class App:
    def __init__(self, root):
        self.root = root; root.title("8-Puzzle Solver (BFS & A*)")
        self.state = (1, 2, 3, 4, 0, 6, 7, 5, 8)
        self.cells = []
        grid = tk.Frame(root); grid.grid(row=0, column=0, padx=10, pady=10)
        for i in range(9):
            l = tk.Label(grid, text="", font=("Arial", 26, "bold"), width=3, height=1, relief="ridge", bd=3)
            l.grid(row=i // 3, column=i % 3, padx=2, pady=2); self.cells.append(l)
        ctrl = tk.Frame(root); ctrl.grid(row=1, column=0)
        tk.Label(ctrl, text="State (9 digits, 0=blank):").grid(row=0, column=0)
        self.entry = tk.Entry(ctrl, width=12); self.entry.insert(0, "123406758"); self.entry.grid(row=0, column=1)
        tk.Button(ctrl, text="Set", command=self.set_state).grid(row=0, column=2)
        tk.Button(ctrl, text="Random", command=self.random_state).grid(row=0, column=3)
        tk.Button(ctrl, text="Solve BFS", command=lambda: self.solve("BFS")).grid(row=1, column=0)
        tk.Button(ctrl, text="Solve A*", command=lambda: self.solve("A*")).grid(row=1, column=1)
        tk.Button(ctrl, text="Compare", command=self.compare).grid(row=1, column=2)
        self.out = tk.Text(root, width=48, height=12); self.out.grid(row=2, column=0, padx=10, pady=10)
        self.set_state()

    def draw(self, s):
        for i, v in enumerate(s):
            self.cells[i].config(text=str(v) if v else "", bg="#ddd" if v else "#555")

    def set_state(self):
        t = self.entry.get().strip()
        if len(t) != 9 or sorted(t) != list("012345678"):
            messagebox.showerror("Error", "enter digits 0-8 exactly once"); return
        s = tuple(int(c) for c in t)
        if not solvable(s):
            messagebox.showerror("Error", "this configuration is unsolvable"); return
        self.state = s; self.draw(s)

    def random_state(self):
        while True:
            l = list(range(9)); random.shuffle(l)
            if solvable(tuple(l)): break
        self.entry.delete(0, tk.END); self.entry.insert(0, "".join(map(str, l)))
        self.state = tuple(l); self.draw(self.state)

    def solve(self, algo):
        r = bfs(self.state) if algo == "BFS" else astar(self.state)
        path, moves, ex, t = r
        self.out.delete("1.0", tk.END)
        self.out.insert(tk.END, f"{algo}: {len(moves)} moves, {ex} states explored, {t*1000:.2f} ms\n")
        self.out.insert(tk.END, "Moves: " + (", ".join(moves) if moves else "already solved") + "\n")
        self.animate(path, 0)

    def animate(self, path, i):
        if i < len(path):
            self.draw(path[i]); self.root.after(400, lambda: self.animate(path, i + 1))

    def compare(self):
        b = bfs(self.state); a = astar(self.state)
        self.out.delete("1.0", tk.END)
        self.out.insert(tk.END, f"{'Algo':<6}{'Moves':<8}{'Explored':<10}{'Time(ms)'}\n")
        self.out.insert(tk.END, f"{'BFS':<6}{len(b[1]):<8}{b[2]:<10}{b[3]*1000:.2f}\n")
        self.out.insert(tk.END, f"{'A*':<6}{len(a[1]):<8}{a[2]:<10}{a[3]*1000:.2f}\n")
        self.out.insert(tk.END, "\nBoth optimal; A* explores fewer states.\n")

if __name__ == "__main__":
    root = tk.Tk(); App(root); root.mainloop()
