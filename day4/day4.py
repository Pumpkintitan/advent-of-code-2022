file = open("day4.txt").read().split("\n")
overlap1 = 0
overlap2 = 0
for line in file:
    elves = line.split(",")
    nums = []
    for ee in elves:
        f = ee.split("-")
        f[0] = int(f[0])
        f[1] = int(f[1])
        nums.append(f)
    #part 1
    if (nums[0][0] >= nums[1][0] and nums[0][1] <= nums[1][1]) or (nums[1][0] >= nums[0][0] and nums[1][1] <= nums[0][1]):
        overlap1 += 1
    #part 2
    if (max(nums[0][0], nums[1][0]) <= min(nums[0][1], nums[1][1])):
        overlap2 += 1
print(overlap1, overlap2)