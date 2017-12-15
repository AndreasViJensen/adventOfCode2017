# Generator A starts with 722
# Generator B starts with 354
import math

#Constants:
a = 722
mul_a = 16807
b = 354
mul_b = 48271
divd = 2147483647
#the 16 bit number consisting only of 1's
b16 = int(math.pow(2,16)-1)

matches = 0
for i in range(5000000):

    while True:
        a = (a*mul_a) % divd
        if a % 4 == 0:
            break

    while True:
        b = (b*mul_b) % divd
        if b % 8 == 0:
                break

    if (a & b16) == (b & b16):
        matches += 1

print(matches)