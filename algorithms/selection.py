
import numpy as np

def tournament_selection(population, fitness, tournament_size, optimization_goal="min"):
    fitness = np.array(fitness)
    new_population = []
    for _ in range(len(population)):
        tournament = np.random.choice(len(population), tournament_size, replace=False)
        if optimization_goal == "min":
            winner = tournament[np.argmin(fitness[tournament])]
        else:  
            winner = tournament[np.argmax(fitness[tournament])]
        new_population.append(population[winner])
    return np.array(new_population)

def roulette_selection(population, fitness, optimization_goal="min"):
    fitness = np.array(fitness)
    if optimization_goal == "min":
    
        fitness = 1.0 / (fitness + 1e-10)
    fitness_sum = np.sum(fitness)
    probabilities = (fitness / fitness_sum) 
    selected_indices = np.random.choice(len(population), size=len(population), p=probabilities)
    return population[selected_indices]