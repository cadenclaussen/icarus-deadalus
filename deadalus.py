n = 5
if_loop = [n]
n = int(n)
print(str(int(n)) + ": ", end="")
while n != 1:
	if n % 2 == 1:
		n = (n*3-1)
		print(str(int((n+1)/3)) + " * 3 - 1 --> " + str(int(n)) + " = ", end="")
		for i in if_loop:
			if i != n:
				if_loop.append(n)
				continue
		
	if n % 2 == 0:
		n = (n/2)
		print(str(int(n*2)) + "/2 --> " + str(int(n)) + " = ", end="")
		for i in if_loop:
			if i != n:
				if_loop.append(n)
			else:
				break

print("1")
print("\n")