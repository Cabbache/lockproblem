import random
import copy

num_digits = 3
num_conds = [5, 8]
num_sols = 1

def pad(num):
	return ("0"*(num_digits - len(num))) + num

def common(num1, num2, position):
	coms = 0
	num2 = list(num2)
	if not(position) and any(num1[x] == num2[x] for x in range(len(num1))):
		return -1
	for x in range(len(num1)):#condition number 0071
		for y in range(len(num2)):#number tested  4066
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


def solve(conditions):
	nums = [pad(str(n)) for n in range(10**num_digits)]
	for c in conditions:
		if len(c[0]) != num_digits or c[1] > num_digits:
			print("Invalid conditions. Check number of digits")
			return None
		nums = filtr(nums, c)
	return nums

def genConds():
	conds = []
	for x in range(random.randint(num_conds[0], num_conds[1])):
		c = [pad(str(random.randint(0, (10**num_digits)-1))), random.randint(1, num_digits), random.randint(0,1) == 1]
		conds.append(c)
	return conds

def allImp(conditions):
	sols = []
	actual = solve(conditions)
	actual.sort()
	for k in range(len(conds)):
		tests = copy.deepcopy(conds)
		tests.pop(k)
		s = solve(tests)
		s.sort()
		sols.append(s)
	
	for sol in sols:
		print(str(sol) + " <---> " + str(actual))
		if len(sol) != len(actual):
			continue
		if sol == actual:
			return False
	return True

conds = genConds()

while True:
	while len(solve(conds)) != num_sols:
		conds = genConds()
	
	if not(allImp(conds)):
		conds = genConds()
		continue
	break

print(str(solve(conds)) + ": " + str(conds))
