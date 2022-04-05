def matrix(n,m):

    if n==1 or m==1:
        return 1
    return matrix(n-1,m)+matrix(n,m-1)

n=int(input("Enter rows "))
m=int(input("Enter Columns "))
print(matrix(n,m))