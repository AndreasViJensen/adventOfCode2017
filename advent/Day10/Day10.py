#Solution to part 1:
input = open("input.txt", "r", encoding="utf-8").read()

lengths = input.split(",")
lengths = [int(elem) for elem in lengths]

list = []

for i in range(0,256):
    list.append(i)

def hash(list, lengths):
    current = 0
    skip = 0

    for length in lengths:
        list = reverse(list, current, length)
        current = (current + length + skip) % 256
        skip = skip + 1

    return list


def reverse(l,p,d):
    q = (p + d - 1) % len(l)
    tmplist = []
    if q>= p:
        # regular reverse
        for i in range(q,p-1,-1):
            tmplist.append(l[i])

    else:
        for i in range (q, -1, -1):
            tmplist.append(l[i])
        for i in range (len(l)-1, p-1, -1):
            tmplist.append(l[i])

    for i in range(0,d):
        j = (i+p) % len(l)
        l[j] = tmplist[i]


    return l

print(hash(list,lengths))

print(80*172)