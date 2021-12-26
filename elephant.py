# Tamsin Rogers
# October 8, 2019
# CS 152 
# Project 5: Simulating Elephant Population Management
""" This program is the first of a three-part project where we'll be simulating the elephant 
population in Kruger National Part, South Africa. The carrying capacity of the park is 
approximately 7000 elephants (1 elephant per square mile of park). Previous efforts to manage 
the population involved culling approximately 400 animals per year. After the development of 
an elephant contraceptive, the current effort to manage the population involves using a 
contraceptive dart on adult female elephants to limit the birth rate.  The conceptual goal 
of this week's simulation is twofold. First, identify differences in the population distributions 
between the two methods of limiting the population. Second, identify the percentage of adult 
females who have to be darted with the contraceptive each year in order to maintain the population without culling."""
# Run the program from the Terminal by entering "python3 elephant.py + [a number for the darting probability]""

import random       #import the random package
import sys			#import the sys package

#parameters IDs
IDXcalv = 0         #calving interval
IDXdarted = 1       #percent darted
IDXjuvage = 2       #juvenile age
IDXmaxage = 3       #maximum age
IDXcalfprob = 4     #probability of calf survival
IDXadultprob = 5    #probability of adult survival
IDXseniorprob = 6   #probability of senior survival
IDXcapacity = 7     #carrying capacity
IDXyears = 7        #number of years
#elephant IDs
IDXGender = 0                       #gender
IDXAge = 1                          #age
IDXMonthsPregnant = 2               #months pregnant
IDXMonthsContraceptiveRemaining = 3 #months of contraceptive remaining

"""This function uses the calving interval (calv), juvenile age (juvage), and maximum age
(maxage) parameters and the random package to assign a random gender and age.  The function
will then create 15 elephants and then print out each elephant list."""
def newElephant (parameters, age):
    
    probability = (1.0/parameters[IDXcalv])
    elephant = [0, 0, 0, 0]
    
    g = random.randint(0,1)
    if g == 0: 
        elephant[IDXGender] = "f"
    if g == 1: 
        elephant[IDXGender] = "m"
    elephant[IDXAge] = age
    if elephant[IDXGender] == "f":
        if age>parameters[IDXjuvage] and age <=parameters[IDXmaxage]:
            if random.random() < probability:
                elephant[IDXMonthsPregnant] = random.randint(1,22)
    return elephant

"""This function uses the newElephant function to create elephants by taking in the parameter
list and returning a list of new elephants, which are also lists.  The number of elephants
to create is the carrying capacity parameter."""
def initPopulation(parameters):
    population = []
    for i in range(parameters[IDXcapacity]):
        population.append(newElephant(parameters, (random.randint(1,parameters[IDXmaxage]))))
        
    return(population)
    print(population)

"""This function takes in a population list and returns a population list after incrementing
each elephant's age by 1 year."""
def incrementAge(parameters, population):
    age = parameters[IDXAge]
    for i in population:
        age = age+1

"""This function goes through the elephant population list and determines whether each 
individual elephant survives to the next year.  The function takes the parameter list (parameters)
and population list (population) as arguments, and uses the parameters maxage, calfprob,
adultprob, and seniorprob to loop over the existing population list and add each elephant
to the new population list depending on its age and survival probability."""        
def calcSurvival(parameters, population):
# Because I have seeded the random number generator, the output will be identical every time you run it. You should see:
# Out of 10000 calves, 8444 survive, leading to a survival rate of 0.844. It should be 0.850.
# Out of 10000 juveniles and adults, 9963 survive, leading to a survival rate of 0.996. It should be 0.996.
# Out of 10000 seniors, 2240 survive, leading to a survival rate of 0.224. It should be 0.200.
# If you would like it to change from run to run, then comment out the call to random.seed.
    new_population = []
    for elephant in population:
        #calves
        if (elephant[IDXAge] <= parameters[IDXjuvage]):
            if random.random() < parameters[IDXcalfprob]:
                new_population.append(elephant)
        #juveniles and adults
        elif (elephant[IDXAge]<=parameters[IDXmaxage]):
            if random.random() < parameters[IDXadultprob]:
                new_population.append(elephant)
        #seniors
        elif (elephant[IDXAge] >= parameters[IDXmaxage]):
            if random.random() < parameters[IDXseniorprob]:
                new_population.append(elephant)
    return new_population

"""This function goes through the adult females and randomly selects individuals for darting 
based on the dart probability parameter (darted).  This function takes in the parameter list 
(parameters) and population list (population) as arguments, returns the population list, and
makes use of the probability of darting (darted), the juvenile age (juvage), and the maximum
age (maxage)."""    
def dartElephants(parameters, population):
    for elephant in population:
        if elephant[IDXGender] == "f":
            if elephant[IDXAge] >= parameters[IDXjuvage]:
                if elephant[IDXAge] <= parameters[IDXmaxage]:
                    if random.random() < parameters[IDXdarted]:
                        elephant[IDXMonthsPregnant] = 0
                        elephant[IDXMonthsContraceptiveRemaining] = 22
    return population

