#Задание: Реализация сортировки пузырьком
# my_list = [64, 34, 25, 12, 22, 11, 90]
# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n): 
#         for j in range(0, n-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]    
#     return arr
# sorted_list = bubble_sort(my_list)
# print(sorted_list)
#Задание: Реализация сортировки пузырьком другой способ
# arr=[64, 34, 25, 12, 22, 11, 90]
# n = len(arr)
# for i in range(n):
#     for j in range(0, n-i-1):
#         if arr[j] > arr[j+1]:
#             arr[j], arr[j+1] = arr[j+1], arr[j]
# print(arr)

#Задание: Реализация линейного поиска в массиве        
# my_list = [64, 34, 25, 12, 22, 11, 90]
# def linear_search(arr, target):
#    for i in range(len(arr)):
#        if arr[i] == target:
#            return i
#    return -1
# target_value = 22
# result = linear_search(my_list, target_value)
# print(result)
#Задание: Реализация линейного поиска в массиве другой способ       
# arr = [64, 34, 25, 12, 22, 11, 90]
# print(arr.index(22))

#Задание: Реализация двоичного поиска в отсортированном массиве
# my_sorted_list = [11, 12, 22, 25, 34, 64, 90]
# def binary_search(arr, target):
#    left, right = 0, len(arr) - 1
#    while left <= right:
#        mid = (left + right) // 2
#        if arr[mid] == target:
#            return mid
#        elif arr[mid] < target:
#            left = mid + 1
#        else:
#            right = mid - 1
#    return -1
# target_value = 22
# result = binary_search(my_sorted_list, target_value)
# print(result)
#Задание: Реализация двоичного поиска в отсортированном массиве другой способ
# arr = [64, 34, 25, 12, 22, 11, 90]
# print(arr.index(22))


#Задание: Реализация стека на основе встроенного списка
#class Stack:
#    def __init__(self):
#        self.items = []
#
#    def is_empty(self):
#        return len(self.items) == 0
#
#    def push(self, item):
#        self.items.append(item)
#
#    def pop(self):
#        if not self.is_empty():
#            return self.items.pop()
#        else:
#            return None
#    def peek(self):
#        if not self.is_empty():
#            return self.items[-1]
#        else:
#            return None
#    def size(self):
#        return len(self.items)
#my_stack =Stack()
#my_stack.push(1)
#my_stack.push(2)
#my_stack.push(3)
#print(my_stack.peek())  # Ожидаемый вывод: 3
#print(my_stack.pop())   # Ожидаемый вывод: 3
#print(my_stack.size())  # Ожидаемый вывод: 2
#print(my_stack.is_empty())  # Ожидаемый вывод: False


#Задание: Реализация очереди на основе встроенного списка
#class Queue:
#    def __init__(self):
#        self.items = []
#    def enqueue(self, item):
#        self.items.append(item)
#    def dequeue(self):
#         if not self.is_empty():
#             return self.items.pop(0)
#     def is_empty(self):
#         return len(self.items) == 0
#     def size(self):
#         return len(self.items)
# my_queue = Queue()
# my_queue.enqueue(1)
# my_queue.enqueue(2)
# my_queue.enqueue(3)
# print(my_queue.dequeue())  # Ожидаемый вывод: 1
# print(my_queue.size())     # Ожидаемый вывод: 2
# print(my_queue.is_empty()) # Ожидаемый вывод: False




