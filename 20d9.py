with open("20d9.txt") as f:
    a = list(map(int, f.read().split('\n')))

part1 = 0
for i in range(25, len(a)):
	found = False
	for j in range(1, 26):
		for k in range(1, 26):
			if j != k and a[i - j] + a[i - k] == a[i]:
				found = True
				break
		if found:
			break
	if not found:
		part1 = a[i]
		print("Part 1:", part1)
		break

cur_sum = 0
left = 0
right = 1
while cur_sum != part1:
	if cur_sum > part1:
		left += 1
	else:
		right += 1
	cur_sum = sum(a[left:right])

print("Part 2", min(a[left:right]) + max(a[left:right]))