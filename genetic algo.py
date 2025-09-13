import random

def generate_population():
    return [random.randint(0, 7) for _ in range(8)]

def fitness(board):
    attacking_pair = 0
    for i in range(len(board)):
        for j in range(i+1, len(board)):
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(j - i):
                attacking_pair += 1
    return attacking_pair


def crossover(parent1, parent2):
    point = 4
    return parent1[:point] + parent2[point:]

def mutate(child):
    idx = random.randint(0, 7)
    value = random.randint(1, 7)
    if child[idx]!=value :
      child[idx] = value
    else:
      child[idx] = value-1

def genetic_algorithm():
    population = [generate_population() for _ in range(100)]
    generations = 0

    while True:
        population = sorted(population, key=lambda x: fitness(x))
        if fitness(population[0]) == 0 or generations == 40000:
            return population[0], generations, fitness(population[0])

        new_population = population[:15]
        parent1, parent2 = population[:2]
        child1 = crossover(parent1, parent2)
        child2 = crossover(parent2, parent1)
        mutate(child1)
        mutate(child2)
        new_population.append(child1)
        new_population.append(child2)
        population = new_population
        generations += 1

solution, generations, fitness = genetic_algorithm()
print(f"Solution found in {generations} generations")
print("Solution:", solution)
print("no of attacking pairs: ", fitness)
