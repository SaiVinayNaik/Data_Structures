# finding the count of occurrence of a number 
arr= list(map(int, input("Enter elements ").split()))
num= int(input("Enter a value to be searched : "))
low= 0 
high = len(arr)-1
first, last= -1, -1 
while low<= high:
    mid= (low+high)//2
    if arr[mid]>= num:
        if arr[mid]== num:
            first= mid 
        high= mid-1 
    else:
        low= mid+1
low= 0 
high = len(arr)-1
while low<= high:
    mid= (low+high)//2
    if arr[mid]<= num:
        if arr[mid]== num:
            last= mid 
        low= mid+1 
    else:
        high= mid-1
print(last-first+1 if first !=-1 else 0)
    