"""This function checks if there are more elephants than the carrying capacity.  If there 
are too many elephants, it removes enough randomly chosen elephants from the population so 
there are as many elephants as the carrying capacity.  The function takes in the parameter 
list (parameters) and population list (population) as arguments.  It then returns a tuple 
containing first the new population list (population), and second the number of elephants
culled (culled).  The function makes use of the carrying capacity of the population (capacity)."""
def cullElephants (parameters, population):
    total = 0
    for i in range(0, len(population)):
        total = total+i
    capacity = parameters[IDXcapacity]
    culled = (total-capacity)
    if total > capacity:
        newpopulation = random.shuffle(population)
    return (newpopulation, culled)

"""This function determines whether the population should be darted or culled, and then calls
the appropriate function (dartElephants or cullElephants).  It then returns the new population
list (newpop) and the number culled (culled) as a tuple."""
def controlPopulation(parameters, population):
    # if the parameter value for "percent darted" is zero:
    if parameters[IDXdarted] == 0:
        # call cullElephants, storing the return values in a two variables 
        (newpopulation, culled) = cullElephants(parameters, population)
        #   ( e.g. (newpop, numCulled) = cullElephants( parameters, population ))
    # else
    else:
        # call dartElephants and store the result in a variable named newpop
        newpopulation = dartElephants(parameters, population)
        # set a variable named numCulled to zero
        culled = 0
    #  return (newpop, numCulled)
    return(newpopulation, culled)

"""This function moves the simulation forward by one month.  It modifies only the adult
females in the population, and add a new calf to the population if one should be born.  The
function takes in the parameter list (parameters) and the population list (population), and
returns the population list (population).  The function uses the calving interval (calv), 
juvenile age (juvage), and maximum age (maxage) parameters."""
def simulateMonth(parameters, population):
    for elephant in population:
        # assign to gender the IDXGender item in e
        gender = elephant[IDXGender]
        # assign to age the IDXAge item in e
        age = elephant[IDXAge]
        # assign to monthsPregnant the IDXMonthsPregnant item in e
        monthsPregnant = elephant[IDXMonthsPregnant]
        # assign to monthsContraceptive the IDXMonthsContraceptiveRemaining item in e
        monthsContraceptive = elephant[IDXMonthsContraceptiveRemaining]
        # if gender is female and the elephant is an adult
        if gender == "f" and (age > parameters[IDXjuvage]) and (age < parameters[IDXmaxage]):
            # if monthsContraceptive is greater than zero
            if monthsContraceptive > 0:
                # decrement the months of contraceptive left (IDXMonthsContraceptiveRemaining element of e) by one
                elephant[IDXMonthsContraceptiveRemaining] = (elephant[IDXMonthsContraceptiveRemaining]-1)
            # else if monthsPregnant is greater than zero
            elif monthsPregnant > 0:
                # if monthsPregnant is greater than or equal to 22
                if monthsPregnant >= 22:
                    # create a new elephant of age 1 and append it to the population list
                    age = 1
                    population.append(elephant)
                    # reset the months pregnant (the IDXMonthsPregnant element of e) to zero
                    elephant[IDXMonthsPregnant] = 0
                # else
                else:
                    # increment the months pregnant (IDXMonthsPregnant element of e) by 1
                    elephant[IDXMonthsPregnant] = (elephant[IDXMonthsPregnant]+1)
            # else
            else:
                # if the elephant becomes pregnant
                if parameters[IDXcalv] > (1.0 / (3.1*12 - 22)):
                    # set months pregnant (IDXMonthsPregnant element of e) to 1
                    elephant[IDXMonthsPregnant] = 1    

"""This function takes in the parameter list (parameters) and population list (population).  
It then calls calcSurvival, incrementAge, and loops twelve times calling simulateMonth.  It
then returns the population list (population)."""
def simulateYear(parameters, population):
    calcSurvival(parameters, population)
    incrementAge(parameters, population)
    for i in range(12):
        simulateMonth(parameters, population)

