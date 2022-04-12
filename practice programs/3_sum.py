# leetcode problem
# return a list with 3 nos whose sum is 0

res=[]

n=int(input("Enter the size of an array "))
print("Enter the elements")
lis=[]
for i in range(n):
    lis.append(int(input()))
lis.sort()
for i,a in enumerate(lis):
    if i>0 and a==lis[i-1]:
        continue
    l,r=i+1,len(lis)-1
    while l<r:
        sum=a+lis[l]+lis[r]
        if sum<0:
            l+=1
        elif sum>0:
            r-=1
        else:
            res.append([a,lis[l],lis[r]])
            l+=1
            while lis[l]==lis[l-1] and l<r:
                l+=1
print(lis)
print("Result ", res)