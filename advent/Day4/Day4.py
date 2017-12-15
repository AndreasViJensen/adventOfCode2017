from collections import Counter

input = open("input.txt", "r", encoding="utf-8").read()

phrases = [phrase.split() for phrase in input.splitlines()]


# Part 1
def validPhrases(phrases):
    valids = []
    for phrase in phrases:
        if len(phrase) == len(set(phrase)):
            valids.append(phrase)

    return len(valids)


print(validPhrases(phrases))


# Part 2

def isAnagram(w1, w2):
    cnt1 = Counter()
    cnt2 = Counter()

    for c in w1:
        cnt1[c] += 1

    for c in w2:
        cnt2[c] += 1

    if cnt1 == cnt2:
        return True
    return False


def validPhrases2(phrases):
    valids = []
    for phrase in phrases:
        valid = True
        for i in range(len(phrase)):
            for j in range(len(phrase)):
                if i != j:
                    if isAnagram(phrase[i], phrase[j]):
                        valid = False
                        break
            if not valid:
                break
        if valid:
            valids.append(phrase)
    return len(valids)


print(validPhrases2(phrases))
