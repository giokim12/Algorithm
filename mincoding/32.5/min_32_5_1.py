arr = ['ABCD', 'ABCE', 'AGEH', 'EIEI', 'FEQE', 'ABAD']
path = []
bucket = [0]*6
word = list(input())
cnt =0

find_cnt = 0
for i in range(4):
    if word[i] != '?':
        find_cnt += 1
        for j in range(6):
            if arr[j][i] == word[i]: #아직 안더해졌음 + 같은거 찾음
                path.append(arr[j])
# print(path)
for i in range(len(path)):
    for j in range(len(arr)):
        if path[i]== arr[j]:
            bucket[j] += 1
# print(bucket)
cnt =0
for i in range(len(bucket)):
    if bucket[i] == find_cnt:
        cnt += 1

print(cnt)

