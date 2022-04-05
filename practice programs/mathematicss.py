# factorial

num=int(input())
res=1
for i in range(1,num+1):
    res=res*i

print("The factorial is", res)

zeros=0
i=1
# no of trailing zeros
while i<=num:
    if i%5==0:
        zeros+=num//i
    i=i*5
print("The trailing zeros are",zeros,i)


# pallimdrome

nums=int(input())
temp=nums
rev=0
while(nums!=0):
    rev=rev*10+nums%10
    nums=nums//10
if rev==temp:
    print("The given number is a Pallindrome")
else:
    print("The given number is not a pallindrome")


# GCD

a=int(input())
b=int(input())

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
print(gcd(a,b))
