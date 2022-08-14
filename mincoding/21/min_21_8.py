y, x = 5, 5
n = int(input())
bucket = []

for i in range(n):
    bucket.append(input())
# print(bucket)

for j in bucket:
    if j == 'up':
        y -= 1
    elif j == 'down':
        y += 1
    elif j == 'left':
        x -= 1
    elif j == 'right':
        x += 1
    elif j == 'click':
        print(f'{y},{x}')
    else:
        print('틀린 입력')

