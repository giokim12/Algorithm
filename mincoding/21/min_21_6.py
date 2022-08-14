branch, level = map(int, input().split())
numb = 1
def recur(br, lv,  cnt):
    global numb
    if cnt == lv:
        return

    for i in range(br):
        numb += 1
        recur(br, lv, cnt + 1)


recur(branch, level, 0)
print(numb)

