friends = ['D', 'T', 'A', 'B', 'W', 'Q']
who = input()

for i in range(len(friends)):
    if friends[i]== who:
        print(f'{i}번 INDEX')