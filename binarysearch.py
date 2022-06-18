def binary(arr,l,r,x):
    mid=l+(r-1)//2
    if arr[mid]==x:
        return mid
    elif arr[mid]>x:
        return(arr,l,mid-1,x)
    else:
        return(arr,mid+1,r,x)

arr=[1,2,3,4,5,6]
x=3
search=binary(arr,0,len(arr)-1,x)
if search!=-1:
    print("searched element is at position % d"  % search)
else:
    print("searched element is not available ")