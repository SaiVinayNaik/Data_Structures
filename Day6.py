'''
greedy approach
backtracking
tail recursion
nested recurion
'''
'''coins = list(map(int, input("Enter coins: ").split()))
amount = int(input("Enter amount: "))
total_count = 0

for coin in coins:
    count = amount // coin

    if count > 0:
        print(coin, "rupees:", count)
        total_count += count
        amount %= coin

print("Total coins:", total_count)'''


'''a=list(map(int,input("Enter coins:").split()))
print(a)'''

'''n = int(input("Enter n:"))

def backtrack(s):
    if len(s) == n:
        print(s)
        return

    backtrack(s + '0')
    backtrack(s + '1')

backtrack("")'''

# Nested recursion
def fun(n):
    if n > 10:
        return n
    return fun(fun(n + 2))

n = int(input("Enter N: "))
print(fun(n))

