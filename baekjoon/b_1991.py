# nodes = int(input())
# arr = [map(int, input().split()) for _ in range(nodes)]
#
# def rcr(level):
# '''
# A > B (a에서 1번) > D (b에서 1번) > . . (return)
# 인덱스 0인거에서 인덱스 1인걸로 가라
# 근데 인덱스 1이 .이면은 2로 가라
# 둘다 .이면은 리턴
#
#
# '''
#     if sth:
#         return
#
#
#     print(arr[level][0], end='')
#     rcr(level+1)

N = int(input())
arr = [list(input().split()) for _ in range(N)]
print(arr)

def preorder(level):
    if level==N:
        return

    for i in range(N):


def preorder(level):
    if root != '.':
        print(root, end='')  # root
        preorder(tree[root][0])  # left
        preorder(tree[root][1])  # right


def inorder(root):
    if root != '.':
        inorder(tree[root][0])  # left
        print(root, end='')  # root
        inorder(tree[root][1])  # right


def postorder(root):
    if root != '.':
        postorder(tree[root][0])  # left
        postorder(tree[root][1])  # right
        print(root, end='')  # root


preorder('A')
print()
inorder('A')
print()
postorder('A')

