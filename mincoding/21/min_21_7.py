letters = input()
length_letters = int(len(letters))

def recur(k):
    print(k, end =' ')
    if k == 1:
        return
    recur(k-1)
    print(k, end =' ')

recur(length_letters)

