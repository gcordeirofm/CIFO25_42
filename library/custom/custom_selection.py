import random
from copy import deepcopy



# RANKING SELECTION
def ranking_selection(population: list, maximization: bool = True):

    # function to get fitness of individual in population
    def get_fitness(ind):
        return ind.fitness()

    # sort the individuals in the population based on fitness values
    if maximization:
        sorted_population = sorted(population, key=get_fitness, reverse=True)
    else:
        sorted_population = sorted(population, key=get_fitness)

    # create ranking list in descending order for maximization
    rankings = list(range(len(population), 0, -1))

    if not maximization:
        rankings = list(range(1, len(population) + 1))

    total_rank = sum(rankings)

    probabilities = []
    for r in rankings:
        ind_prob = r / total_rank
        probabilities.append(ind_prob)

    # box-selection method from Lab Week 6
    # Generate random number between 0 and 1
    random_nr = random.uniform(0, 1)
    box_boundary = 0

    # For each individual, check if random number is inside the individual's "box"
    for ind_idx, ind in enumerate(sorted_population):
        box_boundary += probabilities[ind_idx]
        if random_nr <= box_boundary:
            return deepcopy(ind)
        


# TOURNAMENT SELECTION
def tournament_selection(population: list, maximization: bool = True, k: int = 4):

    # function to get fitness of individual in population
    def get_fitness(ind):
        return ind.fitness()

    # sample k random inidividuals from population
    tournament = random.sample(population, k)

    # choose winner of tournament
    if maximization:
        winner = max(tournament, key=get_fitness)
    
    else:
        winner = min(tournament, key=get_fitness)

    return deepcopy(winner)