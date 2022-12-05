file = open("day5.txt").read().split("\n")
PART = 2
stacks = []
numstacks = int((len(file[0]) + 1)/4)
for i in range(numstacks):
    stacks.append([])
instructions = False
for i in range(len(file)):
    if instructions and not file[i][1] == 1:
        l = file[i]
        inst = l.split(" ")
        c = int(inst[1])
        f = int(inst[3]) - 1
        t = int(inst[5]) - 1
        #part 1
        if PART == 1:
            for k in range(c):
                item = stacks[f].pop(0)
                stacks[t].insert(0,item)
        #part 2
        if PART == 2:
            r = []
            for k in range(c):
                item = stacks[f].pop(0)
                r.insert(0,item)
            for thing in r:
                stacks[t].insert(0,thing)
    if len(file[i]) == 0 and not instructions:
        instructions = True
    if not instructions and not file[i][1] == "1":
        for j in range(numstacks):
            if not file[i][j*4+1] == " ":
                stacks[j].append(file[i][j*4+1])
answer = ""
for s in stacks:
    answer += s[0]
print(answer)