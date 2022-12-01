n = int(input())
start = 666
order = 0

while True:
    if '666' in str(start):
        order += 1

    if order == n:
        print(start)
        break

    else: start +=1



