#Recursive Binary Search
#For sorted list/array
#Pick an index i that divides the list in half
#if L[i] == e return true
#if not ask if L[i] is smaller or greater than e
#Search either on left or right of e

# cook your dish here

def search(L,e):

    def binarySearch(L,e,low,high):

    #Base Case
        if high==low:
            return L[low]==e

        mid=(high+low)//2
        if L[mid]==e:
             return True
        elif L[mid]>e:
            if low == mid: #nothing left to search
                return False
            else:
                return binarySearch(L,e,low,mid-1)
        else:
            return binarySearch(L,e,mid+1,high)


    if len(L)==0:
        return False
    else:
        return binarySearch(L,e,0,len(L)-1)



L=[i for i in range(100)]

e=97

print(search(L,e))



#the function search here is knowna s a Wrapper function, it doesn't
#let the user know what's happening inside search, nice interface for
#client code
#Complexity O(log(n))





