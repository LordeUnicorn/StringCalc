import re

def add_num(numbers):
	if numbers == "":
		return 0

	# The if statement checks for strings that start with // and defines numbers as anything after the //.
	delimiters = [","]
	if numbers[:2] == "//":
		numbers = numbers[2:]

		(delimiters, nl, numbers) = numbers.partition("\n")

		if len(delimiters) > 1:
			if not "][" in delimiters:
				delimiters = [delimiters[1:-1]]
			else:
				delimiters = delimiters[1:-1].split("][")

		else:
			delimiters = [delimiters]

	# using regex to deal with multiple characters
	for char in list("\\*+.?(){}[]^$|"):
		delimiters = list(map(lambda d: d.replace(char, "\\" + char), delimiters))

	delimiters.append("\\n")

	numbers = re.split("|".join(delimiters), numbers)
	numbers = list(map(int, numbers))
	# rejection of negative values
	if any(n < 0 for n in numbers):
		raise Exception("negatives not allowed: " + str(list(n for n in numbers if n < 0)))
	#specifying that only numbers between 0 and 100 must be added
	return sum(n for n in numbers if n <= 1000)

print(add_num('1,2\n9'))
