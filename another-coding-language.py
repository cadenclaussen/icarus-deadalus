alpha = input()
start = input()

answer = set()
for i in range(len(start) + 1):
	for letter in alpha:
		answer.add("".join(start[0:i] + letter + start[i:]))

for i in range(len(start)):
	answer.add("".join(start[0:i] + start[i+1:]))

for i in range(len(start) + 1):
	for letter in alpha:
		answer.add("".join(start[0:i] + letter + start[i+1:]))

answer = list(answer)
answer.remove(start)
answer.sort()

print(*answer, sep="\n")