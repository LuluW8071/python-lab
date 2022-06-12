

def merge(array):
    if len(array)>1:
        mid=len(array)//2
        L=array[:mid]
        R=array[mid:]
        merge(L)
        merge(R)
        i=j=k=0
    
        while i<len(L) and j<len(R):
            if L[i] <= R[j]:
                array[k]=L[i]
                i+=1

            else:
                array[k]=R[j]
                j+=1
            k+=1

        while i<len(L):
            array[k]=L[i]
            i+=1
            k+=1

        while j<len(R):
            array[k]=R[j]
            j+=1
            k+=1

def printarr(array):
    for i in range(len(array)):
        print(array[i],end=" ")
    print()
    

array=[10,9,2,120,30,80,21,6,1]
print("Given array is",end="\n")
printarr(array)
merge(array)
print("sorted array is")
printarr(array)




