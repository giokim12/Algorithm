a= list(input())
b= list(input())
c= list(input())
list_abc = [a, b, c]

length_of_word = 0
index_of_word = 0
for j in range(len(list_abc)):
    if len(list_abc[j]) > length_of_word:
        length_of_word = len(list_abc[j])
        index_of_word = j
list_abc[0], list_abc[index_of_word] = list_abc[index_of_word],list_abc[0]

for k in list_abc:
    print(''.join(k))