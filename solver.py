conditions = [
	["147", 1, False],
	["189", 1, True],
	["964", 2, False],
	["286", 1, False],
	["523", 0, False]
]

#conditions = [
#	["682",1,True],
#	["614",1,False],
#	["206",2,False],
#	["738",0,False],
#	["380",1,False]
#]

#conditions = [
#	['8446', 2, True],
#	['0601', 2, True]
#]

num_digits = 3
strict = True

def pad(num):
	return ("0"*(num_digits - len(num))) + num

def common(num1, num2, position):
	coms = 0
	num2 = list(num2)

	if not(position) and any(num1[x] == num2[x] for x in range(len(num1))):
		return -1
	for x in range(len(num1)):
		for y in range(len(num2)):
			if num1[x] != num2[y]:
				continue
			if position and x != y:
				if strict:
					return -1
				continue
			coms += 1
			num2[y] = "X"
			break
	return coms

def filtr(nums, condition):
	satisfiers = []
	for num in nums:
		coms = common(condition[0], num, condition[2])
		if coms != condition[1]: #if there arent enough numbers
			continue
		if coms == -1:
			continue
		satisfiers.append(num)
	return satisfiers


def solve():
	nums = [pad(str(n)) for n in range(10**num_digits)]
	for c in conditions:
		if len(c[0]) != num_digits or c[1] > num_digits:
			print("Invalid conditions. Check number of digits")
			return None
		nums = filtr(nums, c)
	return nums

sol = solve()
if sol is not None:
	print("found " + str(len(sol)) + " solutions.")
	print(str(sol))
