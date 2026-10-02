# Q6: Greedy Best-First Search vs BFS for route planning
import heapq
from collections import deque

# road graph: city -> {neighbor: road distance km}
GRAPH = {
    "Kolkata":   {"Durgapur": 170, "Kharagpur": 120, "Ranchi": 400},
    "Durgapur":  {"Kolkata": 170, "Asansol": 40, "Dhanbad": 100},
    "Kharagpur": {"Kolkata": 120, "Jamshedpur": 130},
    "Asansol":   {"Durgapur": 40, "Dhanbad": 60},
    "Dhanbad":   {"Durgapur": 100, "Asansol": 60, "Ranchi": 160, "Patna": 330},
    "Jamshedpur":{"Kharagpur": 130, "Ranchi": 130},
    "Ranchi":    {"Kolkata": 400, "Dhanbad": 160, "Jamshedpur": 130, "Patna": 330},
    "Patna":     {"Dhanbad": 330, "Ranchi": 330},
}
# estimated straight-line distance to goal (Patna), km
H = {"Kolkata": 460, "Durgapur": 370, "Kharagpur": 480, "Asansol": 330,
     "Dhanbad": 280, "Jamshedpur": 360, "Ranchi": 250, "Patna": 0}

def cost(path):
    return sum(GRAPH[a][b] for a, b in zip(path, path[1:]))

def greedy(start, goal):
    heap = [(H[start], start)]
    parent = {start: None}
    explored = 0
    seen = set()
    while heap:
        _, n = heapq.heappop(heap)
        if n in seen: continue
        seen.add(n); explored += 1
        if n == goal:
            path = []
            while n: path.append(n); n = parent[n]
            return path[::-1], explored
        for nb in GRAPH[n]:
            if nb not in parent:
                parent[nb] = n
                heapq.heappush(heap, (H[nb], nb))
    return None, explored

def bfs(start, goal):
    q = deque([start]); parent = {start: None}; explored = 0
    while q:
        n = q.popleft(); explored += 1
        if n == goal:
            path = []
            while n: path.append(n); n = parent[n]
            return path[::-1], explored
        for nb in GRAPH[n]:
            if nb not in parent:
                parent[nb] = n; q.append(nb)
    return None, explored

if __name__ == "__main__":
    start, goal = "Kolkata", "Patna"
    gp, ge = greedy(start, goal)
    bp, be = bfs(start, goal)
    print(f"Greedy BFS : {' -> '.join(gp)}\n  hops={len(gp)-1}, distance={cost(gp)} km, nodes explored={ge}")
    print(f"BFS        : {' -> '.join(bp)}\n  hops={len(bp)-1}, distance={cost(bp)} km, nodes explored={be}")
    print("""
Discussion:
- BFS finds the path with the fewest hops (edges) but ignores road distance,
  so it is not guaranteed to be the shortest in km.
- Greedy uses only h(n) (estimated distance to goal). It is usually fast and
  explores fewer nodes, but it is neither optimal nor always complete on
  graphs with traps, since it ignores the cost already travelled.
- BFS explores level by level, so it can expand many irrelevant nodes.""")
