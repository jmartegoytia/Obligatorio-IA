from tabu_search import tabu_search
from hill_climbing import hill_climbing
from ant_colony_optimization import ant_colony_optimization
def test(problem=None):
    if not problem:
        import test_problems
        problem = test_problems.bohachevsky()
   # print(list(hill_climbing(problem, steps=1000)))
    print(ant_colony_optimization(problem))

test()


grafo = Grafo([[0, 2, 3, None], [2, 0, None, 5], [3, None, 0, 4], [None, 5, 4, 0]])


# def test2(problem=None):
#     if not problem:
#         import test_problems
#         problemaTravel = test_problems.traveling_salesman_problem(grafo)
#     print(tabu_search(problemaTravel, iterations = 90000, max_size_tabu_list = 1000))

# test2()