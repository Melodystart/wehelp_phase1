# Python program for implementation of MergeSort

def mergeSort(arr):
	if len(arr) > 1:

		# Finding the mid of the array
		mid = len(arr)//2

		# Dividing the array elements
		L = arr[:mid]

		# Into 2 halves
		R = arr[mid:]

		# Sorting the first half
		mergeSort(L)

		# Sorting the second half
		mergeSort(R)

		i = j = k = 0

		# Copy data to temp arrays L[] and R[]
		while i < len(L) and j < len(R):
			if L[i] <= R[j]:
				arr[k] = L[i]
				i += 1
			else:
				arr[k] = R[j]
				j += 1
			k += 1

		# Checking if any element was left
		while i < len(L):
			arr[k] = L[i]
			i += 1
			k += 1

		while j < len(R):
			arr[k] = R[j]
			j += 1
			k += 1


# Code to print the list
def printList(arr):
	for i in range(len(arr)):
		print(arr[i], end=" ")
	print()


# Driver Code
if __name__ == '__main__':
  import time
  T1 = time.perf_counter()

  import random

  arr = []
  
  for i in range(100):
    arr.append(random.randrange(100))

  print("Given array is")
  printList(arr)
  mergeSort(arr)
  print("\nSorted array is ")
  printList(arr)

  T2 =time.perf_counter()
  print('程序运行时间:%s毫秒' % ((T2 - T1)*1000))

# This code is contributed by Mayank Khanna
