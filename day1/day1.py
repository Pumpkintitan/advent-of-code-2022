file = open("day1.txt").read().split("\n\n")
elfs = []
f = 0
#part 1
for l in file:
    elf = l.split("\n")
    elfs.append(0)
    for num in elf:
        elfs[f] += int(num)
    f += 1
print(max(elfs))
#part 2
elfs.sort()
print(sum(elfs[-3:]))