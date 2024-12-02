
left_list = []
right_list = []
file = open("/Users/ajit/Desktop/Programming/adventOfCode/2024/day1/input.txt","r")
for line in file:
    left_list.append(line.split("   ")[0])
    right_list.append(line.split("   ")[1])

file.close()

right_list.sort()
left_list.sort()

total_distance = 0
for i in range(len(left_list)):
    total_distance += abs(int(left_list[i]) - int(right_list[i]))

print(total_distance)
