#Selection Sort

def SelectionSort(A):

	for i in range(len(A)):

		min_idx=i

		for j in range(i+1,len(A)):
			if A[min_idx]>A[j]:
				min_idx=j

		A[min_idx],A[i]=A[i],A[min_idx]


A=[45,78,26,15,98,1,56]

SelectionSort(A)

print(A)