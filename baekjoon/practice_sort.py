arr = ['A', 'C', 'B', 'F', 'BB', 'G', 'DD', 'E', 'B', 'AA']
sort1 = sorted(arr, key=lambda x: len(x))
print(sort1)


arr = ['A', 'C', 'B', 'F', 'BB', 'G', 'DD', 'E', 'B', 'AA']
sort2 = sorted(arr, key=lambda x: x)
print(sort2)


arr = ['A', 'C', 'B', 'F', 'BB', 'G', 'DD', 'E', 'B', 'AA']
sort3 = sorted(arr, key=lambda x: (len(x), x)) #길이 작은게 앞
sort4 = sorted(arr, key=lambda x: (-len(x), x)) #길이 큰게 앞

print(sort3)
print(sort4)

#길이가 가장 긴 단어를 출력하라.
#단 길이가 같은 경우 사전적으로 우선인 단어를 먼저 출력하라
result = sorted(arr, key=lambda x: (-len(x), x))
print(result[0])


arr = [(1, 3), (0, 3), (1, 4), (1,5), (0, 1), (2, 4)]
sort5 = sorted(arr, key=lambda x: x[0])
print(sort5)

#o번째 인덱스 기준으로 정렬 후
#1번째 인덱스 기준으로 정렬
sort6 = sorted(arr, key=lambda x: (x[0], x[1]))
print(sort6)


#빈도수가 가장 많은 문자를 출력하라
#단, 빈도수가 같다면 사전적으로 빠른 문자를 출력하라
sort7 = sorted(arr, key=lambda x: (arr.count(x), x))
print(sort7)