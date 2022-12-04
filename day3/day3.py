file = open("day3.txt").read().split("\n")
#part 1
score = 0
for line in file:
    found = False
    for char in line[:int(len(line)/2)]:
        if char in line[int(len(line)/2):] and not found:
            if 122 >= ord(char) >= 97:
                score += ord(char) - 96
            if 90 >= ord(char) >= 65:
                score += ord(char) - 38
            found = True
print(score)
#part 2
score = 0
elf = 0
common = []
for line in file:
    if elf == 0:
        for char in line:
            common.append(char)
    if elf == 1:
        new = []
        for char in line:
            if char in common:
                new.append(char)
        common = new
    if elf == 2:
        new = []
        for char in line:
            if char in common:
                new.append(char)
        common = new
        if 122 >= ord(common[0]) >= 97:
            score += ord(common[0]) - 96
        if 90 >= ord(common[0]) >= 65:
            score += ord(common[0]) - 38
        elf = -1
        common = []
    elf += 1
print(score)