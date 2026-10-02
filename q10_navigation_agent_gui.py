# Q10: Intelligent Navigation Agent (BFS, DFS, Greedy, A*) with GUI + comparison + PEAS
import tkinter as tk
from collections import deque
import heapq, random, time

ROWS, COLS, CELL = 15, 20, 30
DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def h(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def nbrs(grid, p):
    for dr, dc in DIRS:
        r, c = p[0] + dr, p[1] + dc
        if 0 <= r < ROWS and 0 <= c < COLS and grid[r][c] == 0:
            yield (r, c)

def trace(parent, g):
    path = []
    while g is not None:
        path.append(g); g = parent[g]
    return path[::-1]

def bfs(grid, s, g):
    q = deque([s]); parent = {s: None}; order = []
    while q:
        n = q.popleft(); order.append(n)
        if n == g: return trace(parent, n), order
        for m in nbrs(grid, n):
            if m not in parent: parent[m] = n; q.append(m)
    return None, order

def dfs(grid, s, g):
    st = [s]; parent = {s: None}; order = []; seen = set()
    while st:
        n = st.pop()
        if n in seen: continue
        seen.add(n); order.append(n)
        if n == g: return trace(parent, n), order
        for m in nbrs(grid, n):
            if m not in seen:
                parent[m] = n; st.append(m)
    return None, order

def greedy(grid, s, g):
    hp = [(h(s, g), s)]; parent = {s: None}; order = []; seen = set()
    while hp:
        _, n = heapq.heappop(hp)
        if n in seen: continue
        seen.add(n); order.append(n)
        if n == g: return trace(parent, n), order
        for m in nbrs(grid, n):
            if m not in parent:
                parent[m] = n; heapq.heappush(hp, (h(m, g), m))
    return None, order

def astar(grid, s, g):
    hp = [(h(s, g), 0, s)]; parent = {s: None}; best = {s: 0}; order = []; seen = set()
    while hp:
        _, gc, n = heapq.heappop(hp)
        if n in seen: continue
        seen.add(n); order.append(n)
        if n == g: return trace(parent, n), order
        for m in nbrs(grid, n):
            ng = gc + 1
            if ng < best.get(m, 1e9):
                best[m] = ng; parent[m] = n
                heapq.heappush(hp, (ng + h(m, g), ng, m))
    return None, order

ALGOS = {"BFS": bfs, "DFS": dfs, "Greedy": greedy, "A*": astar}

PEAS = """PEAS of Navigation Agent
P : path cost, nodes explored, execution time, reaching goal
E : 2D grid with walls/obstacles, start and goal cells
A : move up / down / left / right
S : current position, obstacle detection, goal location"""

class App:
    def __init__(self, root):
        root.title("Intelligent Navigation Agent")
        self.root = root
        self.start, self.goal = (0, 0), (ROWS - 1, COLS - 1)
        self.canvas = tk.Canvas(root, width=COLS * CELL, height=ROWS * CELL)
        self.canvas.grid(row=0, column=0, columnspan=6, padx=8, pady=8)
        self.new_grid()
        for i, a in enumerate(ALGOS):
            tk.Button(root, text=f"Run {a}", command=lambda a=a: self.run(a)).grid(row=1, column=i)
        tk.Button(root, text="Compare All", command=self.compare).grid(row=1, column=4)
        tk.Button(root, text="New Grid", command=self.new_grid).grid(row=1, column=5)
        self.out = tk.Text(root, width=95, height=16); self.out.grid(row=2, column=0, columnspan=6, padx=8, pady=8)
        self.out.insert(tk.END, PEAS + "\n")

    def new_grid(self):
        while True:
            self.grid = [[1 if random.random() < 0.25 else 0 for _ in range(COLS)] for _ in range(ROWS)]
            self.grid[self.start[0]][self.start[1]] = 0
            self.grid[self.goal[0]][self.goal[1]] = 0
            if bfs(self.grid, self.start, self.goal)[0]: break
        self.draw()

    def draw(self):
        self.canvas.delete("all")
        for r in range(ROWS):
            for c in range(COLS):
                col = "black" if self.grid[r][c] else "white"
                self.canvas.create_rectangle(c*CELL, r*CELL, (c+1)*CELL, (r+1)*CELL, fill=col, outline="#ccc", tags=f"c{r}_{c}")
        self.paint(self.start, "green"); self.paint(self.goal, "red")

    def paint(self, p, color):
        r, c = p
        self.canvas.create_rectangle(c*CELL, r*CELL, (c+1)*CELL, (r+1)*CELL, fill=color, outline="#ccc")

    def run(self, name, animate=True):
        t = time.perf_counter()
        path, order = ALGOS[name](self.grid, self.start, self.goal)
        et = (time.perf_counter() - t) * 1000
        res = dict(name=name, cost=len(path) - 1 if path else None, explored=len(order), time=et)
        if animate:
            self.draw()
            self.out.insert(tk.END, f"\n{name}: cost={res['cost']}, explored={res['explored']}, time={et:.3f} ms\n")
            self.out.see(tk.END)
            self.animate(order, path, 0)
        return res

    def animate(self, order, path, i):
        if i < len(order):
            p = order[i]
            if p not in (self.start, self.goal): self.paint(p, "#9ecbff")
            self.root.after(8, lambda: self.animate(order, path, i + 1))
        elif path:
            for p in path:
                if p not in (self.start, self.goal): self.paint(p, "gold")

    def compare(self):
        res = [self.run(a, animate=False) for a in ALGOS]
        self.out.insert(tk.END, f"\n{'Algorithm':<10}{'Path cost':<12}{'Nodes explored':<16}{'Time (ms)'}\n")
        for r in res:
            self.out.insert(tk.END, f"{r['name']:<10}{r['cost']:<12}{r['explored']:<16}{r['time']:.3f}\n")
        best = min(res, key=lambda r: (r["cost"], r["explored"], r["time"]))
        self.out.insert(tk.END, f"\nBest for this environment: {best['name']} "
                                f"(optimal cost with fewest explored nodes)\n")
        self.out.insert(tk.END, "Note: BFS and A* give optimal paths; A* usually explores far fewer nodes. "
                                "DFS is fast but gives long paths; Greedy is fast but not guaranteed optimal.\n")
        self.out.see(tk.END)

if __name__ == "__main__":
    root = tk.Tk(); App(root); root.mainloop()
