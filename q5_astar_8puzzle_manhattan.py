# Q5: A* for 8-puzzle with Manhattan distance
import heapq

GOAL = (1, 2, 3, 4, 5, 6, 7, 8, 0)

def manhattan(s):
    d = 0
    for i, v in enumerate(s):
        if v:
            g = v - 1
            d += abs(i // 3 - g // 3) + abs(i % 3 - g % 3)
    return d

def neighbors(s):
    i = s.index(0); r, c = divmod(i, 3)
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            j = nr * 3 + nc
            l = list(s); l[i], l[j] = l[j], l[i]
            yield tuple(l)

def solvable(s):
    a = [x for x in s if x]
    return sum(1 for i in range(8) for j in range(i + 1, 8) if a[i] > a[j]) % 2 == 0

def astar(start):
    heap = [(manhattan(start), 0, 0, start)]
    parent = {start: None}
    best = {start: 0}
    explored, cnt = 0, 0
    while heap:
        f, _, g, s = heapq.heappop(heap)
        if g > best[s]:
            continue
        explored += 1
        if s == GOAL:
            path = []
            while s is not None:
                path.append(s); s = parent[s]
            return path[::-1], g, explored
        for n in neighbors(s):
            ng = g + 1
            if ng < best.get(n, float("inf")):
                best[n] = ng; parent[n] = s; cnt += 1
                heapq.heappush(heap, (ng + manhattan(n), cnt, ng, n))
    return None, 0, explored

def show(s, label):
    print(label)
    for r in range(3):
        print(" ".join(str(x) if x else "_" for x in s[r * 3:r * 3 + 3]))
    print()

if __name__ == "__main__":
    raw = input("initial state, 9 digits (0=blank) [Enter for default 283164705]: ").strip() or "283164705"
    start = tuple(int(c) for c in raw)
    assert sorted(start) == list(range(9)), "use digits 0-8 once each"
    if not solvable(start):
        print("unsolvable configuration"); raise SystemExit
    path, cost, explored = astar(start)
    show(path[0], "Initial state:")
    for i, s in enumerate(path[1:-1], 1):
        show(s, f"Step {i}:")
    show(path[-1], "Final state:")
    print("Total path cost :", cost)
    print("States explored :", explored)