"""This function calculates how many calves, juveniles, adult males, adult females, and 
seniors are in the population.  It then returns a list with those values in it, along with 
the total number in the population (total), and the number culled from the population that 
year (culled).  It takes as input the parameters (parameters), the population list (population), 
and the number of animals that were just culled from the population (culled).  For each elephant,
the appropriate variable (calves, juveniles, adultmales, adultfemales, seniors) is incremented
depending on the applicable if statements.  When the loop is complete, a list containing the 
total population size (total), the number of calves (calves), the number of juveniles (juveniles),
the number of adult males (adultmales), the number of adult females (adultfemales), the number 
of seniors (seniors), and the number of animals culled (culled) is returned.""e"        
def calcResults(parameters, population, culled)."""
def calcResults(parameters, population, culled):
    calves = 0
    juveniles = 0
    adultmales = 0
    adultfemales = 0
    seniors = 0
    
    test=[]
    
    for elephant in population:
        #calves
        if (elephant[IDXAge] <= parameters[IDXjuvage]):
            calves = calves + 1
        #juveniles
        if (elephant[IDXAge]==parameters[IDXjuvage]):
            juveniles = juveniles + 1
        #adults
        if (elephant[IDXAge]>parameters[IDXjuvage]) and (elephant[IDXAge]<parameters[IDXmaxage]):
            if elephant[IDXGender] == "m":
                adultfemales = adultmales+1
            if elephant[IDXGender] == "f":
                adultfemales = adultfemales+1
        #seniors
        if (elephant[IDXAge] >= parameters[IDXmaxage]):
            seniors = seniors + 1
        
        total = calves+juveniles+adultfemales+adultmales+seniors
        
        test.append(total)
        test.append(calves)
        test.append(juveniles)
        test.append(adultmales)
        test.append(adultfemales)
        test.append(seniors)
        test.append(culled)
    return(test)

"""This function takes the parameter list (parameters) and the number of year (years) to
run the simulation.  Then it creates the new population, applies any control procedures,
loops of the number of years, simulating the year, and keeps track of the demographics for
each year by appending them to a results list."""
def runSimulation(parameters, years):
    popsize = parameters[IDXcapacity]

    # init the population
    population = initPopulation( parameters )
    [population,culled] = controlPopulation( parameters, population )

    # run the simulation for N years, storing the results
    results = []
    for i in range(parameters[IDXyears]):
        population = simulateYear( parameters, population )
        [population,culled] = controlPopulation( parameters, population )
        results.append( calcResults( parameters, population, culled ) )
        if results[i][0] > 2 * popsize or results[i][0] == 0 : # cancel early, out of control
            print( 'Terminating early' )
            break
        
    return results 

def test():
    # assign each parameter from the table above to a variable with an informative name
    calv = 3.1
    darted = 0.0
    juvage = 12
    maxage = 60
    calfprob = 0.850
    adultprob = 0.996
    seniorprob = 0.200
    capacity = 10000
    years = 200
    # make the parameter list out of the variables
    parameters = [calv, darted, juvage, maxage, calfprob, adultprob, seniorprob, capacity, years]
    print(parameters[IDXmaxage])
    # print the parameter list
    print(parameters)

    population = []
    for i in range(15):
        population.append( newElephant( parameters, random.randint(1, parameters[IDXmaxage]) ) )

    for e in population:
        print(e)
    
    initPopulation(parameters)
    population = incrementAge(parameters, population)
    print(population)
    
"""This function takes argv (the list of strings from the command line) as an argument.  
It includes a usage statement to ensure that the user has entered one element in the command
line.  The main function runs through the parameters and the parameter list in the runSimulation
function and stores the return value in a results list, while modifying the "darted" parameter
based on the command line argument.  It then prints out the last item in the results list
and calculates the average results of each variables (total, calves, juveniles, adultmales,
adultfemales, and seniors) and prints these values."""
def main(argv):
    if (len(sys.argv)<1):
        print("enter the probability of darting")
    darted = int(sys.argv[1])
    # assign each parameter from the table above to a variable with an informative name
    calv = 3.1
    darted = 0.0
    juvage = 12
    maxage = 60
    calfprob = 0.850
    adultprob = 0.996
    seniorprob = 0.200
    capacity = 10000
    years = 200
    # make the parameter list out of the variables
    parameters = [calv, darted, juvage, maxage, calfprob, adultprob, seniorprob, capacity, years]
    results = []    
    results = runSimulation(parameters, years)
    print(results[-1])
    
    for i in range(years):
        for x in population:
            total = x+1
        print("Total population value in year ", i, ": total")
    
    avgtotal = (total/years)
    avgcalves = (calves/years)
    avgjuveniles = (juveniles/years)
    avgadultmales = (adultmales/years)
    avgadultfemales = (adultfemales/years)
    avgseniors = (seniors/years)
    
    print("Average total population value: ", avgtotal)
    print("Average number of calves: ", avgcalves)
    print("Average number of juveniles: ", avgjuveniles)
    print("Average number of adult males: ", avgadultmales)
    print("Average number of adult females: ", avgadultfemales)
    print("Average number of seniors: ", avgseniors)
    
if __name__ == "__main__":
    main(sys.argv)