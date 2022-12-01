import sys
input = sys.stdin.readline

N, M = map(int, input().split())
pokemon = []
for i in range(N):
    temp = input()
    pokemon.append([temp, i+1])

pokemon2 = sorted(pokemon, key=lambda x: x[0])

for i in range(M):
    temp2 = input().strip()
    if temp2.isdigit() == True:
        print(pokemon[int(temp2)-1][0])
    else:
        # start, end = 0, N-1
        # while start <= end:
        #     middle = (start+end)//2
        #     if pokemon2[middle][0] == temp2:
        #         print(pokemon2[middle][1])
        #         break
        #     elif pokemon2[middle][0] < temp2:
        #         start = middle +1
        #     else:
        #         end = middle-1
#     else:
        low, high = 0, N
        while low <= high:
            mid = (low + high) // 2
            if pokemon2[mid][0] < temp2: low = mid + 1
            else: high = mid - 1
        print(pokemon2[high + 1][1])


# def check(a):
#     if "1" in a or "2" in a or "3" in a or "4" in a or "5" in a or "6" in a or "7" in a or "8" in a or "9" in a or "0" in a:
#         return True
#     return False
# n, m = map(int, input().split())
# s = [0]
# s_ = []
# for i in range(n):
#     a = input().strip()
#     s.append(a)
#     s_.append([a, i + 1])
# s_.sort()
# for i in range(m):
#     a = input().strip()
#     if check(a): print(s[int(a)])
#     else:
#         low, high = 0, n
#         while low <= high:
#             mid = (low + high) // 2
#             if s_[mid][0] < a: low = mid + 1
#             else: high = mid - 1
#         print(s_[high + 1][1])

