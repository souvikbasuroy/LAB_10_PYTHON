# Q3: BFS for route finding (path + nodes explored)
from collections import deque

def bfs(graph, start, goal):
    queue = deque([start])
    parent = {start: None}
    explored = 0
    while queue:
        node = queue.popleft()
        explored += 1
        if node == goal:
            path = []
            while node is not None:
                path.append(node); node = parent[node]
            return path[::-1], explored
        for nb in graph.get(node, []):
            if nb not in parent:
                parent[nb] = node
                queue.append(nb)
    return None, explored

def read_graph():
    graph = {}
    n = int(input("number of edges: "))
    print("enter edges as 'A B':")
    for _ in range(n):
        u, v = input().split()
        graph.setdefault(u, []).append(v)
        graph.setdefault(v, []).append(u)
    return graph

if __name__ == "__main__":
    use_input = input("enter own graph? (y/n): ").strip().lower() == "y"
    if use_input:
        graph = read_graph()
        start = input("start node: ").strip()
        goal = input("goal node: ").strip()
    else:
        graph = {"A": ["B", "C"], "B": ["A", "D", "E"], "C": ["A", "F"],
                 "D": ["B"], "E": ["B", "F"], "F": ["C", "E", "G"], "G": ["F"]}
        start, goal = "A", "G"
    path, explored = bfs(graph, start, goal)
    if path:
        print("Path found :", " -> ".join(path))
        print("Path length:", len(path) - 1, "edges")
    else:
        print("No path found")
    print("Nodes explored:", explored)
