import collections
def cycleCheck(adjacency):
    graph = collections.defaultdict(list)
    in_degree = collections.defaultdict(int)

    for edge in adjacency:
        graph[edge[0]].append(edge[1])
        in_degree[edge[1]]+=1

    
    num_edges = len(adjacency)
    return 