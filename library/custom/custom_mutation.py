import random
from copy import deepcopy



# BLOCK SWAP MUTATION
def block_swap_mutation(solution_repr, block_size = 4, mut_prob = 0.2):

    '''
    Definition
        Appplies a modified swap mutation (swapping two blocks of indices) in a list represetation of a solution.
        Applied with given mutation probability.

        Block swap randomly selects two segments of the solution represenation
        (segement of length block_size) and swaps all values in the two blocks.
    
    Parameters
        solution_repr: Representation of solution to mutate (list)
        block_size: length of segments to be swapped
        mut_prob: probability of performing the mutation

    Returns
        Copy of original solution if mutation probability condition is not met
        New mutated solution if mutation probability is met

    '''

    block_size = int(block_size)
    new_repr = deepcopy(solution_repr)

    if random.random() <= mut_prob:
    
        # randomly choose two indices for block start positions - must be block_size genes before end
        first_idx = random.randint(0, len(solution_repr) - 1 - block_size)
        second_idx = first_idx
        
        # We want to get two indexes that are at least block_size number of genes away from one another
        while abs(second_idx-first_idx) <= block_size:
            second_idx = random.randint(0, len(solution_repr) - 1 - block_size)

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

    '''
    Definition
        Shuffle Subsequence is a modification of Inverse Subsequence Mutation presented in
        practiacl classes. It applies a shuffling of values between two randomly selected indices.
        Applied with given mutation probability.

        Shuffle Subsequence mutation selects two random indices from the solution,
        and randomly shuffles the values between them.

    Parameters
        solution_repr: Representation of solution to mutate (list)
        mut_prob: probability of performing the mutation
    
    Returns
        Copy of original solution if mutation probability condition is not met
        New mutated solution if mutation probability is met
    
    '''

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

    '''
    Defition
        N-Swap Mutation is a modification of Swap Mutation present in practical classes. It
        selects n random pairs of iniduces to swap perform swap mutation.
        Applied with given mutation probability.

        N-Swap mutation randomly selects n pairs of positions from given solution,
        and swaps their values.

    Parameters
        solution_repr: Representation of solution to mutate (list)
        mut_prob: probability of performing the mutation
        n: number of pairs of indices to swap

    Returns:
        Copy of original solution if mutation probability condition is not met
        New mutated solution if mutation probability is met
        
    '''

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

    '''
    Definition
        Displacement Mutation selects a random subsequence from the solution
        representation. This subsequence is removed, then re-inserted into the solution
        at a random position.
    
    Parameters
        solution_repr: Representation of solution to mutate (list)
        mut_prob: probability of performing the mutation

    Returns
        Copy of original solution if mutation probability condition is not met
        New mutated solution if mutation probability is met
    '''
    
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