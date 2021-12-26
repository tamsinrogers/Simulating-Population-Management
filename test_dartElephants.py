# Stephanie Taylor
# Fall 2015 CS151 (Science)
# Project 5
# This module tests the dartElephants function in elephant.py
#
# NOTE: The following statistics were calculated in Python2, which seems to have had a slightly different
# random number generator. Your results will be close to the following, but will likely not match exactly.
#
# Call it like this:
#    python3 test_dartElephants.py
# Because I have seeded the random number generator, the output will be identical every time you run it. You should see:
# Test 1
# Out of 5089 adult female elephants, 2574 are darted, leading to a percentage of 0.506. It should be 0.500
# 
# Test 2
# Out of 5010 adult female elephants, 0 are darted, leading to a percentage of 0.000. It should be 0.000
# 
# Test 3
# Out of 4944 adult female elephants, 4944 are darted, leading to a percentage of 1.000. It should be 1.000
# If you would like it to change from run to run, then comment out the call to random.seed.

import elephant
import random

def testDarting( darted ):
    calv = 3.1
    juvage = 12
    maxage = 60
    calfprob = 0.85
    adultprob = 0.996
    seniorprob = 0.2
    capacity = 10000

    parameters = [calv, darted, juvage, maxage, calfprob, adultprob, seniorprob, capacity]

    # Create a new, undarted population
    population = []
    for i in range( capacity ):
        # Create a new adult elephant. 
        population.append( [random.choice(['m','f']), random.randint(juvage+1, maxage ), 0, 0] )
    population = elephant.dartElephants( parameters, population )

    numF = 0
    numDarted = 0
    for e in population:
        if e[0] == 'f':
            numF += 1
            if e[3] == 22:
                numDarted += 1
    print("Out of %d adult female elephants, %d are darted, leading to a percentage of %0.3f. It should be %0.3f" % (numF, numDarted, float(numDarted)/numF,darted))

def main():
    random.seed( 0 )

    # Test the function with a darting percentage of 50%
    print("Test 1")
    testDarting( 0.5 )

    # Test the function with a darting percentage of 0%
    print( "\nTest 2")
    testDarting( 0.0 )

    # Test the function with a darting percentage of 100%
    print( "\nTest 3")
    testDarting( 1.0 )
    

if __name__ == '__main__':
    main()