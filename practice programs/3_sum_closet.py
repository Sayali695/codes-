# leetcode problem
# return a list with 3 nos whose sum is 0

import math


res=[]

n=int(input("Enter the size of an array "))
print("Enter the elements")
lis=[]
for i in range(n):
    lis.append(int(input()))
target=int(input("Enter the target element. "))
lis.sort()

# best=math.inf

# for i,a in enumerate(lis):
#     if i>0 and a==lis[i-1]:
#         continue
#     l,r=i+1,len(lis)-1
#     while l<r:
#         sum=a+lis[l]+lis[r]
#         if sum==target:
#             best=sum
#             break
#         if abs(target-sum)<abs(target-best):
#             best=sum
#         if sum<target:
#             l+=1
#         elif sum>target:
#             r-=1
# print(best)

# OR.

min_diff=math.inf
curr_sum=math.inf
for i,a in enumerate(lis):
    if i>0 and a==lis[i-1]:
        continue
    l,r=i+1,len(lis)-1
    while l<r:
        sum=a+lis[l]+lis[r]
        diff=abs(target-sum)
        if diff<min_diff:
            min_diff=diff
            curr_sum=sum
        if sum<target:
            l+=1
        elif sum>target:
            r-=1
        elif sum==target:
            print(sum)
            break
print("currsum",curr_sum)
#  [-1,2,1,-4], target = 1