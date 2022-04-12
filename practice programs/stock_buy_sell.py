n=int(input("Enter the size of an array "))
print("Enter the elements")
lis=[]
h=[]
for i in range(n):
    lis.append(int(input()))
    
min_=lis[0]
max_profit=0
for i in lis:
    p=i-min_
    if p>max_profit:
        max_profit=p
    if i<min_:
        min_=i
print("maximum",max_profit)
print("minimum element",min_)