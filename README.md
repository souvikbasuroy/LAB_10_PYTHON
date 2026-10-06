# AI Lab Assignments: Programming with Python Lab 
## Souvik Basu Roy

Ten Python programs covering core AI topics: adversarial search, uninformed and informed search, knowledge representation, and intelligent agents. Each program is a standalone script with no third-party dependencies.

## Contents

| # | File | Topic | Algorithm(s) | Type |
|---|------|-------|--------------|------|
| 1 | `q1_tictactoe_minimax_gui.py` | Tic-Tac-Toe, human vs AI | Minimax | GUI |
| 2 | `q2_8puzzle_gui_bfs_astar.py` | 8-Puzzle solver with comparison | BFS, A* | GUI |
| 3 | `q3_bfs_route_finding.py` | Route finding in a graph | BFS | CLI |
| 4 | `q4_dfs_maze_solver.py` | Maze solving on a 2D matrix | DFS (backtracking) | CLI |
| 5 | `q5_astar_8puzzle_manhattan.py` | 8-Puzzle with Manhattan heuristic | A* | CLI |
| 6 | `q6_greedy_best_first_route.py` | City route planning, compared with BFS | Greedy Best-First, BFS | CLI |
| 7 | `q7_propositional_logic_kb.py` | Knowledge base (classroom domain) | Forward chaining | CLI |
| 8 | `q8_semantic_network_vehicles.py` | Semantic network (vehicles) | IS-A inheritance traversal | CLI |
| 9 | `q9_peas_generator.py` | PEAS description generator | Dictionary lookup | CLI |
| 10 | `q10_navigation_agent_gui.py` | Navigation agent on a grid | BFS, DFS, Greedy, A* | GUI |

## Requirements

- Python 3.8+
- `tkinter` for Q1, Q2 and Q10. It ships with most Python installs. On Debian/Ubuntu: `sudo apt install python3-tk`

No `pip install` needed.

## Running

```bash
git clone https://github.com/souvikbasuroy/LAB_10_PYTHON
cd LAB_10_PYTHON
python q1_tictactoe_minimax_gui.py
```

Replace the filename with any program from the table above.

## Program notes

### Part A: GUI-based AI applications

**Q1: Tic-Tac-Toe.** The human plays X and the AI plays O. The AI runs full-depth Minimax, so it never loses. The GUI shows the board, whose turn it is, and the final result, with a restart button.

**Q2: 8-Puzzle solver.** Enter a 9-digit state (`0` is the blank) or generate a random one. Unsolvable states are rejected using an inversion-parity check. You can solve with BFS or A*, watch the animated solution, or compare both by moves, states explored and time.

### Part B: Blind (uninformed) search

**Q3: BFS route finding.** Runs on a built-in sample graph or on edges you type in. Prints the path, its length and the number of nodes explored.

**Q4: DFS maze solver.** The maze is a 2D matrix (`0` is open, `1` is wall). Prints the path as coordinates and as an ASCII maze (`S` start, `E` end, `*` path).

### Part C: Heuristic search

**Q5: A\* for the 8-puzzle.** Uses Manhattan distance as the heuristic. Prints the initial state, every intermediate state, the final state, total path cost and states explored.

**Q6: Greedy Best-First vs BFS.** Runs both on a city road graph, using straight-line distance to the goal as the heuristic. Compares hops, distance in km and nodes explored. Neither algorithm is guaranteed to give the shortest road distance. On the sample graph both return 730 km, while a 600 km route exists.

### Part D: Knowledge representation

**Q7: Propositional logic KB.** Stores facts and Horn-clause rules for a classroom domain. Forward chaining determines whether a query can be inferred, and the derivation steps are printed. There is also an interactive query loop.

**Q8: Semantic network.** Models vehicles with `IS-A`, `HAS-A` and `CAN` relations. Properties are inherited through `IS-A` links. Example queries:

```
is sportscar a vehicle
does sportscar have wheels
can truck carry cargo
describe car
```

### Part E: PEAS and intelligent agents

**Q9: PEAS generator.** Prints the Performance measure, Environment, Actuators and Sensors for a given AI task. Built-in tasks: vacuum cleaner agent, self-driving car, medical diagnosis system, chess player, navigation agent. For an unknown task it prompts you to enter the components.

### Part F: Integrated AI problem

**Q10: Navigation agent.** A random grid with walls is shown in a GUI. Run BFS, DFS, Greedy or A* and watch the search animate (blue is explored, yellow is the final path). **Compare All** reports path cost, nodes explored and execution time for each algorithm, and names the best one. The PEAS description of the agent is shown in the output panel.
