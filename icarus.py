# Icarus

def icarus():
	number = 4
	while number != 100:
		time = 50
		while number != 1:
			if number % 2 == 1:
				number = number * 3 + 1
			else:
				number = number/2
			time -= 1
			number += 1
			if time == 0:
				return number

number_in_100 = icarus()

if number_in_100 != None:
	print(number_in_100)
else:
	print("none")