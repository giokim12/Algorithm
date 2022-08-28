
import sys
sys.stdin = open("m_1_input.txt","r")

numbers = list(map(int, input().split()))

for j in range(len(numbers)):
    if numbers[j] < 5:
        print(f'{j}번은 {numbers[j]}점 불합격')
    else:
        print(f'{j}번은 {numbers[j]}점 합격')