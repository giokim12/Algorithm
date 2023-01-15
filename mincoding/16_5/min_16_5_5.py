word = input()
a = input()
b = input()

result = ''
for i in word:
    if i != a:
        result += i
    else:
        result += b

print(result)