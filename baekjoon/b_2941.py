croatia_alphabets = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=' ]
word = input()

for i in croatia_alphabets:
    word = word.replace(i, '*')
print(len(word))