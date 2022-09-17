a = input()

for i in range(-3, 4, 1):
    if ord(a)+i>ord('Z'):
        print(chr(ord(a)+i-1-ord('Z')+ ord('A')), end='')
    elif ord(a)+i<ord('A'):
        print(chr(ord(a)+i+1+ ord('Z')- ord('A')), end='')
    else:
        print(chr(ord(a)+i), end='')
