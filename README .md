# SLE-2: BFS vs DFS on 8-Puzzle

**Course:** 02AML204 – Introduction to Artificial Intelligence  
**PRN:** 25UAM133  
**Name:** Sanchit Sachin Magdum  
**Division:** B  
**GitHub:** https://github.com/sanchitmagdum17/IAI-SLE-25UAM133

## 1. Project Overview

This project compares two uninformed search algorithms:

- Breadth-First Search (BFS)
- Depth-First Search (DFS)

Both algorithms are applied to the **8-Puzzle problem** and are profiled using execution time, nodes expanded, and solution path length.

## 2. Problem Description

The 8-Puzzle consists of eight numbered tiles and one blank space arranged in a 3×3 grid.

The experiment uses the following goal state:

```text
1 2 3
4 5 6
7 8 _
```

The same puzzle rules and goal state are used for BFS and DFS.

## 3. Experimental Cases

Three fixed puzzle instances are used to represent the selected experimental cases:

- **Best case / Easy case**
- **Average case / Medium case**
- **Worst case / Hard case**

These labels describe the selected experimental test cases. They are not claims about the formal theoretical best, average, or worst-case complexity of BFS or DFS.

## 4. Profiling Method

Execution time is measured using Python's `time.perf_counter()`.

For each algorithm and test case:

1. The timer starts immediately before the search.
2. The search algorithm is executed.
3. The timer stops immediately after the search.
4. The elapsed time is recorded.
5. A node counter records each state removed from the frontier and expanded.
6. The solution path length is calculated from the reconstructed path.

The experiment uses repeated timing runs and reports the average execution time.

## 5. Algorithms

### Breadth-First Search (BFS)

BFS uses a FIFO queue and explores states level by level. Since every 8-Puzzle move has equal cost, BFS returns a shortest solution when a solution exists.

### Depth-First Search (DFS)

DFS uses a LIFO stack and explores a branch deeply before moving to another branch. DFS can find a solution but does not guarantee that the returned solution is shortest.

## 6. Measurements

The experiment records:

- Average execution time in milliseconds
- Nodes expanded
- Solution path length
- BFS vs DFS comparison for all three selected cases

## 7. Profiling Visualization

The project includes a cProfile-based flame-style profiling visualization. It provides an additional view of the cumulative execution time of the search functions.

The direct `time.perf_counter()` measurements are used as the primary timing results.

## 8. Files

- `eight_puzzle_bfs_dfs.py` – BFS and DFS implementation for the 8-Puzzle
- `README.md` – Project documentation
- `Contribution_Log.md` – AI contribution record
- `8_puzzle_3case_diagram.png` – Three-case puzzle/result diagram
- `8_puzzle_3case_flame_graph.png` – Profiling visualization
- `execution_time_3cases.png` – Execution-time comparison
- `nodes_expanded_3cases.png` – Node-expansion comparison

## 9. AI Assistance

AI tools were used as development assistance for:

- Structuring the BFS and DFS implementation
- Adapting the profiling experiment to the 8-Puzzle
- Organizing the Best/Average/Worst experimental cases
- Preparing result tables and visualizations
- Preparing project documentation

The student reviewed, executed, and checked the code and experimental results before using them in the SLE-2 submission.

## 10. Conclusion

The experiment demonstrates how BFS and DFS behave differently when solving the same 8-Puzzle problem. Profiling execution time, node expansion, and path length provides measurable evidence for comparing the two search strategies.
