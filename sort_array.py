import time

def do_sort(arr):
	arr.sort()
	return arr


def bubble_sort(arr):
	n = len(arr)
	for i in range(n):
		for j in range(n - i - 1):
			if arr[j] > arr[j+1]:
				arr[j], arr[j + 1] = arr[j + 1], arr[j]
	
	return arr


def measure_time(func, arr):
	start_time = time.time()
	result = func(arr)
	end_time = time.time()

	return end_time - start_time, result



arr = list(range(10000))

bubble_time, bubble_result = measure_time(bubble_sort, arr)
print("time to bubble sort : ", format(bubble_time, ".10f"))

arr = list(range(10000))
reverse_time, reverse_result = measure_time(do_sort, arr)
print("time to bubble sort : ", format(reverse_time, ".10f"))

print("check two results are same : ", bubble_result == reverse_result)
