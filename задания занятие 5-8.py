#1 
#with open('dd.txt', 'w') as s:
#    s.write('1 2 3 4 5 6')
# def sequential_search(arr, target):
#     comparisons = 0
#     for i in range(len(arr)):
#         comparisons += 1
#         if arr[i] == target:
#             return i, comparisons
#     return -1, comparisons
# def binary_search(arr, target):
#     comparisons = 0
#     low = 0
#     high = len(arr) - 1
#     while low <= high:
#         mid = (low + high) // 2
#         comparisons += 1
#         if arr[mid] == target:
#             return mid, comparisons
#         elif arr[mid] < target:
#             low = mid + 1
#         else:
#             high = mid - 1
#     return -1, comparisons
# def interpolation_search(arr, target):
#     comparisons = 0
#     low = 0
#     high = len(arr) - 1
#     while low <= high and arr[low] <= target <= arr[high]:
#         pos = low + ((target - arr[low]) * (high - low)) // (arr[high] - arr[low])
#         comparisons += 1
#         if arr[pos] == target:
#             return pos, comparisons
#         elif arr[pos] < target:
#             low = pos + 1
#         else:
#             high = pos - 1
#     return -1, comparisons
# with open('dd.txt', 'r') as file:
#     numbers = [int(num) for num in file.read().split()]
# target_number = int(input("Введите число для поиска: "))
# sequential_result, sequential_comparisons = sequential_search(numbers, target_number)
# binary_result, binary_comparisons = binary_search(numbers, target_number)
# interpolation_result, interpolation_comparisons = interpolation_search(numbers, target_number)
# print("Местоположение числа по последовательному поиску:", sequential_result)
# print("Количество сравнений при последовательном поиске:", sequential_comparisons)
# print("Местоположение числа по бинарному поиску:", binary_result)
# print("Количество сравнений при бинарном поиске:", binary_comparisons)
# print("Местоположение числа по интерполяционному поиску:", interpolation_result)
# print("Количество сравнений при интерполяционном поиске:", interpolation_comparisons)


#2
# def sequential_search(sequence, target):
#     comparisons = 0
#     for i in range(len(sequence) - len(target) + 1):
#         for j in range(len(target)):
#             comparisons += 1
#             if sequence[i + j] != target[j]:
#                 break
#         else:
#             return i, comparisons
#     return -1, comparisons

# def knuth_morris_pratt(sequence, target):
#     def build_table(pattern):
#         table = [0] * len(pattern)
#         prefix_length = 0
#         for i in range(1, len(pattern)):
#             while prefix_length > 0 and pattern[i] != pattern[prefix_length]:
#                 prefix_length = table[prefix_length - 1]
#             if pattern[i] == pattern[prefix_length]:
#                 prefix_length += 1
#             table[i] = prefix_length
#         return table

#     comparisons = 0
#     table = build_table(target)
#     i = j = 0
#     while i < len(sequence):
#         comparisons += 1
#         if sequence[i] == target[j]:
#             i += 1
#             j += 1
#             if j == len(target):
#                 return i - j, comparisons
#         else:
#             if j > 0:
#                 j = table[j - 1]
#             else:
#                 i += 1
#     return -1, comparisons

# def boyer_moore(sequence, target):
#     def build_table(pattern):
#         table = {}
#         for i in range(len(pattern) - 1):
#             table[pattern[i]] = len(pattern) - 1 - i
#         return table

#     comparisons = 0
#     table = build_table(target)
#     i = len(target) - 1
#     while i < len(sequence):
#         k = i
#         j = len(target) - 1
#         while j >= 0 and sequence[k] == target[j]:
#             comparisons += 1
#             k -= 1
#             j -= 1
#         if j == -1:
#             return k + 1, comparisons
#         else:
#             comparisons += 1
#             if sequence[k] in table:
#                 i += table[sequence[k]]
#             else:
#                 i += len(target)
#     return -1, comparisons

# with open('dd.txt', 'r') as file:
#     sequence = [int(num) for num in file.read().split()]

# target_sequence = input("Введите последовательность чисел для поиска: ").split()
# target_sequence = [int(num) for num in target_sequence]

# sequential_result, sequential_comparisons = sequential_search(sequence, target_sequence)

# # Последовательный поиск
# sequential_result, sequential_comparisons = sequential_search(sequence, target_sequence)
# print(f"Последовательный поиск: {sequential_comparisons} сравнений")

# # Поиск Кнута-Морриса-Пратта
# kmp_result, kmp_comparisons = knuth_morris_pratt(sequence, target_sequence)
# print(f"Поиск Кнута-Морриса-Пратта: {kmp_comparisons} сравнений")

