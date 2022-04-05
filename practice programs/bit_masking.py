# finding i'th bit
num=18                 #10010
i=int(input())                 #2
mask=1<<i                  #01
if num&mask == 0:
    print("The bit is 0")
else:
    print("The bit is 1")


# set i'th bit

set_bit =  num^mask
print(set_bit)

# clear i'th bit

n_mask=~mask
clear=num&n_mask
print(clear)