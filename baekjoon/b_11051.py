N, K = map(int, input().split())

a = 1
for i in range(N, 0, -1):
    a *= i

b = 1
for i in range(1,K+1):
    b *= i

c = 1
for i in range(1, N-K+1):
    c *=i

result1 = a/(b*c)
print(int(result1%10007))