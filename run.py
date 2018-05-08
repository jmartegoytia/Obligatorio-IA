from tabu_search import tabu_search

def test(problem=None):
    if not problem:
        import test_problems
        problemBohachevsky = test_problems.bohachevsky()
        problemSchwefel = test_problems.schwefel(1)
    print(tabu_search(problemBohachevsky, iterations = 90000, max_size_tabu_list = 1000))
    print(tabu_search(problemSchwefel, iterations = 90000, max_size_tabu_list = 1000))

test()