import math
from  chromosome import chromosome
import numpy as np
from cost_functions import minone as  cost_function
from crossovers import singlepointcrossover
from mutations import mutation
import matplotlib.pyplot as plt

# variables defenation
variable_num = 50

iteration_max=200

population_num=20

cross_over_percentage=0.8

cross_over_num= 2 *  math.floor(population_num /2)

mutaion_percentage=0.3

mutation_num=math.floor(mutaion_percentage* population_num)

#population => create , initial , evaluate

population= [chromosome(np.random.randint(low=0,high=2,size=variable_num),cost_function) for i in range(population_num)]

population=sorted(population, key=lambda x: x.cost)

best_solution = population[0]
best_cost = np.zeros(iteration_max)

for it_index in range(iteration_max):

    #crossover
    rows , cols =(int(cross_over_num/2) , 2)
    #temp

    popc= [[chromosome(np.random.randint(2,size=variable_num),cost_function)]*cols] * rows

    for k in range(int(cross_over_num/2)):
        i1=np.random.randint(population_num)
        p1=population[i1]
        i2 = np.random.randint(population_num)
        p2 = population[i2]
        popc[k][0].posotion , popc[k][1].posotion  = singlepointcrossover(p1.posotion,p2.posotion)
        popc[k][0].evaluate()
        popc[k][1].evaluate()


    #mutation
    popm=[chromosome(np.random.randint(2,size=variable_num),cost_function) for i in range(mutation_num)]
    for k in range(mutation_num):
        i= np.random.randint(mutation_num)
        pm=popm[i]
        popm[k].posotion = mutation(pm.posotion)
        popm[k].evaluate()


    pop = list(population) + list(np.asarray(popc).flatten(order='C')) + list(popm)
    pop=sorted(pop, key=lambda x: x.cost)
    population = pop[:population_num]

    best_solution = population[0]
    best_cost[it_index]=best_solution.cost

    print('iteration ' , it_index , ' best cost : ' ,best_cost[it_index])

plt.plot([i for i in range(len(best_cost))] ,best_cost)
plt.show()











