from tabu_search import tabu_search
from grafo import Grafo

def test(problem=None):
    if not problem:
        import test_problems
        problemBohachevsky = test_problems.bohachevsky()
        problemSchwefel = test_problems.schwefel(1)
    print(tabu_search(problemBohachevsky, iterations = 90000, max_size_tabu_list = 1000))
    print(tabu_search(problemSchwefel, iterations = 90000, max_size_tabu_list = 1000))

#test()


grafo = Grafo([[0, 2, 3, None], [2, 0, None, 5], [3, None, 0, 4], [None, 5, 4, 0]])


def test2(problem=None):
    if not problem:
        import test_problems
        problemaTravel = test_problems.traveling_salesman_problem(grafo)
    print(tabu_search(problemaTravel, iterations = 90000, max_size_tabu_list = 1000))

test2()