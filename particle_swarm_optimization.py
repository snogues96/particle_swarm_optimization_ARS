import numpy as np
import math
from particle import Particle


function = 0
population = 20
iterations = 50

a = 0.9
b = 2.0
c = 2.0

a_range = np.linspace(a, 0.4, 50)

bounds = [-5.12,5.12]
neighbourhood = "global" # social, geographical



def pso():
    best_cost = np.inf
    pos_best_cost = []
    x0 = np.random.rand(population, 2)
    swarm = [Particle(x0[i,:]) for i in range(population)]
    position_matrix = [[0 for x in range(population)] for y in range(iterations)]

    i = 0
    while i < iterations:
        for j in range(population):
            swarm[j].evaluate("rosenbrock")

            if swarm[j].cost<best_cost:
                pos_best_cost = swarm[j].position
                best_cost = swarm[j].cost

        for j in range(population):
            swarm[j].update_velocity(a, b, c, pos_best_cost)
            swarm[j].update_position()
            position_matrix[i][j] = swarm[j].position
        i+=1

pso()

if __name__ == "__main__":
    print("AAAAAAAA")