def game_of_death(n,k):
    if n==1:
        return 0
    else:
        return (game_of_death(n-1,k)+k)%n


n=int(input("Enter no. of person's  "))
k=int(input("Rules "))
print(game_of_death(n,k))