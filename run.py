from tabu_search import tabu_search
from ant_colony_optimization import ant_colony_optimization
from grafo import Grafo
import random

def salesman_random(grafo):
    def random_element():
        nodes = list(range(0, len(grafo.matriz)))
        random.shuffle(nodes)
        return nodes
    return random_element

def salesman_surroundings(center, radius, domains):
    permutation = center
    surroundings = []
    for i in range(0, len(permutation)):
        if i + 1 < len(permutation):
            aux = list(permutation)
            aux[i], aux[i + 1] = aux[i + 1], aux[i]
            if aux not in surroundings:
                surroundings.append(tuple(aux))
        if i - 1 >= 0:
            aux = list(permutation)
            aux[i - 1], aux[i] = aux[i], aux[i - 1]
            if aux not in surroundings:
                surroundings.append(tuple(aux))
    return surroundings
None


grafo = Grafo([[1,None,None,1],[None,1,None,None],[1,None,1,1],[None,None,1,1]])

def test(problem=None):
    if not problem:
        import test_problems
        problem = test_problems.traveling_salesman_problem(grafo)
   # print(list(hill_climbing(problem, steps=1000)))
    print(ant_colony_optimization(problem,surroundings_function=salesman_surroundings, randomFunction=salesman_random(grafo)))

test()

def test2(problem=None):
    if not problem:
        import test_problems
        problem = test_problems.bohachevsky()
   # print(list(hill_climbing(problem, steps=1000)))
    print(ant_colony_optimization(problem))

test2()

def simulate(times=10000):
    #Problem bochachevsky
    import test_problems
    wins_tabu = 0
    wins_ant = 0
    draw = 0
    problem = test_problems.bohachevsky()
    for i in range(0, times):
        r_ant = ant_colony_optimization(problem)
        r_tabu = tabu_search(problem)
        if r_tabu[1] > r_ant[1]:
            wins_ant += 1
        elif r_tabu[1] == r_ant[1]:
            draw += 1
        else:
            wins_tabu += 1
    print("Bochachevsky Tabu %d Ant %d Draw %d" % (wins_tabu, wins_ant, draw))
    wins_tabu = 0
    wins_ant = 0
    draw = 0
    problem = test_problems.schwefel(2)
    for i in range(0, times):
        r_ant = ant_colony_optimization(problem)
        r_tabu = tabu_search(problem)
        if r_tabu[1] > r_ant[1]:
            wins_ant += 1
        elif r_tabu[1] == r_ant[1]:
            draw += 1
        else:
            wins_tabu += 1
    print("Scwefel Tabu %d Ant %d Draw %d" % (wins_tabu, wins_ant, draw))
    wins_tabu = 0
    wins_ant = 0
    draw = 0
    problem = test_problems.traveling_salesman_problem(grafo)
    for i in range(0, times):
        r_ant = ant_colony_optimization(problem, surroundings_function=salesman_surroundings, randomFunction=salesman_random(grafo))
        r_tabu = tabu_search(problem, surroundings_function=salesman_surroundings, randomFuction=salesman_random(grafo))
        if r_tabu[1] > r_ant[1]:
            wins_ant += 1
        elif r_tabu[1] == r_ant[1]:
            draw += 1
        else:
            wins_tabu += 1
    print("Traveling salesman Tabu %d Ant %d Draw %d" % (wins_tabu, wins_ant, draw))

simulate(10000)
