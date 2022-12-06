file = open("day6.txt").read().split("\n")
#part 1
for i in range(3,len(file[0])):
    vis = []
    for c in file[0][i-3:i+1]:
        if not c in vis:
            vis.append(c)
    if len(vis) == 4:
        print(i+1)
        break

#part 2
for i in range(13,len(file[0])):
    vis = []
    for c in file[0][i-13:i+1]:
        if not c in vis:
            vis.append(c)
    if len(vis) == 14:
        print(i+1)
        break
