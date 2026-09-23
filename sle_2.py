import time
from collections import deque

START = (5, 8, 2, 1, 7, 3, 0, 4, 6)
GOAL = (1, 2, 3, 4, 5, 6, 7, 8, 0)
MOVE_ORDER = [(-1,0),(1,0),(0,-1),(0,1)]  # up, down, left, right

def neighbors(state):
    z = state.index(0)
    r, c = divmod(z, 3)
    for dr, dc in MOVE_ORDER:
        nr, nc = r + dr, c + dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            j = nr * 3 + nc
            s = list(state)
            s[z], s[j] = s[j], s[z]
            yield tuple(s)

def reconstruct(parent, node):
    path = []
    while node is not None:
        path.append(node)
        node = parent[node]
    return list(reversed(path))

def bfs(start, goal):
    frontier = deque([start])
    visited = {start}
    parent = {start: None}
    nodes_expanded = 0
    while frontier:
        current = frontier.popleft()
        nodes_expanded += 1
        if current == goal:
            return reconstruct(parent, current), nodes_expanded
        for nxt in neighbors(current):
            if nxt not in visited:
                visited.add(nxt)
                parent[nxt] = current
                frontier.append(nxt)
    return None, nodes_expanded

def dfs(start, goal):
    frontier = [start]
    visited = {start}
    parent = {start: None}
    nodes_expanded = 0
    while frontier:
        current = frontier.pop()
        nodes_expanded += 1
        if current == goal:
            return reconstruct(parent, current), nodes_expanded
        for nxt in neighbors(current):
            if nxt not in visited:
                visited.add(nxt)
                parent[nxt] = current
                frontier.append(nxt)
    return None, nodes_expanded

def run_trials(fn, runs=5):
    times = []
    path = nodes = None
    for _ in range(runs):
        t0 = time.perf_counter()
        path, nodes = fn(START, GOAL)
        t1 = time.perf_counter()
        times.append((t1 - t0) * 1000.0)
    return sum(times) / len(times), times, path, nodes

if __name__ == "__main__":
    print("=== BFS ===")
    avg, times, path, nodes = run_trials(bfs, 5)
    print("Per-run times (ms):", [round(t, 4) for t in times])
    print("Average time (ms):", round(avg, 4))
    print("Nodes expanded:", nodes)
    print("Path length (moves):", len(path)-1 if path else None)

    print()
    print("=== DFS ===")
    avg, times, path, nodes = run_trials(dfs, 5)
    print("Per-run times (ms):", [round(t, 4) for t in times])
    print("Average time (ms):", round(avg, 4))
    print("Nodes expanded:", nodes)
    print("Path length (moves):", len(path)-1 if path else None)