# # Поиск Бойера-Мура
# bm_result, bm_comparisons = boyer_moore(sequence, target_sequence)
# print(f"Поиск Бойера-Мура: {bm_comparisons} сравнений")




#3
# def insertion_sort(arr):
#     comparisons = 0
#     for i in range(1, len(arr)):
#         key = arr[i]
#         j = i-1
#         while j >= 0 and key < arr[j] :
#                 comparisons += 1
#                 arr[j + 1] = arr[j]
#                 j -= 1
#         arr[j + 1] = key
#     return comparisons

# def bubble_sort(arr):
#     comparisons = 0
#     n = len(arr)
#     for i in range(n):
#         for j in range(0, n-i-1):
#             comparisons += 1
#             if arr[j] > arr[j+1] :
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#     return comparisons

# def selection_sort(arr):
#     comparisons = 0
#     for i in range(len(arr)):
#         min_idx = i
#         for j in range(i+1, len(arr)):
#             comparisons += 1
#             if arr[min_idx] > arr[j]:
#                 min_idx = j
#         arr[i], arr[min_idx] = arr[min_idx], arr[i]
#     return comparisons

# def shell_sort(arr):
#     comparisons = 0
#     n = len(arr)
#     gap = n//2
#     while gap > 0:
#         for i in range(gap,n):
#             temp = arr[i]
#             j = i
#             while  j >= gap and arr[j-gap] > temp:
#                 comparisons += 1
#                 arr[j] = arr[j-gap]
#                 j -= gap
#             arr[j] = temp
#         gap //= 2
#     return comparisons

# def heapify(arr, n, i):
#     comparisons = 0
#     largest = i
#     l = 2 * i + 1
#     r = 2 * i + 2
#     if l < n and arr[i] < arr[l]:
#         comparisons += 1
#         largest = l
#     if r < n and arr[largest] < arr[r]:
#         comparisons += 1
#         largest = r
#     if largest != i:
#         arr[i],arr[largest] = arr[largest],arr[i]
#         comparisons += heapify(arr, n, largest)
#     return comparisons

# def heap_sort(arr):
#     n = len(arr)
#     comparisons = 0
#     for i in range(n, -1, -1):
#         comparisons += heapify(arr, n, i)
#     for i in range(n-1, 0, -1):
#         arr[i], arr[0] = arr[0], arr[i]
#         comparisons += heapify(arr, i, 0)
#     return comparisons

# def partition(arr, low, high):
#     comparisons = 0
#     i = (low-1)
#     pivot = arr[high]
#     for j in range(low, high):
#         comparisons += 1
#         if arr[j] <= pivot:
#             i = i+1
#             arr[i], arr[j] = arr[j], arr[i]
#     arr[i+1], arr[high] = arr[high], arr[i+1]
#     return (i+1), comparisons

# def quick_sort(arr, low, high):
#     comparisons = 0
#     if len(arr) == 1:
#         return arr
#     if low < high:
#         pi, comparisons = partition(arr, low, high)
#         comparisons += quick_sort(arr, low, pi-1)
#         comparisons += quick_sort(arr, pi+1, high)
#     return comparisons

# with open('dd.txt', 'r') as file:
#     sequence = [int(num) for num in file.read().split()]

# # Сортировка и подсчет сравнений
# print(f"Сортировка вставками: {insertion_sort(sequence[:])} сравнений")
# print(f"Метод пузырька: {bubble_sort(sequence[:])} сравнений")
# print(f"Сортировка выбором: {selection_sort(sequence[:])} сравнений")
# print(f"Сортировка Шелла: {shell_sort(sequence[:])} сравнений")
# print(f"Пирамидальная сортировка: {heap_sort(sequence[:])} сравнений")
# print(f"Быстрая сортировка: {quick_sort(sequence[:], 0, len(sequence)-1)} сравнений")



#4
# def merge_sort(list):
#     if len(list) < 2:
#         return list
#     middle = len(list) // 2
#     left = merge_sort(list[:middle])
#     right = merge_sort(list[middle:])
#     return merge(left, right)

# def merge(left, right):
#     result = []
#     while left and right:
#         if left[0] < right[0]:
#             result.append(left.pop(0))
#         else:
#             result.append(right.pop(0))
#     result.extend(left if left else right)
#     return result

# with open('dd.txt', 'r') as file:
#     numbers = list(map(int, file.read().split()))
# sorted_numbers = merge_sort(numbers)
# print(sorted_numbers)
# with open('d.txt', 'w') as file:
#     file.write(' '.join(map(str, sorted_numbers)))
