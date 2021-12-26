# Stephanie Taylor
# Fall 2015 CS151 (Science)
# Project 5
# This module tests the calcSurvival function in elephant.py
# Call it like this:
#    python test_calcSurvival.py
# Because I have seeded the random number generator, the output will be identical every time you run it. You should see:
# Out of 10000 calves, 8444 survive, leading to a survival rate of 0.844. It should be 0.850.
# Out of 10000 juveniles and adults, 9963 survive, leading to a survival rate of 0.996. It should be 0.996.
# Out of 10000 seniors, 2240 survive, leading to a survival rate of 0.224. It should be 0.200.
# If you would like it to change from run to run, then comment out the call to random.seed.

import elephant
import random

def main():
    random.seed( 0 )
    calv = 3.1
    darted = 0.0
    juvage = 12
    maxage = 60
    calfprob = 0.85
    adultprob = 0.996
    seniorprob = 0.2
    capacity = 10000
    parameters = [calv, darted, juvage, maxage, calfprob, adultprob, seniorprob, capacity]

    min_ages = [1,2,maxage]
    max_ages = [1,maxage,100]
    age_names = ['calves','juveniles and adults','seniors']
    survival_rates = [calfprob, adultprob, seniorprob]

    for population_idx in range(len(min_ages)):
        population = []
        for i in range( capacity ):
            # Create a new elephant in the given age range. It may be male or female
            population.append( [random.choice(['m','f']), random.randint(min_ages[population_idx], max_ages[population_idx] ),0,0 ])
        new_population = elephant.calcSurvival( parameters, population )
        print("Out of %d %s, %d survive, leading to a survival rate of %0.3f. It should be %0.3f." % (len(population),age_names[population_idx],len(new_population),float(len(new_population))/len(population),survival_rates[population_idx]))

if __name__ == '__main__':
    main()