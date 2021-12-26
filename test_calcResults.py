# Stephanie Taylor
# Fall 2015 CS151 (Science)
# Project 5
# This module tests the calcResults function in elephant.py
# Call it like this:
#    python3 test_calcResults.py
#
#                                                                                                                              
#                                                                                                                                     
# NOTE: The following statistics were calculated in Python2, which seems to have had a slightly different                             
# random number generator. Your results will be close to the following, but will likely not match exactly.                            
#         
#
#
#
# Because I have seeded the random number generator, the output will be identical every time you run it. You should see:
# There are 300 total elephants and it reports 10 were culled
# There are 100 calves, 20 juveniles, 42 adult males, 39 adult females, and 99 seniors
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

    population = []
    for population_idx in range(len(min_ages)):
        for i in range( 100 ):
            # Create a new elephant in the given age range. It may be male or female
            population.append( [random.choice(['m','f']), random.randint(min_ages[population_idx], max_ages[population_idx] ),0,0 ])
            
    results = elephant.calcResults( parameters, population, 10 )
    
    # The order of elements in results should be: numTotal, numCalves, numJuveniles, numFemaleAdults, numMaleAdults, numSeniors, numCulled
    print( "There are %d total elephants and it reports %d were culled" % (results[0], results[6]))
    print( "There are %d calves, %d juveniles, %d adult females, %d adult males, and %d seniors" % (results[1], results[2], results[3], results[4], results[5]))

if __name__ == '__main__':
    main()