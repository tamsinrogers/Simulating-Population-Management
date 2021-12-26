# Stephanie Taylor
# Fall 2015 CS151 (Science)
# Project 5
# This module tests the simulateMonth function in elephant.py
# Call it like this:
#    python3 test_simulateMonth.py
#
#
#                                                                                                                              
#                                                                                                                                     
# NOTE: The following statistics were calculated in Python2, which seems to have had a slightly different                             
# random number generator. Your results will be close to the following, but will likely not match exactly.                            
#         
#
#
# Because I have seeded the random number generator, the output will be identical every # time you run it. 
# You should see:
# In month 1, out of 7500 adult female elephants, 212 gave birth, leading to a birth rate of 0.0283. It should be 0.0147
# In month 1, out of 2500 adult female elephants who could become pregnant, 151 became pregnant this month, leading to a conception rate of 0.060. It should be 0.066
# In month 2, out of 1332 adult female elephants who could become pregnant, 76 became pregnant this month, leading to a conception rate of 0.057. It should be 0.066
# In an earlier version of my elephant.py, I was using the wrong code to determine births (I had "> 22" instead of ">= 22", as the instructions indicate). The output from that run was this:
# In month 1, out of 7500 adult female elephants, 112 gave birth, leading to a birth rate of 0.0149. It should be 0.0147
# In month 1, out of 2500 adult female elephants who could become pregnant, 151 became pregnant this month, leading to a conception rate of 0.060. It should be 0.066
# In month 2, out of 1272 adult female elephants who could become pregnant, 82 became pregnant this month, leading to a conception rate of 0.064. It should be 0.066
# If you would like it to change from run to run, then comment out the call to random.seed.

import elephant
import random

def countFemalesEligibleForPregnancy( parameters, population ):
    numF = 0
    for e in population:
        gender = e[0]
        age = e[1]
        monthsPregnant = e[2]
        monthsContraceptive = e[3]
        if gender == 'f' and age > parameters[2] and age <= parameters[3] and monthsPregnant == 0 and monthsContraceptive == 0:
            numF += 1
    return numF

def countFemalesNewlyPregnant( parameters, population ):
    numF = 0
    for e in population:
        gender = e[0]
        age = e[1]
        monthsPregnant = e[2]
        monthsContraceptive = e[3]
        if gender == 'f' and age > parameters[2] and age <= parameters[3] and monthsPregnant == 1:
            numF += 1
    return numF

def countAdultFemales( parameters, population ):
    numF = 0
    for e in population:
        gender = e[0]
        age = e[1]
        monthsPregnant = e[2]
        monthsContraceptive = e[3]
        if gender == 'f' and age > parameters[2] and age <= parameters[3]:
            numF += 1
    return numF
    
def main():
    random.seed( 0 )
    calv = 3.1
    darted = 0.5
    juvage = 12
    maxage = 60
    calfprob = 0.85
    adultprob = 0.996
    seniorprob = 0.2
    capacity = 10000
    parameters = [calv, darted, juvage, maxage, calfprob, adultprob, seniorprob, capacity]

    population = []
    for i in range( capacity//4 ):
        # Create a new juvenile or adult male
        population.append( ['m', random.randint(juvage+1, maxage ) , 0, 0] )
    for i in range( capacity//4 ):
        # Create a new juvenile or adult female elephant that has been darted
        population.append( ['f', random.randint(juvage+1, maxage ), 0, random.randint(1,22)] )
    for i in range( capacity//4 ):
        # Create a new juvenile or adult female elephant that is eligible for pregnancy
        population.append( ['f', random.randint(juvage+1, maxage ),  0, 0] )
    for i in range( capacity-3*(capacity//4) ):
        # Create a new juvenile or adult female elephant that is pregnant
        population.append( ['f', random.randint(juvage+1, maxage ),  random.randint(1,23), 0] )
    
    # Record the number of elephants that could become pregnant during this
    # second month of simulation. Then we an assess the conception rate.
    numBeforeMonth = len(population)
    numF = countAdultFemales( parameters, population )
    numBreedable = countFemalesEligibleForPregnancy( parameters, population )
    population = elephant.simulateMonth( parameters, population )    
    numBabies = len(population) - numBeforeMonth
    numNewlyPregnant = countFemalesNewlyPregnant( parameters, population )
    print("In month 1, out of %d adult female elephants, %d gave birth, leading to a birth rate of %0.4f. It should be %0.4f" % (numF, numBabies, float(numBabies)/numF,(1/calving_interval)/22))
    print("In month 1, out of %d adult female elephants who could become pregnant, %d became pregnant this month, leading to a conception rate of %0.3f. It should be %0.3f" % (numBreedable, numNewlyPregnant, float(numNewlyPregnant)/numBreedable,1.0/(12*calving_interval-22.0)))
    
    # Take into account darting. The above test is on a populations with no contraceptives. but we also want to test the contraception code. 
    population = elephant.dartElephants( parameters, population )
    
    numF = countAdultFemales( parameters, population )
    numBreedable = countFemalesEligibleForPregnancy( parameters, population )
    pop = elephant.simulateMonth( parameters, population )    
    numNewlyPregnant = countFemalesNewlyPregnant( parameters, population )
    print("In month 2, out of %d adult female elephants who could become pregnant, %d became pregnant this month, leading to a conception rate of %0.3f. It should be %0.3f" % (numBreedable, numNewlyPregnant, float(numNewlyPregnant)/numBreedable,1.0/(12*calving_interval-22.0)))
    

if __name__ == '__main__':
    main()