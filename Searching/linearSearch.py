#Linear search in unsorted List
def linearSearch(L,e):
    for i in range(len(L)):
        if L[i]==e:
            return 1
    return -1

#If List is sorted
def linearSearchSorted(L,e):
    for i in range(len(L)):
        if L[i]==e:
            return 1
        if L[i]>e:
            return -1
return -1

L=[1,2,3,4,5,6,7,8,9,0]
e=0

print(linearSearch(L,e))

#Run time is O(n)
#Least Practical use becuase of Binary search and Hash Tables


