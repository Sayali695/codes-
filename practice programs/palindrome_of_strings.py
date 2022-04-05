def pali(s,l,r):
    if l>=r:
        return True
    if s[l]!=s[r]:
        return False
    return pali(s,l+1,r-1)



s=input("Enter the string ")
l=0
r=len(s)-1
print(pali(s,l,r))