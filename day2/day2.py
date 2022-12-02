file = open("day2.txt").read().split("\n")
points = 0
#part 1
for l in file:
    a = l.split(" ")
    if a[1] == "X":
        points += 1 
        if a[0] == "A":
            points += 3
        if a[0] == "C":
            points += 6
    if a[1] == "Y":
        points += 2
        if a[0] == "B":
            points += 3
        if a[0] == "A":
            points += 6
    if a[1] == "Z":
        points += 3
        if a[0] == "C":
            points += 3
        if a[0] == "B":
            points += 6
print(points)
#part 2
points = 0
for l in file:
    a = l.split(" ")
    if a[0] == "A":
        if a[1] == "X":
            points += 3
        if a[1] == "Y":
            points += 4
        if a[1] == "Z":
            points += 8
    if a[0] == "B":
        if a[1] == "X":
            points += 1
        if a[1] == "Y":
            points += 5
        if a[1] == "Z":
            points += 9
    if a[0] == "C":
        if a[1] == "X":
            points += 2
        if a[1] == "Y":
            points += 6
        if a[1] == "Z":
            points += 7
print(points)
