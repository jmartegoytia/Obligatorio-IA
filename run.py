from tabu_search import tabu_search
from hill_climbing import hill_climbing
from ant_colony_optimization import ant_colony_optimization
def test(problem=None):
    if not problem:
        import test_problems
        problem = test_problems.hello_world()
   # print(list(hill_climbing(problem, steps=1000)))
    print(ant_colony_optimization(problem))

test()