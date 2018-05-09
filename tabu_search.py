def surroundings(center, radius, domains):
    """ The surroundings of a `center` is a list of new centers, all equal to the center except for
    one value that has been increased or decreased by `radius`.
    """
    return [center[0:i] + (center[i] + d,) + center[i + 1:]
               for i in range(len(center)) for d in (-radius, +radius) 
               if center[i] - radius >= domains[i][0] and center[i] + radius <= domains[i][1]
           ]

def tabu_search(problem, iterations = 1000, max_size_tabu_list = 100):
    best = None
    bestCandidate = None
    tabu_list = []
    i = 0

    currentCandidate = problem.randomElement()
    print(currentCandidate)

    best = problem.objective(currentCandidate)
    currentCandidate = (currentCandidate, best)

    while(i < iterations):      
        nexts = problem.evaluated(surroundings(currentCandidate[0], 1, problem.domains))
        nexts = list(filter(lambda x : x[0] not in tabu_list, nexts))
        if (nexts):        
            currentCandidate = nexts[0]
            tabu_list.append(bestCandidate)

            if  (problem.compareEvaluations(best, currentCandidate[1]) > 0):
                best = currentCandidate[1]
                bestCandidate = currentCandidate                

            if (len(tabu_list) > max_size_tabu_list):
                tabu_list.pop(0)
        i += 1
    return bestCandidate, best