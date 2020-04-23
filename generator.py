import random
import copy

#configuration
num_digits = 4
num_conds = [5, 9]
num_sols = 1

#set to true if conditions must have same solutions for strict = true and strict = false
doubleP = True

#makes condition logic more restricted, this affects ambiguity of problem
strict = True

def pad(num):
	return ("0"*(num_digits - len(num))) + num

def printProblem(conditions):
	print(str(solve(conditions)) + ": " + str(conditions))

def same(sol1, sol2):
	sol1.sort()
	sol2.sort()
	return sol1 == sol2

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

def removeUnecessary(conditions):
	actual = solve(conditions)
	for k in range(len(conditions)):
		tests = copy.deepcopy(conditions)
		tests.pop(k)
		s = solve(tests)

		if same(solve(tests), actual):
			return removeUnecessary(tests)
	return conditions

while True:
	conds = genConds()
	while len(solve(conds)) != num_sols:
		conds = genConds()
	
	print("Found problem: ")
	printProblem(conds)
	if doubleP:
		print("Checking for doubleP")
		solB = solve(conds)
		strict = not(strict)
		areSame = same(solB, solve(conds))
		strict = not(strict)
		if not(areSame):
			print("doubleP not satisfied")
			continue
		else:
			print("doubleP OK")
	
	conds = removeUnecessary(conds)
	if len(conds) < num_conds[0]:
		print("has less than minimum conditions:")
		printProblem(conds)
		continue
	break

print("All settings are satisfied:")
printProblem(conds)
