import random

# 'tagging' helper function that gives each table instance a unique position
# imagine this as a seat number at a table

def tag_solution(solution_repr):
    counts = {}
    tagged_soln = []
    for table in solution_repr:
        if table not in counts:
            counts[table] = 0 # setting first instance of each table to 0
        tagged_soln.append((table, counts[table]))
        counts[table] += 1
    return tagged_soln


# 'untagging' helper function to return solution to original format
def untag_solution(tagged_solution):
    return [table for table, _ in tagged_solution]



# CYCLE CROSSOVER
# from lab week 8, some adaptations to make suitable for grouping
def cycle_crossover(parent1_repr, parent2_repr):

    tagged_p1 = tag_solution(parent1_repr)
    tagged_p2 = tag_solution(parent2_repr)

    initial_random_idx = random.randint(0, len(parent1_repr) - 1)

    # Initialize the cycle with the starting index
    cycle_idxs = [initial_random_idx]
    current_cycle_idx = initial_random_idx

    # Traverse the cycle by following the mapping from parent2 to parent1
    while True:
        value_parent2 = tagged_p2[current_cycle_idx]
        next_cycle_idx = tagged_p1.index(value_parent2)

        # break when we close the cycle
        if next_cycle_idx == initial_random_idx:
            break

        cycle_idxs.append(next_cycle_idx)
        current_cycle_idx = next_cycle_idx


    # building offspring
    tagged_offspring1 = []
    tagged_offspring2 = []

    for idx in range(len(parent1_repr)):
        if idx in cycle_idxs:
            # Keep values from parent1 in offspring1 in the cycle indexes
            tagged_offspring1.append(tagged_p1[idx])
            # Keep values from parent2 in offspring2 in the cycle indexes
            tagged_offspring2.append(tagged_p2[idx])
        else:
            # Swap elements from parents in non-cycle indexes
            tagged_offspring1.append(tagged_p2[idx])
            tagged_offspring2.append(tagged_p1[idx])

    # untag offspring to bring back to original format
    offspring1_repr = untag_solution(tagged_offspring1)
    offspring2_repr = untag_solution(tagged_offspring2)

    return offspring1_repr, offspring2_repr



# PARTIALLY MATCHED CROSSOVER
def partially_matched_crossover(parent1_repr, parent2_repr):

    tagged_p1 = tag_solution(parent1_repr)
    tagged_p2 = tag_solution(parent2_repr)

    size = len(tagged_p1)

    # randomly choose two indices for crossover window
    first_idx = random.randint(0, len(tagged_p1)-1)
    second_idx = first_idx
    
    # We want to get two indexes that are at least 2 genes away
    while abs(second_idx-first_idx) <= 1:
        second_idx = random.randint(0, len(tagged_p1)-1)

    # Ensure first_idx < second_idx
    if first_idx > second_idx:
        first_idx, second_idx = second_idx, first_idx

    # initiating empty offspring of correct size
    tagged_offspring1 = [None] * size
    tagged_offspring2 = [None] * size

    for i in range(first_idx, second_idx +1):

        # take values from window of opposite parent
        tagged_offspring1[i] = tagged_p2[i]
        tagged_offspring2[i] = tagged_p1[i]

    # to fill the leftover positions
    def fill_remaining(tagged_parent, tagged_offspring):
        for i in range(size):

            # leave the indices in the window alone
            if i >= first_idx and i <= second_idx:
                continue

            # copy any remaining values from primary parent
            for value in tagged_parent:
                if value not in tagged_offspring:
                    tagged_offspring[i] = value
                    break

    fill_remaining(tagged_p1, tagged_offspring1)
    fill_remaining(tagged_p2, tagged_offspring2)

    offspring1_repr = untag_solution(tagged_offspring1)
    offsrping2_repr = untag_solution(tagged_offspring2)

    return offspring1_repr, offsrping2_repr



# POSITION BASED CROSSOVER
def pos_based_crossover(parent1_repr, parent2_repr):

    tagged_p1 = tag_solution(parent1_repr)
    tagged_p2 = tag_solution(parent2_repr)

    size = len(tagged_p1)

    # choose random selection of indices
    num_indices = random.randint(1, size)
    selected_indices = sorted(random.sample(range(size), num_indices))

    # initializing empty offspring of correct size
    tagged_offspring1 = [None] * size
    tagged_offspring2 = [None] * size

    for i in selected_indices:
        tagged_offspring1[i] = tagged_p1[i]
        tagged_offspring2[i] = tagged_p2[i]

    # fill remaining indices with values from opposite parent, in the order which they appear, skipping duplicates
    def fill_remaining(tagged_parent, tagged_offspring):
        for i in range(size):

            # leave the indices that were randomly selected alone
            if i in selected_indices:
                continue

            # copy any remaining values from opposite parent
            for value in tagged_parent:
                if value not in tagged_offspring:
                    tagged_offspring[i] = value
                    break

    fill_remaining(tagged_p1, tagged_offspring2)
    fill_remaining(tagged_p2, tagged_offspring1)

    offspring1_repr = untag_solution(tagged_offspring1)
    offsrping2_repr = untag_solution(tagged_offspring2)

    return offspring1_repr, offsrping2_repr