#Write a Python program to search an element in a list using Linear Search.
'''arr=list(map(int,input("enter values:").split()))
search=int(input("Enter element to be searched:"))
found=False
for i in range(len(arr)):
    if arr[i]==search:
        print("element found at :",i)
        found=True
        break
if not found:
    print("Element out of range")'''
#search for an element in a 2D list using Linear Search.
'''n = int(input("Enter the size:"))
arr = []
for i in range(n):
    arr.append(list(map(int, input("Enter values:").split())))
search = int(input("Enter element to be searched:"))
found = False
for i in range(n):
    for j in range(n):
        if arr[i][j] == search:
            print("Element found at row:", i, "col:", j)
            found = True
            break
    if found:
        break
if not found:
    print("Element not found")'''

#sum of elements
'''n=int(input("Enter the size:"))
s=0
arr=[]
for i in range(n):
    arr.append(list(map(int,input().split())))
for i in range(n):
    for j in range(n):
        s+=arr[i][j]
print("Total:",s)'''


'''n=int(input("Enter the size:"))
arr=[]
for i in range(n):
    arr.append(list(map(int,input().split())))
for i in range(n):
    s=0
    for j in range(n):
        s+=arr[i][j]
    print("Row:",i+1,"sum:",s)
print()
for j in range(n):
    s=0
    for j in range(n):
        s+=arr[i][j]
    print("col:",j+1,"sum:",s)'''

#find the sum of the principal and anti-diagonal elements of a matrix.
'''n=int(input("Enter the size:"))
arr=[]
di=0
ad=0
for i in range(n):
    arr.append(list(map(int,input().split())))
for i in range(n):
    for j in range(n):
        if i==j:
            di+=arr[i][j]
        if i+j==n-1:
            ad+=arr[i][j]
print("Diagnol sum:",di)
print("Anti-Diagnol sum:",ad)'''   































