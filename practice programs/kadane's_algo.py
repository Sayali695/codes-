import math


n=int(input("Size:- "))
lis=[]
print("Enter")
for i in range(n):
    lis.append(int(input()))

curr_sum=0
max_sum=-math.inf
for i in lis:
    curr_sum+=i
    if curr_sum>max_sum:
        max_sum=curr_sum
    if curr_sum<0:
        curr_sum=0
print("ans is ",max_sum)