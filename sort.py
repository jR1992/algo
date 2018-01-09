from random import randint

def quicksort(A):
	if len(A) <= 1:
		return A

	pivotindex = randint(0, len(A)-1)
	pivot = A[pivotindex]
	equal = [x for x in A if x == pivot]
	lesser = [x for x in A if x < pivot]
	greater = [x for x in A if x > pivot]
	return quicksort(lesser) + equal + quicksort(greater)


    