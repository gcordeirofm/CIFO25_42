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
   - /data: The problem data (guest relationship chart)
        - seating_data.csv: source data file
        - relationship_matrix.py: converted .csv file to a numpy array for easy import

- /project: Developed work
   - /development: Experimentation and development notebooks
        - workshop.ipynb: notebook experimenting and developing required functions and classes for the genetic algorithm
        - selection_methods: notebook with development and testing of custom selection methods (Tournament Selection, Ranking Selection)
        - crossover_mutation: notebook with development and testing of custom crossover and mutation operators. Includes a combination of modifications of operators developed in class and entirely new methods. (Crossover: Cycle Crossover, Partially Matched Crossover, Position Based Crossover. Mutation: Block Swap Mutation, Shuffle Subsequence Mutation, N-Swap Mutation, Displacement Mutation).
   - /fitness_results: Resulting csv files containing fitnesses over generations and runs from phase 1 and 2
        - /phase1_concatenated
        - /phase1_run1
        - /phase1_run2
        - /phase2_run
   - **phase_1**: main notebook with pipeline for phase one of the ga-run (combinations of mutations, crossovers and selections)
   - **phase_2**: main notebook with pipeline for phase two of the ga-run (hyperparameter tuning)
   - concat_fitness_results: notebook that concatenates results from multiple phase 1 runs
