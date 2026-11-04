#SLL insert from begining
'''class node:
    def __init__(self,data):
        self.data = data
        self.next = None
head = None
n=int(input("Enter number of nodes : "))
for i in range(n):
    data=int(input("Enter value"))
    newnode=node(data)
    newnode.next = head
    head = newnode
print("SLL:")
temp=head
while temp:
    print(temp.data,end='->')
    temp=temp.next
print("Tail")'''

class node:
    def __init__(self,data):
        self.data = data
        self.next = None
head = None
n=int(input("Enter number of nodes :"))
for i in range(n):
    data=int(input("Enter values:"))
    newnode=node(data)
    if head is None:
        head = newnode
    else:
        temp = head
        while temp.next:
            temp=temp.next
        temp.next = newnode
print("SLL:")
temp=head
while temp:
    print(temp.data,end='->')
    temp=temp.next
print("Tail")
