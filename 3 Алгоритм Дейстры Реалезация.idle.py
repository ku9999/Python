#3 Алгоритм Дейстры Реалезация
# import heapq

# class Graph:
#     def __init__(self):
#         self.graph = {}

#     def add_vertex(self, vertex):
#         if vertex not in self.graph:
#             self.graph[vertex] = []

#     def add_edge(self, from_vertex, to_vertex, weight):
#         self.graph[from_vertex].append((to_vertex, weight))

#     def shortest_path(self, start, end):
#         # Инициализация расстояний до вершин
#         distances = {vertex: float('inf') for vertex in self.graph}
#         distances[start] = 0

#         # Приоритетная очередь для хранения вершин и их текущих расстояний
#         priority_queue = [(0, start)]

#         while priority_queue:
#             current_distance, current_vertex = heapq.heappop(priority_queue)

#             # Пропустить вершину, если мы уже нашли более короткий путь до нее
#             if current_distance > distances[current_vertex]:
#                 continue

#             for neighbor, weight in self.graph[current_vertex]:
#                 distance = current_distance + weight

#                 # Если найден новый, более короткий путь до соседней вершины, обновите его
#                 if distance < distances[neighbor]:
#                     distances[neighbor] = distance
#                     heapq.heappush(priority_queue, (distance, neighbor))

#         # Построение кратчайшего пути
#         path = []
#         while end:
#             path.insert(0, end)
#             end = None
#             for neighbor, weight in self.graph[path[0]]:
#                 if distances[path[0]] == distances[neighbor] + weight:
#                     end = neighbor

#         return path, distances[path[-1]]

# # Пример использования
# graph = Graph()
# graph.add_vertex("A")
# graph.add_vertex("B")
# graph.add_vertex("C")
# graph.add_vertex("D")
# graph.add_edge("A", "B", 1)
# graph.add_edge("A", "C", 3)
# graph.add_edge("B", "C", 1)
# graph.add_edge("B", "D", 4)
# graph.add_edge("C", "D", 1)

# start_vertex = "A"
# end_vertex = "D"
# shortest_path, shortest_distance = graph.shortest_path(start_vertex, end_vertex)

# print(f"Кратчайший путь от {start_vertex} до {end_vertex}: [A,B,C,D]")
# print(f"Длина кратчайшего пути: {shortest_distance}")


import heapq

def calculate_distances(graph, starting_vertex):
    distances = {vertex: float('infinity') for vertex in graph}
    previous_vertices = {vertex: None for vertex in graph}
    distances[starting_vertex] = 0

    pq = [(0, starting_vertex)]
    while len(pq) > 0:
        current_distance, current_vertex = heapq.heappop(pq)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_vertices[neighbor] = current_vertex
                heapq.heappush(pq, (distance, neighbor))

    return distances, previous_vertices

def shortest_path(graph, start, end):
    distances, previous_vertices = calculate_distances(graph, start)
    path = []
    while end is not None:
        path.append(end)
        end = previous_vertices[end]
    path.reverse()
    return path, distances[path[-1]]

graph = {
    'Джал': {'шаурма': 1.5, 'филармония': 6, 'Азиамол': 2.5},
    'шаурма': {'Джал': 1.5, 'филармония': 1, 'Азиамол': 1.5},
    'филармония': {'Джал': 2, 'шаурма': 2.5, 'Азиамол': 0.5},
    'Азиамол': {'Джал': 2.5, 'шаурма': 1, 'филармония': 3.5},
}
print('вершины: Джал,шаурма,филармония,Азиамол')
start=input('Начало пути: ')
end=input('Конец пути: ')
full_path, full_distance = shortest_path(graph,start,end)

print(f"Path: {' -> '.join(full_path)}")
print(f"Total distance: {full_distance}"+' км')
