# importing the knotHash function from Day 10
from advent.Day10.Day10 import knotHash


# translates a dense hash value in hex to a string of bits with 4 bits per hex-digit:
def bitString(hexString):
    bs = ""
    for c in hexString:
        b = bin(int(c, 16))[2:]
        l = len(b)
        for i in range(0, 4 - l):
            b = "0" + b
        bs = bs + b
    return bs


# counts free spaces in a 128*128 disk grid characterized by the key string inp
def countFreeSpaces(inp):
    allFields = ""
    for i in range(0, 128):
        hash1 = knotHash(inp + str(i))
        allFields = allFields + bitString(hash1)
    res = 0
    for c in allFields:
        if c == "1":
            res += 1
    return res


# Solution to Part 1:
# print(countFreeSpaces("stpzcrnm-"))


# Part 2:

# subroutine for countRegions that finds adjacent used slots in memory given a row * column pair.
def findAdjacents(r, c, black, rows):
    group = []
    for r_ in range(r - 1, r + 2):
        for c_ in range(c - 1, c + 2):
            if ((r_ == r) ^ (c_ == c)) and (0 <= r_ <= 127 and 0 <= c_ <= 127):
                if rows[r_][c_] == "1" and (r_, c_) not in black:
                    group.append((r_, c_))
                    black = black.union({(r_, c_)})
                    (g, b) = findAdjacents(r_, c_, black, rows)
                    group = group + g
                    black = b

    return (group, black)


# This function computes the regions of adjacent used slots in a 128*128 memory grid
# and returns them as a list of groups.
def regions(inp):
    print("counting regions...")
    rows = []
    for i in range(0, 128):
        hash_ = knotHash(inp + str(i))
        rows.append(bitString(hash_))

    black = set()
    groups = []

    for r in range(0, 128):
        for c in range(0, 128):
            if ((r, c) not in black) and (rows[r][c] == "1"):
                black = black.union({(r, c)})
                (group, black_) = findAdjacents(r, c, black, rows)
                black = black_
                group.append((r, c))
                groups.append(group)

    return groups


gs = regions("stpzcrnm-")
print(gs)
print(len(gs))
