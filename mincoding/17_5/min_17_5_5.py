vect = [3, 5, 4, 2, 6, 6, 5]
bit = list(map(int, input().split()))

for i in range(len(bit)):
    if bit[i]==0:
        vect[i] =0
    else:
        vect[i]=7
    print(vect[i], end='')