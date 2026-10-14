'''
greedy approach
backtracking
tail recursion
nested recurion
'''

coins=list(map(int,input("Enter coins:").split()))
amoount=int(input("Enter amount:"))
total_count=0
for coin in coins:
    count=amout//coin
    if count>0:
        print(coin,"rupees:",count)
        total_count+=count
        amount%=coins
print("Total coins:"),total_count
