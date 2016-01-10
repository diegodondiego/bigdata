def split_show_channel(line):
    splittedLine = line.split(',')
    show = splittedLine[0]
    channel = splittedLine[1]
    return (show, channel)