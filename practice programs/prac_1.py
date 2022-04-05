# find the non repeatative element where each element is repeated twice

lis=[5,6,9,8,7,10,5,6,9,8,7]
ans=0
for i in lis:
    ans=ans^i

print("The number is", ans)

# find the two non repeating element where each element is repeated twice

lis2=[5,2,3,8,5,8,42,71,2,3]
ans=0
odd=[]  
for i in lis2:
    ans=ans^i
    if i&1==1:
        odd.append(i)          # so that we get all the elements which has its least significant bit=1
temp=ans

for i in odd:
    ans=ans^i
temp=ans^temp
print("the two elements are", ans,temp)

