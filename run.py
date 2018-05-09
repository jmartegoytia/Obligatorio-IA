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