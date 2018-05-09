from tabu_search import tabu_search
from ant_colony_optimization import ant_colony_optimization
from grafo import Grafo
import random

def generateGraph(N):
    matriz = []
    elements = list(range(0, N)) + [None]
    for i in range(0, N):
        lista = []
        for j in range(0, N):            
            lista.append(random.choice(elements))
        matriz.append(lista)
    return Grafo(matriz)

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

def simulate(times=10000):
    #Problem bochachevsky
    import test_problems
    wins_tabu = 0
    wins_ant = 0
    draw = 0
    problem = test_problems.bohachevsky()

    eval_tabu = 0
    eval_ant = 0

    results_tabu = 0
    results_ant = 0

    for i in range(0, times):
        r_ant = ant_colony_optimization(problem)
        results_ant += r_ant[1]
        eval_ant += problem.cantEvaluations

        r_tabu = tabu_search(problem)
        results_tabu += r_tabu[1]
        eval_tabu += problem.cantEvaluations

        if r_tabu[1] > r_ant[1]:
            wins_ant += 1
        elif r_tabu[1] == r_ant[1]:
            draw += 1
        else:
            wins_tabu += 1

    print("Bochachevsky Tabu %d Ant %d Draw %d" % (wins_tabu, wins_ant, draw))
    print("Promedio cantidad evaluaciones Tabu: ", eval_tabu / times)
    print("Promedio cantidad evaluaciones Ant: ", eval_ant / times)
    print("Promedio resultados Tabu: ", results_tabu / times)
    print("Promedio resultados Ant: ", results_ant / times)    

    wins_tabu = 0
    wins_ant = 0
    draw = 0

    eval_tabu = 0
    eval_ant = 0

    results_ant = 0
    results_tabu = 0

    problem = test_problems.schwefel(2)
    for i in range(0, times):
        r_ant = ant_colony_optimization(problem)
        eval_ant += problem.cantEvaluations
        results_ant += r_ant[1]

        r_tabu = tabu_search(problem)
        eval_tabu += problem.cantEvaluations
        results_tabu += r_tabu[1]

        if r_tabu[1] > r_ant[1]:
            wins_ant += 1
        elif r_tabu[1] == r_ant[1]:
            draw += 1
        else:
            wins_tabu += 1
    print("Scwefel Tabu %d Ant %d Draw %d" % (wins_tabu, wins_ant, draw))
    print("Promedio cantidad evaluaciones Tabu: ", eval_tabu / times)
    print("Promedio cantidad evaluaciones Ant: ", eval_ant / times)
    print("Promedio resultados Tabu: ", results_tabu / times)
    print("Promedio resultados Ant: ", results_ant / times)  

    wins_tabu = 0
    wins_ant = 0
    draw = 0

    eval_tabu = 0
    eval_ant = 0

    results_ant = 0
    results_tabu = 0

    for i in range(0, times):
        grafo = generateGraph(20)
        problem = test_problems.traveling_salesman_problem(grafo)

        r_ant = ant_colony_optimization(problem, surroundings_function=salesman_surroundings, randomFunction=salesman_random(grafo))
        eval_ant += problem.cantEvaluations
        results_ant += r_ant[1]

        r_tabu = tabu_search(problem, surroundings_function=salesman_surroundings, randomFuction=salesman_random(grafo))
        eval_tabu += problem.cantEvaluations
        results_tabu += r_tabu[1]
        
        if r_tabu[1] > r_ant[1]:
            wins_ant += 1
        elif r_tabu[1] == r_ant[1]:
            draw += 1
        else:
            wins_tabu += 1
    print("Traveling salesman Tabu %d Ant %d Draw %d" % (wins_tabu, wins_ant, draw))
    print("Promedio cantidad evaluaciones Tabu: ", eval_tabu / times)
    print("Promedio cantidad evaluaciones Ant: ", eval_ant / times)
    print("Promedio resultados Tabu: ", results_tabu / times)
    print("Promedio resultados Ant: ", results_ant / times)

simulate(2)