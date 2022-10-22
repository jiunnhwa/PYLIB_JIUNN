import heapq
import random
 
res = [random.randrange(1, 100, 1) for i in range(7)]
print (res) # [70, 52, 57, 15, 88, 88, 42]

# heapq.nlargest(n, iterable)
n_largest_numbers = heapq.nlargest(3, res)
n_smallest_numbers = heapq.nsmallest(3, res)


print(max(n_largest_numbers),  n_largest_numbers)
print(min(n_smallest_numbers), n_smallest_numbers)
