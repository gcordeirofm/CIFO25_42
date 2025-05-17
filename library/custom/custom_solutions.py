from library.data.relationship_matrix import relationship_matrix
from random import shuffle
from itertools import combinations
from library.solution import Solution



# WEDDING SEAT OPTIMIZATION SOLUTION
class WSOSolution(Solution):
    def __init__(self, repr=None, relationship_matrix=relationship_matrix, table_size=8, num_tables=8):
        self.relationship_matrix = relationship_matrix
        self.table_size = table_size
        self.num_tables = num_tables

        if repr == None:
            repr = self.random_initial_representation()
        self.repr = repr
    
    def random_initial_representation(self):
        seating = [i for i in range(self.num_tables)] * self.table_size #[0,1,2,3,4,5,6,7, 0,1,2,3,4,5,6,7 ... (8 times)]
        shuffle(seating) # randomizes each guest's table
        return seating
    
    def fitness(self):
        # creating a dictionary with table_id (key): list of guests (value)
        tables = { t: [] for t in range(self.num_tables) }
        for guest_idx, table_id in enumerate(self.repr):
            tables[table_id].append(guest_idx)
        
        total_fitness = 0
        for guests in tables.values(): #iterate through each table
            for i, j in combinations(guests, 2): #iterate through each pairing in the table, no repetition
                total_fitness += relationship_matrix[i, j]
        return total_fitness
    


# WEDDING SEAT OPTIMIZATION GENETIC ALGORITHM SOLUTION
class WSOGASolution(WSOSolution):
    def __init__(
        self,
        values,
        weights,
        capacity,
        mutation_function, # Callable
        crossover_function, # Callable
        repr = None
    ):
        super().__init__(
            values=values,
            weights=weights,
            capacity=capacity,
            repr=repr,
        )

        # Save as attributes for access in methods
        self.mutation_function = mutation_function
        self.crossover_function = crossover_function

    def mutation(self, mut_prob):
        # Apply mutation function to representation
        new_repr = self.mutation_function(self.repr, mut_prob)
        # Create and return individual with mutated representation
        return WSOGASolution(
            values=self.values,
            weights=self.weights,
            capacity=self.capacity,
            mutation_function=self.mutation_function,
            crossover_function=self.crossover_function,
            repr=new_repr
        )
    
    def crossover(self, other_solution):
        # Apply crossover function to self representation and other solution representation
        offspring1_repr, offspring2_repr = self.crossover_function(self.repr, other_solution.repr)

        # Create and return offspring with new representations
        return (
            WSOGASolution(
                values=self.values,
                weights=self.weights,
                capacity=self.capacity,
                mutation_function=self.mutation_function,
                crossover_function=self.crossover_function,
                repr=offspring1_repr
            ),
            WSOGASolution(
                values=self.values,
                weights=self.weights,
                capacity=self.capacity,
                mutation_function=self.mutation_function,
                crossover_function=self.crossover_function,
                repr=offspring2_repr
            )
        )