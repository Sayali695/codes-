# find no. of bits to convert a to b
a=13               #1101
b=10               #1010
ans= a^b          #0111

count=0
while ans!=0:
    if ans&1==1:
        count+=1
    ans=ans>>1


print(count)