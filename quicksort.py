#Flip sort or Pancake sort
#quick sort

'''def pancakesort(arr):
    n=len(arr)
    for size in range(n,1,-1):
        max_index=arr.index(max(arr[:size]))
        arr[:max_index+1]=arr[:max_index+1][::-1]
        arr[:size]=arr[:size][::-1]
    return arr
arr=list(map(int,input("Enter elements:").split()))
print("sorted array:",pancakesort(arr))'''
'''
3 2 4 1
n=4
for (4,1,-1)
maxindex=arr[:4]
maxindex=2
arr[:2+1][::1]
1 2 3 4

for(3,1,-1)
maxindex-arr[:3]
maxindex=1
arr[:1+1]=arr[:1+1][::-1]
3 2 1 4
arr[:3]=arr[:3][::-1]
1 2 3 4'''

def quicksort(arr):
    n=len(arr)
    if n<=1:
        return arr
    pivot=arr[-1]
    left=[x for x in arr[:-1] if x<=pivot]
    right=[x for x in arr[:-1] if x>pivot]
    return quicksort(left)+[pivot]+quicksort(right)
arr=list(map(int,input("Enter elements:").split()))
print("Sorted array:", quicksort(arr))
