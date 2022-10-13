bucket = [0]*10

arr = list(map(int, input()))

for i in range(len(arr)):
    bucket[arr[i]] += 1

six_and_nine = 0
if (bucket[6]+bucket[9])%2 == 0:
    six_and_nine = (bucket[6]+bucket[9])/2
else:
    six_and_nine = ((bucket[6]+bucket[9])//2)+1

MAX = 0
for i in range(10):
    if i==6 or i==9:
        continue
    if bucket[i] > MAX:
        MAX = bucket[i]

print(int(max(MAX, six_and_nine)))
