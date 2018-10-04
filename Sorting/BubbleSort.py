def bubbleSort(L):
    n = len(L)

    # Traverse through all Lay elements
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n-i-1):

            # traverse the Lay from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if L[j] > L[j+1] :
                L[j], L[j+1] = L[j+1], L[j]

# Driver code to test above
L = [64, 34, 25, 12, 22, 11, 90]

bubbleSort(L)

print(L)
