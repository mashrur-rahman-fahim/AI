import random

# Goal state
goal_state = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 0]]  # 0 = blank space

# Calculate Manhattan Distance heuristic
def heuristic(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            val = state[i][j]
            if val != 0:  # Skip blank
                goal_x, goal_y = divmod(val - 1, 3)  # Goal position
                distance += abs(goal_x - i) + abs(goal_y - j)
    return distance

# Find the blank (0) position
def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

# Generate neighbors by moving the blank
def generate_neighbors(state):
    neighbors = []
    x, y = find_blank(state)
    moves = [(-1,0),(1,0),(0,-1),(0,1)]  # Up, Down, Left, Right
    
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]  # Copy
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(new_state)
    return neighbors

# Hill Climbing Algorithm
def hill_climbing(initial_state, max_steps=100):
    current = initial_state
    current_h = heuristic(current)
    
    steps = 0
    while steps < max_steps and current_h != 0:
        neighbors = generate_neighbors(current)
        # Choose best neighbor (with lowest heuristic)
        next_state = min(neighbors, key=heuristic)
        next_h = heuristic(next_state)
        
        if next_h >= current_h:  # No improvement
            break
        
        current, current_h = next_state, next_h
        steps += 1
        print(f"Step {steps}: h={current_h}")
        for row in current:
            print(row)
        print()
    
    return current, current_h

# Example run with a random initial state
initial_state = [[1, 2, 3],
                 [4, 0, 6],
                 [7, 5, 8]]

print("Initial State:")
for row in initial_state:
    print(row)

solution, h = hill_climbing(initial_state)

print("Final State (after Hill Climbing):")
for row in solution:
    print(row)
print("Heuristic:", h)