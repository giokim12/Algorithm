a = list(map(int, input().split()))
b = list(map(int, input().split()))
Result = []
i, j = 0, 0
while i+j !=8:
    if i>3:
        Result.append(b[j])
        j+=1

    elif j>3:
        Result.append(a[i])
        i +=1

    elif a[i] <= b[j]:
        Result.append(a[i])
        i += 1

    elif b[j]<=a[i]:
        Result.append(b[j])
        j += 1


for k in range(8):
    print(Result[k], end= " ")