def split_show_views(line):
	splittedLine = line.split(',')
	show = splittedLine[0]
	views = splittedLine[1]
	return (show, views)