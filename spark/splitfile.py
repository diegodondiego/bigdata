def split_fileA(line):
	splittedLine = line.split(',')
	count = int(splittedLine[1])
	return (splittedLine[0], count)