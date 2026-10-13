#direct recurion
'''def numbers(n):
    if n==0:
        return
    print(n)
    numbers(n-1)
n=int(input("Enter n:"))
numbers(n)'''

#direct recurion - factrial of a number
'''def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
n=int(input("Enter n:"))
print("Factorial:",fact(n))'''

#indirect recurssion
'''def one(n):
    if n<=0:
        return
    print("one:",n)
    two(n-1)
def two(n):
    if n<=0:
        return
    print("two:",n)
    one(n-1)
n=int(input("Enter a number:"))
one(n)'''

#odd or even without using modulous
'''def even(n):
    if n==0:
        print(copy, "is even .")
        return
    odd(n-1)
def odd(n):
    if n==0:
        print(copy, "is odd .")
        return
    even(n-1)
n=int(input("Enter a number:"))
copy=n
even(n)'''

#tree recurssion
'''def fun(n):
    if n==0:
        return
    print(n)
    fun(n-1)
    fun(n-1)
n=int(input("Enter the number:"))
fun(n)'''

















































