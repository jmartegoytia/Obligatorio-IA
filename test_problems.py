""" # Test functions

Test functions for benchmarking optimization techniques.
"""

from math import sin, cos, pi, sqrt, inf
from problem import OptimizationProblem

def _bohachevsky_ (elem):
    (x,y) = elem
    return x*x + 2*y*y-0.3*cos( (3*pi*x) + (4*pi*y)) + 0.3

def bohachevsky ():
    return OptimizationProblem(
        domains = ((-100,100),) * 2, objective = _bohachevsky_)

def _schwefel_ (elem):        
    sum = 0
    for i in elem:    
        sum = sum + i*sin(sqrt(abs(i)))
    return (418.9829 * len(elem)) - sum
    
def schwefel  (d):
    return OptimizationProblem(
        domains = ((-500,500),) * d,
        objective = _schwefel_)

def traveling_salesman_problem (grafo):
    return OptimizationProblem(
        domains = ((0, len(grafo.matriz)) * len(grafo.matriz),),
        objective = _traveling_salesman_problem_(grafo))

def _traveling_salesman_problem_ (grafo):
    maxValorArista = 0
    cantNone = 0
    suma = 0
    for i in grafo.matriz:
        for j in i:
            if (j is not None and j > maxValorArista):
                maxValorArista = j
        cantNone += len(list(filter(None, i)))

    for i in grafo.matriz:
        for j in i:
            if (j != None):        # No existe arista que una a los nodos
                suma += j
            else:
                suma += maxValorArista * 2 * cantNone


def hello_world(target_str="Hello world!"):
    target_chars = tuple(map(ord, target_str))
    return OptimizationProblem(
        domains = ((32, 126),) * len(target_str),
        objective = lambda chars: sum(abs(c - t) for (c, t) in zip(chars, target_chars))
    )

# References:
# + [Test functions for optimization @ Wikipedia](https://en.wikipedia.org/wiki/Test_functions_for_optimization)
# + [Test functions and datasets @ Virtual Library of Simulation Experiments](https://www.sfu.ca/~ssurjano/optimization.html)

def __schaffer_N2__(elem):
    (x,y) = elem
    return 0.5 + (sin(x*x - y*y) ** 2 - 0.5)/((1 + 0.001 * (x*x + y*y)) ** 2)

SCHAFFER_N2 = OptimizationProblem(domains= ((-100,+100),)*2, objective=__schaffer_N2__)