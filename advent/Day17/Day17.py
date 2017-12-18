
step_size = 304

mem = [0]
length = 1
current_pos = 0
latest_at_one = 0

for i in range(50000000):
    if i % 100000 == 0:
        print(i)
    current_pos = ((current_pos + step_size) % length) + 1
    if current_pos == 1:
        latest_at_one = i + 1
    length += 1

print(latest_at_one)
print(mem)
# PART 2




