input = open("input.txt", "r", encoding="utf-8").read()

# Making a dictionary of comparison operations:
comps = {"<":   lambda a, b: a < b,
         "<=":  lambda a, b: a <= b,
         "==":  lambda a, b: a == b,
         "!=":  lambda a, b: a != b,
         ">":   lambda a, b: a > b,
         ">=":  lambda a, b: a >= b, }

mutators = {"inc": lambda a, b: a + b,
            "dec": lambda a, b: a - b}

insns = input.splitlines()

insns = [line.split() for line in insns]

env = dict.fromkeys([ins[0] for ins in insns], 0)

maximum = 0
for ins in insns:
    cmp = ins[5]
    n = int(ins[6])
    regval = int(env[ins[4]])
    mut = ins[1]
    chg = int(ins[2])
    reg = ins[0]

    if comps[cmp](regval, n):
        env[reg] = mutators[mut](env[reg], chg)
        maximum = max(maximum, env[reg])

# part1:
print(max(env.values()))
# To learn the register holding max :
# max_regs = [item[0] for item in env.items() if item[1] == max(env.values())]

# part2:
print(maximum)

