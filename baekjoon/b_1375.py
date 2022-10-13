X, Y = map(str, input().split())

a = []
for i in range(len(X)-1, -1, -1):
    a.append(X[i])

b = []
for i in range(len(Y)-1, -1, -1):
    b.append(Y[i])

word1 = ''.join(a)
word2 = ''.join(b)

number1 = int(word1)
number2 = int(word2)

number3 = number1+number2

word3 = str(number3)
c = []
for i in range(len(word3)-1, -1, -1):
    c.append(word3[i])

word4 = ''.join(c)
number4 = int(word4)
print(number4)

