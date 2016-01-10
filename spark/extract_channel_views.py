def extract_channel_views(show_views_channel): 
	aLine = show_views_channel[1]
	views = int(aLine[1])  
	channel = aLine[0]
	return (channel, views)