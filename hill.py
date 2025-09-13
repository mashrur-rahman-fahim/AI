import random

# Goal state
goal_state = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 0]]  # 0 = blank

# Manhattan Distance heuristic
def manhattan_distance(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            val = state[i][j]
            if val != 0:
                goal_x, goal_y = divmod(val - 1, 3)
                distance += abs(goal_x - i) + abs(goal_y - j)
    return distance

# Misplaced Tiles heuristic
def misplaced_tiles(state):
    misplaced = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0 and state[i][j] != goal_state[i][j]:
                misplaced += 1
    return misplaced

# Choose heuristic (pass "manhattan" or "misplaced")
def heuristic(state, method="manhattan"):
    if method == "manhattan":
        return manhattan_distance(state)
    elif method == "misplaced":
        return misplaced_tiles(state)
    else:
        raise ValueError("Invalid heuristic method")

# Find blank position
def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

# Generate neighbors
def generate_neighbors(state):
    neighbors = []
    x, y = find_blank(state)
    moves = [(-1,0),(1,0),(0,-1),(0,1)]  # Up, Down, Left, Right
    
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]  # Deep copy
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(new_state)
    return neighbors

# Hill Climbing
def hill_climbing(initial_state, method="manhattan", max_steps=100):
    current = initial_state
    current_h = heuristic(current, method)
    
    steps = 0
    while steps < max_steps and current_h != 0:
        neighbors = generate_neighbors(current)
        next_state = min(neighbors, key=lambda s: heuristic(s, method))
        next_h = heuristic(next_state, method)
        
        if next_h >= current_h:  # No improvement
            break
        
        current, current_h = next_state, next_h
        steps += 1
        print(f"Step {steps}: h={current_h}")
        for row in current:
            print(row)
        print()
    
    return current, current_h

# Example run
initial_state = [[1, 2, 3],
                 [4, 0, 6],
                 [7, 5, 8]]

print("Initial State:")
for row in initial_state:
    print(row)

# Run with Manhattan Distance
solution, h = hill_climbing(initial_state, method="manhattan")
print("Final State using Manhattan Distance:")
for row in solution:
    print(row)
print("Heuristic:", h, "\n")

# Run with Misplaced Tiles
solution, h = hill_climbing(initial_state, method="misplaced")
print("Final State using Misplaced Tiles:")
for row in solution:
    print(row)
print("Heuristic:", h)