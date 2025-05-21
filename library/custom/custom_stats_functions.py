import sys
import os
sys.path.append('..')

from scipy.stats import ttest_ind
import pandas as pd


def load_fitness_results(folder, longform = False):

    '''
    Loads fitness values of different configurations tested from CSV files that hold results of the experiment.
    Takes as arguments:
        folder: location where fitness values are stored
        longform: boolean

    When longform = False, returns a dictionary of congifuration: fitness of last generation. Useful for
    running ANOVA difference in means statistical test.

    When longform = True, returns a longform dataframe. Useful for plotting with Seaborn and for ANOVA post-hoc
    pairwise t-tests.
    
    '''

    if longform:
        data = []
    else:
        fitness_by_config = {}

    # looping through all csv files in fitness_results folder
    for filename in os.listdir(folder):
        filepath = os.path.join(folder, filename)

        # loading each CSV
        df = pd.read_csv(filepath)

        # selecting only last generation fitness for comparison
        best_fitness = df.iloc[:, -1]

        # taking off .csv from configuration name
        config_label = filename.replace('.csv', '') 

        # for longform: appending configuration and fitness values to data
        if longform:
            for val in best_fitness:
                data.append({
                    'configuration': config_label,
                    'fitness_value': val
                })
            data_long = pd.DataFrame(data)

        # for not longform: adding configuration and fitness value pairs to dictionary
        else:
            fitness_by_config[config_label] = best_fitness.values

    if longform:
        return data_long
    else:
        return fitness_by_config
    

def pairwise_ttest(df_long, best_config):
    
    '''
    Runs pairwise Student T-tests on the configuration with best fitness results against all other configurations.
    Shows whether or not the mean fitness values of our best performing configuration are statistically significantly
    different from the mean fitness values of the other configurations.
    
    '''

    results = []

    # selecting fitness values from best configuration to compare in pairwise t-tests
    best_ind_fitness = df_long[df_long['configuration'] == best_config]['fitness_value']

    # iterating through all other (non-best) configurations
    for config in df_long['configuration'].unique():
        non_best_fitness = df_long[df_long['configuration'] == config]['fitness_value']

        # one sided (greater than) t-test to see if best individual is better than others (ignoring t-stat return value)
        _, p_value = ttest_ind(best_ind_fitness, non_best_fitness, alternative='greater')

        results.append({
            "compared_to": config,
            "mean_best": best_ind_fitness.mean(),
            "mean_other": non_best_fitness.mean(),
            "mean_diff": best_ind_fitness.mean() - non_best_fitness.mean(),
            "p_value": p_value,
            "significant": p_value < 0.05
        })

    return pd.DataFrame(results).sort_values(by="p_value")