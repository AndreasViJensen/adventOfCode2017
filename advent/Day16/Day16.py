import re

input = open("input.txt", "r", encoding="utf-8").read()

insns = input.split(",")

print(insns)

progs = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p"]


def doTheDance(progs, insns):
    for insn in insns:
        if insn[0] == "s":
            l = int(insn[1:])
            progs = progs[16 - l:] + progs[:16 - l]
        if insn[0] == "x":
            num = re.compile("\d+")
            poss = num.findall(insn)
            p1 = int(poss[0])
            p2 = int(poss[1])
            temp = progs[p1]
            progs[p1] = progs[p2]
            progs[p2] = temp
        if insn[0] == "p":
            prog1 = insn[1]
            prog2 = insn[3]
            ind1 = progs.index(prog1)
            ind2 = progs.index(prog2)
            progs[ind1] = prog2
            progs[ind2] = prog1

    return progs


# part 1
# print(doTheDance(progs, insns))


# part 2
def repeatedDance(progs, insns, times):
    p_org = list(progs)
    ps = progs
    for i in range(times):
        plist = [ps]
        if i % 1000 == 0:
            print(i)
        ps = doTheDance(ps, insns)
        if p_org == ps:
            print(i)
            break

    string = ""
    for c in ps:
        string += c
    return string


# ociedpjbmfnkhlga
progs = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p"]
print(repeatedDance(progs, insns, 1000000000))

progs = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p"]
print(repeatedDance(progs,insns, 1000000000%60))