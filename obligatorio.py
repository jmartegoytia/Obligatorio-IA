def ant_colony_optimization(problem, iterations=100, ants=100):
    i = 0
    pheromones = []
    while(i < iterations):
        bestSolution = None
        bestCombination = None
        j = 0
        ants = []
        while(j < ants):
            position = problem.randomElement()
            ant = Ant(problem, pheromones, position)
            ants.append(ant)

        for a in ants:
            path, value = a.findSolution()
            if (value < bestSolution):                 # se desea minimizar, de lo contrario utilizar '>'
                bestSolution = value
                bestCombination = path[-1]


class Ant:
    def __init__(self, problem, pheromones, position):
        self.problem = problem
        self.pheromones = pheromones
        self.position = position

    def findSolution(self):
        next = self.position
        i = 0
        while(i < 1000):                      # puse 1000 como ejemplo
            probabilities = []
            neighbors = surroundings(next, 10, self.problem.domains)
            for n in neighbors:

    def choice(self, pheromone, value):
        




def surroundings(center, radius, domains):
    """ The surroundings of a `center` is a list of new centers, all equal to the center except for
    one value that has been increased or decreased by `radius`.
    """
    return [center[0:i] + (center[i] + d,) + center[i + 1:]
               for i in range(len(center)) for d in (-radius, +radius) 
               if center[i] - radius >= domains[i][0] and center[i] + radius <= domains[i][1]
           ]