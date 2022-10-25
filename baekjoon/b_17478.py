<<<<<<< HEAD
N = int(input())
print('어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.')
def rcr(level):
    print('----' * (level), end='')
    print('"재귀함수가 뭔가요?"')

    if level == N:
        # print('----' * (level), end='')
        # print('"재귀함수가 뭔가요?"')
        print('----' * (level), end='')
        print('"재귀함수는 자기 자신을 호출하는 함수라네"')
        print('----' * (level), end='')
        print('라고 답변하였지.')
        return

    # print('----'*4*(n-1), end = '')


    print('----' * (level), end='')
    print('"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.')
    print('----' * (level), end='')
    print('마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.')
    print('----' * (level), end='')
    print('그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."')
    rcr(level + 1)
    print('----' *(level), end='')
    print('라고 답변하였지.')


rcr(0)


n = int(input())

def recur(level):
    print('----' *(level), end='')
    print('"재귀함수가 뭔가요?"')
    if level == n:
        print('----' *(level), end='')
        print('"재귀함수는 자기 자신을 호출하는 함수라네"')
    else:
        print('----' *(level), end='')
        print('"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.')
        print('----' *(level), end='')
        print("마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.")
        print('----' *(level), end='')
        print('그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."')
        recur(level+1)
    print('----' *(level), end='')
    print("라고 답변하였지.")


print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")
recur(0)
=======
#_*_coding:utf_8_*_
import sys
N = int(input())

sys.stdout = open('stdout.txt', 'w', encoding='utf8')
print('어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.')
def rcr(level):

    if level == N:
        print('____'*N, end = '')
        print('"재귀함수가 뭔가요?"')
        print('____'*N, end = '')
        print('"재귀함수는 자기 자신을 호출하는 함수라네"')
        print('____'*N, end = '')
        print('라고 답변하였지.')
        return

    print('____' * level, end='')
    print('"재귀함수가 뭔가요?"')
    print('____' * level, end='')
    print('"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.')
    print('____' * level, end='')
    print('마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.')
    print('____' * level,       end='')
    print('그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."')
    rcr(level+1)
    print('____' * level, end='')
    print('라고 답변하였지.')

rcr(0)
>>>>>>> ee7918c34c54a8f98533407ef9dd336a7c04e9eb
