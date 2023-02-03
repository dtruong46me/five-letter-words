cnt = 0
stri = 'golds'
strj = 'goals'
for i in stri:
    if i in strj:
        cnt += 1
        print(i, end = ' ')
print(cnt)