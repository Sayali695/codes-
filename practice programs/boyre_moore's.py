# check which element has its occurance greater than n/2


n=int(input("Enter the size of an array "))
print("Enter the elements")
lis=[]
for i in range(n):
    lis.append(int(input()))
# c=0
# for i in lis:
#     if lis.count(i)>n//2:
#         print("the element is ", i)
#         c=1
#         break
# if c!=1:
#     print("There is no such element present in the list.")



# using boyre moor's voting algorithm

freq=1
ele=lis[0]
for i in range(len(lis)):
    if lis[i]==ele:
        freq+=1
    else:
        freq-=1
    if freq==0:
        ele=i
        freq=1
count=0
for i in lis:
    if i==ele:
        count+=1
if count>n//2:
    print("the element is ", ele)
else:
    print("There is no such element present in the list.")