#Edge cases
#second largest
'''arr=list(map(int,input("Enter elements:").split()))
if len(arr)<2:
    print("Not enough elements")
else:
    largest=float('-inf')
    second=float('-inf')
    for val in arr:
        if val>largest:
            second=largest
            largest=val
        elif val>second and val!=largest:
            second=val
    if second==float('-inf'):
        print("No second value exits")
    else:
        print("Second largest",second)'''

#Tom Riddles anagram
'''s1=input("Enter first string: ").lower().replace(' ','')
s2=input("Enter second string: ").lower().replace(' ','')
if len(s1)==len(s2):
    if sorted(s1)==sorted(s2):
        print("Tom Riddles Anagram")
    else:
        print("Not")
else:
    print("Not")'''

'''s1 = input("enter first string:").lower().replace(' ', ' ')
s2 = input("enter second string:").lower().replace(' ', ' ')
s1= ' '.join(ch for ch in s1 if ch.isalpha())
s2= ' '.join(ch for ch in s2 if ch.isalpha())


if len(s1)==0 or len(s2)==0:
    print("Not Tom Riddles Anagram")
elif len(s1)==1 or len(s2)==1:
    print("Not Tom Riddles Anagram")
elif len(s1)!= len(s2):
    print("Not Tom Riddles Anagram")
elif len(set(s1))==1 or len(set(s2))==1:
    print("Not Tom Riddles Anagram")
elif sorted(s1)==sorted(s2):
    print("Tom Riddles Anagram")
else:
    print("Not")'''
