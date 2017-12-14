input = open("input.txt", "r", encoding="utf-8").read()

wall = {int(pair[0]): int(pair[1]) for pair in [row.split(": ") for row in input.splitlines()]}


def isCollision(depth, delay, wall):
    if depth not in wall.keys():
        return False

    tripLength = (wall[depth] - 1) * 2
    if (depth+delay) % tripLength == 0:
        return True
    return False

def collisions(wall, delay):
    collisions = []
    for depth in range(0,max(wall.keys())+1):
        if isCollision(depth, delay, wall):
            collisions.append(depth)
            break
    return collisions

def severity(collisions,wall):
    res = 0
    for c in collisions:
        res = res + (c*wall[c])
    return res

# collisions = collisions(wall,0)
# print(severity(collisions,wall))

def minDelay(wall):
    delay = 0
    while True:
        cols = len(collisions(wall,delay))
        if cols == 0:
            break
        delay += 1
    return delay

print(minDelay(wall))