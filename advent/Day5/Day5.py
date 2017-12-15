input = open("input.txt", "r", encoding="utf-8").read()

insns = [int(line) for line in input.splitlines()]

length = len(insns)
steps = 0
i = 0

while 0 <= i < length:
    jump = insns[i]
    if jump >= 3:
        insns[i] = insns[i] - 1
    else:
        insns[i] = insns[i] + 1
    steps += 1
    i += jump

print(steps)
