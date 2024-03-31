# задание 1 Адгоритм Дейкстры
# import heapq
# def dijkstra(graph, start):
#     # Инициализация расстояний до вершин
#     distances = {vertex: float('infinity') for vertex in graph}
#     distances[start] = 0
#     # Инициализация структуры для хранения пути
#     path = {}
#     # Очередь с приоритетом для обработки вершин
#     priority_queue = [(0, start)]
#     while priority_queue:
#         current_distance, current_vertex = heapq.heappop(priority_queue)
#         # Проверка, что текущее расстояние - это наименьшее
#         if current_distance > distances[current_vertex]:
#             continue
#         # Перебор соседних вершин
#         for neighbor, weight in graph[current_vertex].items():
#             distance = current_distance + weight
#             # Если найден более короткий путь, обновляем расстояние и путь
#             if distance < distances[neighbor]:
#                 distances[neighbor] = distance
#                 path[neighbor] = current_vertex
#                 heapq.heappush(priority_queue, (distance, neighbor))
#     return distances, path
# graph = {
#     'A': {'B': 1, 'C': 4},
#     'B': {'A': 1, 'C': 2, 'D': 5},
#     'C': {'A': 4, 'B': 2, 'D': 1},
#     'D': {'B': 5, 'C': 1}
# }
# start_vertex = 'A'
# print(dijkstra(graph, start_vertex))


# задание 2 Сортировка слиянием (Merge Sort)
# def merge_sort(arr):
#     if len(arr)<=1:
#         return arr
#     def merge(left,right):
#         result=[]
#         left_index,right_index=0,0
#         while left_index<len(left) and right_index< len(right):
#             if left[left_index]<right[right_index]:
#                 result.append(left[left_index])
#                 left_index+=1
#             else:
#                 result.append(right[right_index])
#                 right_index+=1
#         result.extend(left[left_index:])
#         result.extend(right[right_index:])
#         return result

#     middle = len(arr) // 2
#     left = arr[:middle]
#     right = arr[middle:]

#     return merge(merge_sort(left), merge_sort(right))
# arr = [38, 27, 43, 3, 9, 82, 10]
# sorted_arr = merge_sort(arr)
# print(sorted_arr)


#Задания № 3 Связанный список
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def append(self, data):
#         new_node = Node(data)
#         if not self.head:
#             self.head = new_node
#             return
#         current = self.head
#         while current.next:
#             current = current.next
#         current.next = new_node

#     def display(self):
#         current = self.head
#         while current:
#             print(current.data, end=" -> ")
#             current = current.next
#         print("None")

# ll = LinkedList()
# ll.append(1)
# ll.append(2)
# ll.append(3)
# ll.display()
# Задания № 4 Бинарное дерево
# class TreeNode:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def append(self, data):
#         new_node = TreeNode(data)
#         if not self.head:
#             self.head = new_node
#         else:
#             current = self.head
#             while current.next:
#                 current = current.next
#             current.next = new_node

#     def delete(self, value):
#         if not self.head:
#             return

#         if self.head.data == value:
#             self.head = self.head.next
#             return

#         current = self.head
#         while current.next:
#             if current.next.data == value:
#                 current.next = current.next.next
#                 return
#             current = current.next

#     def search(self, value):
#         current = self.head
#         while current:
#             if current.data == value:
#                 return True
#             current = current.next
#         return False
# linked_list = LinkedList()
# linked_list.append(1)
# linked_list.append(2)
# linked_list.append(3)
# print(linked_list.search(2)) 
# linked_list.delete(2)
# print(linked_list.search(2))

# Задания № 5 Хеш-таблица с методом цепочек
# class HashTable:
#     def __init__(self, size):
#         self.size = size
#         self.table = [[] for _ in range(size)]
#     def insert(self, key, value):
#         hash_value = self._hash(key)
#         for i, (existing_key, existing_value) in enumerate(self.table[hash_value]):
#             if existing_key == key:
#                 self.table[hash_value][i] = (key, value)
#                 return
#         self.table[hash_value].append((key, value))
#     def search(self, key):
#         hash_value = self._hash(key)
#         for existing_key, existing_value in self.table[hash_value]:
#             if existing_key == key:
#                 return existing_value  
#         return None 
#     def delete(self, key):
#         hash_value = self._hash(key)
#         for i, (existing_key, existing_value) in enumerate(self.table[hash_value]):
#             if existing_key == key:
#                 del self.table[hash_value][i]
#                 return
#     def display(self):
#         for i, bucket in enumerate(self.table):
#             print(f'Bucket {i}:', end=" ")
#             for key, value in bucket:
#                 print(f'({key}: {value})', end=" ")
#             print()
#     def _hash(self, key):
#         return hash(key) % self.size

# Задания № 6 Алгоритм быстрой сортировки (Quick Sort)

# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr

#     pivot = arr[len(arr) // 2]
#     left = [x for x in arr if x < pivot]
#     middle = [x for x in arr if x == pivot]
#     right = [x for x in arr if x > pivot]

#     # Рекурсивно сортируйте left и right и объедините их с middle
#     return quick_sort(left) + middle + quick_sort(right)
