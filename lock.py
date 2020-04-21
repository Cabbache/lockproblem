#conditions = [
#	["147", 1, False],
#	["189", 1, True],
#	["964", 2, False],
#	["286", 1, False],
#	["523", 0, False]
#]

conditions = [
	["682",1,True],
	["614",1,False],
	["206",2,False],
	["738",0,False],
	["380",1,False]
]

def pad(num):
	return ("0"*(3 - len(num))) + num

def common(num1, num2, position):
	coms = 0
	num2 = list(num2)
	for x in range(len(num1)):
		for y in range(len(num2)):
			if num1[x] != num2[y]:
				continue
			if position and x != y:
				return -1
			if not(position) and x == y:
				return -1
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

nums = [pad(str(n)) for n in range(1000)]

for c in conditions:
	nums = filtr(nums, c)

print("found " + str(len(nums)) + " solutions.")
print(str(nums))
