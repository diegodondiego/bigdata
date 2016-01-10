def split_fileB(line):
	# split the input line into word, date and count_string
	splittedLineBySpace = line.split(' ')
	date = splittedLineBySpace[0]
	splittedLineByComma = splittedLineBySpace[1].split(',')
	word = splittedLineByComma[0]
	count_string = splittedLineByComma[1]
	return (word, date + " " + count_string)