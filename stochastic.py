import random

def fitness(board):
    """Calculate the number of non-attacking pairs."""
    non_attacking = 28  # Total pairs in 8 queens (8C2 = 28)
    attacking_pairs = 0

    for i in range(len(board)):
        for j in range(i + 1, len(board)):
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                attacking_pairs += 1
    
    return non_attacking - attacking_pairs

def generate_successors(state):
    """Generate all possible successors by moving one queen at a time."""
    successors = []
    
    for col in range(len(state)):
        for row in range(1, 9):  # Queens can be in rows 1 to 8
            if state[col] != row:
                new_state = state[:]
                new_state[col] = row
                successors.append(new_state)
    
    return successors

def stochastic_hill_climbing(initial_state):
    """Stochastic Hill Climbing Algorithm."""
    current_state = initial_state
    current_fitness = fitness(current_state)
    
    iterations = 0
    while current_fitness < 28 and iterations < 50:
        successors = generate_successors(current_state)
        random.shuffle(successors)  # Randomize successors for stochastic behavior
        
        # Print any 3 random successors
        print("Three random successors:")
        for s in random.sample(successors, 3):
            print(s, "Fitness:", fitness(s))
        
        # Select only the uphill moves
        uphill_moves = [s for s in successors if fitness(s) > current_fitness]

        if not uphill_moves:
            print("No better move found. Stuck in local maxima!")
            break  # Stop if no better moves exist
        
        # Choose a random uphill move (Stochastic selection)
        current_state = random.choice(uphill_moves)
        current_fitness = fitness(current_state)
        
        print(f"Iteration {iterations + 1}: New state: {current_state} | Fitness: {current_fitness}")
        iterations += 1

    return current_state, current_fitness, iterations

# Initial state from problem statement
initial_state = [2, 3, 4, 5, 6, 5, 7, 8]

# Run the algorithm
solution, final_fitness, total_iterations = stochastic_hill_climbing(initial_state)

# Print final solution
print("\nFinal Solution:")
print("State:", solution)
print("Fitness:", final_fitness)
print("Total Iterations:", total_iterations)
