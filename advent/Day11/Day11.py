input = open("input.txt", "r", encoding="utf-8").read()

steps = input.split(",")


def findShortestPath(r, c):
    ar = abs(r)
    ac = abs(c)
    if max(ar, ac) == ac:
        return ar + ac - ar
    else:
        return ac + (ar - ac) * 0.5


def findCoords(steps):
    r = 0
    c = 0
    maxdist = 0
    for step in steps:
        if step == "n":
            r += 2
        if step == "s":
            r -= 2
        if step == "nw":
            r += 1
            c -= 1
        if step == "ne":
            r += 1
            c += 1
        if step == "se":
            r -= 1
            c += 1
        if step == "sw":
            r -= 1
            c -= 1
        maxdist = max(maxdist, findShortestPath(r, c))
    return r, c, maxdist


(r, c, maxdist) = findCoords(steps)

print(len(steps))
print(findShortestPath(r, c))
print("maxdist: " + str(maxdist))
