import random

def generate_random_board():
    """Generates a random 8-queen board."""
    return [random.randint(1, 8) for _ in range(8)]

def fitness(board):
    """Returns the number of non-attacking pairs (higher is better)."""
    max_pairs = 28  # Total possible non-attacking pairs
    attacking_pairs = 0

    for i in range(len(board)):
        for j in range(i + 1, len(board)):
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                attacking_pairs += 1

    return max_pairs - attacking_pairs  # Higher is better

def generate_random_successor(board):
    """Generates a random successor by moving one queen to a new row."""
    new_board = board[:]
    col = random.randint(0, 7)  # Choose a random column (queen)
    row = random.randint(1, 8)  # Choose a new random row

    while new_board[col] == row:  # Ensure it's a different row
        row = random.randint(1, 8)

    new_board[col] = row  # Move queen
    return new_board

def first_choice_hill_climbing(max_attempts=1000):
    """Performs First-Choice Hill Climbing until a solution is found."""
    current = generate_random_board()
    attempts = 0

    while fitness(current) < 28:  # Keep running until a perfect solution is found
        successor = generate_random_successor(current)

        if fitness(successor) > fitness(current):  # Move if it's better
            current = successor
            attempts = 0  # Reset attempts since progress was made
        else:
            attempts += 1  # Count failed attempts

        if attempts >= max_attempts:  # If stuck, restart from a new state
            current = generate_random_board()
            attempts = 0

    return current

# Run the algorithm
solution = first_choice_hill_climbing()
print("Solution found:")
print(solution)
