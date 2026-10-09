#natural numbers
'''n=int(input("enter n: "))
for i in range(1,n+1):
    if i%2==1:
        print('*',end= ' ')'''

#2-D data square pattern with numbers
'''n=int(input("Enter n: "))
for i in range(n):
    for j in range(n):
        print(i,end=' ')
    print()

n=int(input("Enter n: "))
for i in range(n):
    for j in range(n):
        print(j,end=' ')
    print()'''
#2-D data Hollow square pattern with numbers

#square
'''n=int(input("Enter n: "))
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''

'''n=int(input("Enter n: "))
for i in range(n):
    for j in range(n):
        if i==j or i+j==n-1 or i==0 or i==n-1 or j==0 or j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''
#square X 
'''n=int(input("Enter n: "))
for i in range(n):
    for j in range(n):
        if i==j or i+j==n-1 or i==0 or i==n-1 or j==0 or j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''
#Butterfly
'''n=int(input("Enter n: "))
for i in range(n):
    for j in range(n):
        if j==0 or j==n-1 or i+j==n-1 or i==j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''

#flower star
'''n=int(input("Enter n: "))
for i in range(n):
    for j in range(n):
        if i==j or i+j==n-1 or i==n//2 or j==n//2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''#Amazon question
#plus
'''n=int(input("Enter n: "))
for i in range(n):
    for j in range(n):
        if i==n//2 or j==n//2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''




















