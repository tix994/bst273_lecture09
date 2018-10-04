#!/usr/bin/env python

import argparse

# one choice but want to add more choice
# import sys
# file = sys.argv[1]

parser = argparse.ArgumentParser( description="" )

parser.add_argument(
	"data_file",
	help="path to the file we want to read",
)

#-------------------------------------------------------------------------------
# Are there other arguments we need?
#-------------------------------------------------------------------------------

args = parser.parse_args( )

# Set path
# print( args )
# print( "args.data_file = ", args.data_file )

# open file
# open( "data_file" ) # open a file name called data_file
fh = open( args.data_file ) # need to store it in a variabels
# print( "the file handle is", fh )

# the output are 3 numbers
lines = 0
words = 0
chars = 0 # bytes is a built in one

for line in fh:
    # print(line) # but print a giant output
    lines += 1


# for line in fh:
    # fh is the pointer ot each file
    # fh is not a list
    # during the first loop, the pointer, fh, already point to the last line
    # thus here nothing to loop
    # print("Done!")

print(lines)

#-------------------------------------------------------------------------------
# our code for analyzing the data
#-------------------------------------------------------------------------------
