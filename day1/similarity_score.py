from collections import Counter

left_list = []
right_list = []
file = open("/Users/ajit/Desktop/Programming/adventOfCode/2024/day1/input.txt","r")
for line in file:
    left_list.append(int(line.split("   ")[0]))
    right_list.append(int(line.split("   ")[1]))

file.close()

right_count = Counter(right_list)

similarity_score = 0

for i in range(len(left_list)):
    similarity_score += left_list[i] * right_count[left_list[i]]

print(similarity_score)
