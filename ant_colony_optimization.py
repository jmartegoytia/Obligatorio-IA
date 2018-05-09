import random
import numpy as np
import math
def surroundings(center, radius, domains):
    """ The surroundings of a `center` is a list of new centers, all equal to the center except for
    one value that has been increased or decreased by `radius`.
    """
    return [center[0:i] + (center[i] + d,) + center[i + 1:]
               for i in range(len(center)) for d in (-radius, +radius)
               if center[i] + d >= domains[i][0] and center[i] + d <= domains[i][1]
]
class Ant():
    def __init__(self, position, problem, local_pheromone_function, pheromones, max_iterations=100):
        self.position = position
        self.problem = problem
        self.local_pheromone_function = local_pheromone_function
        self.pheromones = pheromones
        self.iterations = max_iterations
    def solve(self):
        next = (self.position, self.problem.evaluate(self.position))
        path = [next[0]]
        evaluations = self.problem.evaluated(surroundings(next[0], 1, self.problem.domains))
        best_neighbour = evaluations[0]
        iterations = 0
        while self.problem.compareEvaluations(best_neighbour[1], next[1]) <= 0 and not iterations > self.iterations:
            probabilities = {}
            for eval in evaluations:
                node = eval[0]
                evaluation = eval[1]
                pheromone = self.pheromones.get(node, 0)
                probabilities[node] = self.local_pheromone_function(pheromone, evaluation)
            total = float(sum(probabilities.values()))
            for node, probability in probabilities.items():
                probabilities[node] = probability / total
            items = list(probabilities.items())
            keys = list(map(lambda x : x[0], items))
            indexes = range(0, len(keys))
            values = list(map(lambda x: x[1], items))
            elements = np.array(indexes)
            p = np.array(values)
            d = np.random.choice(elements, 1, list(p))
            elem = keys[int(d[0])]
            path.append(elem)
            next = (elem, self.problem.evaluate(elem))
            evaluations = self.problem.evaluated(surroundings(next[0], 1, self.problem.domains))
            best_neighbour = evaluations[0]
            iterations += 1
        return path, next[1]

local_pheromone = lambda pheromone, evaluation: pheromone if pheromone else 1 / evaluation if evaluation else 1
global_pheromone_update = lambda value: 100000 / (value if value else 1)
def ant_colony_optimization(problem, iterations=10, ants_amount=10,
    global_pheromone_update=global_pheromone_update,
    local_pheromone_function=local_pheromone, pheromene_evaporation = 0.20,
    ant_iterations=100):
    j = 0
    pheromones = {}
    best_solution = None
    best_combination = None
    ants = []
    solutions = []
    while j < iterations:
        i = 0
        while i < ants_amount:
            position = problem.randomElement()
            ant = Ant(position, problem, local_pheromone_function, pheromones)
            ants.append(ant)
            i += 1
        for ant in ants:
            path, value = ant.solve()
            if (not best_solution) and (not best_combination):
                best_solution = value
                best_combination = path[len(path) - 1]
            elif problem.compareEvaluations(value, best_solution) < 0:
                best_solution = value
                best_combination = path[len(path) - 1]
            solutions.append([path, value])
        for node, pheromone in pheromones.items():
            pheromones[node] = pheromone * (1 - pheromene_evaporation)
        for solution in solutions:
            value = solution[1]
            for node in solution[0]:
                pheromones[node] = pheromones.get(node, 0) + global_pheromone_update(value)         
        j += 1
    return best_combination, best_solution           

        

            
            
