import re

# Using stateful runthrough:
input = open("input.txt", "r", encoding="utf-8").read()


def scoreStream(str):
    level = 0
    score = 0
    garbage_chars = 0

    # We use the following states: ["Group", "Garbage", "Ignore"]
    state = "Group"

    for c in str:

        if state == "Group":
            if c == "{":
                level = level + 1
                score = score + level
            if c == "}":
                level = level - 1
            if c == "<":
                state = "Garbage"

        elif state == "Garbage":
            if c == ">":
                state = "Group"
            elif c == "!":
                state = "Ignore"
            else:
                garbage_chars = garbage_chars + 1

        elif state == "Ignore":
            state = "Garbage"

    return (score, garbage_chars)


print(scoreStream(input))

# Solution using Regular expressions (Credits to Martin Zach Gronhoj)
input = open("input.txt", "r", encoding="utf-8").read()

gb1 = re.compile("<(!.|[^!>])*>")

str_cleaned = gb1.sub("", input)


def computeScore(str):
    score = 0
    level = 0
    for c in str:
        if c == "{":
            level = level + 1
            score = score + level
        if c == "}":
            level = level - 1

    return score


print(computeScore(str_cleaned))
