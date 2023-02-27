llist = []
n = int(input('N:'))
m = int(input('M:'))
for i in range(n-1):
    llist.append([i+1, i+1])
llist.append([n, 0])
head = 0
long = n
k = head
i = 0
while long > 1:
    i += 1
    #k = llist[k][1]
    if i == m:
        t = llist[k][1]
        llist[k][1] = llist[t][1]
        if t == head:
            head = llist[k][1]
            long -= 1
        i = 0
        k = llist[k][1]
        print(llist)
print(llist[head][0])
