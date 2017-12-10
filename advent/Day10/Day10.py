from functools import reduce

input = open("input.txt", "r", encoding="utf-8").read()

lengths = [ord(c) for c in input] + [17, 31, 73, 47, 23]

baseList = []
for i in range(0, 256):
    baseList.append(i)


def hash(list, lengths):
    current = 0
    skip = 0

    for j in range(0, 64):
        for length in lengths:
            list = reverse(list, current, length)
            current = (current + length + skip) % len(list)
            skip = skip + 1

    return list


def reverse(l, p, d):
    q = (p + d - 1) % len(l)
    tmplist = []
    if q >= p:
        # regular reverse
        for i in range(q, p - 1, -1):
            tmplist.append(l[i])

    else:
        for i in range(q, -1, -1):
            tmplist.append(l[i])
        for i in range(len(l) - 1, p - 1, -1):
            tmplist.append(l[i])

    for i in range(0, d):
        j = (i + p) % len(l)
        l[j] = tmplist[i]

    return l


def densify(sparse):
    blocks = []
    for i in range(0, 16):
        blocks.append(sparse[i * 16:i * 16 + 16])

    dense = []
    for block in blocks:
        dense.append(reduce((lambda a, b: a ^ b), block))

    return dense

def printDense(dense):
    result = ""
    for n in dense:
        result = result + (hex(n)[2:5])
    print(result)

sparse = hash(baseList, lengths)
dense = densify(sparse)
printDense(dense)


