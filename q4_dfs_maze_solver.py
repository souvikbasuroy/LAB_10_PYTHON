# Q4: DFS maze solver (2D matrix). 0 = open, 1 = wall
import sys
sys.setrecursionlimit(10000)

def dfs_maze(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    visited = set()
    path = []

    def dfs(r, c):
        if not (0 <= r < rows and 0 <= c < cols) or maze[r][c] == 1 or (r, c) in visited:
            return False
        visited.add((r, c))
        path.append((r, c))
        if (r, c) == end:
            return True
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            if dfs(r + dr, c + dc):
                return True
        path.pop()          # backtrack
        return False

    return path if dfs(*start) else None

def show(maze, path):
    grid = [["#" if x else "." for x in row] for row in maze]
    for r, c in path or []:
        grid[r][c] = "*"
    if path:
        grid[path[0][0]][path[0][1]] = "S"
        grid[path[-1][0]][path[-1][1]] = "E"
    print("\n".join(" ".join(row) for row in grid))

if __name__ == "__main__":
    maze = [
        [0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 0, 1, 0],
    ]
    start, end = (0, 0), (4, 4)
    path = dfs_maze(maze, start, end)
    if path:
        print("Path:", " -> ".join(map(str, path)))
        print("Steps:", len(path) - 1, "\n")
        show(maze, path)
    else:
        print("No path exists")
