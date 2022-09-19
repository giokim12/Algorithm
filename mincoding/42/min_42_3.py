arr = ['BTS', 'SBS', 'BS', 'CBS', 'SES']
path = ['']*30
word = input()

def recur(level, cnt):

   if ''.join(path)==word:
       print(cnt)
       return

   if len(''.join(path))>len(word):
       return

   for i in range(len(arr)):
       path[level] = arr[i]
       recur(level+1, cnt+1)
       path[level]=''

recur(0,0)




