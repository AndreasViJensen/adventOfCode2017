from functools import reduce

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

def stringOfDense(dense):
    result = ""
    for n in dense:
        hx = hex(n)[2:5]
        if len (hx) == 1:
            result = result + "0" + hx
        else:
            result = result + hx
    return result


def knotHash(inp):
    lengths = [ord(c) for c in inp] + [17, 31, 73, 47, 23]
    baseList = []
    for i in range(0, 256):
        baseList.append(i)

    sparse = hash(baseList, lengths)
    dense = densify(sparse)
    return stringOfDense(dense)


# Test cases:

# input = open("../Day10/input.txt", "r", encoding="utf-8").read()
# print("own input: " + str(knotHash(input) == "2da93395f1a6bb3472203252e3b17fe5"))
# print(knotHash(input))
#
# print("empty string: " + str(knotHash("")=="a2582a3a0e66e6e86e3812dcb672a272"))
# print(knotHash(""))
#
# print("1,2,3: " + str(knotHash("1,2,3")=="3efbe78a8d82f29979031a4aa0b16a9d"))
# print(knotHash("1,2,3"))
#
#
# print("AoC 2017: " + str(knotHash("AoC 2017")=="33efeb34ea91902bb2f59c9920caa6cd"))
# print(knotHash("AoC 2017"))


