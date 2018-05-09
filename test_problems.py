""" # Test functions

Test functions for benchmarking optimization techniques.
"""
import random
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
        domains = [],
        objective = _traveling_salesman_problem_(grafo))


def _traveling_salesman_problem_ (grafo):
    def problem_function(elem):
        maxValorArista = -inf
        cantNone = 0
        suma = 0
        for i in grafo.matriz:
            for j in i:
                if (j is not None and j > maxValorArista):
                    maxValorArista = j
        for i in range(0, len(elem) - 1):
            if grafo.matriz[elem[i]][elem[i + 1]] is None:
                cantNone += 1
            else:
                suma += grafo.matriz[elem[i]][elem[i + 1]]
        if cantNone:
            return cantNone * (maxValorArista + 1) * len(grafo.matriz)
        else:
            return suma
    return problem_function
        


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