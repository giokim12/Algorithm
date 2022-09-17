def bbq(s):
    if s == 3:
        return

    bbq(s+1)

def main(k):
    bbq(k)


main(0)