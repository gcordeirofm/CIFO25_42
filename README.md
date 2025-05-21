# CIFO Project - Group 42
Computational Intelligence for Optimization 24/25 - NOVA IMS

Group 42:
- Guilherme Cordeiro (20240527)
- Louis Berthele (20240552)
- Maria Radix (20240687)

## Repository Structure
This repository is organized as follows:

- /library: The source code for the optimization library built throughout the semester, as well as custom operators developed as per project requirements. This includes:
   - /algorithms: Functions and classes that implement a variety of optimization algorithms
   - /custom: Collection of custom methods, operators and solution classes. Includes:
        - custom_crossover (Cycle Crossover, Partially Matched Crossover, Position Based Crossover)
        - custom_mutation (Block Swap Mutation, Shuffle Subsequence Mutation, N-Swap Mutation, Displacement Mutation)
        - custom_selection (Tournament Selection, Ranking Selection)
        - custom_solution (WSOSolution, WSOGASolution)
   - /problems: Classes that define and implement various optimization problems and provide a way to solve them using the algorithms developed
   - /data: The problem data (guest relationship chart)
        - seating_data.csv: source data file
        - relationship_matrix.py: converting the .csv to a numpy array for easy import

- /project: Developed work
   - workshop.ipynb: notebook experimenting and developing required functions and classes for the genetic algorithm
   - selection_methods: notebook with development and testing of custom selection methods (Tournament Selection, Ranking Selection)
   - crossover_mutation: notebook with development and testing of custom crossover and mutation operators. Includes a combination of modifications of operators developed in class and entirely new methods. (Crossover: Cycle Crossover, Partially Matched Crossover, Position Based Crossover. Mutation: Block Swap Mutation, Shuffle Subsequence Mutation, N-Swap Mutation, Displacement Mutation).
   - phase_1: notebook with pipeline for phase one of the ga-run (combinations of mutations, crossovers and selections)
   - phase_2: notebook with pipeline for phase two of the ga-run (hyperparameter tuning)
   - concat_fitness_results: notebook that concatenates results from multiple phase 1 runs
