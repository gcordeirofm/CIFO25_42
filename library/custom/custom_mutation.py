import random
from copy import deepcopy



# BLOCK SWAP MUTATION
def block_swap_mutation(solution_repr, block_size = 4, mut_prob = 0.2):

    new_repr = deepcopy(solution_repr)

    if random.random() <= mut_prob:
    
        # randomly choose two indices for block start positions - must be block_size genes before end
        first_idx = random.randint(0, len(solution_repr)-(block_size-1))
        second_idx = first_idx
        
        # We want to get two indexes that are at least block_size number of genes away from one another
        while abs(second_idx-first_idx) <= block_size:
            second_idx = random.randint(0, len(solution_repr)-(block_size-1))

        # Ensure first_idx < second_idx
        if first_idx > second_idx:
            first_idx, second_idx = second_idx, first_idx

        for i in range(block_size):
            solution_repr[first_idx + i], solution_repr[second_idx + i] = solution_repr[second_idx + i], solution_repr[first_idx + i]

        return solution_repr
    
    else:
        return new_repr



# SHUFFLE SUBSEQUENCE MUTATION
def shuffle_subsequence_mutation(solution_repr, mut_prob = 0.2):

    new_repr = deepcopy(solution_repr)

    if random.random() <= mut_prob:

        # Select two distinct indices
        first_idx = random.randint(0, len(new_repr)-1)
        second_idx = first_idx

        # We want to get two indices that are at least 2 genes away
        while abs(second_idx-first_idx) <= 1:
            second_idx = random.randint(0, len(new_repr)-1)
    
        # Ensure first_idx < second_idx
        if first_idx > second_idx:
            first_idx, second_idx = second_idx, first_idx

        # Reverse between first and second index
        subsequence = new_repr[first_idx:second_idx]

        # Shuffle the subsequence in place
        random.shuffle(subsequence)
        
        # Reassign shuffled values between 2 indices
        new_repr[first_idx:second_idx] = subsequence

        return new_repr
    
    else:
        return new_repr



# N-SWAP MUTATION
def n_swap_mutation(solution_repr, mut_prob = 0.2, n = 8):

    new_repr = deepcopy(solution_repr)

    if random.random() <= mut_prob:
        for _ in range (n):
            i, j = random.sample(range(len(solution_repr)), 2)
            new_repr[i], new_repr[j] = new_repr[j], new_repr[i]

        return new_repr
    
    else:
        return new_repr
    


# DISPLACEMENT MUTATION
def displacement_mutation(solution_repr, mut_prob = 0.2):
    
    new_repr = deepcopy(solution_repr)

    if random.random() <= mut_prob:

        # Select two distinct indices
        first_idx = random.randint(0, len(new_repr)-1)
        second_idx = first_idx

        # We want to get two indices that are at least 2 genes away
        while abs(second_idx-first_idx) <= 1:
            second_idx = random.randint(0, len(new_repr)-1)
    
        # Ensure first_idx < second_idx
        if first_idx > second_idx:
            first_idx, second_idx = second_idx, first_idx

        subsequence = new_repr[first_idx:second_idx+1]

        # remove selected subsequence from solution representation
        remaining = new_repr[: first_idx] + new_repr[second_idx + 1:]

        # choose a random position to re-insert the cut segment
        insert_position = random.randint(0, len(remaining))

        new_repr = remaining[: insert_position] + subsequence + remaining[insert_position: ]

        return new_repr
    
    else:
        return new_repr