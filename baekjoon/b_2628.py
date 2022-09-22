width, height = map(int, input().split())
cut_number = int(input())

cut = [list(map(int, input().split())) for _ in range(cut_number)]

garo_cut = []
sero_cut = []

for i in range(cut_number):
    if cut[i][0] == 0:
        garo_cut.append(cut[i][1])
    elif cut[i][0] == 1:
        sero_cut.append(cut[i][1])

garo_cut.append(height)
garo_cut.append(0)
sero_cut.append(width)
sero_cut.append(0)
garo_cut = sorted(garo_cut, reverse=True)
sero_cut = sorted(sero_cut, reverse=True)


MAX = 0
for i in range(1, len(garo_cut)):
    for j in range(1, len(sero_cut)):
        if (garo_cut[i-1]-garo_cut[i])*(sero_cut[j-1]-sero_cut[j]) >MAX:
            MAX = (garo_cut[i-1]-garo_cut[i])*(sero_cut[j-1]-sero_cut[j])
print(MAX)

