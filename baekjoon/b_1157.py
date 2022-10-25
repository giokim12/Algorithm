W1 = input()
W = W1.upper()
bucket= [0]*200
for i in range(len(W)):
    bucket[ord(W[i])] +=1

MAX = 0
for i in range(len(bucket)):
    if bucket[i]>MAX:
        MAX = bucket[i]
MAX_word = ''
flg = 0
for i in range(len(bucket)):
    if bucket[i] == MAX:
        flg += 1
        MAX_word = chr(i)

if flg == 1:
    print(MAX_word)
else:
    print('?')
