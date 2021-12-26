# Stephanie Taylor
# Fall 2015 CS151 (Science)
# Project 5
# This module tests the simulateMonth function in elephant.py
# Call it like this:
#    python3 test_simulateYear.py
#
#                                                                                                                              
#                                                                                                                                     
# NOTE: The following statistics were calculated in Python2, which seems to have had a slightly different                             
# random number generator. Your results will be close to the following, but will likely not match exactly.                            
#         
#
#
# Because I have seeded the random number generator, the output will be identical every time you run it. You should see:
# After 1 year of simulation, there are 107 elephants.
# After 2nd year of simulation, there are 118 elephants.
# Before I fixed my bug in simulateMonth, here was my output:
# After 1 year of simulation, there are 107 elephants.
# After 2nd year of simulation, there are 111 elephants.
# If you would like it to change from run to run, then comment out the call to random.seed.

import elephant
import random
    
def main():
    random.seed( 0 )
    calv = 3.1
    darted = 0.5
    juvage = 12
    maxage = 60
    calfprob = 0.85
    adultprob = 0.996
    seniorprob = 0.2
    capacity = 100
    parameters = [calv, darted, juvage, maxage, calfprob, adultprob, seniorprob, capacity]

    population = []
    for i in range( capacity ):
        population.append( elephant.newElephant( parameters, random.randint(juvage+1, maxage ) ) )
        
    population = elephant.simulateYear( parameters, population )
    print("After 1 year of simulation, there are %d elephants." % (len(population)))

    population = elephant.simulateYear( parameters, population )
    print("After 2nd year of simulation, there are %d elephants." % (len(population)))

    
if __name__ == '__main__':
    main()