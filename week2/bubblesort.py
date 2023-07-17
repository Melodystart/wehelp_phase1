# Optimized Python program for implementation of Bubble Sort

def bubbleSort(arr):
	n = len(arr)
	
	# Traverse through all array elements
	for i in range(n):
		swapped = False

		# Last i elements are already in place
		for j in range(0, n-i-1):

			# Traverse the array from 0 to n-i-1
			# Swap if the element found is greater
			# than the next element
			if arr[j] > arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]
				swapped = True
		if (swapped == False):
			break

# Driver code to test above
if __name__ == "__main__":
  import time
  T1 = time.perf_counter()

  import random

  arr = []
  
  for i in range(100):
    arr.append(random.randrange(100))

  bubbleSort(arr)

  print("Sorted array:")
	
  for i in range(len(arr)):
	  print("%d" % arr[i], end=" ")

  T2 =time.perf_counter()
  print('程序运行时间:%s毫秒' % ((T2 - T1)*1000))

# This code is modified by Suraj krushna Yadav
