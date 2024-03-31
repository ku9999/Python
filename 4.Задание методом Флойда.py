#4.Задание методом Флойда 
def floyd_warshall(graph):
    nodes = list(graph.keys())
    dist = {}
    
    for n in nodes:
        dist[n] = {}
        for k in nodes:
            if k == n:
                dist[n][k] = 0
            elif k in graph[n]:
                dist[n][k] = graph[n][k]
            else:
                dist[n][k] = float('inf')

    for p in nodes:
        for n in nodes:
            for k in nodes:
                if dist[n][k] > dist[n][p] + dist[p][k]:
                    dist[n][k] = dist[n][p] + dist[p][k]

    return dist

graph = {
    'Джал': {'шаурма': 1.5, 'филармония': 6, 'Азиамол': 2.5},
    'шаурма': {'Джал': 1.5, 'филармония': 1, 'Азиамол': 1.5},
    'филармония': {'Джал': 2, 'шаурма': 2.5, 'Азиамол': 0.5},
    'Азиамол': {'Джал': 2.5, 'шаурма': 1, 'филармония': 3.5},
}

distances = floyd_warshall(graph)
matrix=[[distances[start][end] for end in distances[start]] for start in distances]
for row in matrix:
    print(*row)
