#!/usr/bin/env python
import sys

# --------------------------------------------------------------------------
#This mapper code will input a <date word, value> input file, and move date into 
#  the value field for output
#  
#  Note, this program is written in a simple style and does not full advantage of Python 
#     data structures, but I believe it is more readable
#
#  Note, there is NO error checking of the input, it is assumed to be correct
#     meaning no extra spaces, missing inputs or counts,etc..
#
# See #  see https://docs.python.org/2/tutorial/index.html for details  and python  tutorials
#
# --------------------------------------------------------------------------


# We're using the haddoop stream lib
for line in sys.stdin:
    line       = line.strip()   #strip out carriage return
    splitted_line  = line.split(",")   #split line, into key and value, returns a list
    key     = splitted_line[0].split(" ")   #key is first item in list
    value   = splitted_line[1]   #value is 2nd item 

    #print key
    if len(key)>=2:           #if this entry has <date word> in key
        date = key[0]      #now get date from key field
        word = key[1]
        value_out = date+" "+value     #concatenate date, blank, and value
        print( '%s\t%s' % (word, value_out) )  #print a string, tab, and string
    else:   #key is only <word> so just pass it through
        print( '%s\t%s' % (key[0], value) )  #print a string tab and string

#Note that Hadoop expects a tab to separate key value
#but this program assumes the input file has a ',' separating key value
join1_reducer.py
